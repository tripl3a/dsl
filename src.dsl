# An extendable source file for the Domain Specific Language
#
# Running this script:
# Python 3 should be installed. Enter "python dsl.py src.dsl" in a terminal to run this script.
#
# A user has to specify the following to execute a command of our DSL:
# - module name
# - function name
# - parameters, separated by whitespaces

module add_str hello world how are you ?
module add_str foo bar baz type=string hello=world
module add_str district=Wedding university=Beuth course=ASE
module add_num 1 2 3 type=int
module add_num 1 2 3.0 type=float
module add_num 1 2 3.5 type=float
