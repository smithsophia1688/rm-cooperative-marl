import os
import functools



class Traces:
    def __init__(self, positive= set(), negative= set(), event_number_dict = {}):
        self.positive = positive
        self.negative = negative
        self.event_number_dict = event_number_dict

    def get_event_number(self, event):
        '''
        grabs the integer label for our event from dictionary.
        Input: 
            event: (str) Must be key in event_number_dict (assigned a #)
        Returns:
            (int)
        '''
        assert type(event) == str, "event is not str"
        assert event in self.event_number_dict.keys(), "event not assigned ingeger value"
        return self.event_number_dict[event] 

    def get_multi_agent_event_history(self, event_list):
        '''
        gets event history put together in single list

        Inputs:
            event_list: (list) contains lists of events from each turn
        Returns: 
            list, events in order 
        '''
        event_history = []
        for turn in event_list:
            for l in turn:
                event_history.append(l)
        return event_history

    def get_multi_agent_trace(self, event_list):
        full_event_history = self.get_multi_agent_event_history(event_list)
        full_trace_events = []
        for l in full_event_history:
            n = self.get_event_number(l)
            full_trace_events.append(n)
        return full_trace_events
          
    ### ADDING TRACES ###

    def _should_add(self, trace, i):
        ''' this should aways be true'''
        prefixTrace = trace[:i]
        if not prefixTrace[-1] == '':
            return True
        else:
            print("         YOU DIDN'T THINK THIS WOULD HAPPEN: TRACE._SHOULD_ADD FALSE")
            return False

    def _get_prefixes(self, trace, up_to_limit = None):
        if up_to_limit is None:
            up_to_limit = len(trace)
        all_prefixes = set()
        for i in range(1, up_to_limit+1):
            if self._should_add(trace, i):
                all_prefixes.add(trace[:i])
        return all_prefixes

    def add_trace(self, trace, reward):
        ''' 
        adds a trace to class.
        Works for either integer representation or string representation
        Inputs:
            trace: list
            reward: int
        
        Updates positive and/or negative attributes
        '''
        trace = tuple(trace)
        if reward > 0:
            self.positive.add(trace)
            #Add previous steps as traces that "didnt" give reward
            self.negative |= self._get_prefixes(trace, len(trace)-1) #can add this back later when sure
        else:
            self.negative |= self._get_prefixes(trace)
    
    def export_traces(self, filename):
        '''
        makes file with traces to be read and used by JR pysat
        '''
        parent_path = os.path.dirname(filename)
        os.makedirs(parent_path,exist_ok=True)
        #print("parent_path", parent_path)

        with open(filename, "w") as output_file:
            print('         in traces output file', output_file)
            output_file.write("POSITIVE:")
            for trace in self.positive:
                print("Added positive")
                output_file.write("\n")
                string_repr = [str(el) for el in trace]
                output_file.write(','.join(string_repr))
            output_file.write("\nNEGATIVE:")
            for trace in self.negative:
                print("added negative")
                output_file.write("\n")
                string_repr = [str(el) for el in trace]
                output_file.write(','.join(string_repr))


        
if __name__ == '__main__':
    end  = {'l1':0, 'l2': 1, 'r1': 2, 'r2': 3, 'r':4, 'g1': 5, 'g2': 6}
    trace = Traces(event_number_dict = end)
    
    event_list = [ ['l1', 'l2'], ['l1', 'r2'], ['l1', 'r2'], ['l1', 'r2'], ['r1', 'r2'], ['r'], ['l1', 'l2'], ['l1', 'l2'], ['l1', 'l2'], [], ['l1'], [], ['l1', 'l2'], ['g1', 'g2']]
    trace_history = trace.get_multi_agent_trace(event_list)
    
    trace.add_trace(trace_history, 1)
    trace.export_traces('./automata_learning_utils/data/data3.txt')
    print("All done")



