from automata_learning_utils import al_utils

print("Yoohoo! hello world!!")

print("How do i run pysat?")




######### IN run_aqrm_experiments #########
#traces_numerical = Traces(positive_new, negative_new)
#traces_file = './automata_learning_utils/data/data.txt'
#traces_numerical.export_traces(traces_file)
#
#      Looks like the traces get made/ exported through Traces methods.
#      happens right before learn_automatan 
#
#Where dos positive_new and negative_new get set? 
#

traces_filename =  "./automata_learning_utils/data/data3.txt" #HOLDS ALL THE TRACES when does it get written
show_plots=False
is_SAT= None
automaton_learning_algorithm= "pysat"
pysat_algorithm = "rc2"
automaton_learning_program = None
sup_hint_dfas = None
output_reward_machine_filename = "./automata_learning_utils/data/rm2.txt"


al_utils.learn_automaton(traces_filename, show_plots, is_SAT,  automaton_learning_algorithm = automaton_learning_algorithm, pysat_algorithm = pysat_algorithm, automaton_learning_program = automaton_learning_program, sup_hint_dfas = sup_hint_dfas, output_reward_machine_filename =output_reward_machine_filename)  




