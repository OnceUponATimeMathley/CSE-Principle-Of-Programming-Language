import sys, os

sys.path.append('./test/')
import subprocess
import unittest
from antlr4 import *
from TestUtils import TestLexer
from TestUtils import TestParser


# Make sure that ANTLR_JAR is set to antlr-4.8-complete.jar
ANTLR_JAR = os.environ.get('ANTLR_JAR')
TARGET = '../target/main/bkit/parser' if os.name == 'posix' else os.path.normpath('../target/')
#TARGET = '../target/main/mc/parser' if os.name == 'posix' else os.path.normpath('../target/')

def main(argv):
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        subprocess.run(
            ["java", "-jar", ANTLR_JAR, "-o", "../target/main/bkit/parser", "-no-listener", "-visitor", "main/bkit/parser/BKIT.g4"])
        #["java", "-jar", ANTLR_JAR, "-o", "../target", "-no-listener", "-visitor", "main/bkit/parser/BKIT.g4"])
    elif argv[0] == 'clean':
        subprocess.run(["rm", "-rf", "../target/main"])
    elif argv[0] == 'test':
        if not './main/bkit/parser/' in sys.path:
            sys.path.append('./main/bkit/parser/')
        if os.path.isdir(TARGET) and not TARGET in sys.path:
            sys.path.append(TARGET)
        if len(argv) < 2:
            printUsage()
        elif argv[1] == 'LexerSuite':
            from LexerSuite import LexerSuite
            suite = unittest.makeSuite(LexerSuite)
            test(suite)
        elif argv[1] == 'ParserSuite':
            from ParserSuite import ParserSuite
            suite = unittest.makeSuite(ParserSuite)
            test(suite)
        else:
            printUsage()
    else:
        printUsage()


def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())


def printUsage():
    print("python3 run.py gen")
    print("python3 run.py test LexerSuite")
    print("python3 run.py test ParserSuite")


if __name__ == "__main__":
    main(sys.argv[1:])
    # print(TestLexer.checkLexeme(""" "abc def  """, """Unclosed String: abc def  """, 106))
    # print(TestLexer.checkLexeme(""" "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 105))
    # print(TestLexer.checkLexeme(""" ** hch
    # dia cac
    # cacm ** ** hekca \n **  ""","""** hch
    #
    # dia cac
    #
    # cacm **,<EOF>""",107))
    # TestLexer.checkLexeme(""" "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 107)
    # input = """Var: x;"""
    # expect = "successful"
    # TestParser.checkParser(input, expect, 201)
    # TestLexer.checkLexeme(""" { } """, """ """, 124)