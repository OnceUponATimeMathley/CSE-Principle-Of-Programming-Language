# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0239\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\7\2\u009c\n\2\f\2\16\2\u009f\13\2\3\3\3\3\3")
        buf.write("\3\3\3\7\3\u00a5\n\3\f\3\16\3\u00a8\13\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\6\4\u00b0\n\4\r\4\16\4\u00b1\3\4\3\4\3\5\3")
        buf.write("\5\3\5\7\5\u00b9\n\5\f\5\16\5\u00bc\13\5\5\5\u00be\n\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\7\6\u00c5\n\6\f\6\16\6\u00c8\13\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\7\6\u00cf\n\6\f\6\16\6\u00d2\13\6")
        buf.write("\5\6\u00d4\n\6\3\7\3\7\3\7\3\7\3\7\7\7\u00db\n\7\f\7\16")
        buf.write("\7\u00de\13\7\3\7\3\7\3\7\3\7\3\7\7\7\u00e5\n\7\f\7\16")
        buf.write("\7\u00e8\13\7\5\7\u00ea\n\7\3\b\3\b\3\b\5\b\u00ef\n\b")
        buf.write("\3\t\3\t\5\t\u00f3\n\t\3\t\6\t\u00f6\n\t\r\t\16\t\u00f7")
        buf.write("\3\n\3\n\3\13\3\13\3\f\6\f\u00ff\n\f\r\f\16\f\u0100\3")
        buf.write("\f\3\f\3\f\6\f\u0106\n\f\r\f\16\f\u0107\3\f\3\f\6\f\u010c")
        buf.write("\n\f\r\f\16\f\u010d\5\f\u0110\n\f\3\f\5\f\u0113\n\f\5")
        buf.write("\f\u0115\n\f\3\r\3\r\5\r\u0119\n\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)")
        buf.write("\3*\3*\3*\3+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\38\38\38\38\39\39\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3")
        buf.write(">\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3E\3E\5E\u01f7")
        buf.write("\nE\3F\3F\3F\3F\5F\u01fd\nF\3G\3G\3G\3H\3H\3I\3I\7I\u0206")
        buf.write("\nI\fI\16I\u0209\13I\3I\5I\u020c\nI\3I\3I\3J\3J\7J\u0212")
        buf.write("\nJ\fJ\16J\u0215\13J\3J\3J\7J\u0219\nJ\fJ\16J\u021c\13")
        buf.write("J\3J\3J\3J\3K\3K\3K\3K\7K\u0225\nK\fK\16K\u0228\13K\3")
        buf.write("K\3K\3K\3K\5K\u022e\nK\3L\3L\7L\u0232\nL\fL\16L\u0235")
        buf.write("\13L\3L\3L\3L\4\u00a6\u0226\2M\3\3\5\4\7\5\t\2\13\2\r")
        buf.write("\2\17\6\21\2\23\2\25\2\27\7\31\b\33\t\35\n\37\13!\f#\r")
        buf.write("%\16\'\17)\20+\21-\22/\23\61\24\63\25\65\26\67\279\30")
        buf.write(";\31=\32?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_")
        buf.write("+a,c-e.g/i\60k\61m\62o\63q\64s\65u\66w\67y8{9}:\177;\u0081")
        buf.write("<\u0083=\u0085>\u0087?\u0089\2\u008b\2\u008d\2\u008f@")
        buf.write("\u0091A\u0093B\u0095C\u0097D\3\2\22\3\2c|\6\2\62;C\\a")
        buf.write("ac|\5\2\13\f\17\17\"\"\3\2\63;\3\2\62;\4\2\63;CH\4\2\62")
        buf.write(";CH\3\2\639\3\2\629\4\2GGgg\4\2--//\t\2))^^ddhhppttvv")
        buf.write("\3\2$$\4\2\f\f$$\3\3\f\f\4\2,,``\2\u024f\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\17\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u0099\3\2\2\2\5\u00a0")
        buf.write("\3\2\2\2\7\u00af\3\2\2\2\t\u00bd\3\2\2\2\13\u00d3\3\2")
        buf.write("\2\2\r\u00e9\3\2\2\2\17\u00ee\3\2\2\2\21\u00f0\3\2\2\2")
        buf.write("\23\u00f9\3\2\2\2\25\u00fb\3\2\2\2\27\u0114\3\2\2\2\31")
        buf.write("\u0118\3\2\2\2\33\u011a\3\2\2\2\35\u011f\3\2\2\2\37\u0125")
        buf.write("\3\2\2\2!\u012e\3\2\2\2#\u0131\3\2\2\2%\u0136\3\2\2\2")
        buf.write("\'\u013d\3\2\2\2)\u0145\3\2\2\2+\u014b\3\2\2\2-\u0152")
        buf.write("\3\2\2\2/\u015b\3\2\2\2\61\u015f\3\2\2\2\63\u0168\3\2")
        buf.write("\2\2\65\u016b\3\2\2\2\67\u0175\3\2\2\29\u017c\3\2\2\2")
        buf.write(";\u0181\3\2\2\2=\u0185\3\2\2\2?\u018b\3\2\2\2A\u0190\3")
        buf.write("\2\2\2C\u0196\3\2\2\2E\u019c\3\2\2\2G\u019e\3\2\2\2I\u01a1")
        buf.write("\3\2\2\2K\u01a3\3\2\2\2M\u01a6\3\2\2\2O\u01a8\3\2\2\2")
        buf.write("Q\u01ab\3\2\2\2S\u01ad\3\2\2\2U\u01b0\3\2\2\2W\u01b2\3")
        buf.write("\2\2\2Y\u01b4\3\2\2\2[\u01b7\3\2\2\2]\u01ba\3\2\2\2_\u01bd")
        buf.write("\3\2\2\2a\u01c0\3\2\2\2c\u01c2\3\2\2\2e\u01c4\3\2\2\2")
        buf.write("g\u01c7\3\2\2\2i\u01ca\3\2\2\2k\u01ce\3\2\2\2m\u01d1\3")
        buf.write("\2\2\2o\u01d4\3\2\2\2q\u01d8\3\2\2\2s\u01dc\3\2\2\2u\u01de")
        buf.write("\3\2\2\2w\u01e0\3\2\2\2y\u01e2\3\2\2\2{\u01e4\3\2\2\2")
        buf.write("}\u01e6\3\2\2\2\177\u01e8\3\2\2\2\u0081\u01ea\3\2\2\2")
        buf.write("\u0083\u01ec\3\2\2\2\u0085\u01ee\3\2\2\2\u0087\u01f0\3")
        buf.write("\2\2\2\u0089\u01f6\3\2\2\2\u008b\u01fc\3\2\2\2\u008d\u01fe")
        buf.write("\3\2\2\2\u008f\u0201\3\2\2\2\u0091\u0203\3\2\2\2\u0093")
        buf.write("\u020f\3\2\2\2\u0095\u0220\3\2\2\2\u0097\u022f\3\2\2\2")
        buf.write("\u0099\u009d\t\2\2\2\u009a\u009c\t\3\2\2\u009b\u009a\3")
        buf.write("\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e")
        buf.write("\3\2\2\2\u009e\4\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a1")
        buf.write("\7,\2\2\u00a1\u00a2\7,\2\2\u00a2\u00a6\3\2\2\2\u00a3\u00a5")
        buf.write("\13\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6")
        buf.write("\u00a7\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a9\3\2\2\2")
        buf.write("\u00a8\u00a6\3\2\2\2\u00a9\u00aa\7,\2\2\u00aa\u00ab\7")
        buf.write(",\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\b\3\2\2\u00ad\6")
        buf.write("\3\2\2\2\u00ae\u00b0\t\4\2\2\u00af\u00ae\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2")
        buf.write("\u00b2\u00b3\3\2\2\2\u00b3\u00b4\b\4\2\2\u00b4\b\3\2\2")
        buf.write("\2\u00b5\u00be\7\62\2\2\u00b6\u00ba\t\5\2\2\u00b7\u00b9")
        buf.write("\t\6\2\2\u00b8\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba")
        buf.write("\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00be\3\2\2\2")
        buf.write("\u00bc\u00ba\3\2\2\2\u00bd\u00b5\3\2\2\2\u00bd\u00b6\3")
        buf.write("\2\2\2\u00be\n\3\2\2\2\u00bf\u00c0\7\62\2\2\u00c0\u00c1")
        buf.write("\7z\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c6\t\7\2\2\u00c3")
        buf.write("\u00c5\t\b\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2")
        buf.write("\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00d4\3")
        buf.write("\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\7\62\2\2\u00ca")
        buf.write("\u00cb\7Z\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00d0\t\7\2\2")
        buf.write("\u00cd\u00cf\t\b\2\2\u00ce\u00cd\3\2\2\2\u00cf\u00d2\3")
        buf.write("\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d4")
        buf.write("\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00bf\3\2\2\2\u00d3")
        buf.write("\u00c9\3\2\2\2\u00d4\f\3\2\2\2\u00d5\u00d6\7\62\2\2\u00d6")
        buf.write("\u00d7\7q\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00dc\t\t\2\2")
        buf.write("\u00d9\u00db\t\n\2\2\u00da\u00d9\3\2\2\2\u00db\u00de\3")
        buf.write("\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00ea")
        buf.write("\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e0\7\62\2\2\u00e0")
        buf.write("\u00e1\7Q\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e6\t\t\2\2")
        buf.write("\u00e3\u00e5\t\n\2\2\u00e4\u00e3\3\2\2\2\u00e5\u00e8\3")
        buf.write("\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00ea")
        buf.write("\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00d5\3\2\2\2\u00e9")
        buf.write("\u00df\3\2\2\2\u00ea\16\3\2\2\2\u00eb\u00ef\5\t\5\2\u00ec")
        buf.write("\u00ef\5\13\6\2\u00ed\u00ef\5\r\7\2\u00ee\u00eb\3\2\2")
        buf.write("\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\20\3")
        buf.write("\2\2\2\u00f0\u00f2\t\13\2\2\u00f1\u00f3\5\25\13\2\u00f2")
        buf.write("\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f5\3\2\2\2")
        buf.write("\u00f4\u00f6\5\23\n\2\u00f5\u00f4\3\2\2\2\u00f6\u00f7")
        buf.write("\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8")
        buf.write("\22\3\2\2\2\u00f9\u00fa\t\6\2\2\u00fa\24\3\2\2\2\u00fb")
        buf.write("\u00fc\t\f\2\2\u00fc\26\3\2\2\2\u00fd\u00ff\5\23\n\2\u00fe")
        buf.write("\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u00fe\3\2\2\2")
        buf.write("\u0100\u0101\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0103\5")
        buf.write("\21\t\2\u0103\u0115\3\2\2\2\u0104\u0106\5\23\n\2\u0105")
        buf.write("\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0107\u0108\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010f\5")
        buf.write("u;\2\u010a\u010c\5\23\n\2\u010b\u010a\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e")
        buf.write("\u0110\3\2\2\2\u010f\u010b\3\2\2\2\u010f\u0110\3\2\2\2")
        buf.write("\u0110\u0112\3\2\2\2\u0111\u0113\5\21\t\2\u0112\u0111")
        buf.write("\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0115\3\2\2\2\u0114")
        buf.write("\u00fe\3\2\2\2\u0114\u0105\3\2\2\2\u0115\30\3\2\2\2\u0116")
        buf.write("\u0119\5? \2\u0117\u0119\5A!\2\u0118\u0116\3\2\2\2\u0118")
        buf.write("\u0117\3\2\2\2\u0119\32\3\2\2\2\u011a\u011b\7D\2\2\u011b")
        buf.write("\u011c\7q\2\2\u011c\u011d\7f\2\2\u011d\u011e\7{\2\2\u011e")
        buf.write("\34\3\2\2\2\u011f\u0120\7D\2\2\u0120\u0121\7t\2\2\u0121")
        buf.write("\u0122\7g\2\2\u0122\u0123\7c\2\2\u0123\u0124\7m\2\2\u0124")
        buf.write("\36\3\2\2\2\u0125\u0126\7E\2\2\u0126\u0127\7q\2\2\u0127")
        buf.write("\u0128\7p\2\2\u0128\u0129\7v\2\2\u0129\u012a\7k\2\2\u012a")
        buf.write("\u012b\7p\2\2\u012b\u012c\7w\2\2\u012c\u012d\7g\2\2\u012d")
        buf.write(" \3\2\2\2\u012e\u012f\7F\2\2\u012f\u0130\7q\2\2\u0130")
        buf.write("\"\3\2\2\2\u0131\u0132\7G\2\2\u0132\u0133\7n\2\2\u0133")
        buf.write("\u0134\7u\2\2\u0134\u0135\7g\2\2\u0135$\3\2\2\2\u0136")
        buf.write("\u0137\7G\2\2\u0137\u0138\7n\2\2\u0138\u0139\7u\2\2\u0139")
        buf.write("\u013a\7g\2\2\u013a\u013b\7K\2\2\u013b\u013c\7h\2\2\u013c")
        buf.write("&\3\2\2\2\u013d\u013e\7G\2\2\u013e\u013f\7p\2\2\u013f")
        buf.write("\u0140\7f\2\2\u0140\u0141\7D\2\2\u0141\u0142\7q\2\2\u0142")
        buf.write("\u0143\7f\2\2\u0143\u0144\7{\2\2\u0144(\3\2\2\2\u0145")
        buf.write("\u0146\7G\2\2\u0146\u0147\7p\2\2\u0147\u0148\7f\2\2\u0148")
        buf.write("\u0149\7K\2\2\u0149\u014a\7h\2\2\u014a*\3\2\2\2\u014b")
        buf.write("\u014c\7G\2\2\u014c\u014d\7p\2\2\u014d\u014e\7f\2\2\u014e")
        buf.write("\u014f\7H\2\2\u014f\u0150\7q\2\2\u0150\u0151\7t\2\2\u0151")
        buf.write(",\3\2\2\2\u0152\u0153\7G\2\2\u0153\u0154\7p\2\2\u0154")
        buf.write("\u0155\7f\2\2\u0155\u0156\7Y\2\2\u0156\u0157\7j\2\2\u0157")
        buf.write("\u0158\7k\2\2\u0158\u0159\7n\2\2\u0159\u015a\7g\2\2\u015a")
        buf.write(".\3\2\2\2\u015b\u015c\7H\2\2\u015c\u015d\7q\2\2\u015d")
        buf.write("\u015e\7t\2\2\u015e\60\3\2\2\2\u015f\u0160\7H\2\2\u0160")
        buf.write("\u0161\7w\2\2\u0161\u0162\7p\2\2\u0162\u0163\7e\2\2\u0163")
        buf.write("\u0164\7v\2\2\u0164\u0165\7k\2\2\u0165\u0166\7q\2\2\u0166")
        buf.write("\u0167\7p\2\2\u0167\62\3\2\2\2\u0168\u0169\7K\2\2\u0169")
        buf.write("\u016a\7h\2\2\u016a\64\3\2\2\2\u016b\u016c\7R\2\2\u016c")
        buf.write("\u016d\7c\2\2\u016d\u016e\7t\2\2\u016e\u016f\7c\2\2\u016f")
        buf.write("\u0170\7o\2\2\u0170\u0171\7g\2\2\u0171\u0172\7v\2\2\u0172")
        buf.write("\u0173\7g\2\2\u0173\u0174\7t\2\2\u0174\66\3\2\2\2\u0175")
        buf.write("\u0176\7T\2\2\u0176\u0177\7g\2\2\u0177\u0178\7v\2\2\u0178")
        buf.write("\u0179\7w\2\2\u0179\u017a\7t\2\2\u017a\u017b\7p\2\2\u017b")
        buf.write("8\3\2\2\2\u017c\u017d\7V\2\2\u017d\u017e\7j\2\2\u017e")
        buf.write("\u017f\7g\2\2\u017f\u0180\7p\2\2\u0180:\3\2\2\2\u0181")
        buf.write("\u0182\7X\2\2\u0182\u0183\7c\2\2\u0183\u0184\7t\2\2\u0184")
        buf.write("<\3\2\2\2\u0185\u0186\7Y\2\2\u0186\u0187\7j\2\2\u0187")
        buf.write("\u0188\7k\2\2\u0188\u0189\7n\2\2\u0189\u018a\7g\2\2\u018a")
        buf.write(">\3\2\2\2\u018b\u018c\7V\2\2\u018c\u018d\7t\2\2\u018d")
        buf.write("\u018e\7w\2\2\u018e\u018f\7g\2\2\u018f@\3\2\2\2\u0190")
        buf.write("\u0191\7H\2\2\u0191\u0192\7c\2\2\u0192\u0193\7n\2\2\u0193")
        buf.write("\u0194\7u\2\2\u0194\u0195\7g\2\2\u0195B\3\2\2\2\u0196")
        buf.write("\u0197\7G\2\2\u0197\u0198\7p\2\2\u0198\u0199\7f\2\2\u0199")
        buf.write("\u019a\7F\2\2\u019a\u019b\7q\2\2\u019bD\3\2\2\2\u019c")
        buf.write("\u019d\7-\2\2\u019dF\3\2\2\2\u019e\u019f\7-\2\2\u019f")
        buf.write("\u01a0\7\60\2\2\u01a0H\3\2\2\2\u01a1\u01a2\7/\2\2\u01a2")
        buf.write("J\3\2\2\2\u01a3\u01a4\7/\2\2\u01a4\u01a5\7\60\2\2\u01a5")
        buf.write("L\3\2\2\2\u01a6\u01a7\7,\2\2\u01a7N\3\2\2\2\u01a8\u01a9")
        buf.write("\7,\2\2\u01a9\u01aa\7\60\2\2\u01aaP\3\2\2\2\u01ab\u01ac")
        buf.write("\7^\2\2\u01acR\3\2\2\2\u01ad\u01ae\7^\2\2\u01ae\u01af")
        buf.write("\7\60\2\2\u01afT\3\2\2\2\u01b0\u01b1\7\'\2\2\u01b1V\3")
        buf.write("\2\2\2\u01b2\u01b3\7#\2\2\u01b3X\3\2\2\2\u01b4\u01b5\7")
        buf.write("(\2\2\u01b5\u01b6\7(\2\2\u01b6Z\3\2\2\2\u01b7\u01b8\7")
        buf.write("~\2\2\u01b8\u01b9\7~\2\2\u01b9\\\3\2\2\2\u01ba\u01bb\7")
        buf.write("?\2\2\u01bb\u01bc\7?\2\2\u01bc^\3\2\2\2\u01bd\u01be\7")
        buf.write("#\2\2\u01be\u01bf\7?\2\2\u01bf`\3\2\2\2\u01c0\u01c1\7")
        buf.write(">\2\2\u01c1b\3\2\2\2\u01c2\u01c3\7@\2\2\u01c3d\3\2\2\2")
        buf.write("\u01c4\u01c5\7>\2\2\u01c5\u01c6\7?\2\2\u01c6f\3\2\2\2")
        buf.write("\u01c7\u01c8\7@\2\2\u01c8\u01c9\7?\2\2\u01c9h\3\2\2\2")
        buf.write("\u01ca\u01cb\7?\2\2\u01cb\u01cc\7\61\2\2\u01cc\u01cd\7")
        buf.write("?\2\2\u01cdj\3\2\2\2\u01ce\u01cf\7>\2\2\u01cf\u01d0\7")
        buf.write("\60\2\2\u01d0l\3\2\2\2\u01d1\u01d2\7@\2\2\u01d2\u01d3")
        buf.write("\7\60\2\2\u01d3n\3\2\2\2\u01d4\u01d5\7>\2\2\u01d5\u01d6")
        buf.write("\7?\2\2\u01d6\u01d7\7\60\2\2\u01d7p\3\2\2\2\u01d8\u01d9")
        buf.write("\7@\2\2\u01d9\u01da\7?\2\2\u01da\u01db\7\60\2\2\u01db")
        buf.write("r\3\2\2\2\u01dc\u01dd\7?\2\2\u01ddt\3\2\2\2\u01de\u01df")
        buf.write("\7\60\2\2\u01dfv\3\2\2\2\u01e0\u01e1\7.\2\2\u01e1x\3\2")
        buf.write("\2\2\u01e2\u01e3\7*\2\2\u01e3z\3\2\2\2\u01e4\u01e5\7+")
        buf.write("\2\2\u01e5|\3\2\2\2\u01e6\u01e7\7=\2\2\u01e7~\3\2\2\2")
        buf.write("\u01e8\u01e9\7<\2\2\u01e9\u0080\3\2\2\2\u01ea\u01eb\7")
        buf.write("]\2\2\u01eb\u0082\3\2\2\2\u01ec\u01ed\7_\2\2\u01ed\u0084")
        buf.write("\3\2\2\2\u01ee\u01ef\7}\2\2\u01ef\u0086\3\2\2\2\u01f0")
        buf.write("\u01f1\7\177\2\2\u01f1\u0088\3\2\2\2\u01f2\u01f3\7^\2")
        buf.write("\2\u01f3\u01f7\n\r\2\2\u01f4\u01f5\7)\2\2\u01f5\u01f7")
        buf.write("\n\16\2\2\u01f6\u01f2\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7")
        buf.write("\u008a\3\2\2\2\u01f8\u01f9\7)\2\2\u01f9\u01fd\7$\2\2\u01fa")
        buf.write("\u01fd\n\17\2\2\u01fb\u01fd\5\u008dG\2\u01fc\u01f8\3\2")
        buf.write("\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fb\3\2\2\2\u01fd\u008c")
        buf.write("\3\2\2\2\u01fe\u01ff\7^\2\2\u01ff\u0200\t\r\2\2\u0200")
        buf.write("\u008e\3\2\2\2\u0201\u0202\13\2\2\2\u0202\u0090\3\2\2")
        buf.write("\2\u0203\u0207\7$\2\2\u0204\u0206\5\u008bF\2\u0205\u0204")
        buf.write("\3\2\2\2\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2\u0207")
        buf.write("\u0208\3\2\2\2\u0208\u020b\3\2\2\2\u0209\u0207\3\2\2\2")
        buf.write("\u020a\u020c\t\20\2\2\u020b\u020a\3\2\2\2\u020c\u020d")
        buf.write("\3\2\2\2\u020d\u020e\bI\3\2\u020e\u0092\3\2\2\2\u020f")
        buf.write("\u0213\7$\2\2\u0210\u0212\5\u008bF\2\u0211\u0210\3\2\2")
        buf.write("\2\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214")
        buf.write("\3\2\2\2\u0214\u0216\3\2\2\2\u0215\u0213\3\2\2\2\u0216")
        buf.write("\u021a\5\u0089E\2\u0217\u0219\5\u008bF\2\u0218\u0217\3")
        buf.write("\2\2\2\u0219\u021c\3\2\2\2\u021a\u0218\3\2\2\2\u021a\u021b")
        buf.write("\3\2\2\2\u021b\u021d\3\2\2\2\u021c\u021a\3\2\2\2\u021d")
        buf.write("\u021e\7$\2\2\u021e\u021f\bJ\4\2\u021f\u0094\3\2\2\2\u0220")
        buf.write("\u0221\7,\2\2\u0221\u0222\7,\2\2\u0222\u0226\3\2\2\2\u0223")
        buf.write("\u0225\13\2\2\2\u0224\u0223\3\2\2\2\u0225\u0228\3\2\2")
        buf.write("\2\u0226\u0227\3\2\2\2\u0226\u0224\3\2\2\2\u0227\u022d")
        buf.write("\3\2\2\2\u0228\u0226\3\2\2\2\u0229\u022a\t\21\2\2\u022a")
        buf.write("\u022e\7,\2\2\u022b\u022c\7,\2\2\u022c\u022e\t\21\2\2")
        buf.write("\u022d\u0229\3\2\2\2\u022d\u022b\3\2\2\2\u022d\u022e\3")
        buf.write("\2\2\2\u022e\u0096\3\2\2\2\u022f\u0233\7$\2\2\u0230\u0232")
        buf.write("\5\u008bF\2\u0231\u0230\3\2\2\2\u0232\u0235\3\2\2\2\u0233")
        buf.write("\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0236\3\2\2\2")
        buf.write("\u0235\u0233\3\2\2\2\u0236\u0237\7$\2\2\u0237\u0238\b")
        buf.write("L\5\2\u0238\u0098\3\2\2\2!\2\u009d\u00a6\u00b1\u00ba\u00bd")
        buf.write("\u00c6\u00d0\u00d3\u00dc\u00e6\u00e9\u00ee\u00f2\u00f7")
        buf.write("\u0100\u0107\u010d\u010f\u0112\u0114\u0118\u01f6\u01fc")
        buf.write("\u0207\u020b\u0213\u021a\u0226\u022d\u0233\6\b\2\2\3I")
        buf.write("\2\3J\3\3L\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    BLOCK_COMMENT = 2
    WS = 3
    INTEGER_LITERAL = 4
    FLOAT_LITERAL = 5
    BOOLEAN_LITERAL = 6
    BODY = 7
    BREAK = 8
    CONTINUE = 9
    DO = 10
    ELSE = 11
    ELSEIF = 12
    ENDBODY = 13
    ENDIF = 14
    ENDFOR = 15
    ENDWHILE = 16
    FOR = 17
    FUCNTION = 18
    IF = 19
    PARAMETER = 20
    RETURN = 21
    THEN = 22
    VAR = 23
    WHILE = 24
    TRUE = 25
    FALSE = 26
    ENDDO = 27
    ADD = 28
    ADD_F = 29
    SUB = 30
    SUB_F = 31
    MUL = 32
    MUL_F = 33
    DIV = 34
    DIV_F = 35
    MOD = 36
    NOT = 37
    AND_OP = 38
    OR_OP = 39
    EQUAL_OP = 40
    DIFF_OP = 41
    LT = 42
    GT = 43
    LTE = 44
    GTE = 45
    DIV_FRAC = 46
    LT_F = 47
    GT_F = 48
    LTE_F = 49
    GTE_F = 50
    EQ = 51
    DOT = 52
    COMMA = 53
    LP = 54
    RP = 55
    SEMI = 56
    COLON = 57
    LSB = 58
    RSB = 59
    LCB = 60
    RCB = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    UNTERMINATED_COMMENT = 65
    STRING_LITERAL = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
            "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", 
            "'>.'", "'<=.'", "'>=.'", "'='", "'.'", "','", "'('", "')'", 
            "';'", "':'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "BLOCK_COMMENT", "WS", "INTEGER_LITERAL", "FLOAT_LITERAL", 
            "BOOLEAN_LITERAL", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
            "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUCNTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
            "FALSE", "ENDDO", "ADD", "ADD_F", "SUB", "SUB_F", "MUL", "MUL_F", 
            "DIV", "DIV_F", "MOD", "NOT", "AND_OP", "OR_OP", "EQUAL_OP", 
            "DIFF_OP", "LT", "GT", "LTE", "GTE", "DIV_FRAC", "LT_F", "GT_F", 
            "LTE_F", "GTE_F", "EQ", "DOT", "COMMA", "LP", "RP", "SEMI", 
            "COLON", "LSB", "RSB", "LCB", "RCB", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", "STRING_LITERAL" ]

    ruleNames = [ "ID", "BLOCK_COMMENT", "WS", "INT_LIT_BASE10", "INT_LIT_BASE16", 
                  "INT_LIT_BASE8", "INTEGER_LITERAL", "EXPONENT", "DIGIT", 
                  "SIGN", "FLOAT_LITERAL", "BOOLEAN_LITERAL", "BODY", "BREAK", 
                  "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                  "ENDFOR", "ENDWHILE", "FOR", "FUCNTION", "IF", "PARAMETER", 
                  "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
                  "ADD", "ADD_F", "SUB", "SUB_F", "MUL", "MUL_F", "DIV", 
                  "DIV_F", "MOD", "NOT", "AND_OP", "OR_OP", "EQUAL_OP", 
                  "DIFF_OP", "LT", "GT", "LTE", "GTE", "DIV_FRAC", "LT_F", 
                  "GT_F", "LTE_F", "GTE_F", "EQ", "DOT", "COMMA", "LP", 
                  "RP", "SEMI", "COLON", "LSB", "RSB", "LCB", "RCB", "ESC_ILLEGAL", 
                  "STR_CHAR", "ESC_SEQ", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", "STRING_LITERAL" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.STRING_LITERAL_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            if self.text[-1] != '\n':
                self.text = self.text[1:]
            else:
                self.text = self.text[1:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            num = [m for m, c in enumerate(self.text) if c == '\\' or c == '\'']
            for ch in num:
                if (self.text[ch] == '\\') and (self.text[ch + 1] not in ['b','t','n','f','r','\'','\\']):
                    self.text = self.text[1: (ch+2)]
                    break
                elif (self.text[ch] == '\'') and (self.text[ch + 1] != '\"'):
                    self.text = self.text[1: (ch+2)]
                    break

     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     


