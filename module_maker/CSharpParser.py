# Generated from CSharpParser.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u00c8")
        buf.write("\u0a54\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4")
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4")
        buf.write("h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4p\tp\4")
        buf.write("q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4")
        buf.write("z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080\t\u0080")
        buf.write("\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083\4\u0084")
        buf.write("\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087")
        buf.write("\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a\t\u008a\4\u008b")
        buf.write("\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d\4\u008e\t\u008e")
        buf.write("\4\u008f\t\u008f\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092")
        buf.write("\t\u0092\4\u0093\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095")
        buf.write("\4\u0096\t\u0096\4\u0097\t\u0097\4\u0098\t\u0098\4\u0099")
        buf.write("\t\u0099\4\u009a\t\u009a\4\u009b\t\u009b\4\u009c\t\u009c")
        buf.write("\4\u009d\t\u009d\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0")
        buf.write("\t\u00a0\4\u00a1\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3")
        buf.write("\4\u00a4\t\u00a4\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7")
        buf.write("\t\u00a7\4\u00a8\t\u00a8\4\u00a9\t\u00a9\4\u00aa\t\u00aa")
        buf.write("\4\u00ab\t\u00ab\4\u00ac\t\u00ac\4\u00ad\t\u00ad\4\u00ae")
        buf.write("\t\u00ae\4\u00af\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1")
        buf.write("\4\u00b2\t\u00b2\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5")
        buf.write("\t\u00b5\4\u00b6\t\u00b6\4\u00b7\t\u00b7\4\u00b8\t\u00b8")
        buf.write("\4\u00b9\t\u00b9\4\u00ba\t\u00ba\4\u00bb\t\u00bb\4\u00bc")
        buf.write("\t\u00bc\4\u00bd\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf")
        buf.write("\4\u00c0\t\u00c0\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3")
        buf.write("\t\u00c3\4\u00c4\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6")
        buf.write("\4\u00c7\t\u00c7\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca")
        buf.write("\t\u00ca\4\u00cb\t\u00cb\4\u00cc\t\u00cc\4\u00cd\t\u00cd")
        buf.write("\4\u00ce\t\u00ce\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1")
        buf.write("\t\u00d1\4\u00d2\t\u00d2\4\u00d3\t\u00d3\4\u00d4\t\u00d4")
        buf.write("\4\u00d5\t\u00d5\4\u00d6\t\u00d6\4\u00d7\t\u00d7\4\u00d8")
        buf.write("\t\u00d8\4\u00d9\t\u00d9\4\u00da\t\u00da\4\u00db\t\u00db")
        buf.write("\3\2\5\2\u01b8\n\2\3\2\5\2\u01bb\n\2\3\2\5\2\u01be\n\2")
        buf.write("\3\2\7\2\u01c1\n\2\f\2\16\2\u01c4\13\2\3\2\5\2\u01c7\n")
        buf.write("\2\3\2\3\2\3\3\3\3\5\3\u01cd\n\3\3\3\5\3\u01d0\n\3\3\3")
        buf.write("\3\3\3\3\5\3\u01d5\n\3\7\3\u01d7\n\3\f\3\16\3\u01da\13")
        buf.write("\3\3\4\3\4\3\4\3\4\7\4\u01e0\n\4\f\4\16\4\u01e3\13\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5\u01ea\n\5\3\6\3\6\3\6\3\6\6\6\u01f0")
        buf.write("\n\6\r\6\16\6\u01f1\3\6\3\6\3\7\3\7\5\7\u01f8\n\7\3\b")
        buf.write("\3\b\5\b\u01fc\n\b\3\t\3\t\3\t\5\t\u0201\n\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\5\f\u020b\n\f\3\r\3\r\3\r\3\r")
        buf.write("\7\r\u0211\n\r\f\r\16\r\u0214\13\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\7\16\u021b\n\16\f\16\16\16\u021e\13\16\3\17\3\17\3")
        buf.write("\17\5\17\u0223\n\17\3\17\5\17\u0226\n\17\3\17\3\17\5\17")
        buf.write("\u022a\n\17\3\17\3\17\3\20\3\20\3\20\3\20\5\20\u0232\n")
        buf.write("\20\3\21\3\21\3\21\5\21\u0237\n\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u0241\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u024e\n\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0256\n\24\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u025c\n\25\5\25\u025e\n\25\3\26\3\26")
        buf.write("\3\26\7\26\u0263\n\26\f\26\16\26\u0266\13\26\3\27\3\27")
        buf.write("\3\27\7\27\u026b\n\27\f\27\16\27\u026e\13\27\3\30\3\30")
        buf.write("\3\30\7\30\u0273\n\30\f\30\16\30\u0276\13\30\3\31\3\31")
        buf.write("\3\31\7\31\u027b\n\31\f\31\16\31\u027e\13\31\3\32\3\32")
        buf.write("\3\32\7\32\u0283\n\32\f\32\16\32\u0286\13\32\3\33\3\33")
        buf.write("\3\33\7\33\u028b\n\33\f\33\16\33\u028e\13\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\7\34\u0297\n\34\f\34\16\34\u029a")
        buf.write("\13\34\3\35\3\35\3\35\5\35\u029f\n\35\3\35\7\35\u02a2")
        buf.write("\n\35\f\35\16\35\u02a5\13\35\3\36\3\36\3\36\7\36\u02aa")
        buf.write("\n\36\f\36\16\36\u02ad\13\36\3\37\3\37\3\37\7\37\u02b2")
        buf.write("\n\37\f\37\16\37\u02b5\13\37\3 \3 \3 \3 \3 \5 \u02bc\n")
        buf.write(" \5 \u02be\n \3 \5 \u02c1\n \3!\3!\3!\7!\u02c6\n!\f!\16")
        buf.write("!\u02c9\13!\3\"\3\"\5\"\u02cd\n\"\3\"\3\"\3\"\3#\3#\5")
        buf.write("#\u02d4\n#\3#\3#\5#\u02d8\n#\5#\u02da\n#\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\5$\u02f6\n$\3%\3%\5%\u02fa\n%\3%\7%\u02fd\n")
        buf.write("%\f%\16%\u0300\13%\3%\5%\u0303\n%\3%\3%\3%\3%\3%\3%\5")
        buf.write("%\u030b\n%\3%\5%\u030e\n%\3%\7%\u0311\n%\f%\16%\u0314")
        buf.write("\13%\3%\5%\u0317\n%\7%\u0319\n%\f%\16%\u031c\13%\3&\3")
        buf.write("&\3&\5&\u0321\n&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5")
        buf.write("&\u032f\n&\3&\3&\3&\3&\5&\u0335\n&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\7&\u033f\n&\f&\16&\u0342\13&\3&\5&\u0345\n&\3&\6")
        buf.write("&\u0348\n&\r&\16&\u0349\3&\3&\5&\u034e\n&\3&\3&\3&\3&")
        buf.write("\5&\u0354\n&\3&\3&\3&\3&\6&\u035a\n&\r&\16&\u035b\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\5&\u0365\n&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\5&\u0377\n&\3&\5&\u037a\n&\3&\3")
        buf.write("&\3&\5&\u037f\n&\3&\5&\u0382\n&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\7&\u038f\n&\f&\16&\u0392\13&\3&\3&\3&\5&\u0397")
        buf.write("\n&\3\'\3\'\5\'\u039b\n\'\3(\3(\3(\3)\5)\u03a1\n)\3)\3")
        buf.write(")\3)\5)\u03a6\n)\3*\5*\u03a9\n*\3*\3*\3*\3*\7*\u03af\n")
        buf.write("*\f*\16*\u03b2\13*\3*\3*\3+\3+\3+\5+\u03b9\n+\3+\3+\3")
        buf.write(",\3,\3-\3-\3-\7-\u03c2\n-\f-\16-\u03c5\13-\3.\3.\5.\u03c9")
        buf.write("\n.\3/\3/\3/\5/\u03ce\n/\5/\u03d0\n/\3/\3/\3\60\3\60\3")
        buf.write("\60\7\60\u03d7\n\60\f\60\16\60\u03da\13\60\3\61\3\61\3")
        buf.write("\61\3\61\3\61\5\61\u03e1\n\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\5\62\u03e8\n\62\3\63\3\63\3\63\3\63\7\63\u03ee\n\63\f")
        buf.write("\63\16\63\u03f1\13\63\3\63\5\63\u03f4\n\63\3\63\3\63\3")
        buf.write("\64\3\64\3\64\3\64\3\64\5\64\u03fd\n\64\3\65\3\65\3\65")
        buf.write("\5\65\u0402\n\65\5\65\u0404\n\65\3\65\3\65\3\66\3\66\3")
        buf.write("\66\7\66\u040b\n\66\f\66\16\66\u040e\13\66\3\67\3\67\3")
        buf.write("\67\3\67\3\67\5\67\u0415\n\67\38\38\58\u0419\n8\38\38")
        buf.write("\38\58\u041e\n8\58\u0420\n8\38\38\38\58\u0425\n8\78\u0427")
        buf.write("\n8\f8\168\u042a\138\39\39\79\u042e\n9\f9\169\u0431\13")
        buf.write("9\39\39\3:\3:\3:\7:\u0438\n:\f:\16:\u043b\13:\3:\5:\u043e")
        buf.write("\n:\3:\5:\u0441\n:\3:\5:\u0444\n:\3;\3;\3;\3;\7;\u044a")
        buf.write("\n;\f;\16;\u044d\13;\3;\3;\3<\3<\3<\3<\3=\5=\u0456\n=")
        buf.write("\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\5>\u0467")
        buf.write("\n>\3?\3?\3?\7?\u046c\n?\f?\16?\u046f\13?\3@\5@\u0472")
        buf.write("\n@\3@\3@\3@\3A\3A\3A\7A\u047a\nA\fA\16A\u047d\13A\3B")
        buf.write("\3B\5B\u0481\nB\3C\3C\3C\3D\3D\5D\u0488\nD\3D\3D\3D\3")
        buf.write("D\3E\7E\u048f\nE\fE\16E\u0492\13E\3E\3E\5E\u0496\nE\3")
        buf.write("F\3F\3F\3F\3F\5F\u049d\nF\3G\3G\3G\3G\3G\3H\3H\3H\3I\3")
        buf.write("I\5I\u04a9\nI\3I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u04b4\nI\3")
        buf.write("J\3J\3J\3J\7J\u04ba\nJ\fJ\16J\u04bd\13J\3K\3K\5K\u04c1")
        buf.write("\nK\3L\3L\3L\3L\3L\3L\3L\5L\u04ca\nL\3M\3M\3M\3M\3N\3")
        buf.write("N\3N\5N\u04d3\nN\3O\3O\3O\3O\3O\3O\3O\5O\u04dc\nO\3P\3")
        buf.write("P\3P\3Q\5Q\u04e2\nQ\3Q\3Q\3Q\5Q\u04e7\nQ\3Q\3Q\5Q\u04eb")
        buf.write("\nQ\3Q\3Q\5Q\u04ef\nQ\3R\3R\5R\u04f3\nR\3R\3R\5R\u04f7")
        buf.write("\nR\3S\3S\3S\3S\3S\5S\u04fe\nS\3T\3T\3T\3T\3U\3U\5U\u0506")
        buf.write("\nU\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\5V\u0513\nV\3V\3")
        buf.write("V\3V\3V\3V\3V\7V\u051b\nV\fV\16V\u051e\13V\3V\3V\3V\3")
        buf.write("V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\5V\u0533")
        buf.write("\nV\3V\3V\5V\u0537\nV\3V\3V\5V\u053b\nV\3V\3V\3V\5V\u0540")
        buf.write("\nV\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3")
        buf.write("V\3V\5V\u0554\nV\3V\3V\3V\5V\u0559\nV\3V\3V\3V\5V\u055e")
        buf.write("\nV\3V\3V\3V\3V\3V\5V\u0565\nV\3V\5V\u0568\nV\3V\3V\3")
        buf.write("V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\5")
        buf.write("V\u057e\nV\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\5V\u058a\nV\3")
        buf.write("W\3W\5W\u058e\nW\3W\3W\3X\3X\3X\3X\5X\u0596\nX\3X\3X\3")
        buf.write("X\3X\7X\u059c\nX\fX\16X\u059f\13X\3X\3X\3X\3X\5X\u05a5")
        buf.write("\nX\3Y\3Y\5Y\u05a9\nY\3Z\3Z\3Z\5Z\u05ae\nZ\3Z\5Z\u05b1")
        buf.write("\nZ\3[\3[\3[\5[\u05b6\n[\3\\\3\\\3\\\3\\\3]\3]\5]\u05be")
        buf.write("\n]\3^\6^\u05c1\n^\r^\16^\u05c2\3^\3^\3_\3_\3_\5_\u05ca")
        buf.write("\n_\3_\3_\3_\3_\5_\u05d0\n_\3`\3`\3`\3a\6a\u05d6\na\r")
        buf.write("a\16a\u05d7\3b\3b\3b\3b\7b\u05de\nb\fb\16b\u05e1\13b\5")
        buf.write("b\u05e3\nb\3c\3c\3c\7c\u05e8\nc\fc\16c\u05eb\13c\3d\3")
        buf.write("d\7d\u05ef\nd\fd\16d\u05f2\13d\3d\5d\u05f5\nd\3d\5d\u05f8")
        buf.write("\nd\3e\3e\3e\3e\5e\u05fe\ne\3e\3e\5e\u0602\ne\3e\3e\3")
        buf.write("f\3f\5f\u0608\nf\3f\3f\3g\3g\3g\3g\3g\3h\3h\3h\3i\3i\5")
        buf.write("i\u0616\ni\3j\3j\3j\3j\5j\u061c\nj\3k\3k\3k\7k\u0621\n")
        buf.write("k\fk\16k\u0624\13k\3l\3l\5l\u0628\nl\3l\5l\u062b\nl\3")
        buf.write("l\5l\u062e\nl\3l\3l\3m\6m\u0633\nm\rm\16m\u0634\3n\3n")
        buf.write("\3n\3n\3n\3o\6o\u063d\no\ro\16o\u063e\3p\3p\3p\3p\3p\3")
        buf.write("p\3p\3p\3p\3p\3p\3p\3p\3p\3p\5p\u0650\np\3q\6q\u0653\n")
        buf.write("q\rq\16q\u0654\3r\3r\5r\u0659\nr\3s\5s\u065c\ns\3s\5s")
        buf.write("\u065f\ns\3s\3s\3s\3s\3s\5s\u0666\ns\3t\3t\3t\3t\5t\u066c")
        buf.write("\nt\3u\3u\3u\3u\7u\u0672\nu\fu\16u\u0675\13u\3u\3u\3v")
        buf.write("\5v\u067a\nv\3v\3v\3w\3w\3w\3w\7w\u0682\nw\fw\16w\u0685")
        buf.write("\13w\3x\3x\3x\7x\u068a\nx\fx\16x\u068d\13x\3y\6y\u0690")
        buf.write("\ny\ry\16y\u0691\3z\3z\3z\3z\3z\3{\3{\3{\3{\5{\u069d\n")
        buf.write("{\3{\3{\5{\u06a1\n{\5{\u06a3\n{\3|\3|\3|\5|\u06a8\n|\3")
        buf.write("|\3|\5|\u06ac\n|\3}\3}\3}\7}\u06b1\n}\f}\16}\u06b4\13")
        buf.write("}\3~\3~\3~\3~\3\177\3\177\5\177\u06bc\n\177\3\177\3\177")
        buf.write("\3\u0080\6\u0080\u06c1\n\u0080\r\u0080\16\u0080\u06c2")
        buf.write("\3\u0081\5\u0081\u06c6\n\u0081\3\u0081\5\u0081\u06c9\n")
        buf.write("\u0081\3\u0081\3\u0081\5\u0081\u06cd\n\u0081\3\u0082\6")
        buf.write("\u0082\u06d0\n\u0082\r\u0082\16\u0082\u06d1\3\u0083\3")
        buf.write("\u0083\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084")
        buf.write("\3\u0084\3\u0084\3\u0084\5\u0084\u06df\n\u0084\3\u0084")
        buf.write("\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084")
        buf.write("\5\u0084\u06e9\n\u0084\3\u0085\3\u0085\3\u0085\3\u0085")
        buf.write("\3\u0085\5\u0085\u06f0\n\u0085\3\u0085\3\u0085\3\u0085")
        buf.write("\3\u0085\3\u0085\3\u0085\3\u0085\3\u0085\3\u0085\3\u0085")
        buf.write("\5\u0085\u06fc\n\u0085\3\u0086\3\u0086\3\u0086\7\u0086")
        buf.write("\u0701\n\u0086\f\u0086\16\u0086\u0704\13\u0086\3\u0087")
        buf.write("\3\u0087\3\u0087\3\u0087\3\u0088\3\u0088\3\u0088\7\u0088")
        buf.write("\u070d\n\u0088\f\u0088\16\u0088\u0710\13\u0088\3\u0089")
        buf.write("\3\u0089\3\u0089\5\u0089\u0715\n\u0089\3\u008a\3\u008a")
        buf.write("\5\u008a\u0719\n\u008a\3\u008b\3\u008b\5\u008b\u071d\n")
        buf.write("\u008b\3\u008c\3\u008c\3\u008d\3\u008d\5\u008d\u0723\n")
        buf.write("\u008d\3\u008e\3\u008e\3\u008e\3\u008e\5\u008e\u0729\n")
        buf.write("\u008e\5\u008e\u072b\n\u008e\3\u008f\3\u008f\3\u008f\7")
        buf.write("\u008f\u0730\n\u008f\f\u008f\16\u008f\u0733\13\u008f\3")
        buf.write("\u0090\5\u0090\u0736\n\u0090\3\u0090\5\u0090\u0739\n\u0090")
        buf.write("\3\u0090\3\u0090\5\u0090\u073d\n\u0090\3\u0091\3\u0091")
        buf.write("\3\u0091\3\u0091\3\u0091\3\u0091\3\u0091\3\u0091\5\u0091")
        buf.write("\u0747\n\u0091\3\u0092\5\u0092\u074a\n\u0092\3\u0092\3")
        buf.write("\u0092\3\u0092\3\u0092\3\u0093\5\u0093\u0751\n\u0093\3")
        buf.write("\u0093\5\u0093\u0754\n\u0093\3\u0093\3\u0093\3\u0093\5")
        buf.write("\u0093\u0759\n\u0093\3\u0093\3\u0093\3\u0093\5\u0093\u075e")
        buf.write("\n\u0093\5\u0093\u0760\n\u0093\3\u0094\5\u0094\u0763\n")
        buf.write("\u0094\3\u0094\5\u0094\u0766\n\u0094\3\u0094\3\u0094\3")
        buf.write("\u0094\3\u0095\5\u0095\u076c\n\u0095\3\u0095\5\u0095\u076f")
        buf.write("\n\u0095\3\u0095\3\u0095\3\u0095\3\u0096\3\u0096\3\u0096")
        buf.write("\3\u0096\3\u0096\3\u0096\3\u0096\5\u0096\u077b\n\u0096")
        buf.write("\3\u0097\3\u0097\5\u0097\u077f\n\u0097\3\u0098\5\u0098")
        buf.write("\u0782\n\u0098\3\u0098\3\u0098\3\u0098\3\u0098\3\u0098")
        buf.write("\3\u0098\3\u0098\3\u0098\5\u0098\u078c\n\u0098\3\u0099")
        buf.write("\5\u0099\u078f\n\u0099\3\u0099\3\u0099\3\u0099\3\u009a")
        buf.write("\5\u009a\u0795\n\u009a\3\u009a\3\u009a\3\u009a\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\5\u009b\u07b0\n\u009b\3\u009c\3\u009c\3\u009c\3\u009c")
        buf.write("\3\u009c\3\u009c\3\u009c\3\u009d\3\u009d\3\u009d\3\u009d")
        buf.write("\5\u009d\u07bd\n\u009d\3\u009d\3\u009d\3\u009e\3\u009e")
        buf.write("\5\u009e\u07c3\n\u009e\3\u009f\3\u009f\3\u009f\3\u00a0")
        buf.write("\3\u00a0\7\u00a0\u07ca\n\u00a0\f\u00a0\16\u00a0\u07cd")
        buf.write("\13\u00a0\3\u00a0\3\u00a0\3\u00a1\5\u00a1\u07d2\n\u00a1")
        buf.write("\3\u00a1\5\u00a1\u07d5\n\u00a1\3\u00a1\3\u00a1\3\u00a1")
        buf.write("\3\u00a1\6\u00a1\u07db\n\u00a1\r\u00a1\16\u00a1\u07dc")
        buf.write("\3\u00a1\3\u00a1\5\u00a1\u07e1\n\u00a1\3\u00a2\3\u00a2")
        buf.write("\7\u00a2\u07e5\n\u00a2\f\u00a2\16\u00a2\u07e8\13\u00a2")
        buf.write("\3\u00a2\6\u00a2\u07eb\n\u00a2\r\u00a2\16\u00a2\u07ec")
        buf.write("\3\u00a3\3\u00a3\7\u00a3\u07f1\n\u00a3\f\u00a3\16\u00a3")
        buf.write("\u07f4\13\u00a3\3\u00a3\3\u00a3\3\u00a4\3\u00a4\3\u00a4")
        buf.write("\3\u00a4\7\u00a4\u07fc\n\u00a4\f\u00a4\16\u00a4\u07ff")
        buf.write("\13\u00a4\3\u00a4\5\u00a4\u0802\n\u00a4\5\u00a4\u0804")
        buf.write("\n\u00a4\3\u00a4\3\u00a4\3\u00a5\3\u00a5\3\u00a5\3\u00a5")
        buf.write("\7\u00a5\u080c\n\u00a5\f\u00a5\16\u00a5\u080f\13\u00a5")
        buf.write("\3\u00a5\3\u00a5\3\u00a6\5\u00a6\u0814\n\u00a6\3\u00a6")
        buf.write("\5\u00a6\u0817\n\u00a6\3\u00a6\3\u00a6\3\u00a7\3\u00a7")
        buf.write("\3\u00a8\3\u00a8\3\u00a8\3\u00a9\3\u00a9\7\u00a9\u0822")
        buf.write("\n\u00a9\f\u00a9\16\u00a9\u0825\13\u00a9\3\u00a9\3\u00a9")
        buf.write("\3\u00aa\5\u00aa\u082a\n\u00aa\3\u00aa\5\u00aa\u082d\n")
        buf.write("\u00aa\3\u00aa\5\u00aa\u0830\n\u00aa\3\u00aa\3\u00aa\3")
        buf.write("\u00aa\3\u00aa\3\u00aa\5\u00aa\u0837\n\u00aa\3\u00aa\3")
        buf.write("\u00aa\3\u00aa\5\u00aa\u083c\n\u00aa\3\u00aa\3\u00aa\5")
        buf.write("\u00aa\u0840\n\u00aa\3\u00aa\3\u00aa\5\u00aa\u0844\n\u00aa")
        buf.write("\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa")
        buf.write("\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa")
        buf.write("\3\u00aa\5\u00aa\u0855\n\u00aa\3\u00aa\5\u00aa\u0858\n")
        buf.write("\u00aa\3\u00aa\3\u00aa\3\u00aa\5\u00aa\u085d\n\u00aa\3")
        buf.write("\u00aa\3\u00aa\5\u00aa\u0861\n\u00aa\3\u00aa\3\u00aa\5")
        buf.write("\u00aa\u0865\n\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3")
        buf.write("\u00aa\3\u00aa\3\u00aa\5\u00aa\u086e\n\u00aa\3\u00ab\5")
        buf.write("\u00ab\u0871\n\u00ab\3\u00ab\3\u00ab\3\u00ab\5\u00ab\u0876")
        buf.write("\n\u00ab\3\u00ab\3\u00ab\5\u00ab\u087a\n\u00ab\3\u00ab")
        buf.write("\3\u00ab\3\u00ab\5\u00ab\u087f\n\u00ab\3\u00ab\3\u00ab")
        buf.write("\5\u00ab\u0883\n\u00ab\5\u00ab\u0885\n\u00ab\3\u00ac\3")
        buf.write("\u00ac\3\u00ac\3\u00ad\3\u00ad\3\u00ad\3\u00ad\7\u00ad")
        buf.write("\u088e\n\u00ad\f\u00ad\16\u00ad\u0891\13\u00ad\3\u00ad")
        buf.write("\5\u00ad\u0894\n\u00ad\5\u00ad\u0896\n\u00ad\3\u00ad\3")
        buf.write("\u00ad\3\u00ae\5\u00ae\u089b\n\u00ae\3\u00ae\3\u00ae\3")
        buf.write("\u00ae\5\u00ae\u08a0\n\u00ae\3\u00af\3\u00af\3\u00af\3")
        buf.write("\u00af\3\u00af\5\u00af\u08a7\n\u00af\3\u00af\3\u00af\3")
        buf.write("\u00b0\3\u00b0\5\u00b0\u08ad\n\u00b0\3\u00b1\6\u00b1\u08b0")
        buf.write("\n\u00b1\r\u00b1\16\u00b1\u08b1\3\u00b2\3\u00b2\3\u00b2")
        buf.write("\3\u00b2\5\u00b2\u08b8\n\u00b2\3\u00b2\3\u00b2\5\u00b2")
        buf.write("\u08bc\n\u00b2\3\u00b2\3\u00b2\3\u00b3\3\u00b3\5\u00b3")
        buf.write("\u08c2\n\u00b3\3\u00b4\3\u00b4\3\u00b4\7\u00b4\u08c7\n")
        buf.write("\u00b4\f\u00b4\16\u00b4\u08ca\13\u00b4\3\u00b5\3\u00b5")
        buf.write("\3\u00b5\3\u00b5\3\u00b5\7\u00b5\u08d1\n\u00b5\f\u00b5")
        buf.write("\16\u00b5\u08d4\13\u00b5\5\u00b5\u08d6\n\u00b5\3\u00b5")
        buf.write("\5\u00b5\u08d9\n\u00b5\3\u00b6\3\u00b6\3\u00b6\5\u00b6")
        buf.write("\u08de\n\u00b6\3\u00b6\3\u00b6\3\u00b7\3\u00b7\5\u00b7")
        buf.write("\u08e4\n\u00b7\3\u00b7\3\u00b7\7\u00b7\u08e8\n\u00b7\f")
        buf.write("\u00b7\16\u00b7\u08eb\13\u00b7\3\u00b7\3\u00b7\3\u00b7")
        buf.write("\3\u00b7\5\u00b7\u08f1\n\u00b7\3\u00b8\3\u00b8\3\u00b8")
        buf.write("\7\u00b8\u08f6\n\u00b8\f\u00b8\16\u00b8\u08f9\13\u00b8")
        buf.write("\3\u00b9\3\u00b9\3\u00b9\3\u00b9\3\u00ba\5\u00ba\u0900")
        buf.write("\n\u00ba\3\u00ba\3\u00ba\5\u00ba\u0904\n\u00ba\3\u00bb")
        buf.write("\3\u00bb\3\u00bb\3\u00bb\3\u00bb\3\u00bc\3\u00bc\3\u00bc")
        buf.write("\3\u00bc\3\u00bc\3\u00bc\3\u00bc\3\u00bc\5\u00bc\u0913")
        buf.write("\n\u00bc\3\u00bc\3\u00bc\5\u00bc\u0917\n\u00bc\3\u00bc")
        buf.write("\3\u00bc\3\u00bc\3\u00bc\3\u00bc\7\u00bc\u091e\n\u00bc")
        buf.write("\f\u00bc\16\u00bc\u0921\13\u00bc\3\u00bc\5\u00bc\u0924")
        buf.write("\n\u00bc\3\u00bc\3\u00bc\5\u00bc\u0928\n\u00bc\3\u00bd")
        buf.write("\3\u00bd\3\u00bd\3\u00bd\3\u00be\3\u00be\3\u00be\3\u00be")
        buf.write("\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00c0\3\u00c0\3\u00c0")
        buf.write("\3\u00c0\3\u00c0\3\u00c0\3\u00c0\3\u00c0\5\u00c0\u093e")
        buf.write("\n\u00c0\3\u00c1\3\u00c1\3\u00c2\3\u00c2\3\u00c2\3\u00c2")
        buf.write("\5\u00c2\u0946\n\u00c2\3\u00c3\3\u00c3\7\u00c3\u094a\n")
        buf.write("\u00c3\f\u00c3\16\u00c3\u094d\13\u00c3\3\u00c3\3\u00c3")
        buf.write("\3\u00c4\3\u00c4\7\u00c4\u0953\n\u00c4\f\u00c4\16\u00c4")
        buf.write("\u0956\13\u00c4\3\u00c4\3\u00c4\3\u00c5\3\u00c5\3\u00c5")
        buf.write("\3\u00c5\5\u00c5\u095e\n\u00c5\3\u00c6\3\u00c6\3\u00c6")
        buf.write("\3\u00c6\5\u00c6\u0964\n\u00c6\3\u00c7\3\u00c7\3\u00c7")
        buf.write("\7\u00c7\u0969\n\u00c7\f\u00c7\16\u00c7\u096c\13\u00c7")
        buf.write("\3\u00c7\3\u00c7\6\u00c7\u0970\n\u00c7\r\u00c7\16\u00c7")
        buf.write("\u0971\5\u00c7\u0974\n\u00c7\3\u00c8\3\u00c8\3\u00c9\3")
        buf.write("\u00c9\3\u00c9\5\u00c9\u097b\n\u00c9\3\u00c9\5\u00c9\u097e")
        buf.write("\n\u00c9\3\u00c9\5\u00c9\u0981\n\u00c9\3\u00c9\3\u00c9")
        buf.write("\5\u00c9\u0985\n\u00c9\3\u00ca\5\u00ca\u0988\n\u00ca\3")
        buf.write("\u00ca\3\u00ca\3\u00ca\5\u00ca\u098d\n\u00ca\3\u00ca\5")
        buf.write("\u00ca\u0990\n\u00ca\3\u00ca\5\u00ca\u0993\n\u00ca\3\u00ca")
        buf.write("\3\u00ca\5\u00ca\u0997\n\u00ca\3\u00cb\3\u00cb\3\u00cb")
        buf.write("\5\u00cb\u099c\n\u00cb\3\u00cb\5\u00cb\u099f\n\u00cb\3")
        buf.write("\u00cb\5\u00cb\u09a2\n\u00cb\3\u00cb\3\u00cb\5\u00cb\u09a6")
        buf.write("\n\u00cb\3\u00cc\3\u00cc\3\u00cc\5\u00cc\u09ab\n\u00cc")
        buf.write("\3\u00cc\3\u00cc\5\u00cc\u09af\n\u00cc\3\u00cd\3\u00cd")
        buf.write("\3\u00cd\3\u00cd\5\u00cd\u09b5\n\u00cd\3\u00cd\3\u00cd")
        buf.write("\5\u00cd\u09b9\n\u00cd\3\u00cd\3\u00cd\5\u00cd\u09bd\n")
        buf.write("\u00cd\3\u00cd\3\u00cd\3\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\5\u00ce")
        buf.write("\u09cb\n\u00ce\3\u00cf\3\u00cf\3\u00cf\3\u00d0\3\u00d0")
        buf.write("\3\u00d0\3\u00d0\3\u00d0\3\u00d0\3\u00d0\3\u00d0\5\u00d0")
        buf.write("\u09d8\n\u00d0\3\u00d0\3\u00d0\3\u00d0\3\u00d0\5\u00d0")
        buf.write("\u09de\n\u00d0\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1")
        buf.write("\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2")
        buf.write("\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2\5\u00d2\u09f1")
        buf.write("\n\u00d2\3\u00d3\3\u00d3\3\u00d3\3\u00d3\3\u00d3\3\u00d3")
        buf.write("\3\u00d4\3\u00d4\3\u00d4\5\u00d4\u09fc\n\u00d4\3\u00d4")
        buf.write("\3\u00d4\5\u00d4\u0a00\n\u00d4\3\u00d4\3\u00d4\3\u00d5")
        buf.write("\3\u00d5\5\u00d5\u0a06\n\u00d5\3\u00d5\3\u00d5\5\u00d5")
        buf.write("\u0a0a\n\u00d5\3\u00d5\3\u00d5\5\u00d5\u0a0e\n\u00d5\3")
        buf.write("\u00d5\3\u00d5\3\u00d5\3\u00d5\3\u00d5\5\u00d5\u0a15\n")
        buf.write("\u00d5\3\u00d6\3\u00d6\3\u00d6\3\u00d6\3\u00d6\5\u00d6")
        buf.write("\u0a1c\n\u00d6\3\u00d6\5\u00d6\u0a1f\n\u00d6\3\u00d6\3")
        buf.write("\u00d6\7\u00d6\u0a23\n\u00d6\f\u00d6\16\u00d6\u0a26\13")
        buf.write("\u00d6\3\u00d7\3\u00d7\3\u00d7\3\u00d7\5\u00d7\u0a2c\n")
        buf.write("\u00d7\3\u00d7\3\u00d7\3\u00d7\5\u00d7\u0a31\n\u00d7\3")
        buf.write("\u00d7\5\u00d7\u0a34\n\u00d7\3\u00d7\3\u00d7\3\u00d7\3")
        buf.write("\u00d7\3\u00d7\3\u00d7\5\u00d7\u0a3c\n\u00d7\3\u00d8\3")
        buf.write("\u00d8\3\u00d8\3\u00d8\5\u00d8\u0a42\n\u00d8\3\u00d9\3")
        buf.write("\u00d9\5\u00d9\u0a46\n\u00d9\3\u00d9\3\u00d9\3\u00da\3")
        buf.write("\u00da\5\u00da\u0a4c\n\u00da\3\u00da\3\u00da\5\u00da\u0a50")
        buf.write("\n\u00da\3\u00db\3\u00db\3\u00db\2\2\u00dc\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098")
        buf.write("\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa")
        buf.write("\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc")
        buf.write("\u00be\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce")
        buf.write("\u00d0\u00d2\u00d4\u00d6\u00d8\u00da\u00dc\u00de\u00e0")
        buf.write("\u00e2\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2")
        buf.write("\u00f4\u00f6\u00f8\u00fa\u00fc\u00fe\u0100\u0102\u0104")
        buf.write("\u0106\u0108\u010a\u010c\u010e\u0110\u0112\u0114\u0116")
        buf.write("\u0118\u011a\u011c\u011e\u0120\u0122\u0124\u0126\u0128")
        buf.write("\u012a\u012c\u012e\u0130\u0132\u0134\u0136\u0138\u013a")
        buf.write("\u013c\u013e\u0140\u0142\u0144\u0146\u0148\u014a\u014c")
        buf.write("\u014e\u0150\u0152\u0154\u0156\u0158\u015a\u015c\u015e")
        buf.write("\u0160\u0162\u0164\u0166\u0168\u016a\u016c\u016e\u0170")
        buf.write("\u0172\u0174\u0176\u0178\u017a\u017c\u017e\u0180\u0182")
        buf.write("\u0184\u0186\u0188\u018a\u018c\u018e\u0190\u0192\u0194")
        buf.write("\u0196\u0198\u019a\u019c\u019e\u01a0\u01a2\u01a4\u01a6")
        buf.write("\u01a8\u01aa\u01ac\u01ae\u01b0\u01b2\u01b4\2\25\n\2\27")
        buf.write("\27\32\3299AAUUYYefjj\4\2$$//\5\288JJRR\3\2\u009e\u009f")
        buf.write("\4\2\u0094\u0095\u00a0\u00a1\3\2\u0089\u008a\3\2\u008b")
        buf.write("\u008d\20\2\24\24\27\27\32\32\37\37$$//99AAFFUUYY]]ef")
        buf.write("jj\4\2\20\20\"\"\4\2\21\21ii\16\2\13\13\21\21++;;DDKK")
        buf.write("MQVV\\\\iimmoo\4\2**\67\67\4\2\23\23``\4\2\u008b\u008b")
        buf.write("\u0096\u0096\4\288JJ\4\2,,bb\25\2\13\13\17\17\23\25\27")
        buf.write("!#$&\')\61\64\64\66;==@ACFHHJLNRTVYkmorr\3\2QR\26\2\f")
        buf.write("\16\20\22\26\26\"\"%%((\62\63\65\65<<>?BBGGIIMMSSWXhh")
        buf.write("llpqst\2\u0b62\2\u01b7\3\2\2\2\4\u01cf\3\2\2\2\6\u01db")
        buf.write("\3\2\2\2\b\u01e9\3\2\2\2\n\u01eb\3\2\2\2\f\u01f5\3\2\2")
        buf.write("\2\16\u01fb\3\2\2\2\20\u0200\3\2\2\2\22\u0202\3\2\2\2")
        buf.write("\24\u0204\3\2\2\2\26\u020a\3\2\2\2\30\u020c\3\2\2\2\32")
        buf.write("\u0217\3\2\2\2\34\u0222\3\2\2\2\36\u0231\3\2\2\2 \u0236")
        buf.write("\3\2\2\2\"\u0240\3\2\2\2$\u024d\3\2\2\2&\u024f\3\2\2\2")
        buf.write("(\u0257\3\2\2\2*\u025f\3\2\2\2,\u0267\3\2\2\2.\u026f\3")
        buf.write("\2\2\2\60\u0277\3\2\2\2\62\u027f\3\2\2\2\64\u0287\3\2")
        buf.write("\2\2\66\u028f\3\2\2\28\u029b\3\2\2\2:\u02a6\3\2\2\2<\u02ae")
        buf.write("\3\2\2\2>\u02b6\3\2\2\2@\u02c2\3\2\2\2B\u02ca\3\2\2\2")
        buf.write("D\u02d9\3\2\2\2F\u02f5\3\2\2\2H\u02f7\3\2\2\2J\u0396\3")
        buf.write("\2\2\2L\u039a\3\2\2\2N\u039c\3\2\2\2P\u03a0\3\2\2\2R\u03a8")
        buf.write("\3\2\2\2T\u03b8\3\2\2\2V\u03bc\3\2\2\2X\u03be\3\2\2\2")
        buf.write("Z\u03c8\3\2\2\2\\\u03ca\3\2\2\2^\u03d3\3\2\2\2`\u03e0")
        buf.write("\3\2\2\2b\u03e7\3\2\2\2d\u03e9\3\2\2\2f\u03fc\3\2\2\2")
        buf.write("h\u03fe\3\2\2\2j\u0407\3\2\2\2l\u0414\3\2\2\2n\u0416\3")
        buf.write("\2\2\2p\u042b\3\2\2\2r\u0434\3\2\2\2t\u0445\3\2\2\2v\u0450")
        buf.write("\3\2\2\2x\u0455\3\2\2\2z\u0466\3\2\2\2|\u0468\3\2\2\2")
        buf.write("~\u0471\3\2\2\2\u0080\u0476\3\2\2\2\u0082\u0480\3\2\2")
        buf.write("\2\u0084\u0482\3\2\2\2\u0086\u0485\3\2\2\2\u0088\u0490")
        buf.write("\3\2\2\2\u008a\u049c\3\2\2\2\u008c\u049e\3\2\2\2\u008e")
        buf.write("\u04a3\3\2\2\2\u0090\u04a6\3\2\2\2\u0092\u04b5\3\2\2\2")
        buf.write("\u0094\u04be\3\2\2\2\u0096\u04c9\3\2\2\2\u0098\u04cb\3")
        buf.write("\2\2\2\u009a\u04d2\3\2\2\2\u009c\u04db\3\2\2\2\u009e\u04dd")
        buf.write("\3\2\2\2\u00a0\u04e1\3\2\2\2\u00a2\u04f6\3\2\2\2\u00a4")
        buf.write("\u04fd\3\2\2\2\u00a6\u04ff\3\2\2\2\u00a8\u0505\3\2\2\2")
        buf.write("\u00aa\u0589\3\2\2\2\u00ac\u058b\3\2\2\2\u00ae\u05a4\3")
        buf.write("\2\2\2\u00b0\u05a8\3\2\2\2\u00b2\u05aa\3\2\2\2\u00b4\u05b5")
        buf.write("\3\2\2\2\u00b6\u05b7\3\2\2\2\u00b8\u05bd\3\2\2\2\u00ba")
        buf.write("\u05c0\3\2\2\2\u00bc\u05cf\3\2\2\2\u00be\u05d1\3\2\2\2")
        buf.write("\u00c0\u05d5\3\2\2\2\u00c2\u05e2\3\2\2\2\u00c4\u05e4\3")
        buf.write("\2\2\2\u00c6\u05f7\3\2\2\2\u00c8\u05f9\3\2\2\2\u00ca\u0605")
        buf.write("\3\2\2\2\u00cc\u060b\3\2\2\2\u00ce\u0610\3\2\2\2\u00d0")
        buf.write("\u0615\3\2\2\2\u00d2\u0617\3\2\2\2\u00d4\u061d\3\2\2\2")
        buf.write("\u00d6\u0625\3\2\2\2\u00d8\u0632\3\2\2\2\u00da\u0636\3")
        buf.write("\2\2\2\u00dc\u063c\3\2\2\2\u00de\u064f\3\2\2\2\u00e0\u0652")
        buf.write("\3\2\2\2\u00e2\u0658\3\2\2\2\u00e4\u065b\3\2\2\2\u00e6")
        buf.write("\u0667\3\2\2\2\u00e8\u066d\3\2\2\2\u00ea\u0679\3\2\2\2")
        buf.write("\u00ec\u067d\3\2\2\2\u00ee\u0686\3\2\2\2\u00f0\u068f\3")
        buf.write("\2\2\2\u00f2\u0693\3\2\2\2\u00f4\u06a2\3\2\2\2\u00f6\u06ab")
        buf.write("\3\2\2\2\u00f8\u06ad\3\2\2\2\u00fa\u06b5\3\2\2\2\u00fc")
        buf.write("\u06b9\3\2\2\2\u00fe\u06c0\3\2\2\2\u0100\u06c5\3\2\2\2")
        buf.write("\u0102\u06cf\3\2\2\2\u0104\u06d3\3\2\2\2\u0106\u06e8\3")
        buf.write("\2\2\2\u0108\u06ef\3\2\2\2\u010a\u06fd\3\2\2\2\u010c\u0705")
        buf.write("\3\2\2\2\u010e\u0709\3\2\2\2\u0110\u0711\3\2\2\2\u0112")
        buf.write("\u0718\3\2\2\2\u0114\u071c\3\2\2\2\u0116\u071e\3\2\2\2")
        buf.write("\u0118\u0722\3\2\2\2\u011a\u072a\3\2\2\2\u011c\u072c\3")
        buf.write("\2\2\2\u011e\u073c\3\2\2\2\u0120\u0746\3\2\2\2\u0122\u0749")
        buf.write("\3\2\2\2\u0124\u0750\3\2\2\2\u0126\u0762\3\2\2\2\u0128")
        buf.write("\u076b\3\2\2\2\u012a\u077a\3\2\2\2\u012c\u077e\3\2\2\2")
        buf.write("\u012e\u0781\3\2\2\2\u0130\u078e\3\2\2\2\u0132\u0794\3")
        buf.write("\2\2\2\u0134\u07af\3\2\2\2\u0136\u07b1\3\2\2\2\u0138\u07b8")
        buf.write("\3\2\2\2\u013a\u07c2\3\2\2\2\u013c\u07c4\3\2\2\2\u013e")
        buf.write("\u07c7\3\2\2\2\u0140\u07d1\3\2\2\2\u0142\u07e2\3\2\2\2")
        buf.write("\u0144\u07ee\3\2\2\2\u0146\u07f7\3\2\2\2\u0148\u0807\3")
        buf.write("\2\2\2\u014a\u0813\3\2\2\2\u014c\u081a\3\2\2\2\u014e\u081c")
        buf.write("\3\2\2\2\u0150\u081f\3\2\2\2\u0152\u0829\3\2\2\2\u0154")
        buf.write("\u0870\3\2\2\2\u0156\u0886\3\2\2\2\u0158\u0889\3\2\2\2")
        buf.write("\u015a\u089a\3\2\2\2\u015c\u08a1\3\2\2\2\u015e\u08ac\3")
        buf.write("\2\2\2\u0160\u08af\3\2\2\2\u0162\u08b3\3\2\2\2\u0164\u08c1")
        buf.write("\3\2\2\2\u0166\u08c3\3\2\2\2\u0168\u08cb\3\2\2\2\u016a")
        buf.write("\u08dd\3\2\2\2\u016c\u08f0\3\2\2\2\u016e\u08f2\3\2\2\2")
        buf.write("\u0170\u08fa\3\2\2\2\u0172\u0903\3\2\2\2\u0174\u0905\3")
        buf.write("\2\2\2\u0176\u0927\3\2\2\2\u0178\u0929\3\2\2\2\u017a\u092d")
        buf.write("\3\2\2\2\u017c\u0931\3\2\2\2\u017e\u093d\3\2\2\2\u0180")
        buf.write("\u093f\3\2\2\2\u0182\u0945\3\2\2\2\u0184\u0947\3\2\2\2")
        buf.write("\u0186\u0950\3\2\2\2\u0188\u095d\3\2\2\2\u018a\u0963\3")
        buf.write("\2\2\2\u018c\u0965\3\2\2\2\u018e\u0975\3\2\2\2\u0190\u0977")
        buf.write("\3\2\2\2\u0192\u0987\3\2\2\2\u0194\u0998\3\2\2\2\u0196")
        buf.write("\u09a7\3\2\2\2\u0198\u09b0\3\2\2\2\u019a\u09c0\3\2\2\2")
        buf.write("\u019c\u09cc\3\2\2\2\u019e\u09cf\3\2\2\2\u01a0\u09df\3")
        buf.write("\2\2\2\u01a2\u09e4\3\2\2\2\u01a4\u09f2\3\2\2\2\u01a6\u09f8")
        buf.write("\3\2\2\2\u01a8\u0a03\3\2\2\2\u01aa\u0a1b\3\2\2\2\u01ac")
        buf.write("\u0a27\3\2\2\2\u01ae\u0a3d\3\2\2\2\u01b0\u0a43\3\2\2\2")
        buf.write("\u01b2\u0a49\3\2\2\2\u01b4\u0a51\3\2\2\2\u01b6\u01b8\7")
        buf.write("\3\2\2\u01b7\u01b6\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01ba")
        buf.write("\3\2\2\2\u01b9\u01bb\5\u00d8m\2\u01ba\u01b9\3\2\2\2\u01ba")
        buf.write("\u01bb\3\2\2\2\u01bb\u01bd\3\2\2\2\u01bc\u01be\5\u00dc")
        buf.write("o\2\u01bd\u01bc\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c2")
        buf.write("\3\2\2\2\u01bf\u01c1\5\u015c\u00af\2\u01c0\u01bf\3\2\2")
        buf.write("\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3")
        buf.write("\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5")
        buf.write("\u01c7\5\u00e0q\2\u01c6\u01c5\3\2\2\2\u01c6\u01c7\3\2")
        buf.write("\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9\7\2\2\3\u01c9\3\3")
        buf.write("\2\2\2\u01ca\u01cc\5\u01b4\u00db\2\u01cb\u01cd\5\30\r")
        buf.write("\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01d0")
        buf.write("\3\2\2\2\u01ce\u01d0\5\u00e6t\2\u01cf\u01ca\3\2\2\2\u01cf")
        buf.write("\u01ce\3\2\2\2\u01d0\u01d8\3\2\2\2\u01d1\u01d2\7\u0085")
        buf.write("\2\2\u01d2\u01d4\5\u01b4\u00db\2\u01d3\u01d5\5\30\r\2")
        buf.write("\u01d4\u01d3\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d7\3")
        buf.write("\2\2\2\u01d6\u01d1\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6")
        buf.write("\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\5\3\2\2\2\u01da\u01d8")
        buf.write("\3\2\2\2\u01db\u01e1\5\b\5\2\u01dc\u01e0\7\u0096\2\2\u01dd")
        buf.write("\u01e0\5\u0144\u00a3\2\u01de\u01e0\7\u008b\2\2\u01df\u01dc")
        buf.write("\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01de\3\2\2\2\u01e0")
        buf.write("\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2")
        buf.write("\u01e2\7\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4\u01ea\5\16")
        buf.write("\b\2\u01e5\u01ea\5\26\f\2\u01e6\u01e7\7n\2\2\u01e7\u01ea")
        buf.write("\7\u008b\2\2\u01e8\u01ea\5\n\6\2\u01e9\u01e4\3\2\2\2\u01e9")
        buf.write("\u01e5\3\2\2\2\u01e9\u01e6\3\2\2\2\u01e9\u01e8\3\2\2\2")
        buf.write("\u01ea\t\3\2\2\2\u01eb\u01ec\7\u0083\2\2\u01ec\u01ef\5")
        buf.write("\f\7\2\u01ed\u01ee\7\u0086\2\2\u01ee\u01f0\5\f\7\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01ef\3\2\2\2")
        buf.write("\u01f1\u01f2\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4\7")
        buf.write("\u0084\2\2\u01f4\13\3\2\2\2\u01f5\u01f7\5\6\4\2\u01f6")
        buf.write("\u01f8\5\u01b4\u00db\2\u01f7\u01f6\3\2\2\2\u01f7\u01f8")
        buf.write("\3\2\2\2\u01f8\r\3\2\2\2\u01f9\u01fc\5\20\t\2\u01fa\u01fc")
        buf.write("\7\24\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fa\3\2\2\2\u01fc")
        buf.write("\17\3\2\2\2\u01fd\u0201\5\22\n\2\u01fe\u0201\5\24\13\2")
        buf.write("\u01ff\u0201\7\37\2\2\u0200\u01fd\3\2\2\2\u0200\u01fe")
        buf.write("\3\2\2\2\u0200\u01ff\3\2\2\2\u0201\21\3\2\2\2\u0202\u0203")
        buf.write("\t\2\2\2\u0203\23\3\2\2\2\u0204\u0205\t\3\2\2\u0205\25")
        buf.write("\3\2\2\2\u0206\u020b\5\4\3\2\u0207\u020b\7F\2\2\u0208")
        buf.write("\u020b\7%\2\2\u0209\u020b\7]\2\2\u020a\u0206\3\2\2\2\u020a")
        buf.write("\u0207\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u0209\3\2\2\2")
        buf.write("\u020b\27\3\2\2\2\u020c\u020d\7\u0094\2\2\u020d\u0212")
        buf.write("\5\6\4\2\u020e\u020f\7\u0086\2\2\u020f\u0211\5\6\4\2\u0210")
        buf.write("\u020e\3\2\2\2\u0211\u0214\3\2\2\2\u0212\u0210\3\2\2\2")
        buf.write("\u0212\u0213\3\2\2\2\u0213\u0215\3\2\2\2\u0214\u0212\3")
        buf.write("\2\2\2\u0215\u0216\7\u0095\2\2\u0216\31\3\2\2\2\u0217")
        buf.write("\u021c\5\34\17\2\u0218\u0219\7\u0086\2\2\u0219\u021b\5")
        buf.write("\34\17\2\u021a\u0218\3\2\2\2\u021b\u021e\3\2\2\2\u021c")
        buf.write("\u021a\3\2\2\2\u021c\u021d\3\2\2\2\u021d\33\3\2\2\2\u021e")
        buf.write("\u021c\3\2\2\2\u021f\u0220\5\u01b4\u00db\2\u0220\u0221")
        buf.write("\7\u0087\2\2\u0221\u0223\3\2\2\2\u0222\u021f\3\2\2\2\u0222")
        buf.write("\u0223\3\2\2\2\u0223\u0225\3\2\2\2\u0224\u0226\t\4\2\2")
        buf.write("\u0225\u0224\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0229\3")
        buf.write("\2\2\2\u0227\u022a\7l\2\2\u0228\u022a\5\6\4\2\u0229\u0227")
        buf.write("\3\2\2\2\u0229\u0228\3\2\2\2\u0229\u022a\3\2\2\2\u022a")
        buf.write("\u022b\3\2\2\2\u022b\u022c\5\36\20\2\u022c\35\3\2\2\2")
        buf.write("\u022d\u0232\5\"\22\2\u022e\u0232\5 \21\2\u022f\u0230")
        buf.write("\7R\2\2\u0230\u0232\5 \21\2\u0231\u022d\3\2\2\2\u0231")
        buf.write("\u022e\3\2\2\2\u0231\u022f\3\2\2\2\u0232\37\3\2\2\2\u0233")
        buf.write("\u0237\5x=\2\u0234\u0237\5\u0084C\2\u0235\u0237\5&\24")
        buf.write("\2\u0236\u0233\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0235")
        buf.write("\3\2\2\2\u0237!\3\2\2\2\u0238\u0239\5F$\2\u0239\u023a")
        buf.write("\5$\23\2\u023a\u023b\5\36\20\2\u023b\u0241\3\2\2\2\u023c")
        buf.write("\u023d\5F$\2\u023d\u023e\7\u00ac\2\2\u023e\u023f\5L\'")
        buf.write("\2\u023f\u0241\3\2\2\2\u0240\u0238\3\2\2\2\u0240\u023c")
        buf.write("\3\2\2\2\u0241#\3\2\2\2\u0242\u024e\7\u0093\2\2\u0243")
        buf.write("\u024e\7\u00a2\2\2\u0244\u024e\7\u00a3\2\2\u0245\u024e")
        buf.write("\7\u00a4\2\2\u0246\u024e\7\u00a5\2\2\u0247\u024e\7\u00a6")
        buf.write("\2\2\u0248\u024e\7\u00a7\2\2\u0249\u024e\7\u00a8\2\2\u024a")
        buf.write("\u024e\7\u00a9\2\2\u024b\u024e\7\u00ab\2\2\u024c\u024e")
        buf.write("\5\u017c\u00bf\2\u024d\u0242\3\2\2\2\u024d\u0243\3\2\2")
        buf.write("\2\u024d\u0244\3\2\2\2\u024d\u0245\3\2\2\2\u024d\u0246")
        buf.write("\3\2\2\2\u024d\u0247\3\2\2\2\u024d\u0248\3\2\2\2\u024d")
        buf.write("\u0249\3\2\2\2\u024d\u024a\3\2\2\2\u024d\u024b\3\2\2\2")
        buf.write("\u024d\u024c\3\2\2\2\u024e%\3\2\2\2\u024f\u0255\5(\25")
        buf.write("\2\u0250\u0251\7\u0096\2\2\u0251\u0252\5L\'\2\u0252\u0253")
        buf.write("\7\u0087\2\2\u0253\u0254\5L\'\2\u0254\u0256\3\2\2\2\u0255")
        buf.write("\u0250\3\2\2\2\u0255\u0256\3\2\2\2\u0256\'\3\2\2\2\u0257")
        buf.write("\u025d\5*\26\2\u0258\u025b\7\u0098\2\2\u0259\u025c\5(")
        buf.write("\25\2\u025a\u025c\5N(\2\u025b\u0259\3\2\2\2\u025b\u025a")
        buf.write("\3\2\2\2\u025c\u025e\3\2\2\2\u025d\u0258\3\2\2\2\u025d")
        buf.write("\u025e\3\2\2\2\u025e)\3\2\2\2\u025f\u0264\5,\27\2\u0260")
        buf.write("\u0261\7\u009c\2\2\u0261\u0263\5,\27\2\u0262\u0260\3\2")
        buf.write("\2\2\u0263\u0266\3\2\2\2\u0264\u0262\3\2\2\2\u0264\u0265")
        buf.write("\3\2\2\2\u0265+\3\2\2\2\u0266\u0264\3\2\2\2\u0267\u026c")
        buf.write("\5.\30\2\u0268\u0269\7\u009b\2\2\u0269\u026b\5.\30\2\u026a")
        buf.write("\u0268\3\2\2\2\u026b\u026e\3\2\2\2\u026c\u026a\3\2\2\2")
        buf.write("\u026c\u026d\3\2\2\2\u026d-\3\2\2\2\u026e\u026c\3\2\2")
        buf.write("\2\u026f\u0274\5\60\31\2\u0270\u0271\7\u008f\2\2\u0271")
        buf.write("\u0273\5\60\31\2\u0272\u0270\3\2\2\2\u0273\u0276\3\2\2")
        buf.write("\2\u0274\u0272\3\2\2\2\u0274\u0275\3\2\2\2\u0275/\3\2")
        buf.write("\2\2\u0276\u0274\3\2\2\2\u0277\u027c\5\62\32\2\u0278\u0279")
        buf.write("\7\u0090\2\2\u0279\u027b\5\62\32\2\u027a\u0278\3\2\2\2")
        buf.write("\u027b\u027e\3\2\2\2\u027c\u027a\3\2\2\2\u027c\u027d\3")
        buf.write("\2\2\2\u027d\61\3\2\2\2\u027e\u027c\3\2\2\2\u027f\u0284")
        buf.write("\5\64\33\2\u0280\u0281\7\u008e\2\2\u0281\u0283\5\64\33")
        buf.write("\2\u0282\u0280\3\2\2\2\u0283\u0286\3\2\2\2\u0284\u0282")
        buf.write("\3\2\2\2\u0284\u0285\3\2\2\2\u0285\63\3\2\2\2\u0286\u0284")
        buf.write("\3\2\2\2\u0287\u028c\5\66\34\2\u0288\u0289\t\5\2\2\u0289")
        buf.write("\u028b\5\66\34\2\u028a\u0288\3\2\2\2\u028b\u028e\3\2\2")
        buf.write("\2\u028c\u028a\3\2\2\2\u028c\u028d\3\2\2\2\u028d\65\3")
        buf.write("\2\2\2\u028e\u028c\3\2\2\2\u028f\u0298\58\35\2\u0290\u0291")
        buf.write("\t\6\2\2\u0291\u0297\58\35\2\u0292\u0293\7=\2\2\u0293")
        buf.write("\u0297\5r:\2\u0294\u0295\7\17\2\2\u0295\u0297\5\6\4\2")
        buf.write("\u0296\u0290\3\2\2\2\u0296\u0292\3\2\2\2\u0296\u0294\3")
        buf.write("\2\2\2\u0297\u029a\3\2\2\2\u0298\u0296\3\2\2\2\u0298\u0299")
        buf.write("\3\2\2\2\u0299\67\3\2\2\2\u029a\u0298\3\2\2\2\u029b\u02a3")
        buf.write("\5:\36\2\u029c\u029f\7\u00aa\2\2\u029d\u029f\5\u017a\u00be")
        buf.write("\2\u029e\u029c\3\2\2\2\u029e\u029d\3\2\2\2\u029f\u02a0")
        buf.write("\3\2\2\2\u02a0\u02a2\5:\36\2\u02a1\u029e\3\2\2\2\u02a2")
        buf.write("\u02a5\3\2\2\2\u02a3\u02a1\3\2\2\2\u02a3\u02a4\3\2\2\2")
        buf.write("\u02a49\3\2\2\2\u02a5\u02a3\3\2\2\2\u02a6\u02ab\5<\37")
        buf.write("\2\u02a7\u02a8\t\7\2\2\u02a8\u02aa\5<\37\2\u02a9\u02a7")
        buf.write("\3\2\2\2\u02aa\u02ad\3\2\2\2\u02ab\u02a9\3\2\2\2\u02ab")
        buf.write("\u02ac\3\2\2\2\u02ac;\3\2\2\2\u02ad\u02ab\3\2\2\2\u02ae")
        buf.write("\u02b3\5> \2\u02af\u02b0\t\b\2\2\u02b0\u02b2\5> \2\u02b1")
        buf.write("\u02af\3\2\2\2\u02b2\u02b5\3\2\2\2\u02b3\u02b1\3\2\2\2")
        buf.write("\u02b3\u02b4\3\2\2\2\u02b4=\3\2\2\2\u02b5\u02b3\3\2\2")
        buf.write("\2\u02b6\u02c0\5D#\2\u02b7\u02b8\7_\2\2\u02b8\u02bd\7")
        buf.write("\177\2\2\u02b9\u02bb\5@!\2\u02ba\u02bc\7\u0086\2\2\u02bb")
        buf.write("\u02ba\3\2\2\2\u02bb\u02bc\3\2\2\2\u02bc\u02be\3\2\2\2")
        buf.write("\u02bd\u02b9\3\2\2\2\u02bd\u02be\3\2\2\2\u02be\u02bf\3")
        buf.write("\2\2\2\u02bf\u02c1\7\u0080\2\2\u02c0\u02b7\3\2\2\2\u02c0")
        buf.write("\u02c1\3\2\2\2\u02c1?\3\2\2\2\u02c2\u02c7\5B\"\2\u02c3")
        buf.write("\u02c4\7\u0086\2\2\u02c4\u02c6\5B\"\2\u02c5\u02c3\3\2")
        buf.write("\2\2\u02c6\u02c9\3\2\2\2\u02c7\u02c5\3\2\2\2\u02c7\u02c8")
        buf.write("\3\2\2\2\u02c8A\3\2\2\2\u02c9\u02c7\3\2\2\2\u02ca\u02cc")
        buf.write("\5\36\20\2\u02cb\u02cd\5\u00be`\2\u02cc\u02cb\3\2\2\2")
        buf.write("\u02cc\u02cd\3\2\2\2\u02cd\u02ce\3\2\2\2\u02ce\u02cf\5")
        buf.write("\u0178\u00bd\2\u02cf\u02d0\5L\'\2\u02d0C\3\2\2\2\u02d1")
        buf.write("\u02da\5F$\2\u02d2\u02d4\5F$\2\u02d3\u02d2\3\2\2\2\u02d3")
        buf.write("\u02d4\3\2\2\2\u02d4\u02d5\3\2\2\2\u02d5\u02d7\7\u00ad")
        buf.write("\2\2\u02d6\u02d8\5F$\2\u02d7\u02d6\3\2\2\2\u02d7\u02d8")
        buf.write("\3\2\2\2\u02d8\u02da\3\2\2\2\u02d9\u02d1\3\2\2\2\u02d9")
        buf.write("\u02d3\3\2\2\2\u02daE\3\2\2\2\u02db\u02f6\5H%\2\u02dc")
        buf.write("\u02dd\7\u0089\2\2\u02dd\u02f6\5F$\2\u02de\u02df\7\u008a")
        buf.write("\2\2\u02df\u02f6\5F$\2\u02e0\u02e1\7\u0091\2\2\u02e1\u02f6")
        buf.write("\5F$\2\u02e2\u02e3\7\u0092\2\2\u02e3\u02f6\5F$\2\u02e4")
        buf.write("\u02e5\7\u0099\2\2\u02e5\u02f6\5F$\2\u02e6\u02e7\7\u009a")
        buf.write("\2\2\u02e7\u02f6\5F$\2\u02e8\u02e9\7\u0083\2\2\u02e9\u02ea")
        buf.write("\5\6\4\2\u02ea\u02eb\7\u0084\2\2\u02eb\u02ec\5F$\2\u02ec")
        buf.write("\u02f6\3\2\2\2\u02ed\u02ee\7\22\2\2\u02ee\u02f6\5F$\2")
        buf.write("\u02ef\u02f0\7\u008e\2\2\u02f0\u02f6\5F$\2\u02f1\u02f2")
        buf.write("\7\u008b\2\2\u02f2\u02f6\5F$\2\u02f3\u02f4\7\u0090\2\2")
        buf.write("\u02f4\u02f6\5F$\2\u02f5\u02db\3\2\2\2\u02f5\u02dc\3\2")
        buf.write("\2\2\u02f5\u02de\3\2\2\2\u02f5\u02e0\3\2\2\2\u02f5\u02e2")
        buf.write("\3\2\2\2\u02f5\u02e4\3\2\2\2\u02f5\u02e6\3\2\2\2\u02f5")
        buf.write("\u02e8\3\2\2\2\u02f5\u02ed\3\2\2\2\u02f5\u02ef\3\2\2\2")
        buf.write("\u02f5\u02f1\3\2\2\2\u02f5\u02f3\3\2\2\2\u02f6G\3\2\2")
        buf.write("\2\u02f7\u02f9\5J&\2\u02f8\u02fa\7\u0091\2\2\u02f9\u02f8")
        buf.write("\3\2\2\2\u02f9\u02fa\3\2\2\2\u02fa\u02fe\3\2\2\2\u02fb")
        buf.write("\u02fd\5R*\2\u02fc\u02fb\3\2\2\2\u02fd\u0300\3\2\2\2\u02fe")
        buf.write("\u02fc\3\2\2\2\u02fe\u02ff\3\2\2\2\u02ff\u0302\3\2\2\2")
        buf.write("\u0300\u02fe\3\2\2\2\u0301\u0303\7\u0091\2\2\u0302\u0301")
        buf.write("\3\2\2\2\u0302\u0303\3\2\2\2\u0303\u031a\3\2\2\2\u0304")
        buf.write("\u030b\5P)\2\u0305\u030b\5\u01b0\u00d9\2\u0306\u030b\7")
        buf.write("\u0099\2\2\u0307\u030b\7\u009a\2\2\u0308\u0309\7\u009d")
        buf.write("\2\2\u0309\u030b\5\u01b4\u00db\2\u030a\u0304\3\2\2\2\u030a")
        buf.write("\u0305\3\2\2\2\u030a\u0306\3\2\2\2\u030a\u0307\3\2\2\2")
        buf.write("\u030a\u0308\3\2\2\2\u030b\u030d\3\2\2\2\u030c\u030e\7")
        buf.write("\u0091\2\2\u030d\u030c\3\2\2\2\u030d\u030e\3\2\2\2\u030e")
        buf.write("\u0312\3\2\2\2\u030f\u0311\5R*\2\u0310\u030f\3\2\2\2\u0311")
        buf.write("\u0314\3\2\2\2\u0312\u0310\3\2\2\2\u0312\u0313\3\2\2\2")
        buf.write("\u0313\u0316\3\2\2\2\u0314\u0312\3\2\2\2\u0315\u0317\7")
        buf.write("\u0091\2\2\u0316\u0315\3\2\2\2\u0316\u0317\3\2\2\2\u0317")
        buf.write("\u0319\3\2\2\2\u0318\u030a\3\2\2\2\u0319\u031c\3\2\2\2")
        buf.write("\u031a\u0318\3\2\2\2\u031a\u031b\3\2\2\2\u031bI\3\2\2")
        buf.write("\2\u031c\u031a\3\2\2\2\u031d\u0397\5\u017e\u00c0\2\u031e")
        buf.write("\u0320\5\u01b4\u00db\2\u031f\u0321\5\30\r\2\u0320\u031f")
        buf.write("\3\2\2\2\u0320\u0321\3\2\2\2\u0321\u0397\3\2\2\2\u0322")
        buf.write("\u0323\7\u0083\2\2\u0323\u0324\5\36\20\2\u0324\u0325\7")
        buf.write("\u0084\2\2\u0325\u0397\3\2\2\2\u0326\u0397\5V,\2\u0327")
        buf.write("\u0397\5\u00e6t\2\u0328\u0397\7u\2\2\u0329\u0397\7`\2")
        buf.write("\2\u032a\u0334\7\23\2\2\u032b\u032c\7\u0085\2\2\u032c")
        buf.write("\u032e\5\u01b4\u00db\2\u032d\u032f\5\30\r\2\u032e\u032d")
        buf.write("\3\2\2\2\u032e\u032f\3\2\2\2\u032f\u0335\3\2\2\2\u0330")
        buf.write("\u0331\7\u0081\2\2\u0331\u0332\5X-\2\u0332\u0333\7\u0082")
        buf.write("\2\2\u0333\u0335\3\2\2\2\u0334\u032b\3\2\2\2\u0334\u0330")
        buf.write("\3\2\2\2\u0335\u0397\3\2\2\2\u0336\u0353\7D\2\2\u0337")
        buf.write("\u034d\5\6\4\2\u0338\u034e\5\u01b2\u00da\2\u0339\u034e")
        buf.write("\5Z.\2\u033a\u033b\7\u0081\2\2\u033b\u033c\5X-\2\u033c")
        buf.write("\u0340\7\u0082\2\2\u033d\u033f\5\u0144\u00a3\2\u033e\u033d")
        buf.write("\3\2\2\2\u033f\u0342\3\2\2\2\u0340\u033e\3\2\2\2\u0340")
        buf.write("\u0341\3\2\2\2\u0341\u0344\3\2\2\2\u0342\u0340\3\2\2\2")
        buf.write("\u0343\u0345\5\u0146\u00a4\2\u0344\u0343\3\2\2\2\u0344")
        buf.write("\u0345\3\2\2\2\u0345\u034e\3\2\2\2\u0346\u0348\5\u0144")
        buf.write("\u00a3\2\u0347\u0346\3\2\2\2\u0348\u0349\3\2\2\2\u0349")
        buf.write("\u0347\3\2\2\2\u0349\u034a\3\2\2\2\u034a\u034b\3\2\2\2")
        buf.write("\u034b\u034c\5\u0146\u00a4\2\u034c\u034e\3\2\2\2\u034d")
        buf.write("\u0338\3\2\2\2\u034d\u0339\3\2\2\2\u034d\u033a\3\2\2\2")
        buf.write("\u034d\u0347\3\2\2\2\u034e\u0354\3\2\2\2\u034f\u0354\5")
        buf.write("h\65\2\u0350\u0351\5\u0144\u00a3\2\u0351\u0352\5\u0146")
        buf.write("\u00a4\2\u0352\u0354\3\2\2\2\u0353\u0337\3\2\2\2\u0353")
        buf.write("\u034f\3\2\2\2\u0353\u0350\3\2\2\2\u0354\u0397\3\2\2\2")
        buf.write("\u0355\u0356\7\u0083\2\2\u0356\u0359\5\34\17\2\u0357\u0358")
        buf.write("\7\u0086\2\2\u0358\u035a\5\34\17\2\u0359\u0357\3\2\2\2")
        buf.write("\u035a\u035b\3\2\2\2\u035b\u0359\3\2\2\2\u035b\u035c\3")
        buf.write("\2\2\2\u035c\u035d\3\2\2\2\u035d\u035e\7\u0084\2\2\u035e")
        buf.write("\u0397\3\2\2\2\u035f\u0360\7d\2\2\u0360\u0364\7\u0083")
        buf.write("\2\2\u0361\u0365\5n8\2\u0362\u0365\5\6\4\2\u0363\u0365")
        buf.write("\7n\2\2\u0364\u0361\3\2\2\2\u0364\u0362\3\2\2\2\u0364")
        buf.write("\u0363\3\2\2\2\u0365\u0366\3\2\2\2\u0366\u0397\7\u0084")
        buf.write("\2\2\u0367\u0368\7\33\2\2\u0368\u0369\7\u0083\2\2\u0369")
        buf.write("\u036a\5\36\20\2\u036a\u036b\7\u0084\2\2\u036b\u0397\3")
        buf.write("\2\2\2\u036c\u036d\7g\2\2\u036d\u036e\7\u0083\2\2\u036e")
        buf.write("\u036f\5\36\20\2\u036f\u0370\7\u0084\2\2\u0370\u0397\3")
        buf.write("\2\2\2\u0371\u0376\7 \2\2\u0372\u0373\7\u0083\2\2\u0373")
        buf.write("\u0374\5\6\4\2\u0374\u0375\7\u0084\2\2\u0375\u0377\3\2")
        buf.write("\2\2\u0376\u0372\3\2\2\2\u0376\u0377\3\2\2\2\u0377\u0397")
        buf.write("\3\2\2\2\u0378\u037a\7\21\2\2\u0379\u0378\3\2\2\2\u0379")
        buf.write("\u037a\3\2\2\2\u037a\u037b\3\2\2\2\u037b\u0381\7!\2\2")
        buf.write("\u037c\u037e\7\u0083\2\2\u037d\u037f\5|?\2\u037e\u037d")
        buf.write("\3\2\2\2\u037e\u037f\3\2\2\2\u037f\u0380\3\2\2\2\u0380")
        buf.write("\u0382\7\u0084\2\2\u0381\u037c\3\2\2\2\u0381\u0382\3\2")
        buf.write("\2\2\u0382\u0383\3\2\2\2\u0383\u0397\5\u00acW\2\u0384")
        buf.write("\u0385\7Z\2\2\u0385\u0386\7\u0083\2\2\u0386\u0387\5\6")
        buf.write("\4\2\u0387\u0388\7\u0084\2\2\u0388\u0397\3\2\2\2\u0389")
        buf.write("\u038a\7B\2\2\u038a\u0390\7\u0083\2\2\u038b\u038c\5\u01b4")
        buf.write("\u00db\2\u038c\u038d\7\u0085\2\2\u038d\u038f\3\2\2\2\u038e")
        buf.write("\u038b\3\2\2\2\u038f\u0392\3\2\2\2\u0390\u038e\3\2\2\2")
        buf.write("\u0390\u0391\3\2\2\2\u0391\u0393\3\2\2\2\u0392\u0390\3")
        buf.write("\2\2\2\u0393\u0394\5\u01b4\u00db\2\u0394\u0395\7\u0084")
        buf.write("\2\2\u0395\u0397\3\2\2\2\u0396\u031d\3\2\2\2\u0396\u031e")
        buf.write("\3\2\2\2\u0396\u0322\3\2\2\2\u0396\u0326\3\2\2\2\u0396")
        buf.write("\u0327\3\2\2\2\u0396\u0328\3\2\2\2\u0396\u0329\3\2\2\2")
        buf.write("\u0396\u032a\3\2\2\2\u0396\u0336\3\2\2\2\u0396\u0355\3")
        buf.write("\2\2\2\u0396\u035f\3\2\2\2\u0396\u0367\3\2\2\2\u0396\u036c")
        buf.write("\3\2\2\2\u0396\u0371\3\2\2\2\u0396\u0379\3\2\2\2\u0396")
        buf.write("\u0384\3\2\2\2\u0396\u0389\3\2\2\2\u0397K\3\2\2\2\u0398")
        buf.write("\u039b\5\36\20\2\u0399\u039b\5N(\2\u039a\u0398\3\2\2\2")
        buf.write("\u039a\u0399\3\2\2\2\u039bM\3\2\2\2\u039c\u039d\7a\2\2")
        buf.write("\u039d\u039e\5\36\20\2\u039eO\3\2\2\2\u039f\u03a1\7\u0096")
        buf.write("\2\2\u03a0\u039f\3\2\2\2\u03a0\u03a1\3\2\2\2\u03a1\u03a2")
        buf.write("\3\2\2\2\u03a2\u03a3\7\u0085\2\2\u03a3\u03a5\5\u01b4\u00db")
        buf.write("\2\u03a4\u03a6\5\30\r\2\u03a5\u03a4\3\2\2\2\u03a5\u03a6")
        buf.write("\3\2\2\2\u03a6Q\3\2\2\2\u03a7\u03a9\7\u0096\2\2\u03a8")
        buf.write("\u03a7\3\2\2\2\u03a8\u03a9\3\2\2\2\u03a9\u03aa\3\2\2\2")
        buf.write("\u03aa\u03ab\7\u0081\2\2\u03ab\u03b0\5T+\2\u03ac\u03ad")
        buf.write("\7\u0086\2\2\u03ad\u03af\5T+\2\u03ae\u03ac\3\2\2\2\u03af")
        buf.write("\u03b2\3\2\2\2\u03b0\u03ae\3\2\2\2\u03b0\u03b1\3\2\2\2")
        buf.write("\u03b1\u03b3\3\2\2\2\u03b2\u03b0\3\2\2\2\u03b3\u03b4\7")
        buf.write("\u0082\2\2\u03b4S\3\2\2\2\u03b5\u03b6\5\u01b4\u00db\2")
        buf.write("\u03b6\u03b7\7\u0087\2\2\u03b7\u03b9\3\2\2\2\u03b8\u03b5")
        buf.write("\3\2\2\2\u03b8\u03b9\3\2\2\2\u03b9\u03ba\3\2\2\2\u03ba")
        buf.write("\u03bb\5\36\20\2\u03bbU\3\2\2\2\u03bc\u03bd\t\t\2\2\u03bd")
        buf.write("W\3\2\2\2\u03be\u03c3\5\36\20\2\u03bf\u03c0\7\u0086\2")
        buf.write("\2\u03c0\u03c2\5\36\20\2\u03c1\u03bf\3\2\2\2\u03c2\u03c5")
        buf.write("\3\2\2\2\u03c3\u03c1\3\2\2\2\u03c3\u03c4\3\2\2\2\u03c4")
        buf.write("Y\3\2\2\2\u03c5\u03c3\3\2\2\2\u03c6\u03c9\5\\/\2\u03c7")
        buf.write("\u03c9\5d\63\2\u03c8\u03c6\3\2\2\2\u03c8\u03c7\3\2\2\2")
        buf.write("\u03c9[\3\2\2\2\u03ca\u03cf\7\177\2\2\u03cb\u03cd\5^\60")
        buf.write("\2\u03cc\u03ce\7\u0086\2\2\u03cd\u03cc\3\2\2\2\u03cd\u03ce")
        buf.write("\3\2\2\2\u03ce\u03d0\3\2\2\2\u03cf\u03cb\3\2\2\2\u03cf")
        buf.write("\u03d0\3\2\2\2\u03d0\u03d1\3\2\2\2\u03d1\u03d2\7\u0080")
        buf.write("\2\2\u03d2]\3\2\2\2\u03d3\u03d8\5`\61\2\u03d4\u03d5\7")
        buf.write("\u0086\2\2\u03d5\u03d7\5`\61\2\u03d6\u03d4\3\2\2\2\u03d7")
        buf.write("\u03da\3\2\2\2\u03d8\u03d6\3\2\2\2\u03d8\u03d9\3\2\2\2")
        buf.write("\u03d9_\3\2\2\2\u03da\u03d8\3\2\2\2\u03db\u03e1\5\u01b4")
        buf.write("\u00db\2\u03dc\u03dd\7\u0081\2\2\u03dd\u03de\5\36\20\2")
        buf.write("\u03de\u03df\7\u0082\2\2\u03df\u03e1\3\2\2\2\u03e0\u03db")
        buf.write("\3\2\2\2\u03e0\u03dc\3\2\2\2\u03e1\u03e2\3\2\2\2\u03e2")
        buf.write("\u03e3\7\u0093\2\2\u03e3\u03e4\5b\62\2\u03e4a\3\2\2\2")
        buf.write("\u03e5\u03e8\5\36\20\2\u03e6\u03e8\5Z.\2\u03e7\u03e5\3")
        buf.write("\2\2\2\u03e7\u03e6\3\2\2\2\u03e8c\3\2\2\2\u03e9\u03ea")
        buf.write("\7\177\2\2\u03ea\u03ef\5f\64\2\u03eb\u03ec\7\u0086\2\2")
        buf.write("\u03ec\u03ee\5f\64\2\u03ed\u03eb\3\2\2\2\u03ee\u03f1\3")
        buf.write("\2\2\2\u03ef\u03ed\3\2\2\2\u03ef\u03f0\3\2\2\2\u03f0\u03f3")
        buf.write("\3\2\2\2\u03f1\u03ef\3\2\2\2\u03f2\u03f4\7\u0086\2\2\u03f3")
        buf.write("\u03f2\3\2\2\2\u03f3\u03f4\3\2\2\2\u03f4\u03f5\3\2\2\2")
        buf.write("\u03f5\u03f6\7\u0080\2\2\u03f6e\3\2\2\2\u03f7\u03fd\5")
        buf.write(" \21\2\u03f8\u03f9\7\177\2\2\u03f9\u03fa\5X-\2\u03fa\u03fb")
        buf.write("\7\u0080\2\2\u03fb\u03fd\3\2\2\2\u03fc\u03f7\3\2\2\2\u03fc")
        buf.write("\u03f8\3\2\2\2\u03fdg\3\2\2\2\u03fe\u0403\7\177\2\2\u03ff")
        buf.write("\u0401\5j\66\2\u0400\u0402\7\u0086\2\2\u0401\u0400\3\2")
        buf.write("\2\2\u0401\u0402\3\2\2\2\u0402\u0404\3\2\2\2\u0403\u03ff")
        buf.write("\3\2\2\2\u0403\u0404\3\2\2\2\u0404\u0405\3\2\2\2\u0405")
        buf.write("\u0406\7\u0080\2\2\u0406i\3\2\2\2\u0407\u040c\5l\67\2")
        buf.write("\u0408\u0409\7\u0086\2\2\u0409\u040b\5l\67\2\u040a\u0408")
        buf.write("\3\2\2\2\u040b\u040e\3\2\2\2\u040c\u040a\3\2\2\2\u040c")
        buf.write("\u040d\3\2\2\2\u040dk\3\2\2\2\u040e\u040c\3\2\2\2\u040f")
        buf.write("\u0415\5H%\2\u0410\u0411\5\u01b4\u00db\2\u0411\u0412\7")
        buf.write("\u0093\2\2\u0412\u0413\5\36\20\2\u0413\u0415\3\2\2\2\u0414")
        buf.write("\u040f\3\2\2\2\u0414\u0410\3\2\2\2\u0415m\3\2\2\2\u0416")
        buf.write("\u041f\5\u01b4\u00db\2\u0417\u0419\5p9\2\u0418\u0417\3")
        buf.write("\2\2\2\u0418\u0419\3\2\2\2\u0419\u0420\3\2\2\2\u041a\u041b")
        buf.write("\7\u0097\2\2\u041b\u041d\5\u01b4\u00db\2\u041c\u041e\5")
        buf.write("p9\2\u041d\u041c\3\2\2\2\u041d\u041e\3\2\2\2\u041e\u0420")
        buf.write("\3\2\2\2\u041f\u0418\3\2\2\2\u041f\u041a\3\2\2\2\u0420")
        buf.write("\u0428\3\2\2\2\u0421\u0422\7\u0085\2\2\u0422\u0424\5\u01b4")
        buf.write("\u00db\2\u0423\u0425\5p9\2\u0424\u0423\3\2\2\2\u0424\u0425")
        buf.write("\3\2\2\2\u0425\u0427\3\2\2\2\u0426\u0421\3\2\2\2\u0427")
        buf.write("\u042a\3\2\2\2\u0428\u0426\3\2\2\2\u0428\u0429\3\2\2\2")
        buf.write("\u0429o\3\2\2\2\u042a\u0428\3\2\2\2\u042b\u042f\7\u0094")
        buf.write("\2\2\u042c\u042e\7\u0086\2\2\u042d\u042c\3\2\2\2\u042e")
        buf.write("\u0431\3\2\2\2\u042f\u042d\3\2\2\2\u042f\u0430\3\2\2\2")
        buf.write("\u0430\u0432\3\2\2\2\u0431\u042f\3\2\2\2\u0432\u0433\7")
        buf.write("\u0095\2\2\u0433q\3\2\2\2\u0434\u0439\5\b\5\2\u0435\u0438")
        buf.write("\5\u0144\u00a3\2\u0436\u0438\7\u008b\2\2\u0437\u0435\3")
        buf.write("\2\2\2\u0437\u0436\3\2\2\2\u0438\u043b\3\2\2\2\u0439\u0437")
        buf.write("\3\2\2\2\u0439\u043a\3\2\2\2\u043a\u043d\3\2\2\2\u043b")
        buf.write("\u0439\3\2\2\2\u043c\u043e\7\u0096\2\2\u043d\u043c\3\2")
        buf.write("\2\2\u043d\u043e\3\2\2\2\u043e\u0440\3\2\2\2\u043f\u0441")
        buf.write("\5t;\2\u0440\u043f\3\2\2\2\u0440\u0441\3\2\2\2\u0441\u0443")
        buf.write("\3\2\2\2\u0442\u0444\5\u01b4\u00db\2\u0443\u0442\3\2\2")
        buf.write("\2\u0443\u0444\3\2\2\2\u0444s\3\2\2\2\u0445\u0446\7\177")
        buf.write("\2\2\u0446\u044b\5v<\2\u0447\u0448\7\u0086\2\2\u0448\u044a")
        buf.write("\5v<\2\u0449\u0447\3\2\2\2\u044a\u044d\3\2\2\2\u044b\u0449")
        buf.write("\3\2\2\2\u044b\u044c\3\2\2\2\u044c\u044e\3\2\2\2\u044d")
        buf.write("\u044b\3\2\2\2\u044e\u044f\7\u0080\2\2\u044fu\3\2\2\2")
        buf.write("\u0450\u0451\5\u01b4\u00db\2\u0451\u0452\7\u0087\2\2\u0452")
        buf.write("\u0453\5\36\20\2\u0453w\3\2\2\2\u0454\u0456\7\21\2\2\u0455")
        buf.write("\u0454\3\2\2\2\u0455\u0456\3\2\2\2\u0456\u0457\3\2\2\2")
        buf.write("\u0457\u0458\5z>\2\u0458\u0459\5\u0178\u00bd\2\u0459\u045a")
        buf.write("\5\u0082B\2\u045ay\3\2\2\2\u045b\u045c\7\u0083\2\2\u045c")
        buf.write("\u0467\7\u0084\2\2\u045d\u045e\7\u0083\2\2\u045e\u045f")
        buf.write("\5|?\2\u045f\u0460\7\u0084\2\2\u0460\u0467\3\2\2\2\u0461")
        buf.write("\u0462\7\u0083\2\2\u0462\u0463\5\u0080A\2\u0463\u0464")
        buf.write("\7\u0084\2\2\u0464\u0467\3\2\2\2\u0465\u0467\5\u01b4\u00db")
        buf.write("\2\u0466\u045b\3\2\2\2\u0466\u045d\3\2\2\2\u0466\u0461")
        buf.write("\3\2\2\2\u0466\u0465\3\2\2\2\u0467{\3\2\2\2\u0468\u046d")
        buf.write("\5~@\2\u0469\u046a\7\u0086\2\2\u046a\u046c\5~@\2\u046b")
        buf.write("\u0469\3\2\2\2\u046c\u046f\3\2\2\2\u046d\u046b\3\2\2\2")
        buf.write("\u046d\u046e\3\2\2\2\u046e}\3\2\2\2\u046f\u046d\3\2\2")
        buf.write("\2\u0470\u0472\t\4\2\2\u0471\u0470\3\2\2\2\u0471\u0472")
        buf.write("\3\2\2\2\u0472\u0473\3\2\2\2\u0473\u0474\5\6\4\2\u0474")
        buf.write("\u0475\5\u01b4\u00db\2\u0475\177\3\2\2\2\u0476\u047b\5")
        buf.write("\u01b4\u00db\2\u0477\u0478\7\u0086\2\2\u0478\u047a\5\u01b4")
        buf.write("\u00db\2\u0479\u0477\3\2\2\2\u047a\u047d\3\2\2\2\u047b")
        buf.write("\u0479\3\2\2\2\u047b\u047c\3\2\2\2\u047c\u0081\3\2\2\2")
        buf.write("\u047d\u047b\3\2\2\2\u047e\u0481\5L\'\2\u047f\u0481\5")
        buf.write("\u00acW\2\u0480\u047e\3\2\2\2\u0480\u047f\3\2\2\2\u0481")
        buf.write("\u0083\3\2\2\2\u0482\u0483\5\u0086D\2\u0483\u0484\5\u0088")
        buf.write("E\2\u0484\u0085\3\2\2\2\u0485\u0487\7\62\2\2\u0486\u0488")
        buf.write("\5\6\4\2\u0487\u0486\3\2\2\2\u0487\u0488\3\2\2\2\u0488")
        buf.write("\u0489\3\2\2\2\u0489\u048a\5\u01b4\u00db\2\u048a\u048b")
        buf.write("\78\2\2\u048b\u048c\5\36\20\2\u048c\u0087\3\2\2\2\u048d")
        buf.write("\u048f\5\u008aF\2\u048e\u048d\3\2\2\2\u048f\u0492\3\2")
        buf.write("\2\2\u0490\u048e\3\2\2\2\u0490\u0491\3\2\2\2\u0491\u0493")
        buf.write("\3\2\2\2\u0492\u0490\3\2\2\2\u0493\u0495\5\u0096L\2\u0494")
        buf.write("\u0496\5\u0098M\2\u0495\u0494\3\2\2\2\u0495\u0496\3\2")
        buf.write("\2\2\u0496\u0089\3\2\2\2\u0497\u049d\5\u0086D\2\u0498")
        buf.write("\u049d\5\u008cG\2\u0499\u049d\5\u008eH\2\u049a\u049d\5")
        buf.write("\u0090I\2\u049b\u049d\5\u0092J\2\u049c\u0497\3\2\2\2\u049c")
        buf.write("\u0498\3\2\2\2\u049c\u0499\3\2\2\2\u049c\u049a\3\2\2\2")
        buf.write("\u049c\u049b\3\2\2\2\u049d\u008b\3\2\2\2\u049e\u049f\7")
        buf.write("?\2\2\u049f\u04a0\5\u01b4\u00db\2\u04a0\u04a1\7\u0093")
        buf.write("\2\2\u04a1\u04a2\5\36\20\2\u04a2\u008d\3\2\2\2\u04a3\u04a4")
        buf.write("\7q\2\2\u04a4\u04a5\5\36\20\2\u04a5\u008f\3\2\2\2\u04a6")
        buf.write("\u04a8\7>\2\2\u04a7\u04a9\5\6\4\2\u04a8\u04a7\3\2\2\2")
        buf.write("\u04a8\u04a9\3\2\2\2\u04a9\u04aa\3\2\2\2\u04aa\u04ab\5")
        buf.write("\u01b4\u00db\2\u04ab\u04ac\78\2\2\u04ac\u04ad\5\36\20")
        buf.write("\2\u04ad\u04ae\7G\2\2\u04ae\u04af\5\36\20\2\u04af\u04b0")
        buf.write("\7(\2\2\u04b0\u04b3\5\36\20\2\u04b1\u04b2\7<\2\2\u04b2")
        buf.write("\u04b4\5\u01b4\u00db\2\u04b3\u04b1\3\2\2\2\u04b3\u04b4")
        buf.write("\3\2\2\2\u04b4\u0091\3\2\2\2\u04b5\u04b6\7I\2\2\u04b6")
        buf.write("\u04bb\5\u0094K\2\u04b7\u04b8\7\u0086\2\2\u04b8\u04ba")
        buf.write("\5\u0094K\2\u04b9\u04b7\3\2\2\2\u04ba\u04bd\3\2\2\2\u04bb")
        buf.write("\u04b9\3\2\2\2\u04bb\u04bc\3\2\2\2\u04bc\u0093\3\2\2\2")
        buf.write("\u04bd\u04bb\3\2\2\2\u04be\u04c0\5\36\20\2\u04bf\u04c1")
        buf.write("\t\n\2\2\u04c0\u04bf\3\2\2\2\u04c0\u04c1\3\2\2\2\u04c1")
        buf.write("\u0095\3\2\2\2\u04c2\u04c3\7W\2\2\u04c3\u04ca\5\36\20")
        buf.write("\2\u04c4\u04c5\7\65\2\2\u04c5\u04c6\5\36\20\2\u04c6\u04c7")
        buf.write("\7\26\2\2\u04c7\u04c8\5\36\20\2\u04c8\u04ca\3\2\2\2\u04c9")
        buf.write("\u04c2\3\2\2\2\u04c9\u04c4\3\2\2\2\u04ca\u0097\3\2\2\2")
        buf.write("\u04cb\u04cc\7<\2\2\u04cc\u04cd\5\u01b4\u00db\2\u04cd")
        buf.write("\u04ce\5\u0088E\2\u04ce\u0099\3\2\2\2\u04cf\u04d3\5\u00a6")
        buf.write("T\2\u04d0\u04d3\5\u009cO\2\u04d1\u04d3\5\u00a8U\2\u04d2")
        buf.write("\u04cf\3\2\2\2\u04d2\u04d0\3\2\2\2\u04d2\u04d1\3\2\2\2")
        buf.write("\u04d3\u009b\3\2\2\2\u04d4\u04d5\5\u00aeX\2\u04d5\u04d6")
        buf.write("\7\u0088\2\2\u04d6\u04dc\3\2\2\2\u04d7\u04d8\5\u00b6\\")
        buf.write("\2\u04d8\u04d9\7\u0088\2\2\u04d9\u04dc\3\2\2\2\u04da\u04dc")
        buf.write("\5\u009eP\2\u04db\u04d4\3\2\2\2\u04db\u04d7\3\2\2\2\u04db")
        buf.write("\u04da\3\2\2\2\u04dc\u009d\3\2\2\2\u04dd\u04de\5\u00a0")
        buf.write("Q\2\u04de\u04df\5\u00a4S\2\u04df\u009f\3\2\2\2\u04e0\u04e2")
        buf.write("\5\u00a2R\2\u04e1\u04e0\3\2\2\2\u04e1\u04e2\3\2\2\2\u04e2")
        buf.write("\u04e3\3\2\2\2\u04e3\u04e4\5\u0114\u008b\2\u04e4\u04e6")
        buf.write("\5\u01b4\u00db\2\u04e5\u04e7\5\u00e8u\2\u04e6\u04e5\3")
        buf.write("\2\2\2\u04e6\u04e7\3\2\2\2\u04e7\u04e8\3\2\2\2\u04e8\u04ea")
        buf.write("\7\u0083\2\2\u04e9\u04eb\5\u011a\u008e\2\u04ea\u04e9\3")
        buf.write("\2\2\2\u04ea\u04eb\3\2\2\2\u04eb\u04ec\3\2\2\2\u04ec\u04ee")
        buf.write("\7\u0084\2\2\u04ed\u04ef\5\u00f0y\2\u04ee\u04ed\3\2\2")
        buf.write("\2\u04ee\u04ef\3\2\2\2\u04ef\u00a1\3\2\2\2\u04f0\u04f2")
        buf.write("\t\13\2\2\u04f1\u04f3\7\\\2\2\u04f2\u04f1\3\2\2\2\u04f2")
        buf.write("\u04f3\3\2\2\2\u04f3\u04f7\3\2\2\2\u04f4\u04f5\7\\\2\2")
        buf.write("\u04f5\u04f7\t\13\2\2\u04f6\u04f0\3\2\2\2\u04f6\u04f4")
        buf.write("\3\2\2\2\u04f7\u00a3\3\2\2\2\u04f8\u04fe\5\u00acW\2\u04f9")
        buf.write("\u04fa\5\u0178\u00bd\2\u04fa\u04fb\5L\'\2\u04fb\u04fc")
        buf.write("\7\u0088\2\2\u04fc\u04fe\3\2\2\2\u04fd\u04f8\3\2\2\2\u04fd")
        buf.write("\u04f9\3\2\2\2\u04fe\u00a5\3\2\2\2\u04ff\u0500\5\u01b4")
        buf.write("\u00db\2\u0500\u0501\7\u0087\2\2\u0501\u0502\5\u009aN")
        buf.write("\2\u0502\u00a7\3\2\2\2\u0503\u0506\5\u00acW\2\u0504\u0506")
        buf.write("\5\u00aaV\2\u0505\u0503\3\2\2\2\u0505\u0504\3\2\2\2\u0506")
        buf.write("\u00a9\3\2\2\2\u0507\u058a\7\u0088\2\2\u0508\u0509\5\36")
        buf.write("\20\2\u0509\u050a\7\u0088\2\2\u050a\u058a\3\2\2\2\u050b")
        buf.write("\u050c\7\66\2\2\u050c\u050d\7\u0083\2\2\u050d\u050e\5")
        buf.write("\36\20\2\u050e\u050f\7\u0084\2\2\u050f\u0512\5\u00b8]")
        buf.write("\2\u0510\u0511\7&\2\2\u0511\u0513\5\u00b8]\2\u0512\u0510")
        buf.write("\3\2\2\2\u0512\u0513\3\2\2\2\u0513\u058a\3\2\2\2\u0514")
        buf.write("\u0515\7_\2\2\u0515\u0516\7\u0083\2\2\u0516\u0517\5\36")
        buf.write("\20\2\u0517\u0518\7\u0084\2\2\u0518\u051c\7\177\2\2\u0519")
        buf.write("\u051b\5\u00ba^\2\u051a\u0519\3\2\2\2\u051b\u051e\3\2")
        buf.write("\2\2\u051c\u051a\3\2\2\2\u051c\u051d\3\2\2\2\u051d\u051f")
        buf.write("\3\2\2\2\u051e\u051c\3\2\2\2\u051f\u0520\7\u0080\2\2\u0520")
        buf.write("\u058a\3\2\2\2\u0521\u0522\7r\2\2\u0522\u0523\7\u0083")
        buf.write("\2\2\u0523\u0524\5\36\20\2\u0524\u0525\7\u0084\2\2\u0525")
        buf.write("\u0526\5\u00a8U\2\u0526\u058a\3\2\2\2\u0527\u0528\7#\2")
        buf.write("\2\u0528\u0529\5\u00a8U\2\u0529\u052a\7r\2\2\u052a\u052b")
        buf.write("\7\u0083\2\2\u052b\u052c\5\36\20\2\u052c\u052d\7\u0084")
        buf.write("\2\2\u052d\u052e\7\u0088\2\2\u052e\u058a\3\2\2\2\u052f")
        buf.write("\u0530\7\60\2\2\u0530\u0532\7\u0083\2\2\u0531\u0533\5")
        buf.write("\u00c2b\2\u0532\u0531\3\2\2\2\u0532\u0533\3\2\2\2\u0533")
        buf.write("\u0534\3\2\2\2\u0534\u0536\7\u0088\2\2\u0535\u0537\5\36")
        buf.write("\20\2\u0536\u0535\3\2\2\2\u0536\u0537\3\2\2\2\u0537\u0538")
        buf.write("\3\2\2\2\u0538\u053a\7\u0088\2\2\u0539\u053b\5\u00c4c")
        buf.write("\2\u053a\u0539\3\2\2\2\u053a\u053b\3\2\2\2\u053b\u053c")
        buf.write("\3\2\2\2\u053c\u053d\7\u0084\2\2\u053d\u058a\5\u00a8U")
        buf.write("\2\u053e\u0540\7\22\2\2\u053f\u053e\3\2\2\2\u053f\u0540")
        buf.write("\3\2\2\2\u0540\u0541\3\2\2\2\u0541\u0542\7\61\2\2\u0542")
        buf.write("\u0543\7\u0083\2\2\u0543\u0544\5\u00b0Y\2\u0544\u0545")
        buf.write("\5\u01b4\u00db\2\u0545\u0546\78\2\2\u0546\u0547\5\36\20")
        buf.write("\2\u0547\u0548\7\u0084\2\2\u0548\u0549\5\u00a8U\2\u0549")
        buf.write("\u058a\3\2\2\2\u054a\u054b\7\25\2\2\u054b\u058a\7\u0088")
        buf.write("\2\2\u054c\u054d\7\36\2\2\u054d\u058a\7\u0088\2\2\u054e")
        buf.write("\u0553\7\64\2\2\u054f\u0554\5\u01b4\u00db\2\u0550\u0551")
        buf.write("\7\30\2\2\u0551\u0554\5\36\20\2\u0552\u0554\7 \2\2\u0553")
        buf.write("\u054f\3\2\2\2\u0553\u0550\3\2\2\2\u0553\u0552\3\2\2\2")
        buf.write("\u0554\u0555\3\2\2\2\u0555\u058a\7\u0088\2\2\u0556\u0558")
        buf.write("\7T\2\2\u0557\u0559\5\36\20\2\u0558\u0557\3\2\2\2\u0558")
        buf.write("\u0559\3\2\2\2\u0559\u055a\3\2\2\2\u055a\u058a\7\u0088")
        buf.write("\2\2\u055b\u055d\7a\2\2\u055c\u055e\5\36\20\2\u055d\u055c")
        buf.write("\3\2\2\2\u055d\u055e\3\2\2\2\u055e\u055f\3\2\2\2\u055f")
        buf.write("\u058a\7\u0088\2\2\u0560\u0561\7c\2\2\u0561\u0567\5\u00ac")
        buf.write("W\2\u0562\u0564\5\u00c6d\2\u0563\u0565\5\u00ceh\2\u0564")
        buf.write("\u0563\3\2\2\2\u0564\u0565\3\2\2\2\u0565\u0568\3\2\2\2")
        buf.write("\u0566\u0568\5\u00ceh\2\u0567\u0562\3\2\2\2\u0567\u0566")
        buf.write("\3\2\2\2\u0568\u058a\3\2\2\2\u0569\u056a\7\33\2\2\u056a")
        buf.write("\u058a\5\u00acW\2\u056b\u056c\7g\2\2\u056c\u058a\5\u00ac")
        buf.write("W\2\u056d\u056e\7@\2\2\u056e\u056f\7\u0083\2\2\u056f\u0570")
        buf.write("\5\36\20\2\u0570\u0571\7\u0084\2\2\u0571\u0572\5\u00a8")
        buf.write("U\2\u0572\u058a\3\2\2\2\u0573\u0574\7k\2\2\u0574\u0575")
        buf.write("\7\u0083\2\2\u0575\u0576\5\u00d0i\2\u0576\u0577\7\u0084")
        buf.write("\2\2\u0577\u0578\5\u00a8U\2\u0578\u058a\3\2\2\2\u0579")
        buf.write("\u057d\7s\2\2\u057a\u057b\7T\2\2\u057b\u057e\5\36\20\2")
        buf.write("\u057c\u057e\7\25\2\2\u057d\u057a\3\2\2\2\u057d\u057c")
        buf.write("\3\2\2\2\u057e\u057f\3\2\2\2\u057f\u058a\7\u0088\2\2\u0580")
        buf.write("\u0581\7i\2\2\u0581\u058a\5\u00acW\2\u0582\u0583\7.\2")
        buf.write("\2\u0583\u0584\7\u0083\2\2\u0584\u0585\5\u016c\u00b7\2")
        buf.write("\u0585\u0586\5\u016e\u00b8\2\u0586\u0587\7\u0084\2\2\u0587")
        buf.write("\u0588\5\u00a8U\2\u0588\u058a\3\2\2\2\u0589\u0507\3\2")
        buf.write("\2\2\u0589\u0508\3\2\2\2\u0589\u050b\3\2\2\2\u0589\u0514")
        buf.write("\3\2\2\2\u0589\u0521\3\2\2\2\u0589\u0527\3\2\2\2\u0589")
        buf.write("\u052f\3\2\2\2\u0589\u053f\3\2\2\2\u0589\u054a\3\2\2\2")
        buf.write("\u0589\u054c\3\2\2\2\u0589\u054e\3\2\2\2\u0589\u0556\3")
        buf.write("\2\2\2\u0589\u055b\3\2\2\2\u0589\u0560\3\2\2\2\u0589\u0569")
        buf.write("\3\2\2\2\u0589\u056b\3\2\2\2\u0589\u056d\3\2\2\2\u0589")
        buf.write("\u0573\3\2\2\2\u0589\u0579\3\2\2\2\u0589\u0580\3\2\2\2")
        buf.write("\u0589\u0582\3\2\2\2\u058a\u00ab\3\2\2\2\u058b\u058d\7")
        buf.write("\177\2\2\u058c\u058e\5\u00c0a\2\u058d\u058c\3\2\2\2\u058d")
        buf.write("\u058e\3\2\2\2\u058e\u058f\3\2\2\2\u058f\u0590\7\u0080")
        buf.write("\2\2\u0590\u00ad\3\2\2\2\u0591\u0596\7k\2\2\u0592\u0596")
        buf.write("\7R\2\2\u0593\u0594\7R\2\2\u0594\u0596\7Q\2\2\u0595\u0591")
        buf.write("\3\2\2\2\u0595\u0592\3\2\2\2\u0595\u0593\3\2\2\2\u0595")
        buf.write("\u0596\3\2\2\2\u0596\u0597\3\2\2\2\u0597\u0598\5\u00b0")
        buf.write("Y\2\u0598\u059d\5\u00b2Z\2\u0599\u059a\7\u0086\2\2\u059a")
        buf.write("\u059c\5\u00b2Z\2\u059b\u0599\3\2\2\2\u059c\u059f\3\2")
        buf.write("\2\2\u059d\u059b\3\2\2\2\u059d\u059e\3\2\2\2\u059e\u05a5")
        buf.write("\3\2\2\2\u059f\u059d\3\2\2\2\u05a0\u05a1\7.\2\2\u05a1")
        buf.write("\u05a2\5\u016c\u00b7\2\u05a2\u05a3\5\u016e\u00b8\2\u05a3")
        buf.write("\u05a5\3\2\2\2\u05a4\u0595\3\2\2\2\u05a4\u05a0\3\2\2\2")
        buf.write("\u05a5\u00af\3\2\2\2\u05a6\u05a9\7l\2\2\u05a7\u05a9\5")
        buf.write("\6\4\2\u05a8\u05a6\3\2\2\2\u05a8\u05a7\3\2\2\2\u05a9\u00b1")
        buf.write("\3\2\2\2\u05aa\u05b0\5\u01b4\u00db\2\u05ab\u05ad\7\u0093")
        buf.write("\2\2\u05ac\u05ae\7R\2\2\u05ad\u05ac\3\2\2\2\u05ad\u05ae")
        buf.write("\3\2\2\2\u05ae\u05af\3\2\2\2\u05af\u05b1\5\u00b4[\2\u05b0")
        buf.write("\u05ab\3\2\2\2\u05b0\u05b1\3\2\2\2\u05b1\u00b3\3\2\2\2")
        buf.write("\u05b2\u05b6\5\36\20\2\u05b3\u05b6\5\u0146\u00a4\2\u05b4")
        buf.write("\u05b6\5\u0176\u00bc\2\u05b5\u05b2\3\2\2\2\u05b5\u05b3")
        buf.write("\3\2\2\2\u05b5\u05b4\3\2\2\2\u05b6\u00b5\3\2\2\2\u05b7")
        buf.write("\u05b8\7\35\2\2\u05b8\u05b9\5\6\4\2\u05b9\u05ba\5\u010a")
        buf.write("\u0086\2\u05ba\u00b7\3\2\2\2\u05bb\u05be\5\u00acW\2\u05bc")
        buf.write("\u05be\5\u00aaV\2\u05bd\u05bb\3\2\2\2\u05bd\u05bc\3\2")
        buf.write("\2\2\u05be\u00b9\3\2\2\2\u05bf\u05c1\5\u00bc_\2\u05c0")
        buf.write("\u05bf\3\2\2\2\u05c1\u05c2\3\2\2\2\u05c2\u05c0\3\2\2\2")
        buf.write("\u05c2\u05c3\3\2\2\2\u05c3\u05c4\3\2\2\2\u05c4\u05c5\5")
        buf.write("\u00c0a\2\u05c5\u00bb\3\2\2\2\u05c6\u05c7\7\30\2\2\u05c7")
        buf.write("\u05c9\5\36\20\2\u05c8\u05ca\5\u00be`\2\u05c9\u05c8\3")
        buf.write("\2\2\2\u05c9\u05ca\3\2\2\2\u05ca\u05cb\3\2\2\2\u05cb\u05cc")
        buf.write("\7\u0087\2\2\u05cc\u05d0\3\2\2\2\u05cd\u05ce\7 \2\2\u05ce")
        buf.write("\u05d0\7\u0087\2\2\u05cf\u05c6\3\2\2\2\u05cf\u05cd\3\2")
        buf.write("\2\2\u05d0\u00bd\3\2\2\2\u05d1\u05d2\7p\2\2\u05d2\u05d3")
        buf.write("\5\36\20\2\u05d3\u00bf\3\2\2\2\u05d4\u05d6\5\u009aN\2")
        buf.write("\u05d5\u05d4\3\2\2\2\u05d6\u05d7\3\2\2\2\u05d7\u05d5\3")
        buf.write("\2\2\2\u05d7\u05d8\3\2\2\2\u05d8\u00c1\3\2\2\2\u05d9\u05e3")
        buf.write("\5\u00aeX\2\u05da\u05df\5\36\20\2\u05db\u05dc\7\u0086")
        buf.write("\2\2\u05dc\u05de\5\36\20\2\u05dd\u05db\3\2\2\2\u05de\u05e1")
        buf.write("\3\2\2\2\u05df\u05dd\3\2\2\2\u05df\u05e0\3\2\2\2\u05e0")
        buf.write("\u05e3\3\2\2\2\u05e1\u05df\3\2\2\2\u05e2\u05d9\3\2\2\2")
        buf.write("\u05e2\u05da\3\2\2\2\u05e3\u00c3\3\2\2\2\u05e4\u05e9\5")
        buf.write("\36\20\2\u05e5\u05e6\7\u0086\2\2\u05e6\u05e8\5\36\20\2")
        buf.write("\u05e7\u05e5\3\2\2\2\u05e8\u05eb\3\2\2\2\u05e9\u05e7\3")
        buf.write("\2\2\2\u05e9\u05ea\3\2\2\2\u05ea\u00c5\3\2\2\2\u05eb\u05e9")
        buf.write("\3\2\2\2\u05ec\u05f0\5\u00c8e\2\u05ed\u05ef\5\u00c8e\2")
        buf.write("\u05ee\u05ed\3\2\2\2\u05ef\u05f2\3\2\2\2\u05f0\u05ee\3")
        buf.write("\2\2\2\u05f0\u05f1\3\2\2\2\u05f1\u05f4\3\2\2\2\u05f2\u05f0")
        buf.write("\3\2\2\2\u05f3\u05f5\5\u00caf\2\u05f4\u05f3\3\2\2\2\u05f4")
        buf.write("\u05f5\3\2\2\2\u05f5\u05f8\3\2\2\2\u05f6\u05f8\5\u00ca")
        buf.write("f\2\u05f7\u05ec\3\2\2\2\u05f7\u05f6\3\2\2\2\u05f8\u00c7")
        buf.write("\3\2\2\2\u05f9\u05fa\7\31\2\2\u05fa\u05fb\7\u0083\2\2")
        buf.write("\u05fb\u05fd\5\26\f\2\u05fc\u05fe\5\u01b4\u00db\2\u05fd")
        buf.write("\u05fc\3\2\2\2\u05fd\u05fe\3\2\2\2\u05fe\u05ff\3\2\2\2")
        buf.write("\u05ff\u0601\7\u0084\2\2\u0600\u0602\5\u00ccg\2\u0601")
        buf.write("\u0600\3\2\2\2\u0601\u0602\3\2\2\2\u0602\u0603\3\2\2\2")
        buf.write("\u0603\u0604\5\u00acW\2\u0604\u00c9\3\2\2\2\u0605\u0607")
        buf.write("\7\31\2\2\u0606\u0608\5\u00ccg\2\u0607\u0606\3\2\2\2\u0607")
        buf.write("\u0608\3\2\2\2\u0608\u0609\3\2\2\2\u0609\u060a\5\u00ac")
        buf.write("W\2\u060a\u00cb\3\2\2\2\u060b\u060c\7p\2\2\u060c\u060d")
        buf.write("\7\u0083\2\2\u060d\u060e\5\36\20\2\u060e\u060f\7\u0084")
        buf.write("\2\2\u060f\u00cd\3\2\2\2\u0610\u0611\7-\2\2\u0611\u0612")
        buf.write("\5\u00acW\2\u0612\u00cf\3\2\2\2\u0613\u0616\5\u00aeX\2")
        buf.write("\u0614\u0616\5\36\20\2\u0615\u0613\3\2\2\2\u0615\u0614")
        buf.write("\3\2\2\2\u0616\u00d1\3\2\2\2\u0617\u0618\7C\2\2\u0618")
        buf.write("\u0619\5\u00d4k\2\u0619\u061b\5\u00d6l\2\u061a\u061c\7")
        buf.write("\u0088\2\2\u061b\u061a\3\2\2\2\u061b\u061c\3\2\2\2\u061c")
        buf.write("\u00d3\3\2\2\2\u061d\u0622\5\u01b4\u00db\2\u061e\u061f")
        buf.write("\7\u0085\2\2\u061f\u0621\5\u01b4\u00db\2\u0620\u061e\3")
        buf.write("\2\2\2\u0621\u0624\3\2\2\2\u0622\u0620\3\2\2\2\u0622\u0623")
        buf.write("\3\2\2\2\u0623\u00d5\3\2\2\2\u0624\u0622\3\2\2\2\u0625")
        buf.write("\u0627\7\177\2\2\u0626\u0628\5\u00d8m\2\u0627\u0626\3")
        buf.write("\2\2\2\u0627\u0628\3\2\2\2\u0628\u062a\3\2\2\2\u0629\u062b")
        buf.write("\5\u00dco\2\u062a\u0629\3\2\2\2\u062a\u062b\3\2\2\2\u062b")
        buf.write("\u062d\3\2\2\2\u062c\u062e\5\u00e0q\2\u062d\u062c\3\2")
        buf.write("\2\2\u062d\u062e\3\2\2\2\u062e\u062f\3\2\2\2\u062f\u0630")
        buf.write("\7\u0080\2\2\u0630\u00d7\3\2\2\2\u0631\u0633\5\u00dan")
        buf.write("\2\u0632\u0631\3\2\2\2\u0633\u0634\3\2\2\2\u0634\u0632")
        buf.write("\3\2\2\2\u0634\u0635\3\2\2\2\u0635\u00d9\3\2\2\2\u0636")
        buf.write("\u0637\7+\2\2\u0637\u0638\7\r\2\2\u0638\u0639\5\u01b4")
        buf.write("\u00db\2\u0639\u063a\7\u0088\2\2\u063a\u00db\3\2\2\2\u063b")
        buf.write("\u063d\5\u00dep\2\u063c\u063b\3\2\2\2\u063d\u063e\3\2")
        buf.write("\2\2\u063e\u063c\3\2\2\2\u063e\u063f\3\2\2\2\u063f\u00dd")
        buf.write("\3\2\2\2\u0640\u0641\7k\2\2\u0641\u0642\5\u01b4\u00db")
        buf.write("\2\u0642\u0643\7\u0093\2\2\u0643\u0644\5\4\3\2\u0644\u0645")
        buf.write("\7\u0088\2\2\u0645\u0650\3\2\2\2\u0646\u0647\7k\2\2\u0647")
        buf.write("\u0648\5\4\3\2\u0648\u0649\7\u0088\2\2\u0649\u0650\3\2")
        buf.write("\2\2\u064a\u064b\7k\2\2\u064b\u064c\7\\\2\2\u064c\u064d")
        buf.write("\5\4\3\2\u064d\u064e\7\u0088\2\2\u064e\u0650\3\2\2\2\u064f")
        buf.write("\u0640\3\2\2\2\u064f\u0646\3\2\2\2\u064f\u064a\3\2\2\2")
        buf.write("\u0650\u00df\3\2\2\2\u0651\u0653\5\u00e2r\2\u0652\u0651")
        buf.write("\3\2\2\2\u0653\u0654\3\2\2\2\u0654\u0652\3\2\2\2\u0654")
        buf.write("\u0655\3\2\2\2\u0655\u00e1\3\2\2\2\u0656\u0659\5\u00d2")
        buf.write("j\2\u0657\u0659\5\u00e4s\2\u0658\u0656\3\2\2\2\u0658\u0657")
        buf.write("\3\2\2\2\u0659\u00e3\3\2\2\2\u065a\u065c\5\u0160\u00b1")
        buf.write("\2\u065b\u065a\3\2\2\2\u065b\u065c\3\2\2\2\u065c\u065e")
        buf.write("\3\2\2\2\u065d\u065f\5\u0102\u0082\2\u065e\u065d\3\2\2")
        buf.write("\2\u065e\u065f\3\2\2\2\u065f\u0665\3\2\2\2\u0660\u0666")
        buf.write("\5\u0190\u00c9\2\u0661\u0666\5\u0192\u00ca\2\u0662\u0666")
        buf.write("\5\u0194\u00cb\2\u0663\u0666\5\u0196\u00cc\2\u0664\u0666")
        buf.write("\5\u0198\u00cd\2\u0665\u0660\3\2\2\2\u0665\u0661\3\2\2")
        buf.write("\2\u0665\u0662\3\2\2\2\u0665\u0663\3\2\2\2\u0665\u0664")
        buf.write("\3\2\2\2\u0666\u00e5\3\2\2\2\u0667\u0668\5\u01b4\u00db")
        buf.write("\2\u0668\u0669\7\u0097\2\2\u0669\u066b\5\u01b4\u00db\2")
        buf.write("\u066a\u066c\5\30\r\2\u066b\u066a\3\2\2\2\u066b\u066c")
        buf.write("\3\2\2\2\u066c\u00e7\3\2\2\2\u066d\u066e\7\u0094\2\2\u066e")
        buf.write("\u0673\5\u00eav\2\u066f\u0670\7\u0086\2\2\u0670\u0672")
        buf.write("\5\u00eav\2\u0671\u066f\3\2\2\2\u0672\u0675\3\2\2\2\u0673")
        buf.write("\u0671\3\2\2\2\u0673\u0674\3\2\2\2\u0674\u0676\3\2\2\2")
        buf.write("\u0675\u0673\3\2\2\2\u0676\u0677\7\u0095\2\2\u0677\u00e9")
        buf.write("\3\2\2\2\u0678\u067a\5\u0160\u00b1\2\u0679\u0678\3\2\2")
        buf.write("\2\u0679\u067a\3\2\2\2\u067a\u067b\3\2\2\2\u067b\u067c")
        buf.write("\5\u01b4\u00db\2\u067c\u00eb\3\2\2\2\u067d\u067e\7\u0087")
        buf.write("\2\2\u067e\u0683\5\26\f\2\u067f\u0680\7\u0086\2\2\u0680")
        buf.write("\u0682\5\4\3\2\u0681\u067f\3\2\2\2\u0682\u0685\3\2\2\2")
        buf.write("\u0683\u0681\3\2\2\2\u0683\u0684\3\2\2\2\u0684\u00ed\3")
        buf.write("\2\2\2\u0685\u0683\3\2\2\2\u0686\u068b\5\4\3\2\u0687\u0688")
        buf.write("\7\u0086\2\2\u0688\u068a\5\4\3\2\u0689\u0687\3\2\2\2\u068a")
        buf.write("\u068d\3\2\2\2\u068b\u0689\3\2\2\2\u068b\u068c\3\2\2\2")
        buf.write("\u068c\u00ef\3\2\2\2\u068d\u068b\3\2\2\2\u068e\u0690\5")
        buf.write("\u00f2z\2\u068f\u068e\3\2\2\2\u0690\u0691\3\2\2\2\u0691")
        buf.write("\u068f\3\2\2\2\u0691\u0692\3\2\2\2\u0692\u00f1\3\2\2\2")
        buf.write("\u0693\u0694\7q\2\2\u0694\u0695\5\u01b4\u00db\2\u0695")
        buf.write("\u0696\7\u0087\2\2\u0696\u0697\5\u00f4{\2\u0697\u00f3")
        buf.write("\3\2\2\2\u0698\u06a3\5\u00fa~\2\u0699\u069c\5\u00f6|\2")
        buf.write("\u069a\u069b\7\u0086\2\2\u069b\u069d\5\u00f8}\2\u069c")
        buf.write("\u069a\3\2\2\2\u069c\u069d\3\2\2\2\u069d\u06a0\3\2\2\2")
        buf.write("\u069e\u069f\7\u0086\2\2\u069f\u06a1\5\u00fa~\2\u06a0")
        buf.write("\u069e\3\2\2\2\u06a0\u06a1\3\2\2\2\u06a1\u06a3\3\2\2\2")
        buf.write("\u06a2\u0698\3\2\2\2\u06a2\u0699\3\2\2\2\u06a3\u00f5\3")
        buf.write("\2\2\2\u06a4\u06ac\5\26\f\2\u06a5\u06a7\7\34\2\2\u06a6")
        buf.write("\u06a8\7\u0096\2\2\u06a7\u06a6\3\2\2\2\u06a7\u06a8\3\2")
        buf.write("\2\2\u06a8\u06ac\3\2\2\2\u06a9\u06ac\7^\2\2\u06aa\u06ac")
        buf.write("\7h\2\2\u06ab\u06a4\3\2\2\2\u06ab\u06a5\3\2\2\2\u06ab")
        buf.write("\u06a9\3\2\2\2\u06ab\u06aa\3\2\2\2\u06ac\u00f7\3\2\2\2")
        buf.write("\u06ad\u06b2\5\4\3\2\u06ae\u06af\7\u0086\2\2\u06af\u06b1")
        buf.write("\5\4\3\2\u06b0\u06ae\3\2\2\2\u06b1\u06b4\3\2\2\2\u06b2")
        buf.write("\u06b0\3\2\2\2\u06b2\u06b3\3\2\2\2\u06b3\u00f9\3\2\2\2")
        buf.write("\u06b4\u06b2\3\2\2\2\u06b5\u06b6\7D\2\2\u06b6\u06b7\7")
        buf.write("\u0083\2\2\u06b7\u06b8\7\u0084\2\2\u06b8\u00fb\3\2\2\2")
        buf.write("\u06b9\u06bb\7\177\2\2\u06ba\u06bc\5\u00fe\u0080\2\u06bb")
        buf.write("\u06ba\3\2\2\2\u06bb\u06bc\3\2\2\2\u06bc\u06bd\3\2\2\2")
        buf.write("\u06bd\u06be\7\u0080\2\2\u06be\u00fd\3\2\2\2\u06bf\u06c1")
        buf.write("\5\u0100\u0081\2\u06c0\u06bf\3\2\2\2\u06c1\u06c2\3\2\2")
        buf.write("\2\u06c2\u06c0\3\2\2\2\u06c2\u06c3\3\2\2\2\u06c3\u00ff")
        buf.write("\3\2\2\2\u06c4\u06c6\5\u0160\u00b1\2\u06c5\u06c4\3\2\2")
        buf.write("\2\u06c5\u06c6\3\2\2\2\u06c6\u06c8\3\2\2\2\u06c7\u06c9")
        buf.write("\5\u0102\u0082\2\u06c8\u06c7\3\2\2\2\u06c8\u06c9\3\2\2")
        buf.write("\2\u06c9\u06cc\3\2\2\2\u06ca\u06cd\5\u0106\u0084\2\u06cb")
        buf.write("\u06cd\5\u01a4\u00d3\2\u06cc\u06ca\3\2\2\2\u06cc\u06cb")
        buf.write("\3\2\2\2\u06cd\u0101\3\2\2\2\u06ce\u06d0\5\u0104\u0083")
        buf.write("\2\u06cf\u06ce\3\2\2\2\u06d0\u06d1\3\2\2\2\u06d1\u06cf")
        buf.write("\3\2\2\2\u06d1\u06d2\3\2\2\2\u06d2\u0103\3\2\2\2\u06d3")
        buf.write("\u06d4\t\f\2\2\u06d4\u0105\3\2\2\2\u06d5\u06e9\5\u01a0")
        buf.write("\u00d1\2\u06d6\u06e9\5\u0108\u0085\2\u06d7\u06e9\5\u019a")
        buf.write("\u00ce\2\u06d8\u06de\5\u0136\u009c\2\u06d9\u06df\5\u013a")
        buf.write("\u009e\2\u06da\u06db\5\u0178\u00bd\2\u06db\u06dc\5L\'")
        buf.write("\2\u06dc\u06dd\7\u0088\2\2\u06dd\u06df\3\2\2\2\u06de\u06d9")
        buf.write("\3\2\2\2\u06de\u06da\3\2\2\2\u06df\u06e9\3\2\2\2\u06e0")
        buf.write("\u06e9\5\u01a6\u00d4\2\u06e1\u06e2\7n\2\2\u06e2\u06e9")
        buf.write("\5\u01a8\u00d5\2\u06e3\u06e9\5\u0190\u00c9\2\u06e4\u06e9")
        buf.write("\5\u0192\u00ca\2\u06e5\u06e9\5\u0194\u00cb\2\u06e6\u06e9")
        buf.write("\5\u0196\u00cc\2\u06e7\u06e9\5\u0198\u00cd\2\u06e8\u06d5")
        buf.write("\3\2\2\2\u06e8\u06d6\3\2\2\2\u06e8\u06d7\3\2\2\2\u06e8")
        buf.write("\u06d8\3\2\2\2\u06e8\u06e0\3\2\2\2\u06e8\u06e1\3\2\2\2")
        buf.write("\u06e8\u06e3\3\2\2\2\u06e8\u06e4\3\2\2\2\u06e8\u06e5\3")
        buf.write("\2\2\2\u06e8\u06e6\3\2\2\2\u06e8\u06e7\3\2\2\2\u06e9\u0107")
        buf.write("\3\2\2\2\u06ea\u06f0\7R\2\2\u06eb\u06ec\7Q\2\2\u06ec\u06f0")
        buf.write("\7R\2\2\u06ed\u06ee\7R\2\2\u06ee\u06f0\7Q\2\2\u06ef\u06ea")
        buf.write("\3\2\2\2\u06ef\u06eb\3\2\2\2\u06ef\u06ed\3\2\2\2\u06ef")
        buf.write("\u06f0\3\2\2\2\u06f0\u06f1\3\2\2\2\u06f1\u06fb\5\6\4\2")
        buf.write("\u06f2\u06f3\5\4\3\2\u06f3\u06f4\7\u0085\2\2\u06f4\u06f5")
        buf.write("\5\u01a2\u00d2\2\u06f5\u06fc\3\2\2\2\u06f6\u06fc\5\u01a8")
        buf.write("\u00d5\2\u06f7\u06fc\5\u019e\u00d0\2\u06f8\u06fc\5\u01a2")
        buf.write("\u00d2\2\u06f9\u06fc\5\u01ac\u00d7\2\u06fa\u06fc\5\u019c")
        buf.write("\u00cf\2\u06fb\u06f2\3\2\2\2\u06fb\u06f6\3\2\2\2\u06fb")
        buf.write("\u06f7\3\2\2\2\u06fb\u06f8\3\2\2\2\u06fb\u06f9\3\2\2\2")
        buf.write("\u06fb\u06fa\3\2\2\2\u06fc\u0109\3\2\2\2\u06fd\u0702\5")
        buf.write("\u010c\u0087\2\u06fe\u06ff\7\u0086\2\2\u06ff\u0701\5\u010c")
        buf.write("\u0087\2\u0700\u06fe\3\2\2\2\u0701\u0704\3\2\2\2\u0702")
        buf.write("\u0700\3\2\2\2\u0702\u0703\3\2\2\2\u0703\u010b\3\2\2\2")
        buf.write("\u0704\u0702\3\2\2\2\u0705\u0706\5\u01b4\u00db\2\u0706")
        buf.write("\u0707\7\u0093\2\2\u0707\u0708\5\36\20\2\u0708\u010d\3")
        buf.write("\2\2\2\u0709\u070e\5\u0110\u0089\2\u070a\u070b\7\u0086")
        buf.write("\2\2\u070b\u070d\5\u0110\u0089\2\u070c\u070a\3\2\2\2\u070d")
        buf.write("\u0710\3\2\2\2\u070e\u070c\3\2\2\2\u070e\u070f\3\2\2\2")
        buf.write("\u070f\u010f\3\2\2\2\u0710\u070e\3\2\2\2\u0711\u0714\5")
        buf.write("\u01b4\u00db\2\u0712\u0713\7\u0093\2\2\u0713\u0715\5\u0112")
        buf.write("\u008a\2\u0714\u0712\3\2\2\2\u0714\u0715\3\2\2\2\u0715")
        buf.write("\u0111\3\2\2\2\u0716\u0719\5\36\20\2\u0717\u0719\5\u0146")
        buf.write("\u00a4\2\u0718\u0716\3\2\2\2\u0718\u0717\3\2\2\2\u0719")
        buf.write("\u0113\3\2\2\2\u071a\u071d\5\6\4\2\u071b\u071d\7n\2\2")
        buf.write("\u071c\u071a\3\2\2\2\u071c\u071b\3\2\2\2\u071d\u0115\3")
        buf.write("\2\2\2\u071e\u071f\5\4\3\2\u071f\u0117\3\2\2\2\u0720\u0723")
        buf.write("\5\u00acW\2\u0721\u0723\7\u0088\2\2\u0722\u0720\3\2\2")
        buf.write("\2\u0722\u0721\3\2\2\2\u0723\u0119\3\2\2\2\u0724\u072b")
        buf.write("\5\u0122\u0092\2\u0725\u0728\5\u011c\u008f\2\u0726\u0727")
        buf.write("\7\u0086\2\2\u0727\u0729\5\u0122\u0092\2\u0728\u0726\3")
        buf.write("\2\2\2\u0728\u0729\3\2\2\2\u0729\u072b\3\2\2\2\u072a\u0724")
        buf.write("\3\2\2\2\u072a\u0725\3\2\2\2\u072b\u011b\3\2\2\2\u072c")
        buf.write("\u0731\5\u011e\u0090\2\u072d\u072e\7\u0086\2\2\u072e\u0730")
        buf.write("\5\u011e\u0090\2\u072f\u072d\3\2\2\2\u0730\u0733\3\2\2")
        buf.write("\2\u0731\u072f\3\2\2\2\u0731\u0732\3\2\2\2\u0732\u011d")
        buf.write("\3\2\2\2\u0733\u0731\3\2\2\2\u0734\u0736\5\u0160\u00b1")
        buf.write("\2\u0735\u0734\3\2\2\2\u0735\u0736\3\2\2\2\u0736\u0738")
        buf.write("\3\2\2\2\u0737\u0739\5\u0120\u0091\2\u0738\u0737\3\2\2")
        buf.write("\2\u0738\u0739\3\2\2\2\u0739\u073a\3\2\2\2\u073a\u073d")
        buf.write("\5\u01ae\u00d8\2\u073b\u073d\7\16\2\2\u073c\u0735\3\2")
        buf.write("\2\2\u073c\u073b\3\2\2\2\u073d\u011f\3\2\2\2\u073e\u0747")
        buf.write("\7R\2\2\u073f\u0747\7J\2\2\u0740\u0747\78\2\2\u0741\u0742")
        buf.write("\7R\2\2\u0742\u0747\7`\2\2\u0743\u0744\78\2\2\u0744\u0747")
        buf.write("\7`\2\2\u0745\u0747\7`\2\2\u0746\u073e\3\2\2\2\u0746\u073f")
        buf.write("\3\2\2\2\u0746\u0740\3\2\2\2\u0746\u0741\3\2\2\2\u0746")
        buf.write("\u0743\3\2\2\2\u0746\u0745\3\2\2\2\u0747\u0121\3\2\2\2")
        buf.write("\u0748\u074a\5\u0160\u00b1\2\u0749\u0748\3\2\2\2\u0749")
        buf.write("\u074a\3\2\2\2\u074a\u074b\3\2\2\2\u074b\u074c\7L\2\2")
        buf.write("\u074c\u074d\5\u0142\u00a2\2\u074d\u074e\5\u01b4\u00db")
        buf.write("\2\u074e\u0123\3\2\2\2\u074f\u0751\5\u0160\u00b1\2\u0750")
        buf.write("\u074f\3\2\2\2\u0750\u0751\3\2\2\2\u0751\u0753\3\2\2\2")
        buf.write("\u0752\u0754\5\u012a\u0096\2\u0753\u0752\3\2\2\2\u0753")
        buf.write("\u0754\3\2\2\2\u0754\u075f\3\2\2\2\u0755\u0756\7\63\2")
        buf.write("\2\u0756\u0758\5\u012c\u0097\2\u0757\u0759\5\u0128\u0095")
        buf.write("\2\u0758\u0757\3\2\2\2\u0758\u0759\3\2\2\2\u0759\u0760")
        buf.write("\3\2\2\2\u075a\u075b\7X\2\2\u075b\u075d\5\u012c\u0097")
        buf.write("\2\u075c\u075e\5\u0126\u0094\2\u075d\u075c\3\2\2\2\u075d")
        buf.write("\u075e\3\2\2\2\u075e\u0760\3\2\2\2\u075f\u0755\3\2\2\2")
        buf.write("\u075f\u075a\3\2\2\2\u0760\u0125\3\2\2\2\u0761\u0763\5")
        buf.write("\u0160\u00b1\2\u0762\u0761\3\2\2\2\u0762\u0763\3\2\2\2")
        buf.write("\u0763\u0765\3\2\2\2\u0764\u0766\5\u012a\u0096\2\u0765")
        buf.write("\u0764\3\2\2\2\u0765\u0766\3\2\2\2\u0766\u0767\3\2\2\2")
        buf.write("\u0767\u0768\7\63\2\2\u0768\u0769\5\u012c\u0097\2\u0769")
        buf.write("\u0127\3\2\2\2\u076a\u076c\5\u0160\u00b1\2\u076b\u076a")
        buf.write("\3\2\2\2\u076b\u076c\3\2\2\2\u076c\u076e\3\2\2\2\u076d")
        buf.write("\u076f\5\u012a\u0096\2\u076e\u076d\3\2\2\2\u076e\u076f")
        buf.write("\3\2\2\2\u076f\u0770\3\2\2\2\u0770\u0771\7X\2\2\u0771")
        buf.write("\u0772\5\u012c\u0097\2\u0772\u0129\3\2\2\2\u0773\u077b")
        buf.write("\7O\2\2\u0774\u077b\7;\2\2\u0775\u077b\7N\2\2\u0776\u0777")
        buf.write("\7O\2\2\u0777\u077b\7;\2\2\u0778\u0779\7;\2\2\u0779\u077b")
        buf.write("\7O\2\2\u077a\u0773\3\2\2\2\u077a\u0774\3\2\2\2\u077a")
        buf.write("\u0775\3\2\2\2\u077a\u0776\3\2\2\2\u077a\u0778\3\2\2\2")
        buf.write("\u077b\u012b\3\2\2\2\u077c\u077f\5\u00acW\2\u077d\u077f")
        buf.write("\7\u0088\2\2\u077e\u077c\3\2\2\2\u077e\u077d\3\2\2\2\u077f")
        buf.write("\u012d\3\2\2\2\u0780\u0782\5\u0160\u00b1\2\u0781\u0780")
        buf.write("\3\2\2\2\u0781\u0782\3\2\2\2\u0782\u078b\3\2\2\2\u0783")
        buf.write("\u0784\7\f\2\2\u0784\u0785\5\u00acW\2\u0785\u0786\5\u0132")
        buf.write("\u009a\2\u0786\u078c\3\2\2\2\u0787\u0788\7S\2\2\u0788")
        buf.write("\u0789\5\u00acW\2\u0789\u078a\5\u0130\u0099\2\u078a\u078c")
        buf.write("\3\2\2\2\u078b\u0783\3\2\2\2\u078b\u0787\3\2\2\2\u078c")
        buf.write("\u012f\3\2\2\2\u078d\u078f\5\u0160\u00b1\2\u078e\u078d")
        buf.write("\3\2\2\2\u078e\u078f\3\2\2\2\u078f\u0790\3\2\2\2\u0790")
        buf.write("\u0791\7\f\2\2\u0791\u0792\5\u00acW\2\u0792\u0131\3\2")
        buf.write("\2\2\u0793\u0795\5\u0160\u00b1\2\u0794\u0793\3\2\2\2\u0794")
        buf.write("\u0795\3\2\2\2\u0795\u0796\3\2\2\2\u0796\u0797\7S\2\2")
        buf.write("\u0797\u0798\5\u00acW\2\u0798\u0133\3\2\2\2\u0799\u07b0")
        buf.write("\7\u0089\2\2\u079a\u07b0\7\u008a\2\2\u079b\u07b0\7\u0091")
        buf.write("\2\2\u079c\u07b0\7\u0092\2\2\u079d\u07b0\7\u0099\2\2\u079e")
        buf.write("\u07b0\7\u009a\2\2\u079f\u07b0\7b\2\2\u07a0\u07b0\7,\2")
        buf.write("\2\u07a1\u07b0\7\u008b\2\2\u07a2\u07b0\7\u008c\2\2\u07a3")
        buf.write("\u07b0\7\u008d\2\2\u07a4\u07b0\7\u008e\2\2\u07a5\u07b0")
        buf.write("\7\u008f\2\2\u07a6\u07b0\7\u0090\2\2\u07a7\u07b0\7\u00aa")
        buf.write("\2\2\u07a8\u07b0\5\u017a\u00be\2\u07a9\u07b0\7\u009e\2")
        buf.write("\2\u07aa\u07b0\7\u009f\2\2\u07ab\u07b0\7\u0095\2\2\u07ac")
        buf.write("\u07b0\7\u0094\2\2\u07ad\u07b0\7\u00a1\2\2\u07ae\u07b0")
        buf.write("\7\u00a0\2\2\u07af\u0799\3\2\2\2\u07af\u079a\3\2\2\2\u07af")
        buf.write("\u079b\3\2\2\2\u07af\u079c\3\2\2\2\u07af\u079d\3\2\2\2")
        buf.write("\u07af\u079e\3\2\2\2\u07af\u079f\3\2\2\2\u07af\u07a0\3")
        buf.write("\2\2\2\u07af\u07a1\3\2\2\2\u07af\u07a2\3\2\2\2\u07af\u07a3")
        buf.write("\3\2\2\2\u07af\u07a4\3\2\2\2\u07af\u07a5\3\2\2\2\u07af")
        buf.write("\u07a6\3\2\2\2\u07af\u07a7\3\2\2\2\u07af\u07a8\3\2\2\2")
        buf.write("\u07af\u07a9\3\2\2\2\u07af\u07aa\3\2\2\2\u07af\u07ab\3")
        buf.write("\2\2\2\u07af\u07ac\3\2\2\2\u07af\u07ad\3\2\2\2\u07af\u07ae")
        buf.write("\3\2\2\2\u07b0\u0135\3\2\2\2\u07b1\u07b2\t\r\2\2\u07b2")
        buf.write("\u07b3\7H\2\2\u07b3\u07b4\5\6\4\2\u07b4\u07b5\7\u0083")
        buf.write("\2\2\u07b5\u07b6\5\u01ae\u00d8\2\u07b6\u07b7\7\u0084\2")
        buf.write("\2\u07b7\u0137\3\2\2\2\u07b8\u07b9\7\u0087\2\2\u07b9\u07ba")
        buf.write("\t\16\2\2\u07ba\u07bc\7\u0083\2\2\u07bb\u07bd\5\32\16")
        buf.write("\2\u07bc\u07bb\3\2\2\2\u07bc\u07bd\3\2\2\2\u07bd\u07be")
        buf.write("\3\2\2\2\u07be\u07bf\7\u0084\2\2\u07bf\u0139\3\2\2\2\u07c0")
        buf.write("\u07c3\5\u00acW\2\u07c1\u07c3\7\u0088\2\2\u07c2\u07c0")
        buf.write("\3\2\2\2\u07c2\u07c1\3\2\2\2\u07c3\u013b\3\2\2\2\u07c4")
        buf.write("\u07c5\7\u0087\2\2\u07c5\u07c6\5\u00eex\2\u07c6\u013d")
        buf.write("\3\2\2\2\u07c7\u07cb\7\177\2\2\u07c8\u07ca\5\u0140\u00a1")
        buf.write("\2\u07c9\u07c8\3\2\2\2\u07ca\u07cd\3\2\2\2\u07cb\u07c9")
        buf.write("\3\2\2\2\u07cb\u07cc\3\2\2\2\u07cc\u07ce\3\2\2\2\u07cd")
        buf.write("\u07cb\3\2\2\2\u07ce\u07cf\7\u0080\2\2\u07cf\u013f\3\2")
        buf.write("\2\2\u07d0\u07d2\5\u0160\u00b1\2\u07d1\u07d0\3\2\2\2\u07d1")
        buf.write("\u07d2\3\2\2\2\u07d2\u07d4\3\2\2\2\u07d3\u07d5\5\u0102")
        buf.write("\u0082\2\u07d4\u07d3\3\2\2\2\u07d4\u07d5\3\2\2\2\u07d5")
        buf.write("\u07e0\3\2\2\2\u07d6\u07e1\5\u0106\u0084\2\u07d7\u07d8")
        buf.write("\7.\2\2\u07d8\u07da\5\6\4\2\u07d9\u07db\5\u0174\u00bb")
        buf.write("\2\u07da\u07d9\3\2\2\2\u07db\u07dc\3\2\2\2\u07dc\u07da")
        buf.write("\3\2\2\2\u07dc\u07dd\3\2\2\2\u07dd\u07de\3\2\2\2\u07de")
        buf.write("\u07df\7\u0088\2\2\u07df\u07e1\3\2\2\2\u07e0\u07d6\3\2")
        buf.write("\2\2\u07e0\u07d7\3\2\2\2\u07e1\u0141\3\2\2\2\u07e2\u07ea")
        buf.write("\5\b\5\2\u07e3\u07e5\t\17\2\2\u07e4\u07e3\3\2\2\2\u07e5")
        buf.write("\u07e8\3\2\2\2\u07e6\u07e4\3\2\2\2\u07e6\u07e7\3\2\2\2")
        buf.write("\u07e7\u07e9\3\2\2\2\u07e8\u07e6\3\2\2\2\u07e9\u07eb\5")
        buf.write("\u0144\u00a3\2\u07ea\u07e6\3\2\2\2\u07eb\u07ec\3\2\2\2")
        buf.write("\u07ec\u07ea\3\2\2\2\u07ec\u07ed\3\2\2\2\u07ed\u0143\3")
        buf.write("\2\2\2\u07ee\u07f2\7\u0081\2\2\u07ef\u07f1\7\u0086\2\2")
        buf.write("\u07f0\u07ef\3\2\2\2\u07f1\u07f4\3\2\2\2\u07f2\u07f0\3")
        buf.write("\2\2\2\u07f2\u07f3\3\2\2\2\u07f3\u07f5\3\2\2\2\u07f4\u07f2")
        buf.write("\3\2\2\2\u07f5\u07f6\7\u0082\2\2\u07f6\u0145\3\2\2\2\u07f7")
        buf.write("\u0803\7\177\2\2\u07f8\u07fd\5\u0112\u008a\2\u07f9\u07fa")
        buf.write("\7\u0086\2\2\u07fa\u07fc\5\u0112\u008a\2\u07fb\u07f9\3")
        buf.write("\2\2\2\u07fc\u07ff\3\2\2\2\u07fd\u07fb\3\2\2\2\u07fd\u07fe")
        buf.write("\3\2\2\2\u07fe\u0801\3\2\2\2\u07ff\u07fd\3\2\2\2\u0800")
        buf.write("\u0802\7\u0086\2\2\u0801\u0800\3\2\2\2\u0801\u0802\3\2")
        buf.write("\2\2\u0802\u0804\3\2\2\2\u0803\u07f8\3\2\2\2\u0803\u0804")
        buf.write("\3\2\2\2\u0804\u0805\3\2\2\2\u0805\u0806\7\u0080\2\2\u0806")
        buf.write("\u0147\3\2\2\2\u0807\u0808\7\u0094\2\2\u0808\u080d\5\u014a")
        buf.write("\u00a6\2\u0809\u080a\7\u0086\2\2\u080a\u080c\5\u014a\u00a6")
        buf.write("\2\u080b\u0809\3\2\2\2\u080c\u080f\3\2\2\2\u080d\u080b")
        buf.write("\3\2\2\2\u080d\u080e\3\2\2\2\u080e\u0810\3\2\2\2\u080f")
        buf.write("\u080d\3\2\2\2\u0810\u0811\7\u0095\2\2\u0811\u0149\3\2")
        buf.write("\2\2\u0812\u0814\5\u0160\u00b1\2\u0813\u0812\3\2\2\2\u0813")
        buf.write("\u0814\3\2\2\2\u0814\u0816\3\2\2\2\u0815\u0817\5\u014c")
        buf.write("\u00a7\2\u0816\u0815\3\2\2\2\u0816\u0817\3\2\2\2\u0817")
        buf.write("\u0818\3\2\2\2\u0818\u0819\5\u01b4\u00db\2\u0819\u014b")
        buf.write("\3\2\2\2\u081a\u081b\t\20\2\2\u081b\u014d\3\2\2\2\u081c")
        buf.write("\u081d\7\u0087\2\2\u081d\u081e\5\u00eex\2\u081e\u014f")
        buf.write("\3\2\2\2\u081f\u0823\7\177\2\2\u0820\u0822\5\u0152\u00aa")
        buf.write("\2\u0821\u0820\3\2\2\2\u0822\u0825\3\2\2\2\u0823\u0821")
        buf.write("\3\2\2\2\u0823\u0824\3\2\2\2\u0824\u0826\3\2\2\2\u0825")
        buf.write("\u0823\3\2\2\2\u0826\u0827\7\u0080\2\2\u0827\u0151\3\2")
        buf.write("\2\2\u0828\u082a\5\u0160\u00b1\2\u0829\u0828\3\2\2\2\u0829")
        buf.write("\u082a\3\2\2\2\u082a\u082c\3\2\2\2\u082b\u082d\7D\2\2")
        buf.write("\u082c\u082b\3\2\2\2\u082c\u082d\3\2\2\2\u082d\u086d\3")
        buf.write("\2\2\2\u082e\u0830\7i\2\2\u082f\u082e\3\2\2\2\u082f\u0830")
        buf.write("\3\2\2\2\u0830\u0836\3\2\2\2\u0831\u0837\7R\2\2\u0832")
        buf.write("\u0833\7R\2\2\u0833\u0837\7Q\2\2\u0834\u0835\7Q\2\2\u0835")
        buf.write("\u0837\7R\2\2\u0836\u0831\3\2\2\2\u0836\u0832\3\2\2\2")
        buf.write("\u0836\u0834\3\2\2\2\u0836\u0837\3\2\2\2\u0837\u0838\3")
        buf.write("\2\2\2\u0838\u0854\5\6\4\2\u0839\u083b\5\u01b4\u00db\2")
        buf.write("\u083a\u083c\5\u00e8u\2\u083b\u083a\3\2\2\2\u083b\u083c")
        buf.write("\3\2\2\2\u083c\u083d\3\2\2\2\u083d\u083f\7\u0083\2\2\u083e")
        buf.write("\u0840\5\u011a\u008e\2\u083f\u083e\3\2\2\2\u083f\u0840")
        buf.write("\3\2\2\2\u0840\u0841\3\2\2\2\u0841\u0843\7\u0084\2\2\u0842")
        buf.write("\u0844\5\u00f0y\2\u0843\u0842\3\2\2\2\u0843\u0844\3\2")
        buf.write("\2\2\u0844\u0845\3\2\2\2\u0845\u0846\7\u0088\2\2\u0846")
        buf.write("\u0855\3\2\2\2\u0847\u0848\5\u01b4\u00db\2\u0848\u0849")
        buf.write("\7\177\2\2\u0849\u084a\5\u0154\u00ab\2\u084a\u084b\7\u0080")
        buf.write("\2\2\u084b\u0855\3\2\2\2\u084c\u084d\7`\2\2\u084d\u084e")
        buf.write("\7\u0081\2\2\u084e\u084f\5\u011a\u008e\2\u084f\u0850\7")
        buf.write("\u0082\2\2\u0850\u0851\7\177\2\2\u0851\u0852\5\u0154\u00ab")
        buf.write("\2\u0852\u0853\7\u0080\2\2\u0853\u0855\3\2\2\2\u0854\u0839")
        buf.write("\3\2\2\2\u0854\u0847\3\2\2\2\u0854\u084c\3\2\2\2\u0855")
        buf.write("\u086e\3\2\2\2\u0856\u0858\7i\2\2\u0857\u0856\3\2\2\2")
        buf.write("\u0857\u0858\3\2\2\2\u0858\u0859\3\2\2\2\u0859\u085a\7")
        buf.write("n\2\2\u085a\u085c\5\u01b4\u00db\2\u085b\u085d\5\u00e8")
        buf.write("u\2\u085c\u085b\3\2\2\2\u085c\u085d\3\2\2\2\u085d\u085e")
        buf.write("\3\2\2\2\u085e\u0860\7\u0083\2\2\u085f\u0861\5\u011a\u008e")
        buf.write("\2\u0860\u085f\3\2\2\2\u0860\u0861\3\2\2\2\u0861\u0862")
        buf.write("\3\2\2\2\u0862\u0864\7\u0084\2\2\u0863\u0865\5\u00f0y")
        buf.write("\2\u0864\u0863\3\2\2\2\u0864\u0865\3\2\2\2\u0865\u0866")
        buf.write("\3\2\2\2\u0866\u0867\7\u0088\2\2\u0867\u086e\3\2\2\2\u0868")
        buf.write("\u0869\7)\2\2\u0869\u086a\5\6\4\2\u086a\u086b\5\u01b4")
        buf.write("\u00db\2\u086b\u086c\7\u0088\2\2\u086c\u086e\3\2\2\2\u086d")
        buf.write("\u082f\3\2\2\2\u086d\u0857\3\2\2\2\u086d\u0868\3\2\2\2")
        buf.write("\u086e\u0153\3\2\2\2\u086f\u0871\5\u0160\u00b1\2\u0870")
        buf.write("\u086f\3\2\2\2\u0870\u0871\3\2\2\2\u0871\u0884\3\2\2\2")
        buf.write("\u0872\u0873\7\63\2\2\u0873\u0879\7\u0088\2\2\u0874\u0876")
        buf.write("\5\u0160\u00b1\2\u0875\u0874\3\2\2\2\u0875\u0876\3\2\2")
        buf.write("\2\u0876\u0877\3\2\2\2\u0877\u0878\7X\2\2\u0878\u087a")
        buf.write("\7\u0088\2\2\u0879\u0875\3\2\2\2\u0879\u087a\3\2\2\2\u087a")
        buf.write("\u0885\3\2\2\2\u087b\u087c\7X\2\2\u087c\u0882\7\u0088")
        buf.write("\2\2\u087d\u087f\5\u0160\u00b1\2\u087e\u087d\3\2\2\2\u087e")
        buf.write("\u087f\3\2\2\2\u087f\u0880\3\2\2\2\u0880\u0881\7\63\2")
        buf.write("\2\u0881\u0883\7\u0088\2\2\u0882\u087e\3\2\2\2\u0882\u0883")
        buf.write("\3\2\2\2\u0883\u0885\3\2\2\2\u0884\u0872\3\2\2\2\u0884")
        buf.write("\u087b\3\2\2\2\u0885\u0155\3\2\2\2\u0886\u0887\7\u0087")
        buf.write("\2\2\u0887\u0888\5\6\4\2\u0888\u0157\3\2\2\2\u0889\u0895")
        buf.write("\7\177\2\2\u088a\u088f\5\u015a\u00ae\2\u088b\u088c\7\u0086")
        buf.write("\2\2\u088c\u088e\5\u015a\u00ae\2\u088d\u088b\3\2\2\2\u088e")
        buf.write("\u0891\3\2\2\2\u088f\u088d\3\2\2\2\u088f\u0890\3\2\2\2")
        buf.write("\u0890\u0893\3\2\2\2\u0891\u088f\3\2\2\2\u0892\u0894\7")
        buf.write("\u0086\2\2\u0893\u0892\3\2\2\2\u0893\u0894\3\2\2\2\u0894")
        buf.write("\u0896\3\2\2\2\u0895\u088a\3\2\2\2\u0895\u0896\3\2\2\2")
        buf.write("\u0896\u0897\3\2\2\2\u0897\u0898\7\u0080\2\2\u0898\u0159")
        buf.write("\3\2\2\2\u0899\u089b\5\u0160\u00b1\2\u089a\u0899\3\2\2")
        buf.write("\2\u089a\u089b\3\2\2\2\u089b\u089c\3\2\2\2\u089c\u089f")
        buf.write("\5\u01b4\u00db\2\u089d\u089e\7\u0093\2\2\u089e\u08a0\5")
        buf.write("\36\20\2\u089f\u089d\3\2\2\2\u089f\u08a0\3\2\2\2\u08a0")
        buf.write("\u015b\3\2\2\2\u08a1\u08a2\7\u0081\2\2\u08a2\u08a3\5\u015e")
        buf.write("\u00b0\2\u08a3\u08a4\7\u0087\2\2\u08a4\u08a6\5\u0166\u00b4")
        buf.write("\2\u08a5\u08a7\7\u0086\2\2\u08a6\u08a5\3\2\2\2\u08a6\u08a7")
        buf.write("\3\2\2\2\u08a7\u08a8\3\2\2\2\u08a8\u08a9\7\u0082\2\2\u08a9")
        buf.write("\u015d\3\2\2\2\u08aa\u08ad\5\u018e\u00c8\2\u08ab\u08ad")
        buf.write("\5\u01b4\u00db\2\u08ac\u08aa\3\2\2\2\u08ac\u08ab\3\2\2")
        buf.write("\2\u08ad\u015f\3\2\2\2\u08ae\u08b0\5\u0162\u00b2\2\u08af")
        buf.write("\u08ae\3\2\2\2\u08b0\u08b1\3\2\2\2\u08b1\u08af\3\2\2\2")
        buf.write("\u08b1\u08b2\3\2\2\2\u08b2\u0161\3\2\2\2\u08b3\u08b7\7")
        buf.write("\u0081\2\2\u08b4\u08b5\5\u0164\u00b3\2\u08b5\u08b6\7\u0087")
        buf.write("\2\2\u08b6\u08b8\3\2\2\2\u08b7\u08b4\3\2\2\2\u08b7\u08b8")
        buf.write("\3\2\2\2\u08b8\u08b9\3\2\2\2\u08b9\u08bb\5\u0166\u00b4")
        buf.write("\2\u08ba\u08bc\7\u0086\2\2\u08bb\u08ba\3\2\2\2\u08bb\u08bc")
        buf.write("\3\2\2\2\u08bc\u08bd\3\2\2\2\u08bd\u08be\7\u0082\2\2\u08be")
        buf.write("\u0163\3\2\2\2\u08bf\u08c2\5\u018e\u00c8\2\u08c0\u08c2")
        buf.write("\5\u01b4\u00db\2\u08c1\u08bf\3\2\2\2\u08c1\u08c0\3\2\2")
        buf.write("\2\u08c2\u0165\3\2\2\2\u08c3\u08c8\5\u0168\u00b5\2\u08c4")
        buf.write("\u08c5\7\u0086\2\2\u08c5\u08c7\5\u0168\u00b5\2\u08c6\u08c4")
        buf.write("\3\2\2\2\u08c7\u08ca\3\2\2\2\u08c8\u08c6\3\2\2\2\u08c8")
        buf.write("\u08c9\3\2\2\2\u08c9\u0167\3\2\2\2\u08ca\u08c8\3\2\2\2")
        buf.write("\u08cb\u08d8\5\4\3\2\u08cc\u08d5\7\u0083\2\2\u08cd\u08d2")
        buf.write("\5\u016a\u00b6\2\u08ce\u08cf\7\u0086\2\2\u08cf\u08d1\5")
        buf.write("\u016a\u00b6\2\u08d0\u08ce\3\2\2\2\u08d1\u08d4\3\2\2\2")
        buf.write("\u08d2\u08d0\3\2\2\2\u08d2\u08d3\3\2\2\2\u08d3\u08d6\3")
        buf.write("\2\2\2\u08d4\u08d2\3\2\2\2\u08d5\u08cd\3\2\2\2\u08d5\u08d6")
        buf.write("\3\2\2\2\u08d6\u08d7\3\2\2\2\u08d7\u08d9\7\u0084\2\2\u08d8")
        buf.write("\u08cc\3\2\2\2\u08d8\u08d9\3\2\2\2\u08d9\u0169\3\2\2\2")
        buf.write("\u08da\u08db\5\u01b4\u00db\2\u08db\u08dc\7\u0087\2\2\u08dc")
        buf.write("\u08de\3\2\2\2\u08dd\u08da\3\2\2\2\u08dd\u08de\3\2\2\2")
        buf.write("\u08de\u08df\3\2\2\2\u08df\u08e0\5\36\20\2\u08e0\u016b")
        buf.write("\3\2\2\2\u08e1\u08e4\5\16\b\2\u08e2\u08e4\5\26\f\2\u08e3")
        buf.write("\u08e1\3\2\2\2\u08e3\u08e2\3\2\2\2\u08e4\u08e9\3\2\2\2")
        buf.write("\u08e5\u08e8\5\u0144\u00a3\2\u08e6\u08e8\7\u0096\2\2\u08e7")
        buf.write("\u08e5\3\2\2\2\u08e7\u08e6\3\2\2\2\u08e8\u08eb\3\2\2\2")
        buf.write("\u08e9\u08e7\3\2\2\2\u08e9\u08ea\3\2\2\2\u08ea\u08ec\3")
        buf.write("\2\2\2\u08eb\u08e9\3\2\2\2\u08ec\u08ed\7\u008b\2\2\u08ed")
        buf.write("\u08f1\3\2\2\2\u08ee\u08ef\7n\2\2\u08ef\u08f1\7\u008b")
        buf.write("\2\2\u08f0\u08e3\3\2\2\2\u08f0\u08ee\3\2\2\2\u08f1\u016d")
        buf.write("\3\2\2\2\u08f2\u08f7\5\u0170\u00b9\2\u08f3\u08f4\7\u0086")
        buf.write("\2\2\u08f4\u08f6\5\u0170\u00b9\2\u08f5\u08f3\3\2\2\2\u08f6")
        buf.write("\u08f9\3\2\2\2\u08f7\u08f5\3\2\2\2\u08f7\u08f8\3\2\2\2")
        buf.write("\u08f8\u016f\3\2\2\2\u08f9\u08f7\3\2\2\2\u08fa\u08fb\5")
        buf.write("\u01b4\u00db\2\u08fb\u08fc\7\u0093\2\2\u08fc\u08fd\5\u0172")
        buf.write("\u00ba\2\u08fd\u0171\3\2\2\2\u08fe\u0900\7\u008e\2\2\u08ff")
        buf.write("\u08fe\3\2\2\2\u08ff\u0900\3\2\2\2\u0900\u0901\3\2\2\2")
        buf.write("\u0901\u0904\5\36\20\2\u0902\u0904\5\u0176\u00bc\2\u0903")
        buf.write("\u08ff\3\2\2\2\u0903\u0902\3\2\2\2\u0904\u0173\3\2\2\2")
        buf.write("\u0905\u0906\5\u01b4\u00db\2\u0906\u0907\7\u0081\2\2\u0907")
        buf.write("\u0908\5\36\20\2\u0908\u0909\7\u0082\2\2\u0909\u0175\3")
        buf.write("\2\2\2\u090a\u090b\7[\2\2\u090b\u090c\5\6\4\2\u090c\u090d")
        buf.write("\7\u0081\2\2\u090d\u090e\5\36\20\2\u090e\u090f\7\u0082")
        buf.write("\2\2\u090f\u0928\3\2\2\2\u0910\u0912\7[\2\2\u0911\u0913")
        buf.write("\5\6\4\2\u0912\u0911\3\2\2\2\u0912\u0913\3\2\2\2\u0913")
        buf.write("\u0914\3\2\2\2\u0914\u0916\7\u0081\2\2\u0915\u0917\5\36")
        buf.write("\20\2\u0916\u0915\3\2\2\2\u0916\u0917\3\2\2\2\u0917\u0918")
        buf.write("\3\2\2\2\u0918\u0919\7\u0082\2\2\u0919\u091a\7\177\2\2")
        buf.write("\u091a\u091f\5\36\20\2\u091b\u091c\7\u0086\2\2\u091c\u091e")
        buf.write("\5\36\20\2\u091d\u091b\3\2\2\2\u091e\u0921\3\2\2\2\u091f")
        buf.write("\u091d\3\2\2\2\u091f\u0920\3\2\2\2\u0920\u0923\3\2\2\2")
        buf.write("\u0921\u091f\3\2\2\2\u0922\u0924\7\u0086\2\2\u0923\u0922")
        buf.write("\3\2\2\2\u0923\u0924\3\2\2\2\u0924\u0925\3\2\2\2\u0925")
        buf.write("\u0926\7\u0080\2\2\u0926\u0928\3\2\2\2\u0927\u090a\3\2")
        buf.write("\2\2\u0927\u0910\3\2\2\2\u0928\u0177\3\2\2\2\u0929\u092a")
        buf.write("\7\u0093\2\2\u092a\u092b\7\u0095\2\2\u092b\u092c\6\u00bd")
        buf.write("\2\3\u092c\u0179\3\2\2\2\u092d\u092e\7\u0095\2\2\u092e")
        buf.write("\u092f\7\u0095\2\2\u092f\u0930\6\u00be\3\3\u0930\u017b")
        buf.write("\3\2\2\2\u0931\u0932\7\u0095\2\2\u0932\u0933\7\u00a1\2")
        buf.write("\2\u0933\u0934\6\u00bf\4\3\u0934\u017d\3\2\2\2\u0935\u093e")
        buf.write("\5\u0180\u00c1\2\u0936\u093e\5\u0182\u00c2\2\u0937\u093e")
        buf.write("\7v\2\2\u0938\u093e\7w\2\2\u0939\u093e\7x\2\2\u093a\u093e")
        buf.write("\7y\2\2\u093b\u093e\7z\2\2\u093c\u093e\7E\2\2\u093d\u0935")
        buf.write("\3\2\2\2\u093d\u0936\3\2\2\2\u093d\u0937\3\2\2\2\u093d")
        buf.write("\u0938\3\2\2\2\u093d\u0939\3\2\2\2\u093d\u093a\3\2\2\2")
        buf.write("\u093d\u093b\3\2\2\2\u093d\u093c\3\2\2\2\u093e\u017f\3")
        buf.write("\2\2\2\u093f\u0940\t\21\2\2\u0940\u0181\3\2\2\2\u0941")
        buf.write("\u0946\5\u0184\u00c3\2\u0942\u0946\5\u0186\u00c4\2\u0943")
        buf.write("\u0946\7{\2\2\u0944\u0946\7|\2\2\u0945\u0941\3\2\2\2\u0945")
        buf.write("\u0942\3\2\2\2\u0945\u0943\3\2\2\2\u0945\u0944\3\2\2\2")
        buf.write("\u0946\u0183\3\2\2\2\u0947\u094b\7}\2\2\u0948\u094a\5")
        buf.write("\u0188\u00c5\2\u0949\u0948\3\2\2\2\u094a\u094d\3\2\2\2")
        buf.write("\u094b\u0949\3\2\2\2\u094b\u094c\3\2\2\2\u094c\u094e\3")
        buf.write("\2\2\2\u094d\u094b\3\2\2\2\u094e\u094f\7\u00b2\2\2\u094f")
        buf.write("\u0185\3\2\2\2\u0950\u0954\7~\2\2\u0951\u0953\5\u018a")
        buf.write("\u00c6\2\u0952\u0951\3\2\2\2\u0953\u0956\3\2\2\2\u0954")
        buf.write("\u0952\3\2\2\2\u0954\u0955\3\2\2\2\u0955\u0957\3\2\2\2")
        buf.write("\u0956\u0954\3\2\2\2\u0957\u0958\7\u00b2\2\2\u0958\u0187")
        buf.write("\3\2\2\2\u0959\u095e\5\u018c\u00c7\2\u095a\u095e\7\u00ae")
        buf.write("\2\2\u095b\u095e\7\u00b0\2\2\u095c\u095e\7\u00b3\2\2\u095d")
        buf.write("\u0959\3\2\2\2\u095d\u095a\3\2\2\2\u095d\u095b\3\2\2\2")
        buf.write("\u095d\u095c\3\2\2\2\u095e\u0189\3\2\2\2\u095f\u0964\5")
        buf.write("\u018c\u00c7\2\u0960\u0964\7\u00ae\2\2\u0961\u0964\7\u00b1")
        buf.write("\2\2\u0962\u0964\7\u00b4\2\2\u0963\u095f\3\2\2\2\u0963")
        buf.write("\u0960\3\2\2\2\u0963\u0961\3\2\2\2\u0963\u0962\3\2\2\2")
        buf.write("\u0964\u018b\3\2\2\2\u0965\u096a\5\36\20\2\u0966\u0967")
        buf.write("\7\u0086\2\2\u0967\u0969\5\36\20\2\u0968\u0966\3\2\2\2")
        buf.write("\u0969\u096c\3\2\2\2\u096a\u0968\3\2\2\2\u096a\u096b\3")
        buf.write("\2\2\2\u096b\u0973\3\2\2\2\u096c\u096a\3\2\2\2\u096d\u096f")
        buf.write("\7\u0087\2\2\u096e\u0970\7\u00b6\2\2\u096f\u096e\3\2\2")
        buf.write("\2\u0970\u0971\3\2\2\2\u0971\u096f\3\2\2\2\u0971\u0972")
        buf.write("\3\2\2\2\u0972\u0974\3\2\2\2\u0973\u096d\3\2\2\2\u0973")
        buf.write("\u0974\3\2\2\2\u0974\u018d\3\2\2\2\u0975\u0976\t\22\2")
        buf.write("\2\u0976\u018f\3\2\2\2\u0977\u0978\7\34\2\2\u0978\u097a")
        buf.write("\5\u01b4\u00db\2\u0979\u097b\5\u00e8u\2\u097a\u0979\3")
        buf.write("\2\2\2\u097a\u097b\3\2\2\2\u097b\u097d\3\2\2\2\u097c\u097e")
        buf.write("\5\u00ecw\2\u097d\u097c\3\2\2\2\u097d\u097e\3\2\2\2\u097e")
        buf.write("\u0980\3\2\2\2\u097f\u0981\5\u00f0y\2\u0980\u097f\3\2")
        buf.write("\2\2\u0980\u0981\3\2\2\2\u0981\u0982\3\2\2\2\u0982\u0984")
        buf.write("\5\u00fc\177\2\u0983\u0985\7\u0088\2\2\u0984\u0983\3\2")
        buf.write("\2\2\u0984\u0985\3\2\2\2\u0985\u0191\3\2\2\2\u0986\u0988")
        buf.write("\t\23\2\2\u0987\u0986\3\2\2\2\u0987\u0988\3\2\2\2\u0988")
        buf.write("\u0989\3\2\2\2\u0989\u098a\7^\2\2\u098a\u098c\5\u01b4")
        buf.write("\u00db\2\u098b\u098d\5\u00e8u\2\u098c\u098b\3\2\2\2\u098c")
        buf.write("\u098d\3\2\2\2\u098d\u098f\3\2\2\2\u098e\u0990\5\u013c")
        buf.write("\u009f\2\u098f\u098e\3\2\2\2\u098f\u0990\3\2\2\2\u0990")
        buf.write("\u0992\3\2\2\2\u0991\u0993\5\u00f0y\2\u0992\u0991\3\2")
        buf.write("\2\2\u0992\u0993\3\2\2\2\u0993\u0994\3\2\2\2\u0994\u0996")
        buf.write("\5\u013e\u00a0\2\u0995\u0997\7\u0088\2\2\u0996\u0995\3")
        buf.write("\2\2\2\u0996\u0997\3\2\2\2\u0997\u0193\3\2\2\2\u0998\u0999")
        buf.write("\7:\2\2\u0999\u099b\5\u01b4\u00db\2\u099a\u099c\5\u0148")
        buf.write("\u00a5\2\u099b\u099a\3\2\2\2\u099b\u099c\3\2\2\2\u099c")
        buf.write("\u099e\3\2\2\2\u099d\u099f\5\u014e\u00a8\2\u099e\u099d")
        buf.write("\3\2\2\2\u099e\u099f\3\2\2\2\u099f\u09a1\3\2\2\2\u09a0")
        buf.write("\u09a2\5\u00f0y\2\u09a1\u09a0\3\2\2\2\u09a1\u09a2\3\2")
        buf.write("\2\2\u09a2\u09a3\3\2\2\2\u09a3\u09a5\5\u00fc\177\2\u09a4")
        buf.write("\u09a6\7\u0088\2\2\u09a5\u09a4\3\2\2\2\u09a5\u09a6\3\2")
        buf.write("\2\2\u09a6\u0195\3\2\2\2\u09a7\u09a8\7\'\2\2\u09a8\u09aa")
        buf.write("\5\u01b4\u00db\2\u09a9\u09ab\5\u0156\u00ac\2\u09aa\u09a9")
        buf.write("\3\2\2\2\u09aa\u09ab\3\2\2\2\u09ab\u09ac\3\2\2\2\u09ac")
        buf.write("\u09ae\5\u0158\u00ad\2\u09ad\u09af\7\u0088\2\2\u09ae\u09ad")
        buf.write("\3\2\2\2\u09ae\u09af\3\2\2\2\u09af\u0197\3\2\2\2\u09b0")
        buf.write("\u09b1\7!\2\2\u09b1\u09b2\5\u0114\u008b\2\u09b2\u09b4")
        buf.write("\5\u01b4\u00db\2\u09b3\u09b5\5\u0148\u00a5\2\u09b4\u09b3")
        buf.write("\3\2\2\2\u09b4\u09b5\3\2\2\2\u09b5\u09b6\3\2\2\2\u09b6")
        buf.write("\u09b8\7\u0083\2\2\u09b7\u09b9\5\u011a\u008e\2\u09b8\u09b7")
        buf.write("\3\2\2\2\u09b8\u09b9\3\2\2\2\u09b9\u09ba\3\2\2\2\u09ba")
        buf.write("\u09bc\7\u0084\2\2\u09bb\u09bd\5\u00f0y\2\u09bc\u09bb")
        buf.write("\3\2\2\2\u09bc\u09bd\3\2\2\2\u09bd\u09be\3\2\2\2\u09be")
        buf.write("\u09bf\7\u0088\2\2\u09bf\u0199\3\2\2\2\u09c0\u09c1\7)")
        buf.write("\2\2\u09c1\u09ca\5\6\4\2\u09c2\u09c3\5\u010e\u0088\2\u09c3")
        buf.write("\u09c4\7\u0088\2\2\u09c4\u09cb\3\2\2\2\u09c5\u09c6\5\u0116")
        buf.write("\u008c\2\u09c6\u09c7\7\177\2\2\u09c7\u09c8\5\u012e\u0098")
        buf.write("\2\u09c8\u09c9\7\u0080\2\2\u09c9\u09cb\3\2\2\2\u09ca\u09c2")
        buf.write("\3\2\2\2\u09ca\u09c5\3\2\2\2\u09cb\u019b\3\2\2\2\u09cc")
        buf.write("\u09cd\5\u010e\u0088\2\u09cd\u09ce\7\u0088\2\2\u09ce\u019d")
        buf.write("\3\2\2\2\u09cf\u09dd\5\u0116\u008c\2\u09d0\u09d1\7\177")
        buf.write("\2\2\u09d1\u09d2\5\u0124\u0093\2\u09d2\u09d7\7\u0080\2")
        buf.write("\2\u09d3\u09d4\7\u0093\2\2\u09d4\u09d5\5\u0112\u008a\2")
        buf.write("\u09d5\u09d6\7\u0088\2\2\u09d6\u09d8\3\2\2\2\u09d7\u09d3")
        buf.write("\3\2\2\2\u09d7\u09d8\3\2\2\2\u09d8\u09de\3\2\2\2\u09d9")
        buf.write("\u09da\5\u0178\u00bd\2\u09da\u09db\5L\'\2\u09db\u09dc")
        buf.write("\7\u0088\2\2\u09dc\u09de\3\2\2\2\u09dd\u09d0\3\2\2\2\u09dd")
        buf.write("\u09d9\3\2\2\2\u09de\u019f\3\2\2\2\u09df\u09e0\7\35\2")
        buf.write("\2\u09e0\u09e1\5\6\4\2\u09e1\u09e2\5\u010a\u0086\2\u09e2")
        buf.write("\u09e3\7\u0088\2\2\u09e3\u01a1\3\2\2\2\u09e4\u09e5\7`")
        buf.write("\2\2\u09e5\u09e6\7\u0081\2\2\u09e6\u09e7\5\u011a\u008e")
        buf.write("\2\u09e7\u09f0\7\u0082\2\2\u09e8\u09e9\7\177\2\2\u09e9")
        buf.write("\u09ea\5\u0124\u0093\2\u09ea\u09eb\7\u0080\2\2\u09eb\u09f1")
        buf.write("\3\2\2\2\u09ec\u09ed\5\u0178\u00bd\2\u09ed\u09ee\5L\'")
        buf.write("\2\u09ee\u09ef\7\u0088\2\2\u09ef\u09f1\3\2\2\2\u09f0\u09e8")
        buf.write("\3\2\2\2\u09f0\u09ec\3\2\2\2\u09f1\u01a3\3\2\2\2\u09f2")
        buf.write("\u09f3\7\u0092\2\2\u09f3\u09f4\5\u01b4\u00db\2\u09f4\u09f5")
        buf.write("\7\u0083\2\2\u09f5\u09f6\7\u0084\2\2\u09f6\u09f7\5\u013a")
        buf.write("\u009e\2\u09f7\u01a5\3\2\2\2\u09f8\u09f9\5\u01b4\u00db")
        buf.write("\2\u09f9\u09fb\7\u0083\2\2\u09fa\u09fc\5\u011a\u008e\2")
        buf.write("\u09fb\u09fa\3\2\2\2\u09fb\u09fc\3\2\2\2\u09fc\u09fd\3")
        buf.write("\2\2\2\u09fd\u09ff\7\u0084\2\2\u09fe\u0a00\5\u0138\u009d")
        buf.write("\2\u09ff\u09fe\3\2\2\2\u09ff\u0a00\3\2\2\2\u0a00\u0a01")
        buf.write("\3\2\2\2\u0a01\u0a02\5\u013a\u009e\2\u0a02\u01a7\3\2\2")
        buf.write("\2\u0a03\u0a05\5\u01aa\u00d6\2\u0a04\u0a06\5\u00e8u\2")
        buf.write("\u0a05\u0a04\3\2\2\2\u0a05\u0a06\3\2\2\2\u0a06\u0a07\3")
        buf.write("\2\2\2\u0a07\u0a09\7\u0083\2\2\u0a08\u0a0a\5\u011a\u008e")
        buf.write("\2\u0a09\u0a08\3\2\2\2\u0a09\u0a0a\3\2\2\2\u0a0a\u0a0b")
        buf.write("\3\2\2\2\u0a0b\u0a0d\7\u0084\2\2\u0a0c\u0a0e\5\u00f0y")
        buf.write("\2\u0a0d\u0a0c\3\2\2\2\u0a0d\u0a0e\3\2\2\2\u0a0e\u0a14")
        buf.write("\3\2\2\2\u0a0f\u0a15\5\u0118\u008d\2\u0a10\u0a11\5\u0178")
        buf.write("\u00bd\2\u0a11\u0a12\5L\'\2\u0a12\u0a13\7\u0088\2\2\u0a13")
        buf.write("\u0a15\3\2\2\2\u0a14\u0a0f\3\2\2\2\u0a14\u0a10\3\2\2\2")
        buf.write("\u0a15\u01a9\3\2\2\2\u0a16\u0a1c\5\u01b4\u00db\2\u0a17")
        buf.write("\u0a18\5\u01b4\u00db\2\u0a18\u0a19\7\u0097\2\2\u0a19\u0a1a")
        buf.write("\5\u01b4\u00db\2\u0a1a\u0a1c\3\2\2\2\u0a1b\u0a16\3\2\2")
        buf.write("\2\u0a1b\u0a17\3\2\2\2\u0a1c\u0a24\3\2\2\2\u0a1d\u0a1f")
        buf.write("\5\30\r\2\u0a1e\u0a1d\3\2\2\2\u0a1e\u0a1f\3\2\2\2\u0a1f")
        buf.write("\u0a20\3\2\2\2\u0a20\u0a21\7\u0085\2\2\u0a21\u0a23\5\u01b4")
        buf.write("\u00db\2\u0a22\u0a1e\3\2\2\2\u0a23\u0a26\3\2\2\2\u0a24")
        buf.write("\u0a22\3\2\2\2\u0a24\u0a25\3\2\2\2\u0a25\u01ab\3\2\2\2")
        buf.write("\u0a26\u0a24\3\2\2\2\u0a27\u0a28\7H\2\2\u0a28\u0a29\5")
        buf.write("\u0134\u009b\2\u0a29\u0a2b\7\u0083\2\2\u0a2a\u0a2c\78")
        buf.write("\2\2\u0a2b\u0a2a\3\2\2\2\u0a2b\u0a2c\3\2\2\2\u0a2c\u0a2d")
        buf.write("\3\2\2\2\u0a2d\u0a33\5\u01ae\u00d8\2\u0a2e\u0a30\7\u0086")
        buf.write("\2\2\u0a2f\u0a31\78\2\2\u0a30\u0a2f\3\2\2\2\u0a30\u0a31")
        buf.write("\3\2\2\2\u0a31\u0a32\3\2\2\2\u0a32\u0a34\5\u01ae\u00d8")
        buf.write("\2\u0a33\u0a2e\3\2\2\2\u0a33\u0a34\3\2\2\2\u0a34\u0a35")
        buf.write("\3\2\2\2\u0a35\u0a3b\7\u0084\2\2\u0a36\u0a3c\5\u013a\u009e")
        buf.write("\2\u0a37\u0a38\5\u0178\u00bd\2\u0a38\u0a39\5L\'\2\u0a39")
        buf.write("\u0a3a\7\u0088\2\2\u0a3a\u0a3c\3\2\2\2\u0a3b\u0a36\3\2")
        buf.write("\2\2\u0a3b\u0a37\3\2\2\2\u0a3c\u01ad\3\2\2\2\u0a3d\u0a3e")
        buf.write("\5\6\4\2\u0a3e\u0a41\5\u01b4\u00db\2\u0a3f\u0a40\7\u0093")
        buf.write("\2\2\u0a40\u0a42\5\36\20\2\u0a41\u0a3f\3\2\2\2\u0a41\u0a42")
        buf.write("\3\2\2\2\u0a42\u01af\3\2\2\2\u0a43\u0a45\7\u0083\2\2\u0a44")
        buf.write("\u0a46\5\32\16\2\u0a45\u0a44\3\2\2\2\u0a45\u0a46\3\2\2")
        buf.write("\2\u0a46\u0a47\3\2\2\2\u0a47\u0a48\7\u0084\2\2\u0a48\u01b1")
        buf.write("\3\2\2\2\u0a49\u0a4b\7\u0083\2\2\u0a4a\u0a4c\5\32\16\2")
        buf.write("\u0a4b\u0a4a\3\2\2\2\u0a4b\u0a4c\3\2\2\2\u0a4c\u0a4d\3")
        buf.write("\2\2\2\u0a4d\u0a4f\7\u0084\2\2\u0a4e\u0a50\5Z.\2\u0a4f")
        buf.write("\u0a4e\3\2\2\2\u0a4f\u0a50\3\2\2\2\u0a50\u01b3\3\2\2\2")
        buf.write("\u0a51\u0a52\t\24\2\2\u0a52\u01b5\3\2\2\2\u015a\u01b7")
        buf.write("\u01ba\u01bd\u01c2\u01c6\u01cc\u01cf\u01d4\u01d8\u01df")
        buf.write("\u01e1\u01e9\u01f1\u01f7\u01fb\u0200\u020a\u0212\u021c")
        buf.write("\u0222\u0225\u0229\u0231\u0236\u0240\u024d\u0255\u025b")
        buf.write("\u025d\u0264\u026c\u0274\u027c\u0284\u028c\u0296\u0298")
        buf.write("\u029e\u02a3\u02ab\u02b3\u02bb\u02bd\u02c0\u02c7\u02cc")
        buf.write("\u02d3\u02d7\u02d9\u02f5\u02f9\u02fe\u0302\u030a\u030d")
        buf.write("\u0312\u0316\u031a\u0320\u032e\u0334\u0340\u0344\u0349")
        buf.write("\u034d\u0353\u035b\u0364\u0376\u0379\u037e\u0381\u0390")
        buf.write("\u0396\u039a\u03a0\u03a5\u03a8\u03b0\u03b8\u03c3\u03c8")
        buf.write("\u03cd\u03cf\u03d8\u03e0\u03e7\u03ef\u03f3\u03fc\u0401")
        buf.write("\u0403\u040c\u0414\u0418\u041d\u041f\u0424\u0428\u042f")
        buf.write("\u0437\u0439\u043d\u0440\u0443\u044b\u0455\u0466\u046d")
        buf.write("\u0471\u047b\u0480\u0487\u0490\u0495\u049c\u04a8\u04b3")
        buf.write("\u04bb\u04c0\u04c9\u04d2\u04db\u04e1\u04e6\u04ea\u04ee")
        buf.write("\u04f2\u04f6\u04fd\u0505\u0512\u051c\u0532\u0536\u053a")
        buf.write("\u053f\u0553\u0558\u055d\u0564\u0567\u057d\u0589\u058d")
        buf.write("\u0595\u059d\u05a4\u05a8\u05ad\u05b0\u05b5\u05bd\u05c2")
        buf.write("\u05c9\u05cf\u05d7\u05df\u05e2\u05e9\u05f0\u05f4\u05f7")
        buf.write("\u05fd\u0601\u0607\u0615\u061b\u0622\u0627\u062a\u062d")
        buf.write("\u0634\u063e\u064f\u0654\u0658\u065b\u065e\u0665\u066b")
        buf.write("\u0673\u0679\u0683\u068b\u0691\u069c\u06a0\u06a2\u06a7")
        buf.write("\u06ab\u06b2\u06bb\u06c2\u06c5\u06c8\u06cc\u06d1\u06de")
        buf.write("\u06e8\u06ef\u06fb\u0702\u070e\u0714\u0718\u071c\u0722")
        buf.write("\u0728\u072a\u0731\u0735\u0738\u073c\u0746\u0749\u0750")
        buf.write("\u0753\u0758\u075d\u075f\u0762\u0765\u076b\u076e\u077a")
        buf.write("\u077e\u0781\u078b\u078e\u0794\u07af\u07bc\u07c2\u07cb")
        buf.write("\u07d1\u07d4\u07dc\u07e0\u07e6\u07ec\u07f2\u07fd\u0801")
        buf.write("\u0803\u080d\u0813\u0816\u0823\u0829\u082c\u082f\u0836")
        buf.write("\u083b\u083f\u0843\u0854\u0857\u085c\u0860\u0864\u086d")
        buf.write("\u0870\u0875\u0879\u087e\u0882\u0884\u088f\u0893\u0895")
        buf.write("\u089a\u089f\u08a6\u08ac\u08b1\u08b7\u08bb\u08c1\u08c8")
        buf.write("\u08d2\u08d5\u08d8\u08dd\u08e3\u08e7\u08e9\u08f0\u08f7")
        buf.write("\u08ff\u0903\u0912\u0916\u091f\u0923\u0927\u093d\u0945")
        buf.write("\u094b\u0954\u095d\u0963\u096a\u0971\u0973\u097a\u097d")
        buf.write("\u0980\u0984\u0987\u098c\u098f\u0992\u0996\u099b\u099e")
        buf.write("\u09a1\u09a5\u09aa\u09ae\u09b4\u09b8\u09bc\u09ca\u09d7")
        buf.write("\u09dd\u09f0\u09fb\u09ff\u0a05\u0a09\u0a0d\u0a14\u0a1b")
        buf.write("\u0a1e\u0a24\u0a2b\u0a30\u0a33\u0a3b\u0a41\u0a45\u0a4b")
        buf.write("\u0a4f")
        return buf.getvalue()


class CSharpParser ( Parser ):

    grammarFileName = "CSharpParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\u00EF\u00BB\u00BF'", "<INVALID>", "'/***/'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'#'", "'abstract'", "'add'", "'alias'", "'__arglist'", 
                     "'as'", "'ascending'", "'async'", "'await'", "'base'", 
                     "'bool'", "'break'", "'by'", "'byte'", "'case'", "'catch'", 
                     "'char'", "'checked'", "'class'", "'const'", "'continue'", 
                     "'decimal'", "'default'", "'delegate'", "'descending'", 
                     "'do'", "'double'", "'dynamic'", "'else'", "'enum'", 
                     "'equals'", "'event'", "'explicit'", "'extern'", "'false'", 
                     "'finally'", "'fixed'", "'float'", "'for'", "'foreach'", 
                     "'from'", "'get'", "'goto'", "'group'", "'if'", "'implicit'", 
                     "'in'", "'int'", "'interface'", "'internal'", "'into'", 
                     "'is'", "'join'", "'let'", "'lock'", "'long'", "'nameof'", 
                     "'namespace'", "'new'", "'null'", "'object'", "'on'", 
                     "'operator'", "'orderby'", "'out'", "'override'", "'params'", 
                     "'partial'", "'private'", "'protected'", "'public'", 
                     "'readonly'", "'ref'", "'remove'", "'return'", "'sbyte'", 
                     "'sealed'", "'select'", "'set'", "'short'", "'sizeof'", 
                     "'stackalloc'", "'static'", "'string'", "'struct'", 
                     "'switch'", "'this'", "'throw'", "'true'", "'try'", 
                     "'typeof'", "'uint'", "'ulong'", "'unchecked'", "'unmanaged'", 
                     "'unsafe'", "'ushort'", "'using'", "'var'", "'virtual'", 
                     "'void'", "'volatile'", "'when'", "'where'", "'while'", 
                     "'yield'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'{'", "'}'", 
                     "'['", "']'", "'('", "')'", "'.'", "','", "':'", "';'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'&'", "'|'", "'^'", 
                     "'!'", "'~'", "'='", "'<'", "'>'", "'?'", "'::'", "'??'", 
                     "'++'", "'--'", "'&&'", "'||'", "'->'", "'=='", "'!='", 
                     "'<='", "'>='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'&='", "'|='", "'^='", "'<<'", "'<<='", "'??='", "'..'", 
                     "'{{'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'define'", "'undef'", "'elif'", 
                     "'endif'", "'line'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'hidden'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'}}'" ]

    symbolicNames = [ "<INVALID>", "BYTE_ORDER_MARK", "SINGLE_LINE_DOC_COMMENT", 
                      "EMPTY_DELIMITED_DOC_COMMENT", "DELIMITED_DOC_COMMENT", 
                      "SINGLE_LINE_COMMENT", "DELIMITED_COMMENT", "WHITESPACES", 
                      "SHARP", "ABSTRACT", "ADD", "ALIAS", "ARGLIST", "AS", 
                      "ASCENDING", "ASYNC", "AWAIT", "BASE", "BOOL", "BREAK", 
                      "BY", "BYTE", "CASE", "CATCH", "CHAR", "CHECKED", 
                      "CLASS", "CONST", "CONTINUE", "DECIMAL", "DEFAULT", 
                      "DELEGATE", "DESCENDING", "DO", "DOUBLE", "DYNAMIC", 
                      "ELSE", "ENUM", "EQUALS", "EVENT", "EXPLICIT", "EXTERN", 
                      "FALSE", "FINALLY", "FIXED", "FLOAT", "FOR", "FOREACH", 
                      "FROM", "GET", "GOTO", "GROUP", "IF", "IMPLICIT", 
                      "IN", "INT", "INTERFACE", "INTERNAL", "INTO", "IS", 
                      "JOIN", "LET", "LOCK", "LONG", "NAMEOF", "NAMESPACE", 
                      "NEW", "NULL", "OBJECT", "ON", "OPERATOR", "ORDERBY", 
                      "OUT", "OVERRIDE", "PARAMS", "PARTIAL", "PRIVATE", 
                      "PROTECTED", "PUBLIC", "READONLY", "REF", "REMOVE", 
                      "RETURN", "SBYTE", "SEALED", "SELECT", "SET", "SHORT", 
                      "SIZEOF", "STACKALLOC", "STATIC", "STRING", "STRUCT", 
                      "SWITCH", "THIS", "THROW", "TRUE", "TRY", "TYPEOF", 
                      "UINT", "ULONG", "UNCHECKED", "UNMANAGED", "UNSAFE", 
                      "USHORT", "USING", "VAR", "VIRTUAL", "VOID", "VOLATILE", 
                      "WHEN", "WHERE", "WHILE", "YIELD", "IDENTIFIER", "LITERAL_ACCESS", 
                      "INTEGER_LITERAL", "HEX_INTEGER_LITERAL", "BIN_INTEGER_LITERAL", 
                      "REAL_LITERAL", "CHARACTER_LITERAL", "REGULAR_STRING", 
                      "VERBATIUM_STRING", "INTERPOLATED_REGULAR_STRING_START", 
                      "INTERPOLATED_VERBATIUM_STRING_START", "OPEN_BRACE", 
                      "CLOSE_BRACE", "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_PARENS", 
                      "CLOSE_PARENS", "DOT", "COMMA", "COLON", "SEMICOLON", 
                      "PLUS", "MINUS", "STAR", "DIV", "PERCENT", "AMP", 
                      "BITWISE_OR", "CARET", "BANG", "TILDE", "ASSIGNMENT", 
                      "LT", "GT", "INTERR", "DOUBLE_COLON", "OP_COALESCING", 
                      "OP_INC", "OP_DEC", "OP_AND", "OP_OR", "OP_PTR", "OP_EQ", 
                      "OP_NE", "OP_LE", "OP_GE", "OP_ADD_ASSIGNMENT", "OP_SUB_ASSIGNMENT", 
                      "OP_MULT_ASSIGNMENT", "OP_DIV_ASSIGNMENT", "OP_MOD_ASSIGNMENT", 
                      "OP_AND_ASSIGNMENT", "OP_OR_ASSIGNMENT", "OP_XOR_ASSIGNMENT", 
                      "OP_LEFT_SHIFT", "OP_LEFT_SHIFT_ASSIGNMENT", "OP_COALESCING_ASSIGNMENT", 
                      "OP_RANGE", "DOUBLE_CURLY_INSIDE", "OPEN_BRACE_INSIDE", 
                      "REGULAR_CHAR_INSIDE", "VERBATIUM_DOUBLE_QUOTE_INSIDE", 
                      "DOUBLE_QUOTE_INSIDE", "REGULAR_STRING_INSIDE", "VERBATIUM_INSIDE_STRING", 
                      "CLOSE_BRACE_INSIDE", "FORMAT_STRING", "DIRECTIVE_WHITESPACES", 
                      "DIGITS", "DEFINE", "UNDEF", "ELIF", "ENDIF", "LINE", 
                      "ERROR", "WARNING", "REGION", "ENDREGION", "PRAGMA", 
                      "NULLABLE", "DIRECTIVE_HIDDEN", "CONDITIONAL_SYMBOL", 
                      "DIRECTIVE_NEW_LINE", "TEXT", "DOUBLE_CURLY_CLOSE_INSIDE" ]

    RULE_compilation_unit = 0
    RULE_namespace_or_type_name = 1
    RULE_type_ = 2
    RULE_base_type = 3
    RULE_tuple_type = 4
    RULE_tuple_element = 5
    RULE_simple_type = 6
    RULE_numeric_type = 7
    RULE_integral_type = 8
    RULE_floating_point_type = 9
    RULE_class_type = 10
    RULE_type_argument_list = 11
    RULE_argument_list = 12
    RULE_argument = 13
    RULE_expression = 14
    RULE_non_assignment_expression = 15
    RULE_assignment = 16
    RULE_assignment_operator = 17
    RULE_conditional_expression = 18
    RULE_null_coalescing_expression = 19
    RULE_conditional_or_expression = 20
    RULE_conditional_and_expression = 21
    RULE_inclusive_or_expression = 22
    RULE_exclusive_or_expression = 23
    RULE_and_expression = 24
    RULE_equality_expression = 25
    RULE_relational_expression = 26
    RULE_shift_expression = 27
    RULE_additive_expression = 28
    RULE_multiplicative_expression = 29
    RULE_switch_expression = 30
    RULE_switch_expression_arms = 31
    RULE_switch_expression_arm = 32
    RULE_range_expression = 33
    RULE_unary_expression = 34
    RULE_primary_expression = 35
    RULE_primary_expression_start = 36
    RULE_throwable_expression = 37
    RULE_throw_expression = 38
    RULE_member_access = 39
    RULE_bracket_expression = 40
    RULE_indexer_argument = 41
    RULE_predefined_type = 42
    RULE_expression_list = 43
    RULE_object_or_collection_initializer = 44
    RULE_object_initializer = 45
    RULE_member_initializer_list = 46
    RULE_member_initializer = 47
    RULE_initializer_value = 48
    RULE_collection_initializer = 49
    RULE_element_initializer = 50
    RULE_anonymous_object_initializer = 51
    RULE_member_declarator_list = 52
    RULE_member_declarator = 53
    RULE_unbound_type_name = 54
    RULE_generic_dimension_specifier = 55
    RULE_isType = 56
    RULE_isTypePatternArms = 57
    RULE_isTypePatternArm = 58
    RULE_lambda_expression = 59
    RULE_anonymous_function_signature = 60
    RULE_explicit_anonymous_function_parameter_list = 61
    RULE_explicit_anonymous_function_parameter = 62
    RULE_implicit_anonymous_function_parameter_list = 63
    RULE_anonymous_function_body = 64
    RULE_query_expression = 65
    RULE_from_clause = 66
    RULE_query_body = 67
    RULE_query_body_clause = 68
    RULE_let_clause = 69
    RULE_where_clause = 70
    RULE_combined_join_clause = 71
    RULE_orderby_clause = 72
    RULE_ordering = 73
    RULE_select_or_group_clause = 74
    RULE_query_continuation = 75
    RULE_statement = 76
    RULE_declarationStatement = 77
    RULE_local_function_declaration = 78
    RULE_local_function_header = 79
    RULE_local_function_modifiers = 80
    RULE_local_function_body = 81
    RULE_labeled_Statement = 82
    RULE_embedded_statement = 83
    RULE_simple_embedded_statement = 84
    RULE_block = 85
    RULE_local_variable_declaration = 86
    RULE_local_variable_type = 87
    RULE_local_variable_declarator = 88
    RULE_local_variable_initializer = 89
    RULE_local_constant_declaration = 90
    RULE_if_body = 91
    RULE_switch_section = 92
    RULE_switch_label = 93
    RULE_case_guard = 94
    RULE_statement_list = 95
    RULE_for_initializer = 96
    RULE_for_iterator = 97
    RULE_catch_clauses = 98
    RULE_specific_catch_clause = 99
    RULE_general_catch_clause = 100
    RULE_exception_filter = 101
    RULE_finally_clause = 102
    RULE_resource_acquisition = 103
    RULE_namespace_declaration = 104
    RULE_qualified_identifier = 105
    RULE_namespace_body = 106
    RULE_extern_alias_directives = 107
    RULE_extern_alias_directive = 108
    RULE_using_directives = 109
    RULE_using_directive = 110
    RULE_namespace_member_declarations = 111
    RULE_namespace_member_declaration = 112
    RULE_type_declaration = 113
    RULE_qualified_alias_member = 114
    RULE_type_parameter_list = 115
    RULE_type_parameter = 116
    RULE_class_base = 117
    RULE_interface_type_list = 118
    RULE_type_parameter_constraints_clauses = 119
    RULE_type_parameter_constraints_clause = 120
    RULE_type_parameter_constraints = 121
    RULE_primary_constraint = 122
    RULE_secondary_constraints = 123
    RULE_constructor_constraint = 124
    RULE_class_body = 125
    RULE_class_member_declarations = 126
    RULE_class_member_declaration = 127
    RULE_all_member_modifiers = 128
    RULE_all_member_modifier = 129
    RULE_common_member_declaration = 130
    RULE_typed_member_declaration = 131
    RULE_constant_declarators = 132
    RULE_constant_declarator = 133
    RULE_variable_declarators = 134
    RULE_variable_declarator = 135
    RULE_variable_initializer = 136
    RULE_return_type = 137
    RULE_member_name = 138
    RULE_method_body = 139
    RULE_formal_parameter_list = 140
    RULE_fixed_parameters = 141
    RULE_fixed_parameter = 142
    RULE_parameter_modifier = 143
    RULE_parameter_array = 144
    RULE_accessor_declarations = 145
    RULE_get_accessor_declaration = 146
    RULE_set_accessor_declaration = 147
    RULE_accessor_modifier = 148
    RULE_accessor_body = 149
    RULE_event_accessor_declarations = 150
    RULE_add_accessor_declaration = 151
    RULE_remove_accessor_declaration = 152
    RULE_overloadable_operator = 153
    RULE_conversion_operator_declarator = 154
    RULE_constructor_initializer = 155
    RULE_body = 156
    RULE_struct_interfaces = 157
    RULE_struct_body = 158
    RULE_struct_member_declaration = 159
    RULE_array_type = 160
    RULE_rank_specifier = 161
    RULE_array_initializer = 162
    RULE_variant_type_parameter_list = 163
    RULE_variant_type_parameter = 164
    RULE_variance_annotation = 165
    RULE_interface_base = 166
    RULE_interface_body = 167
    RULE_interface_member_declaration = 168
    RULE_interface_accessors = 169
    RULE_enum_base = 170
    RULE_enum_body = 171
    RULE_enum_member_declaration = 172
    RULE_global_attribute_section = 173
    RULE_global_attribute_target = 174
    RULE_attributes = 175
    RULE_attribute_section = 176
    RULE_attribute_target = 177
    RULE_attribute_list = 178
    RULE_attribute = 179
    RULE_attribute_argument = 180
    RULE_pointer_type = 181
    RULE_fixed_pointer_declarators = 182
    RULE_fixed_pointer_declarator = 183
    RULE_fixed_pointer_initializer = 184
    RULE_fixed_size_buffer_declarator = 185
    RULE_stackalloc_initializer = 186
    RULE_right_arrow = 187
    RULE_right_shift = 188
    RULE_right_shift_assignment = 189
    RULE_literal = 190
    RULE_boolean_literal = 191
    RULE_string_literal = 192
    RULE_interpolated_regular_string = 193
    RULE_interpolated_verbatium_string = 194
    RULE_interpolated_regular_string_part = 195
    RULE_interpolated_verbatium_string_part = 196
    RULE_interpolated_string_expression = 197
    RULE_keyword = 198
    RULE_class_definition = 199
    RULE_struct_definition = 200
    RULE_interface_definition = 201
    RULE_enum_definition = 202
    RULE_delegate_definition = 203
    RULE_event_declaration = 204
    RULE_field_declaration = 205
    RULE_property_declaration = 206
    RULE_constant_declaration = 207
    RULE_indexer_declaration = 208
    RULE_destructor_definition = 209
    RULE_constructor_declaration = 210
    RULE_method_declaration = 211
    RULE_method_member_name = 212
    RULE_operator_declaration = 213
    RULE_arg_declaration = 214
    RULE_method_invocation = 215
    RULE_object_creation_expression = 216
    RULE_identifier = 217

    ruleNames =  [ "compilation_unit", "namespace_or_type_name", "type_", 
                   "base_type", "tuple_type", "tuple_element", "simple_type", 
                   "numeric_type", "integral_type", "floating_point_type", 
                   "class_type", "type_argument_list", "argument_list", 
                   "argument", "expression", "non_assignment_expression", 
                   "assignment", "assignment_operator", "conditional_expression", 
                   "null_coalescing_expression", "conditional_or_expression", 
                   "conditional_and_expression", "inclusive_or_expression", 
                   "exclusive_or_expression", "and_expression", "equality_expression", 
                   "relational_expression", "shift_expression", "additive_expression", 
                   "multiplicative_expression", "switch_expression", "switch_expression_arms", 
                   "switch_expression_arm", "range_expression", "unary_expression", 
                   "primary_expression", "primary_expression_start", "throwable_expression", 
                   "throw_expression", "member_access", "bracket_expression", 
                   "indexer_argument", "predefined_type", "expression_list", 
                   "object_or_collection_initializer", "object_initializer", 
                   "member_initializer_list", "member_initializer", "initializer_value", 
                   "collection_initializer", "element_initializer", "anonymous_object_initializer", 
                   "member_declarator_list", "member_declarator", "unbound_type_name", 
                   "generic_dimension_specifier", "isType", "isTypePatternArms", 
                   "isTypePatternArm", "lambda_expression", "anonymous_function_signature", 
                   "explicit_anonymous_function_parameter_list", "explicit_anonymous_function_parameter", 
                   "implicit_anonymous_function_parameter_list", "anonymous_function_body", 
                   "query_expression", "from_clause", "query_body", "query_body_clause", 
                   "let_clause", "where_clause", "combined_join_clause", 
                   "orderby_clause", "ordering", "select_or_group_clause", 
                   "query_continuation", "statement", "declarationStatement", 
                   "local_function_declaration", "local_function_header", 
                   "local_function_modifiers", "local_function_body", "labeled_Statement", 
                   "embedded_statement", "simple_embedded_statement", "block", 
                   "local_variable_declaration", "local_variable_type", 
                   "local_variable_declarator", "local_variable_initializer", 
                   "local_constant_declaration", "if_body", "switch_section", 
                   "switch_label", "case_guard", "statement_list", "for_initializer", 
                   "for_iterator", "catch_clauses", "specific_catch_clause", 
                   "general_catch_clause", "exception_filter", "finally_clause", 
                   "resource_acquisition", "namespace_declaration", "qualified_identifier", 
                   "namespace_body", "extern_alias_directives", "extern_alias_directive", 
                   "using_directives", "using_directive", "namespace_member_declarations", 
                   "namespace_member_declaration", "type_declaration", "qualified_alias_member", 
                   "type_parameter_list", "type_parameter", "class_base", 
                   "interface_type_list", "type_parameter_constraints_clauses", 
                   "type_parameter_constraints_clause", "type_parameter_constraints", 
                   "primary_constraint", "secondary_constraints", "constructor_constraint", 
                   "class_body", "class_member_declarations", "class_member_declaration", 
                   "all_member_modifiers", "all_member_modifier", "common_member_declaration", 
                   "typed_member_declaration", "constant_declarators", "constant_declarator", 
                   "variable_declarators", "variable_declarator", "variable_initializer", 
                   "return_type", "member_name", "method_body", "formal_parameter_list", 
                   "fixed_parameters", "fixed_parameter", "parameter_modifier", 
                   "parameter_array", "accessor_declarations", "get_accessor_declaration", 
                   "set_accessor_declaration", "accessor_modifier", "accessor_body", 
                   "event_accessor_declarations", "add_accessor_declaration", 
                   "remove_accessor_declaration", "overloadable_operator", 
                   "conversion_operator_declarator", "constructor_initializer", 
                   "body", "struct_interfaces", "struct_body", "struct_member_declaration", 
                   "array_type", "rank_specifier", "array_initializer", 
                   "variant_type_parameter_list", "variant_type_parameter", 
                   "variance_annotation", "interface_base", "interface_body", 
                   "interface_member_declaration", "interface_accessors", 
                   "enum_base", "enum_body", "enum_member_declaration", 
                   "global_attribute_section", "global_attribute_target", 
                   "attributes", "attribute_section", "attribute_target", 
                   "attribute_list", "attribute", "attribute_argument", 
                   "pointer_type", "fixed_pointer_declarators", "fixed_pointer_declarator", 
                   "fixed_pointer_initializer", "fixed_size_buffer_declarator", 
                   "stackalloc_initializer", "right_arrow", "right_shift", 
                   "right_shift_assignment", "literal", "boolean_literal", 
                   "string_literal", "interpolated_regular_string", "interpolated_verbatium_string", 
                   "interpolated_regular_string_part", "interpolated_verbatium_string_part", 
                   "interpolated_string_expression", "keyword", "class_definition", 
                   "struct_definition", "interface_definition", "enum_definition", 
                   "delegate_definition", "event_declaration", "field_declaration", 
                   "property_declaration", "constant_declaration", "indexer_declaration", 
                   "destructor_definition", "constructor_declaration", "method_declaration", 
                   "method_member_name", "operator_declaration", "arg_declaration", 
                   "method_invocation", "object_creation_expression", "identifier" ]

    EOF = Token.EOF
    BYTE_ORDER_MARK=1
    SINGLE_LINE_DOC_COMMENT=2
    EMPTY_DELIMITED_DOC_COMMENT=3
    DELIMITED_DOC_COMMENT=4
    SINGLE_LINE_COMMENT=5
    DELIMITED_COMMENT=6
    WHITESPACES=7
    SHARP=8
    ABSTRACT=9
    ADD=10
    ALIAS=11
    ARGLIST=12
    AS=13
    ASCENDING=14
    ASYNC=15
    AWAIT=16
    BASE=17
    BOOL=18
    BREAK=19
    BY=20
    BYTE=21
    CASE=22
    CATCH=23
    CHAR=24
    CHECKED=25
    CLASS=26
    CONST=27
    CONTINUE=28
    DECIMAL=29
    DEFAULT=30
    DELEGATE=31
    DESCENDING=32
    DO=33
    DOUBLE=34
    DYNAMIC=35
    ELSE=36
    ENUM=37
    EQUALS=38
    EVENT=39
    EXPLICIT=40
    EXTERN=41
    FALSE=42
    FINALLY=43
    FIXED=44
    FLOAT=45
    FOR=46
    FOREACH=47
    FROM=48
    GET=49
    GOTO=50
    GROUP=51
    IF=52
    IMPLICIT=53
    IN=54
    INT=55
    INTERFACE=56
    INTERNAL=57
    INTO=58
    IS=59
    JOIN=60
    LET=61
    LOCK=62
    LONG=63
    NAMEOF=64
    NAMESPACE=65
    NEW=66
    NULL=67
    OBJECT=68
    ON=69
    OPERATOR=70
    ORDERBY=71
    OUT=72
    OVERRIDE=73
    PARAMS=74
    PARTIAL=75
    PRIVATE=76
    PROTECTED=77
    PUBLIC=78
    READONLY=79
    REF=80
    REMOVE=81
    RETURN=82
    SBYTE=83
    SEALED=84
    SELECT=85
    SET=86
    SHORT=87
    SIZEOF=88
    STACKALLOC=89
    STATIC=90
    STRING=91
    STRUCT=92
    SWITCH=93
    THIS=94
    THROW=95
    TRUE=96
    TRY=97
    TYPEOF=98
    UINT=99
    ULONG=100
    UNCHECKED=101
    UNMANAGED=102
    UNSAFE=103
    USHORT=104
    USING=105
    VAR=106
    VIRTUAL=107
    VOID=108
    VOLATILE=109
    WHEN=110
    WHERE=111
    WHILE=112
    YIELD=113
    IDENTIFIER=114
    LITERAL_ACCESS=115
    INTEGER_LITERAL=116
    HEX_INTEGER_LITERAL=117
    BIN_INTEGER_LITERAL=118
    REAL_LITERAL=119
    CHARACTER_LITERAL=120
    REGULAR_STRING=121
    VERBATIUM_STRING=122
    INTERPOLATED_REGULAR_STRING_START=123
    INTERPOLATED_VERBATIUM_STRING_START=124
    OPEN_BRACE=125
    CLOSE_BRACE=126
    OPEN_BRACKET=127
    CLOSE_BRACKET=128
    OPEN_PARENS=129
    CLOSE_PARENS=130
    DOT=131
    COMMA=132
    COLON=133
    SEMICOLON=134
    PLUS=135
    MINUS=136
    STAR=137
    DIV=138
    PERCENT=139
    AMP=140
    BITWISE_OR=141
    CARET=142
    BANG=143
    TILDE=144
    ASSIGNMENT=145
    LT=146
    GT=147
    INTERR=148
    DOUBLE_COLON=149
    OP_COALESCING=150
    OP_INC=151
    OP_DEC=152
    OP_AND=153
    OP_OR=154
    OP_PTR=155
    OP_EQ=156
    OP_NE=157
    OP_LE=158
    OP_GE=159
    OP_ADD_ASSIGNMENT=160
    OP_SUB_ASSIGNMENT=161
    OP_MULT_ASSIGNMENT=162
    OP_DIV_ASSIGNMENT=163
    OP_MOD_ASSIGNMENT=164
    OP_AND_ASSIGNMENT=165
    OP_OR_ASSIGNMENT=166
    OP_XOR_ASSIGNMENT=167
    OP_LEFT_SHIFT=168
    OP_LEFT_SHIFT_ASSIGNMENT=169
    OP_COALESCING_ASSIGNMENT=170
    OP_RANGE=171
    DOUBLE_CURLY_INSIDE=172
    OPEN_BRACE_INSIDE=173
    REGULAR_CHAR_INSIDE=174
    VERBATIUM_DOUBLE_QUOTE_INSIDE=175
    DOUBLE_QUOTE_INSIDE=176
    REGULAR_STRING_INSIDE=177
    VERBATIUM_INSIDE_STRING=178
    CLOSE_BRACE_INSIDE=179
    FORMAT_STRING=180
    DIRECTIVE_WHITESPACES=181
    DIGITS=182
    DEFINE=183
    UNDEF=184
    ELIF=185
    ENDIF=186
    LINE=187
    ERROR=188
    WARNING=189
    REGION=190
    ENDREGION=191
    PRAGMA=192
    NULLABLE=193
    DIRECTIVE_HIDDEN=194
    CONDITIONAL_SYMBOL=195
    DIRECTIVE_NEW_LINE=196
    TEXT=197
    DOUBLE_CURLY_CLOSE_INSIDE=198

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Compilation_unitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSharpParser.EOF, 0)

        def BYTE_ORDER_MARK(self):
            return self.getToken(CSharpParser.BYTE_ORDER_MARK, 0)

        def extern_alias_directives(self):
            return self.getTypedRuleContext(CSharpParser.Extern_alias_directivesContext,0)


        def using_directives(self):
            return self.getTypedRuleContext(CSharpParser.Using_directivesContext,0)


        def global_attribute_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Global_attribute_sectionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Global_attribute_sectionContext,i)


        def namespace_member_declarations(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_member_declarationsContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_compilation_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilation_unit" ):
                listener.enterCompilation_unit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilation_unit" ):
                listener.exitCompilation_unit(self)




    def compilation_unit(self):

        localctx = CSharpParser.Compilation_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilation_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.BYTE_ORDER_MARK:
                self.state = 436
                self.match(CSharpParser.BYTE_ORDER_MARK)


            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 439
                self.extern_alias_directives()


            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.USING:
                self.state = 442
                self.using_directives()


            self.state = 448
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 445
                    self.global_attribute_section() 
                self.state = 450
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.CLASS) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.ENUM) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.INTERFACE) | (1 << CSharpParser.INTERNAL))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NAMESPACE - 65)) | (1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.OVERRIDE - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.PRIVATE - 65)) | (1 << (CSharpParser.PROTECTED - 65)) | (1 << (CSharpParser.PUBLIC - 65)) | (1 << (CSharpParser.READONLY - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.SEALED - 65)) | (1 << (CSharpParser.STATIC - 65)) | (1 << (CSharpParser.STRUCT - 65)) | (1 << (CSharpParser.UNSAFE - 65)) | (1 << (CSharpParser.VIRTUAL - 65)) | (1 << (CSharpParser.VOLATILE - 65)) | (1 << (CSharpParser.OPEN_BRACKET - 65)))) != 0):
                self.state = 451
                self.namespace_member_declarations()


            self.state = 454
            self.match(CSharpParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Namespace_or_type_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def qualified_alias_member(self):
            return self.getTypedRuleContext(CSharpParser.Qualified_alias_memberContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.DOT)
            else:
                return self.getToken(CSharpParser.DOT, i)

        def type_argument_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Type_argument_listContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Type_argument_listContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_namespace_or_type_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace_or_type_name" ):
                listener.enterNamespace_or_type_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace_or_type_name" ):
                listener.exitNamespace_or_type_name(self)




    def namespace_or_type_name(self):

        localctx = CSharpParser.Namespace_or_type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_namespace_or_type_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 456
                self.identifier()
                self.state = 458
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 457
                    self.type_argument_list()


                pass

            elif la_ == 2:
                self.state = 460
                self.qualified_alias_member()
                pass


            self.state = 470
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 463
                    self.match(CSharpParser.DOT)
                    self.state = 464
                    self.identifier()
                    self.state = 466
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        self.state = 465
                        self.type_argument_list()

             
                self.state = 472
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def base_type(self):
            return self.getTypedRuleContext(CSharpParser.Base_typeContext,0)


        def INTERR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.INTERR)
            else:
                return self.getToken(CSharpParser.INTERR, i)

        def rank_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Rank_specifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Rank_specifierContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.STAR)
            else:
                return self.getToken(CSharpParser.STAR, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_type_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_" ):
                listener.enterType_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_" ):
                listener.exitType_(self)




    def type_(self):

        localctx = CSharpParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.base_type()
            self.state = 479
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 477
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CSharpParser.INTERR]:
                        self.state = 474
                        self.match(CSharpParser.INTERR)
                        pass
                    elif token in [CSharpParser.OPEN_BRACKET]:
                        self.state = 475
                        self.rank_specifier()
                        pass
                    elif token in [CSharpParser.STAR]:
                        self.state = 476
                        self.match(CSharpParser.STAR)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 481
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_type(self):
            return self.getTypedRuleContext(CSharpParser.Simple_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(CSharpParser.Class_typeContext,0)


        def VOID(self):
            return self.getToken(CSharpParser.VOID, 0)

        def STAR(self):
            return self.getToken(CSharpParser.STAR, 0)

        def tuple_type(self):
            return self.getTypedRuleContext(CSharpParser.Tuple_typeContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_base_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_type" ):
                listener.enterBase_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_type" ):
                listener.exitBase_type(self)




    def base_type(self):

        localctx = CSharpParser.Base_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_base_type)
        try:
            self.state = 487
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.BOOL, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.DECIMAL, CSharpParser.DOUBLE, CSharpParser.FLOAT, CSharpParser.INT, CSharpParser.LONG, CSharpParser.SBYTE, CSharpParser.SHORT, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.USHORT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.simple_type()
                pass
            elif token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BY, CSharpParser.DESCENDING, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.STRING, CSharpParser.UNMANAGED, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.class_type()
                pass
            elif token in [CSharpParser.VOID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 484
                self.match(CSharpParser.VOID)
                self.state = 485
                self.match(CSharpParser.STAR)
                pass
            elif token in [CSharpParser.OPEN_PARENS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 486
                self.tuple_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tuple_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def tuple_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Tuple_elementContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Tuple_elementContext,i)


        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_tuple_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_type" ):
                listener.enterTuple_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_type" ):
                listener.exitTuple_type(self)




    def tuple_type(self):

        localctx = CSharpParser.Tuple_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tuple_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 490
            self.tuple_element()
            self.state = 493 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 491
                self.match(CSharpParser.COMMA)
                self.state = 492
                self.tuple_element()
                self.state = 495 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSharpParser.COMMA):
                    break

            self.state = 497
            self.match(CSharpParser.CLOSE_PARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tuple_elementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_tuple_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_element" ):
                listener.enterTuple_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_element" ):
                listener.exitTuple_element(self)




    def tuple_element(self):

        localctx = CSharpParser.Tuple_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tuple_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.type_()
            self.state = 501
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BY) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)))) != 0):
                self.state = 500
                self.identifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numeric_type(self):
            return self.getTypedRuleContext(CSharpParser.Numeric_typeContext,0)


        def BOOL(self):
            return self.getToken(CSharpParser.BOOL, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_simple_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_type" ):
                listener.enterSimple_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_type" ):
                listener.exitSimple_type(self)




    def simple_type(self):

        localctx = CSharpParser.Simple_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_simple_type)
        try:
            self.state = 505
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.DECIMAL, CSharpParser.DOUBLE, CSharpParser.FLOAT, CSharpParser.INT, CSharpParser.LONG, CSharpParser.SBYTE, CSharpParser.SHORT, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.USHORT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.numeric_type()
                pass
            elif token in [CSharpParser.BOOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 504
                self.match(CSharpParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numeric_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integral_type(self):
            return self.getTypedRuleContext(CSharpParser.Integral_typeContext,0)


        def floating_point_type(self):
            return self.getTypedRuleContext(CSharpParser.Floating_point_typeContext,0)


        def DECIMAL(self):
            return self.getToken(CSharpParser.DECIMAL, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_numeric_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumeric_type" ):
                listener.enterNumeric_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumeric_type" ):
                listener.exitNumeric_type(self)




    def numeric_type(self):

        localctx = CSharpParser.Numeric_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_numeric_type)
        try:
            self.state = 510
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.INT, CSharpParser.LONG, CSharpParser.SBYTE, CSharpParser.SHORT, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.USHORT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.integral_type()
                pass
            elif token in [CSharpParser.DOUBLE, CSharpParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 508
                self.floating_point_type()
                pass
            elif token in [CSharpParser.DECIMAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 509
                self.match(CSharpParser.DECIMAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Integral_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SBYTE(self):
            return self.getToken(CSharpParser.SBYTE, 0)

        def BYTE(self):
            return self.getToken(CSharpParser.BYTE, 0)

        def SHORT(self):
            return self.getToken(CSharpParser.SHORT, 0)

        def USHORT(self):
            return self.getToken(CSharpParser.USHORT, 0)

        def INT(self):
            return self.getToken(CSharpParser.INT, 0)

        def UINT(self):
            return self.getToken(CSharpParser.UINT, 0)

        def LONG(self):
            return self.getToken(CSharpParser.LONG, 0)

        def ULONG(self):
            return self.getToken(CSharpParser.ULONG, 0)

        def CHAR(self):
            return self.getToken(CSharpParser.CHAR, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_integral_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegral_type" ):
                listener.enterIntegral_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegral_type" ):
                listener.exitIntegral_type(self)




    def integral_type(self):

        localctx = CSharpParser.Integral_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_integral_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.INT) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & ((1 << (CSharpParser.SBYTE - 83)) | (1 << (CSharpParser.SHORT - 83)) | (1 << (CSharpParser.UINT - 83)) | (1 << (CSharpParser.ULONG - 83)) | (1 << (CSharpParser.USHORT - 83)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Floating_point_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(CSharpParser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(CSharpParser.DOUBLE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_floating_point_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloating_point_type" ):
                listener.enterFloating_point_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloating_point_type" ):
                listener.exitFloating_point_type(self)




    def floating_point_type(self):

        localctx = CSharpParser.Floating_point_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_floating_point_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            _la = self._input.LA(1)
            if not(_la==CSharpParser.DOUBLE or _la==CSharpParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace_or_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,0)


        def OBJECT(self):
            return self.getToken(CSharpParser.OBJECT, 0)

        def DYNAMIC(self):
            return self.getToken(CSharpParser.DYNAMIC, 0)

        def STRING(self):
            return self.getToken(CSharpParser.STRING, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_class_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_type" ):
                listener.enterClass_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_type" ):
                listener.exitClass_type(self)




    def class_type(self):

        localctx = CSharpParser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_class_type)
        try:
            self.state = 520
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.namespace_or_type_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.match(CSharpParser.OBJECT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 518
                self.match(CSharpParser.DYNAMIC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 519
                self.match(CSharpParser.STRING)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(CSharpParser.LT, 0)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Type_Context)
            else:
                return self.getTypedRuleContext(CSharpParser.Type_Context,i)


        def GT(self):
            return self.getToken(CSharpParser.GT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_type_argument_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_argument_list" ):
                listener.enterType_argument_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_argument_list" ):
                listener.exitType_argument_list(self)




    def type_argument_list(self):

        localctx = CSharpParser.Type_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.match(CSharpParser.LT)
            self.state = 523
            self.type_()
            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 524
                self.match(CSharpParser.COMMA)
                self.state = 525
                self.type_()
                self.state = 530
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 531
            self.match(CSharpParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_argument_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument_list" ):
                listener.enterArgument_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument_list" ):
                listener.exitArgument_list(self)




    def argument_list(self):

        localctx = CSharpParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.argument()
            self.state = 538
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 534
                self.match(CSharpParser.COMMA)
                self.state = 535
                self.argument()
                self.state = 540
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.refout = None # Token

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def VAR(self):
            return self.getToken(CSharpParser.VAR, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def OUT(self):
            return self.getToken(CSharpParser.OUT, 0)

        def IN(self):
            return self.getToken(CSharpParser.IN, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = CSharpParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 541
                self.identifier()
                self.state = 542
                self.match(CSharpParser.COLON)


            self.state = 547
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 546
                localctx.refout = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 54)) & ~0x3f) == 0 and ((1 << (_la - 54)) & ((1 << (CSharpParser.IN - 54)) | (1 << (CSharpParser.OUT - 54)) | (1 << (CSharpParser.REF - 54)))) != 0)):
                    localctx.refout = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 551
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 549
                self.match(CSharpParser.VAR)

            elif la_ == 2:
                self.state = 550
                self.type_()


            self.state = 553
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(CSharpParser.AssignmentContext,0)


        def non_assignment_expression(self):
            return self.getTypedRuleContext(CSharpParser.Non_assignment_expressionContext,0)


        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = CSharpParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression)
        try:
            self.state = 559
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 556
                self.non_assignment_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 557
                self.match(CSharpParser.REF)
                self.state = 558
                self.non_assignment_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_assignment_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambda_expression(self):
            return self.getTypedRuleContext(CSharpParser.Lambda_expressionContext,0)


        def query_expression(self):
            return self.getTypedRuleContext(CSharpParser.Query_expressionContext,0)


        def conditional_expression(self):
            return self.getTypedRuleContext(CSharpParser.Conditional_expressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_non_assignment_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_assignment_expression" ):
                listener.enterNon_assignment_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_assignment_expression" ):
                listener.exitNon_assignment_expression(self)




    def non_assignment_expression(self):

        localctx = CSharpParser.Non_assignment_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_non_assignment_expression)
        try:
            self.state = 564
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 561
                self.lambda_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
                self.query_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 563
                self.conditional_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expression(self):
            return self.getTypedRuleContext(CSharpParser.Unary_expressionContext,0)


        def assignment_operator(self):
            return self.getTypedRuleContext(CSharpParser.Assignment_operatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def OP_COALESCING_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_COALESCING_ASSIGNMENT, 0)

        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = CSharpParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assignment)
        try:
            self.state = 574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 566
                self.unary_expression()
                self.state = 567
                self.assignment_operator()
                self.state = 568
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 570
                self.unary_expression()
                self.state = 571
                self.match(CSharpParser.OP_COALESCING_ASSIGNMENT)
                self.state = 572
                self.throwable_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def OP_ADD_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_ADD_ASSIGNMENT, 0)

        def OP_SUB_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_SUB_ASSIGNMENT, 0)

        def OP_MULT_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_MULT_ASSIGNMENT, 0)

        def OP_DIV_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_DIV_ASSIGNMENT, 0)

        def OP_MOD_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_MOD_ASSIGNMENT, 0)

        def OP_AND_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_AND_ASSIGNMENT, 0)

        def OP_OR_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_OR_ASSIGNMENT, 0)

        def OP_XOR_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_XOR_ASSIGNMENT, 0)

        def OP_LEFT_SHIFT_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_LEFT_SHIFT_ASSIGNMENT, 0)

        def right_shift_assignment(self):
            return self.getTypedRuleContext(CSharpParser.Right_shift_assignmentContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_assignment_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_operator" ):
                listener.enterAssignment_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_operator" ):
                listener.exitAssignment_operator(self)




    def assignment_operator(self):

        localctx = CSharpParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assignment_operator)
        try:
            self.state = 587
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ASSIGNMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.match(CSharpParser.ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_ADD_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 577
                self.match(CSharpParser.OP_ADD_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_SUB_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 578
                self.match(CSharpParser.OP_SUB_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_MULT_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 579
                self.match(CSharpParser.OP_MULT_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_DIV_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 580
                self.match(CSharpParser.OP_DIV_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_MOD_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 581
                self.match(CSharpParser.OP_MOD_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_AND_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 582
                self.match(CSharpParser.OP_AND_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_OR_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 8)
                self.state = 583
                self.match(CSharpParser.OP_OR_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_XOR_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 9)
                self.state = 584
                self.match(CSharpParser.OP_XOR_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_LEFT_SHIFT_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 585
                self.match(CSharpParser.OP_LEFT_SHIFT_ASSIGNMENT)
                pass
            elif token in [CSharpParser.GT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 586
                self.right_shift_assignment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def null_coalescing_expression(self):
            return self.getTypedRuleContext(CSharpParser.Null_coalescing_expressionContext,0)


        def INTERR(self):
            return self.getToken(CSharpParser.INTERR, 0)

        def throwable_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Throwable_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,i)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_conditional_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_expression" ):
                listener.enterConditional_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_expression" ):
                listener.exitConditional_expression(self)




    def conditional_expression(self):

        localctx = CSharpParser.Conditional_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_conditional_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.null_coalescing_expression()
            self.state = 595
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 590
                self.match(CSharpParser.INTERR)
                self.state = 591
                self.throwable_expression()
                self.state = 592
                self.match(CSharpParser.COLON)
                self.state = 593
                self.throwable_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Null_coalescing_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional_or_expression(self):
            return self.getTypedRuleContext(CSharpParser.Conditional_or_expressionContext,0)


        def OP_COALESCING(self):
            return self.getToken(CSharpParser.OP_COALESCING, 0)

        def null_coalescing_expression(self):
            return self.getTypedRuleContext(CSharpParser.Null_coalescing_expressionContext,0)


        def throw_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throw_expressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_null_coalescing_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNull_coalescing_expression" ):
                listener.enterNull_coalescing_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNull_coalescing_expression" ):
                listener.exitNull_coalescing_expression(self)




    def null_coalescing_expression(self):

        localctx = CSharpParser.Null_coalescing_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_null_coalescing_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.conditional_or_expression()
            self.state = 603
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OP_COALESCING:
                self.state = 598
                self.match(CSharpParser.OP_COALESCING)
                self.state = 601
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                    self.state = 599
                    self.null_coalescing_expression()
                    pass
                elif token in [CSharpParser.THROW]:
                    self.state = 600
                    self.throw_expression()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_or_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional_and_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Conditional_and_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Conditional_and_expressionContext,i)


        def OP_OR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_OR)
            else:
                return self.getToken(CSharpParser.OP_OR, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_conditional_or_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_or_expression" ):
                listener.enterConditional_or_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_or_expression" ):
                listener.exitConditional_or_expression(self)




    def conditional_or_expression(self):

        localctx = CSharpParser.Conditional_or_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_conditional_or_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.conditional_and_expression()
            self.state = 610
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.OP_OR:
                self.state = 606
                self.match(CSharpParser.OP_OR)
                self.state = 607
                self.conditional_and_expression()
                self.state = 612
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_and_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inclusive_or_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Inclusive_or_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Inclusive_or_expressionContext,i)


        def OP_AND(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_AND)
            else:
                return self.getToken(CSharpParser.OP_AND, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_conditional_and_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_and_expression" ):
                listener.enterConditional_and_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_and_expression" ):
                listener.exitConditional_and_expression(self)




    def conditional_and_expression(self):

        localctx = CSharpParser.Conditional_and_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_conditional_and_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
            self.inclusive_or_expression()
            self.state = 618
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.OP_AND:
                self.state = 614
                self.match(CSharpParser.OP_AND)
                self.state = 615
                self.inclusive_or_expression()
                self.state = 620
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inclusive_or_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exclusive_or_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Exclusive_or_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Exclusive_or_expressionContext,i)


        def BITWISE_OR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.BITWISE_OR)
            else:
                return self.getToken(CSharpParser.BITWISE_OR, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_inclusive_or_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclusive_or_expression" ):
                listener.enterInclusive_or_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclusive_or_expression" ):
                listener.exitInclusive_or_expression(self)




    def inclusive_or_expression(self):

        localctx = CSharpParser.Inclusive_or_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_inclusive_or_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.exclusive_or_expression()
            self.state = 626
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.BITWISE_OR:
                self.state = 622
                self.match(CSharpParser.BITWISE_OR)
                self.state = 623
                self.exclusive_or_expression()
                self.state = 628
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exclusive_or_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.And_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.And_expressionContext,i)


        def CARET(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.CARET)
            else:
                return self.getToken(CSharpParser.CARET, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_exclusive_or_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExclusive_or_expression" ):
                listener.enterExclusive_or_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExclusive_or_expression" ):
                listener.exitExclusive_or_expression(self)




    def exclusive_or_expression(self):

        localctx = CSharpParser.Exclusive_or_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exclusive_or_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.and_expression()
            self.state = 634
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 630
                    self.match(CSharpParser.CARET)
                    self.state = 631
                    self.and_expression() 
                self.state = 636
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Equality_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Equality_expressionContext,i)


        def AMP(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.AMP)
            else:
                return self.getToken(CSharpParser.AMP, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_and_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_expression" ):
                listener.enterAnd_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_expression" ):
                listener.exitAnd_expression(self)




    def and_expression(self):

        localctx = CSharpParser.And_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_and_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            self.equality_expression()
            self.state = 642
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 638
                    self.match(CSharpParser.AMP)
                    self.state = 639
                    self.equality_expression() 
                self.state = 644
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Equality_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Relational_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Relational_expressionContext,i)


        def OP_EQ(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_EQ)
            else:
                return self.getToken(CSharpParser.OP_EQ, i)

        def OP_NE(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_NE)
            else:
                return self.getToken(CSharpParser.OP_NE, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_equality_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality_expression" ):
                listener.enterEquality_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality_expression" ):
                listener.exitEquality_expression(self)




    def equality_expression(self):

        localctx = CSharpParser.Equality_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_equality_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            self.relational_expression()
            self.state = 650
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.OP_EQ or _la==CSharpParser.OP_NE:
                self.state = 646
                _la = self._input.LA(1)
                if not(_la==CSharpParser.OP_EQ or _la==CSharpParser.OP_NE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 647
                self.relational_expression()
                self.state = 652
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shift_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Shift_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Shift_expressionContext,i)


        def IS(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.IS)
            else:
                return self.getToken(CSharpParser.IS, i)

        def isType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IsTypeContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IsTypeContext,i)


        def AS(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.AS)
            else:
                return self.getToken(CSharpParser.AS, i)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Type_Context)
            else:
                return self.getTypedRuleContext(CSharpParser.Type_Context,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.LT)
            else:
                return self.getToken(CSharpParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.GT)
            else:
                return self.getToken(CSharpParser.GT, i)

        def OP_LE(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_LE)
            else:
                return self.getToken(CSharpParser.OP_LE, i)

        def OP_GE(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_GE)
            else:
                return self.getToken(CSharpParser.OP_GE, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_relational_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational_expression" ):
                listener.enterRelational_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational_expression" ):
                listener.exitRelational_expression(self)




    def relational_expression(self):

        localctx = CSharpParser.Relational_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_relational_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 653
            self.shift_expression()
            self.state = 662
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.AS or _la==CSharpParser.IS or ((((_la - 146)) & ~0x3f) == 0 and ((1 << (_la - 146)) & ((1 << (CSharpParser.LT - 146)) | (1 << (CSharpParser.GT - 146)) | (1 << (CSharpParser.OP_LE - 146)) | (1 << (CSharpParser.OP_GE - 146)))) != 0):
                self.state = 660
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.LT, CSharpParser.GT, CSharpParser.OP_LE, CSharpParser.OP_GE]:
                    self.state = 654
                    _la = self._input.LA(1)
                    if not(((((_la - 146)) & ~0x3f) == 0 and ((1 << (_la - 146)) & ((1 << (CSharpParser.LT - 146)) | (1 << (CSharpParser.GT - 146)) | (1 << (CSharpParser.OP_LE - 146)) | (1 << (CSharpParser.OP_GE - 146)))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 655
                    self.shift_expression()
                    pass
                elif token in [CSharpParser.IS]:
                    self.state = 656
                    self.match(CSharpParser.IS)
                    self.state = 657
                    self.isType()
                    pass
                elif token in [CSharpParser.AS]:
                    self.state = 658
                    self.match(CSharpParser.AS)
                    self.state = 659
                    self.type_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 664
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Shift_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Additive_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Additive_expressionContext,i)


        def OP_LEFT_SHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_LEFT_SHIFT)
            else:
                return self.getToken(CSharpParser.OP_LEFT_SHIFT, i)

        def right_shift(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Right_shiftContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Right_shiftContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_shift_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShift_expression" ):
                listener.enterShift_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShift_expression" ):
                listener.exitShift_expression(self)




    def shift_expression(self):

        localctx = CSharpParser.Shift_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_shift_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 665
            self.additive_expression()
            self.state = 673
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 668
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CSharpParser.OP_LEFT_SHIFT]:
                        self.state = 666
                        self.match(CSharpParser.OP_LEFT_SHIFT)
                        pass
                    elif token in [CSharpParser.GT]:
                        self.state = 667
                        self.right_shift()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 670
                    self.additive_expression() 
                self.state = 675
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Additive_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Multiplicative_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Multiplicative_expressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.PLUS)
            else:
                return self.getToken(CSharpParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.MINUS)
            else:
                return self.getToken(CSharpParser.MINUS, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_additive_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive_expression" ):
                listener.enterAdditive_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive_expression" ):
                listener.exitAdditive_expression(self)




    def additive_expression(self):

        localctx = CSharpParser.Additive_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_additive_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 676
            self.multiplicative_expression()
            self.state = 681
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 677
                    _la = self._input.LA(1)
                    if not(_la==CSharpParser.PLUS or _la==CSharpParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 678
                    self.multiplicative_expression() 
                self.state = 683
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplicative_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switch_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Switch_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Switch_expressionContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.STAR)
            else:
                return self.getToken(CSharpParser.STAR, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.DIV)
            else:
                return self.getToken(CSharpParser.DIV, i)

        def PERCENT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.PERCENT)
            else:
                return self.getToken(CSharpParser.PERCENT, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_multiplicative_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative_expression" ):
                listener.enterMultiplicative_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative_expression" ):
                listener.exitMultiplicative_expression(self)




    def multiplicative_expression(self):

        localctx = CSharpParser.Multiplicative_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_multiplicative_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 684
            self.switch_expression()
            self.state = 689
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 685
                    _la = self._input.LA(1)
                    if not(((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (CSharpParser.STAR - 137)) | (1 << (CSharpParser.DIV - 137)) | (1 << (CSharpParser.PERCENT - 137)))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 686
                    self.switch_expression() 
                self.state = 691
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def range_expression(self):
            return self.getTypedRuleContext(CSharpParser.Range_expressionContext,0)


        def SWITCH(self):
            return self.getToken(CSharpParser.SWITCH, 0)

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def switch_expression_arms(self):
            return self.getTypedRuleContext(CSharpParser.Switch_expression_armsContext,0)


        def COMMA(self):
            return self.getToken(CSharpParser.COMMA, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_switch_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_expression" ):
                listener.enterSwitch_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_expression" ):
                listener.exitSwitch_expression(self)




    def switch_expression(self):

        localctx = CSharpParser.Switch_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_switch_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 692
            self.range_expression()
            self.state = 702
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.SWITCH:
                self.state = 693
                self.match(CSharpParser.SWITCH)
                self.state = 694
                self.match(CSharpParser.OPEN_BRACE)
                self.state = 699
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)))) != 0):
                    self.state = 695
                    self.switch_expression_arms()
                    self.state = 697
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpParser.COMMA:
                        self.state = 696
                        self.match(CSharpParser.COMMA)




                self.state = 701
                self.match(CSharpParser.CLOSE_BRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_expression_armsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switch_expression_arm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Switch_expression_armContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Switch_expression_armContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_switch_expression_arms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_expression_arms" ):
                listener.enterSwitch_expression_arms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_expression_arms" ):
                listener.exitSwitch_expression_arms(self)




    def switch_expression_arms(self):

        localctx = CSharpParser.Switch_expression_armsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_switch_expression_arms)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 704
            self.switch_expression_arm()
            self.state = 709
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 705
                    self.match(CSharpParser.COMMA)
                    self.state = 706
                    self.switch_expression_arm() 
                self.state = 711
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_expression_armContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def case_guard(self):
            return self.getTypedRuleContext(CSharpParser.Case_guardContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_switch_expression_arm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_expression_arm" ):
                listener.enterSwitch_expression_arm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_expression_arm" ):
                listener.exitSwitch_expression_arm(self)




    def switch_expression_arm(self):

        localctx = CSharpParser.Switch_expression_armContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_switch_expression_arm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712
            self.expression()
            self.state = 714
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHEN:
                self.state = 713
                self.case_guard()


            self.state = 716
            self.right_arrow()
            self.state = 717
            self.throwable_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Unary_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Unary_expressionContext,i)


        def OP_RANGE(self):
            return self.getToken(CSharpParser.OP_RANGE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_range_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_expression" ):
                listener.enterRange_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_expression" ):
                listener.exitRange_expression(self)




    def range_expression(self):

        localctx = CSharpParser.Range_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_range_expression)
        self._la = 0 # Token type
        try:
            self.state = 727
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 719
                self.unary_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 721
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)))) != 0):
                    self.state = 720
                    self.unary_expression()


                self.state = 723
                self.match(CSharpParser.OP_RANGE)
                self.state = 725
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 724
                    self.unary_expression()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expression(self):
            return self.getTypedRuleContext(CSharpParser.Primary_expressionContext,0)


        def PLUS(self):
            return self.getToken(CSharpParser.PLUS, 0)

        def unary_expression(self):
            return self.getTypedRuleContext(CSharpParser.Unary_expressionContext,0)


        def MINUS(self):
            return self.getToken(CSharpParser.MINUS, 0)

        def BANG(self):
            return self.getToken(CSharpParser.BANG, 0)

        def TILDE(self):
            return self.getToken(CSharpParser.TILDE, 0)

        def OP_INC(self):
            return self.getToken(CSharpParser.OP_INC, 0)

        def OP_DEC(self):
            return self.getToken(CSharpParser.OP_DEC, 0)

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def AWAIT(self):
            return self.getToken(CSharpParser.AWAIT, 0)

        def AMP(self):
            return self.getToken(CSharpParser.AMP, 0)

        def STAR(self):
            return self.getToken(CSharpParser.STAR, 0)

        def CARET(self):
            return self.getToken(CSharpParser.CARET, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_unary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_expression" ):
                listener.enterUnary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_expression" ):
                listener.exitUnary_expression(self)




    def unary_expression(self):

        localctx = CSharpParser.Unary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_unary_expression)
        try:
            self.state = 755
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 729
                self.primary_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 730
                self.match(CSharpParser.PLUS)
                self.state = 731
                self.unary_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 732
                self.match(CSharpParser.MINUS)
                self.state = 733
                self.unary_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 734
                self.match(CSharpParser.BANG)
                self.state = 735
                self.unary_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 736
                self.match(CSharpParser.TILDE)
                self.state = 737
                self.unary_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 738
                self.match(CSharpParser.OP_INC)
                self.state = 739
                self.unary_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 740
                self.match(CSharpParser.OP_DEC)
                self.state = 741
                self.unary_expression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 742
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 743
                self.type_()
                self.state = 744
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 745
                self.unary_expression()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 747
                self.match(CSharpParser.AWAIT)
                self.state = 748
                self.unary_expression()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 749
                self.match(CSharpParser.AMP)
                self.state = 750
                self.unary_expression()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 751
                self.match(CSharpParser.STAR)
                self.state = 752
                self.unary_expression()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 753
                self.match(CSharpParser.CARET)
                self.state = 754
                self.unary_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pe = None # Primary_expression_startContext

        def primary_expression_start(self):
            return self.getTypedRuleContext(CSharpParser.Primary_expression_startContext,0)


        def BANG(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.BANG)
            else:
                return self.getToken(CSharpParser.BANG, i)

        def bracket_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Bracket_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Bracket_expressionContext,i)


        def member_access(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Member_accessContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Member_accessContext,i)


        def method_invocation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Method_invocationContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Method_invocationContext,i)


        def OP_INC(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_INC)
            else:
                return self.getToken(CSharpParser.OP_INC, i)

        def OP_DEC(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_DEC)
            else:
                return self.getToken(CSharpParser.OP_DEC, i)

        def OP_PTR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_PTR)
            else:
                return self.getToken(CSharpParser.OP_PTR, i)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_primary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expression" ):
                listener.enterPrimary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expression" ):
                listener.exitPrimary_expression(self)




    def primary_expression(self):

        localctx = CSharpParser.Primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_primary_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 757
            localctx.pe = self.primary_expression_start()
            self.state = 759
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 758
                self.match(CSharpParser.BANG)


            self.state = 764
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 761
                    self.bracket_expression() 
                self.state = 766
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

            self.state = 768
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 767
                self.match(CSharpParser.BANG)


            self.state = 792
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 776
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CSharpParser.DOT, CSharpParser.INTERR]:
                        self.state = 770
                        self.member_access()
                        pass
                    elif token in [CSharpParser.OPEN_PARENS]:
                        self.state = 771
                        self.method_invocation()
                        pass
                    elif token in [CSharpParser.OP_INC]:
                        self.state = 772
                        self.match(CSharpParser.OP_INC)
                        pass
                    elif token in [CSharpParser.OP_DEC]:
                        self.state = 773
                        self.match(CSharpParser.OP_DEC)
                        pass
                    elif token in [CSharpParser.OP_PTR]:
                        self.state = 774
                        self.match(CSharpParser.OP_PTR)
                        self.state = 775
                        self.identifier()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 779
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                    if la_ == 1:
                        self.state = 778
                        self.match(CSharpParser.BANG)


                    self.state = 784
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 781
                            self.bracket_expression() 
                        self.state = 786
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

                    self.state = 788
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                    if la_ == 1:
                        self.state = 787
                        self.match(CSharpParser.BANG)

             
                self.state = 794
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_expression_startContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSharpParser.RULE_primary_expression_start

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LiteralAccessExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LITERAL_ACCESS(self):
            return self.getToken(CSharpParser.LITERAL_ACCESS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralAccessExpression" ):
                listener.enterLiteralAccessExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralAccessExpression" ):
                listener.exitLiteralAccessExpression(self)


    class DefaultValueExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEFAULT(self):
            return self.getToken(CSharpParser.DEFAULT, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultValueExpression" ):
                listener.enterDefaultValueExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultValueExpression" ):
                listener.exitDefaultValueExpression(self)


    class BaseAccessExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BASE(self):
            return self.getToken(CSharpParser.BASE, 0)
        def DOT(self):
            return self.getToken(CSharpParser.DOT, 0)
        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)
        def expression_list(self):
            return self.getTypedRuleContext(CSharpParser.Expression_listContext,0)

        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)
        def type_argument_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_argument_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseAccessExpression" ):
                listener.enterBaseAccessExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseAccessExpression" ):
                listener.exitBaseAccessExpression(self)


    class SizeofExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIZEOF(self):
            return self.getToken(CSharpParser.SIZEOF, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizeofExpression" ):
                listener.enterSizeofExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizeofExpression" ):
                listener.exitSizeofExpression(self)


    class ParenthesisExpressionsContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesisExpressions" ):
                listener.enterParenthesisExpressions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesisExpressions" ):
                listener.exitParenthesisExpressions(self)


    class ThisReferenceExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def THIS(self):
            return self.getToken(CSharpParser.THIS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThisReferenceExpression" ):
                listener.enterThisReferenceExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThisReferenceExpression" ):
                listener.exitThisReferenceExpression(self)


    class ObjectCreationExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(CSharpParser.NEW, 0)
        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)

        def anonymous_object_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Anonymous_object_initializerContext,0)

        def rank_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Rank_specifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Rank_specifierContext,i)

        def array_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Array_initializerContext,0)

        def object_creation_expression(self):
            return self.getTypedRuleContext(CSharpParser.Object_creation_expressionContext,0)

        def object_or_collection_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Object_or_collection_initializerContext,0)

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)
        def expression_list(self):
            return self.getTypedRuleContext(CSharpParser.Expression_listContext,0)

        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectCreationExpression" ):
                listener.enterObjectCreationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectCreationExpression" ):
                listener.exitObjectCreationExpression(self)


    class AnonymousMethodExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DELEGATE(self):
            return self.getToken(CSharpParser.DELEGATE, 0)
        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)

        def ASYNC(self):
            return self.getToken(CSharpParser.ASYNC, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def explicit_anonymous_function_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Explicit_anonymous_function_parameter_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnonymousMethodExpression" ):
                listener.enterAnonymousMethodExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnonymousMethodExpression" ):
                listener.exitAnonymousMethodExpression(self)


    class TypeofExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPEOF(self):
            return self.getToken(CSharpParser.TYPEOF, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def unbound_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Unbound_type_nameContext,0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)

        def VOID(self):
            return self.getToken(CSharpParser.VOID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeofExpression" ):
                listener.enterTypeofExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeofExpression" ):
                listener.exitTypeofExpression(self)


    class TupleExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ArgumentContext,i)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTupleExpression" ):
                listener.enterTupleExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTupleExpression" ):
                listener.exitTupleExpression(self)


    class UncheckedExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UNCHECKED(self):
            return self.getToken(CSharpParser.UNCHECKED, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUncheckedExpression" ):
                listener.enterUncheckedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUncheckedExpression" ):
                listener.exitUncheckedExpression(self)


    class SimpleNameExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)

        def type_argument_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_argument_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleNameExpression" ):
                listener.enterSimpleNameExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleNameExpression" ):
                listener.exitSimpleNameExpression(self)


    class MemberAccessExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predefined_type(self):
            return self.getTypedRuleContext(CSharpParser.Predefined_typeContext,0)

        def qualified_alias_member(self):
            return self.getTypedRuleContext(CSharpParser.Qualified_alias_memberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberAccessExpression" ):
                listener.enterMemberAccessExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberAccessExpression" ):
                listener.exitMemberAccessExpression(self)


    class CheckedExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHECKED(self):
            return self.getToken(CSharpParser.CHECKED, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCheckedExpression" ):
                listener.enterCheckedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCheckedExpression" ):
                listener.exitCheckedExpression(self)


    class LiteralExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(CSharpParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpression" ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpression" ):
                listener.exitLiteralExpression(self)


    class NameofExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAMEOF(self):
            return self.getToken(CSharpParser.NAMEOF, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.DOT)
            else:
                return self.getToken(CSharpParser.DOT, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameofExpression" ):
                listener.enterNameofExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameofExpression" ):
                listener.exitNameofExpression(self)



    def primary_expression_start(self):

        localctx = CSharpParser.Primary_expression_startContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_primary_expression_start)
        self._la = 0 # Token type
        try:
            self.state = 916
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                localctx = CSharpParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 795
                self.literal()
                pass

            elif la_ == 2:
                localctx = CSharpParser.SimpleNameExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 796
                self.identifier()
                self.state = 798
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                if la_ == 1:
                    self.state = 797
                    self.type_argument_list()


                pass

            elif la_ == 3:
                localctx = CSharpParser.ParenthesisExpressionsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 800
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 801
                self.expression()
                self.state = 802
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 4:
                localctx = CSharpParser.MemberAccessExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 804
                self.predefined_type()
                pass

            elif la_ == 5:
                localctx = CSharpParser.MemberAccessExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 805
                self.qualified_alias_member()
                pass

            elif la_ == 6:
                localctx = CSharpParser.LiteralAccessExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 806
                self.match(CSharpParser.LITERAL_ACCESS)
                pass

            elif la_ == 7:
                localctx = CSharpParser.ThisReferenceExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 807
                self.match(CSharpParser.THIS)
                pass

            elif la_ == 8:
                localctx = CSharpParser.BaseAccessExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 808
                self.match(CSharpParser.BASE)
                self.state = 818
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.DOT]:
                    self.state = 809
                    self.match(CSharpParser.DOT)
                    self.state = 810
                    self.identifier()
                    self.state = 812
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                    if la_ == 1:
                        self.state = 811
                        self.type_argument_list()


                    pass
                elif token in [CSharpParser.OPEN_BRACKET]:
                    self.state = 814
                    self.match(CSharpParser.OPEN_BRACKET)
                    self.state = 815
                    self.expression_list()
                    self.state = 816
                    self.match(CSharpParser.CLOSE_BRACKET)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 9:
                localctx = CSharpParser.ObjectCreationExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 820
                self.match(CSharpParser.NEW)
                self.state = 849
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.DECIMAL, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.STRING, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.VOID, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.OPEN_PARENS]:
                    self.state = 821
                    self.type_()
                    self.state = 843
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                    if la_ == 1:
                        self.state = 822
                        self.object_creation_expression()
                        pass

                    elif la_ == 2:
                        self.state = 823
                        self.object_or_collection_initializer()
                        pass

                    elif la_ == 3:
                        self.state = 824
                        self.match(CSharpParser.OPEN_BRACKET)
                        self.state = 825
                        self.expression_list()
                        self.state = 826
                        self.match(CSharpParser.CLOSE_BRACKET)
                        self.state = 830
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 827
                                self.rank_specifier() 
                            self.state = 832
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

                        self.state = 834
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==CSharpParser.OPEN_BRACE:
                            self.state = 833
                            self.array_initializer()


                        pass

                    elif la_ == 4:
                        self.state = 837 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 836
                            self.rank_specifier()
                            self.state = 839 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==CSharpParser.OPEN_BRACKET):
                                break

                        self.state = 841
                        self.array_initializer()
                        pass


                    pass
                elif token in [CSharpParser.OPEN_BRACE]:
                    self.state = 845
                    self.anonymous_object_initializer()
                    pass
                elif token in [CSharpParser.OPEN_BRACKET]:
                    self.state = 846
                    self.rank_specifier()
                    self.state = 847
                    self.array_initializer()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 10:
                localctx = CSharpParser.TupleExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 851
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 852
                self.argument()
                self.state = 855 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 853
                    self.match(CSharpParser.COMMA)
                    self.state = 854
                    self.argument()
                    self.state = 857 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==CSharpParser.COMMA):
                        break

                self.state = 859
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 11:
                localctx = CSharpParser.TypeofExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 861
                self.match(CSharpParser.TYPEOF)
                self.state = 862
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 866
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
                if la_ == 1:
                    self.state = 863
                    self.unbound_type_name()
                    pass

                elif la_ == 2:
                    self.state = 864
                    self.type_()
                    pass

                elif la_ == 3:
                    self.state = 865
                    self.match(CSharpParser.VOID)
                    pass


                self.state = 868
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 12:
                localctx = CSharpParser.CheckedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 869
                self.match(CSharpParser.CHECKED)
                self.state = 870
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 871
                self.expression()
                self.state = 872
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 13:
                localctx = CSharpParser.UncheckedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 874
                self.match(CSharpParser.UNCHECKED)
                self.state = 875
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 876
                self.expression()
                self.state = 877
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 14:
                localctx = CSharpParser.DefaultValueExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 879
                self.match(CSharpParser.DEFAULT)
                self.state = 884
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
                if la_ == 1:
                    self.state = 880
                    self.match(CSharpParser.OPEN_PARENS)
                    self.state = 881
                    self.type_()
                    self.state = 882
                    self.match(CSharpParser.CLOSE_PARENS)


                pass

            elif la_ == 15:
                localctx = CSharpParser.AnonymousMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 887
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.ASYNC:
                    self.state = 886
                    self.match(CSharpParser.ASYNC)


                self.state = 889
                self.match(CSharpParser.DELEGATE)
                self.state = 895
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.OPEN_PARENS:
                    self.state = 890
                    self.match(CSharpParser.OPEN_PARENS)
                    self.state = 892
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (CSharpParser.ADD - 10)) | (1 << (CSharpParser.ALIAS - 10)) | (1 << (CSharpParser.ARGLIST - 10)) | (1 << (CSharpParser.ASCENDING - 10)) | (1 << (CSharpParser.ASYNC - 10)) | (1 << (CSharpParser.AWAIT - 10)) | (1 << (CSharpParser.BOOL - 10)) | (1 << (CSharpParser.BY - 10)) | (1 << (CSharpParser.BYTE - 10)) | (1 << (CSharpParser.CHAR - 10)) | (1 << (CSharpParser.DECIMAL - 10)) | (1 << (CSharpParser.DESCENDING - 10)) | (1 << (CSharpParser.DOUBLE - 10)) | (1 << (CSharpParser.DYNAMIC - 10)) | (1 << (CSharpParser.EQUALS - 10)) | (1 << (CSharpParser.FLOAT - 10)) | (1 << (CSharpParser.FROM - 10)) | (1 << (CSharpParser.GET - 10)) | (1 << (CSharpParser.GROUP - 10)) | (1 << (CSharpParser.IN - 10)) | (1 << (CSharpParser.INT - 10)) | (1 << (CSharpParser.INTO - 10)) | (1 << (CSharpParser.JOIN - 10)) | (1 << (CSharpParser.LET - 10)) | (1 << (CSharpParser.LONG - 10)) | (1 << (CSharpParser.NAMEOF - 10)) | (1 << (CSharpParser.OBJECT - 10)) | (1 << (CSharpParser.ON - 10)) | (1 << (CSharpParser.ORDERBY - 10)) | (1 << (CSharpParser.OUT - 10)))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CSharpParser.PARTIAL - 75)) | (1 << (CSharpParser.REF - 75)) | (1 << (CSharpParser.REMOVE - 75)) | (1 << (CSharpParser.SBYTE - 75)) | (1 << (CSharpParser.SELECT - 75)) | (1 << (CSharpParser.SET - 75)) | (1 << (CSharpParser.SHORT - 75)) | (1 << (CSharpParser.STRING - 75)) | (1 << (CSharpParser.UINT - 75)) | (1 << (CSharpParser.ULONG - 75)) | (1 << (CSharpParser.UNMANAGED - 75)) | (1 << (CSharpParser.USHORT - 75)) | (1 << (CSharpParser.VAR - 75)) | (1 << (CSharpParser.VOID - 75)) | (1 << (CSharpParser.WHEN - 75)) | (1 << (CSharpParser.WHERE - 75)) | (1 << (CSharpParser.YIELD - 75)) | (1 << (CSharpParser.IDENTIFIER - 75)) | (1 << (CSharpParser.OPEN_PARENS - 75)))) != 0):
                        self.state = 891
                        self.explicit_anonymous_function_parameter_list()


                    self.state = 894
                    self.match(CSharpParser.CLOSE_PARENS)


                self.state = 897
                self.block()
                pass

            elif la_ == 16:
                localctx = CSharpParser.SizeofExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 898
                self.match(CSharpParser.SIZEOF)
                self.state = 899
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 900
                self.type_()
                self.state = 901
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 17:
                localctx = CSharpParser.NameofExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 903
                self.match(CSharpParser.NAMEOF)
                self.state = 904
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 910
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,72,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 905
                        self.identifier()
                        self.state = 906
                        self.match(CSharpParser.DOT) 
                    self.state = 912
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,72,self._ctx)

                self.state = 913
                self.identifier()
                self.state = 914
                self.match(CSharpParser.CLOSE_PARENS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Throwable_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def throw_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throw_expressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_throwable_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowable_expression" ):
                listener.enterThrowable_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowable_expression" ):
                listener.exitThrowable_expression(self)




    def throwable_expression(self):

        localctx = CSharpParser.Throwable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_throwable_expression)
        try:
            self.state = 920
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 918
                self.expression()
                pass
            elif token in [CSharpParser.THROW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 919
                self.throw_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Throw_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THROW(self):
            return self.getToken(CSharpParser.THROW, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_throw_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrow_expression" ):
                listener.enterThrow_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrow_expression" ):
                listener.exitThrow_expression(self)




    def throw_expression(self):

        localctx = CSharpParser.Throw_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_throw_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 922
            self.match(CSharpParser.THROW)
            self.state = 923
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(CSharpParser.DOT, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def INTERR(self):
            return self.getToken(CSharpParser.INTERR, 0)

        def type_argument_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_argument_listContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_member_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_access" ):
                listener.enterMember_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_access" ):
                listener.exitMember_access(self)




    def member_access(self):

        localctx = CSharpParser.Member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_member_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 926
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.INTERR:
                self.state = 925
                self.match(CSharpParser.INTERR)


            self.state = 928
            self.match(CSharpParser.DOT)
            self.state = 929
            self.identifier()
            self.state = 931
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.state = 930
                self.type_argument_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bracket_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def indexer_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Indexer_argumentContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Indexer_argumentContext,i)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def INTERR(self):
            return self.getToken(CSharpParser.INTERR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_bracket_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracket_expression" ):
                listener.enterBracket_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracket_expression" ):
                listener.exitBracket_expression(self)




    def bracket_expression(self):

        localctx = CSharpParser.Bracket_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_bracket_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 934
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.INTERR:
                self.state = 933
                self.match(CSharpParser.INTERR)


            self.state = 936
            self.match(CSharpParser.OPEN_BRACKET)
            self.state = 937
            self.indexer_argument()
            self.state = 942
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 938
                self.match(CSharpParser.COMMA)
                self.state = 939
                self.indexer_argument()
                self.state = 944
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 945
            self.match(CSharpParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexer_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_indexer_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexer_argument" ):
                listener.enterIndexer_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexer_argument" ):
                listener.exitIndexer_argument(self)




    def indexer_argument(self):

        localctx = CSharpParser.Indexer_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_indexer_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 950
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.state = 947
                self.identifier()
                self.state = 948
                self.match(CSharpParser.COLON)


            self.state = 952
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predefined_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(CSharpParser.BOOL, 0)

        def BYTE(self):
            return self.getToken(CSharpParser.BYTE, 0)

        def CHAR(self):
            return self.getToken(CSharpParser.CHAR, 0)

        def DECIMAL(self):
            return self.getToken(CSharpParser.DECIMAL, 0)

        def DOUBLE(self):
            return self.getToken(CSharpParser.DOUBLE, 0)

        def FLOAT(self):
            return self.getToken(CSharpParser.FLOAT, 0)

        def INT(self):
            return self.getToken(CSharpParser.INT, 0)

        def LONG(self):
            return self.getToken(CSharpParser.LONG, 0)

        def OBJECT(self):
            return self.getToken(CSharpParser.OBJECT, 0)

        def SBYTE(self):
            return self.getToken(CSharpParser.SBYTE, 0)

        def SHORT(self):
            return self.getToken(CSharpParser.SHORT, 0)

        def STRING(self):
            return self.getToken(CSharpParser.STRING, 0)

        def UINT(self):
            return self.getToken(CSharpParser.UINT, 0)

        def ULONG(self):
            return self.getToken(CSharpParser.ULONG, 0)

        def USHORT(self):
            return self.getToken(CSharpParser.USHORT, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_predefined_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredefined_type" ):
                listener.enterPredefined_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredefined_type" ):
                listener.exitPredefined_type(self)




    def predefined_type(self):

        localctx = CSharpParser.Predefined_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_predefined_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 954
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.BOOL) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.INT) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (CSharpParser.OBJECT - 68)) | (1 << (CSharpParser.SBYTE - 68)) | (1 << (CSharpParser.SHORT - 68)) | (1 << (CSharpParser.STRING - 68)) | (1 << (CSharpParser.UINT - 68)) | (1 << (CSharpParser.ULONG - 68)) | (1 << (CSharpParser.USHORT - 68)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)




    def expression_list(self):

        localctx = CSharpParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 956
            self.expression()
            self.state = 961
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 957
                self.match(CSharpParser.COMMA)
                self.state = 958
                self.expression()
                self.state = 963
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_or_collection_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Object_initializerContext,0)


        def collection_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Collection_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_object_or_collection_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_or_collection_initializer" ):
                listener.enterObject_or_collection_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_or_collection_initializer" ):
                listener.exitObject_or_collection_initializer(self)




    def object_or_collection_initializer(self):

        localctx = CSharpParser.Object_or_collection_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_object_or_collection_initializer)
        try:
            self.state = 966
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 964
                self.object_initializer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 965
                self.collection_initializer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def member_initializer_list(self):
            return self.getTypedRuleContext(CSharpParser.Member_initializer_listContext,0)


        def COMMA(self):
            return self.getToken(CSharpParser.COMMA, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_object_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_initializer" ):
                listener.enterObject_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_initializer" ):
                listener.exitObject_initializer(self)




    def object_initializer(self):

        localctx = CSharpParser.Object_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_object_initializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 968
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 973
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BY) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.OPEN_BRACKET - 64)))) != 0):
                self.state = 969
                self.member_initializer_list()
                self.state = 971
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.COMMA:
                    self.state = 970
                    self.match(CSharpParser.COMMA)




            self.state = 975
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_initializer_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_initializer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Member_initializerContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Member_initializerContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_member_initializer_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_initializer_list" ):
                listener.enterMember_initializer_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_initializer_list" ):
                listener.exitMember_initializer_list(self)




    def member_initializer_list(self):

        localctx = CSharpParser.Member_initializer_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_member_initializer_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 977
            self.member_initializer()
            self.state = 982
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,84,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 978
                    self.match(CSharpParser.COMMA)
                    self.state = 979
                    self.member_initializer() 
                self.state = 984
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,84,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def initializer_value(self):
            return self.getTypedRuleContext(CSharpParser.Initializer_valueContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_member_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_initializer" ):
                listener.enterMember_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_initializer" ):
                listener.exitMember_initializer(self)




    def member_initializer(self):

        localctx = CSharpParser.Member_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_member_initializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 990
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BY, CSharpParser.DESCENDING, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.NAMEOF, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.UNMANAGED, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER]:
                self.state = 985
                self.identifier()
                pass
            elif token in [CSharpParser.OPEN_BRACKET]:
                self.state = 986
                self.match(CSharpParser.OPEN_BRACKET)
                self.state = 987
                self.expression()
                self.state = 988
                self.match(CSharpParser.CLOSE_BRACKET)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 992
            self.match(CSharpParser.ASSIGNMENT)
            self.state = 993
            self.initializer_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Initializer_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def object_or_collection_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Object_or_collection_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_initializer_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializer_value" ):
                listener.enterInitializer_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializer_value" ):
                listener.exitInitializer_value(self)




    def initializer_value(self):

        localctx = CSharpParser.Initializer_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_initializer_value)
        try:
            self.state = 997
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 995
                self.expression()
                pass
            elif token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 996
                self.object_or_collection_initializer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Collection_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def element_initializer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Element_initializerContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Element_initializerContext,i)


        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_collection_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCollection_initializer" ):
                listener.enterCollection_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCollection_initializer" ):
                listener.exitCollection_initializer(self)




    def collection_initializer(self):

        localctx = CSharpParser.Collection_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_collection_initializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 999
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 1000
            self.element_initializer()
            self.state = 1005
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,87,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1001
                    self.match(CSharpParser.COMMA)
                    self.state = 1002
                    self.element_initializer() 
                self.state = 1007
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,87,self._ctx)

            self.state = 1009
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COMMA:
                self.state = 1008
                self.match(CSharpParser.COMMA)


            self.state = 1011
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_assignment_expression(self):
            return self.getTypedRuleContext(CSharpParser.Non_assignment_expressionContext,0)


        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(CSharpParser.Expression_listContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_element_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement_initializer" ):
                listener.enterElement_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement_initializer" ):
                listener.exitElement_initializer(self)




    def element_initializer(self):

        localctx = CSharpParser.Element_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_element_initializer)
        try:
            self.state = 1018
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1013
                self.non_assignment_expression()
                pass
            elif token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1014
                self.match(CSharpParser.OPEN_BRACE)
                self.state = 1015
                self.expression_list()
                self.state = 1016
                self.match(CSharpParser.CLOSE_BRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Anonymous_object_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def member_declarator_list(self):
            return self.getTypedRuleContext(CSharpParser.Member_declarator_listContext,0)


        def COMMA(self):
            return self.getToken(CSharpParser.COMMA, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_anonymous_object_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnonymous_object_initializer" ):
                listener.enterAnonymous_object_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnonymous_object_initializer" ):
                listener.exitAnonymous_object_initializer(self)




    def anonymous_object_initializer(self):

        localctx = CSharpParser.Anonymous_object_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_anonymous_object_initializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1020
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 1025
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (CSharpParser.ADD - 10)) | (1 << (CSharpParser.ALIAS - 10)) | (1 << (CSharpParser.ARGLIST - 10)) | (1 << (CSharpParser.ASCENDING - 10)) | (1 << (CSharpParser.ASYNC - 10)) | (1 << (CSharpParser.AWAIT - 10)) | (1 << (CSharpParser.BASE - 10)) | (1 << (CSharpParser.BOOL - 10)) | (1 << (CSharpParser.BY - 10)) | (1 << (CSharpParser.BYTE - 10)) | (1 << (CSharpParser.CHAR - 10)) | (1 << (CSharpParser.CHECKED - 10)) | (1 << (CSharpParser.DECIMAL - 10)) | (1 << (CSharpParser.DEFAULT - 10)) | (1 << (CSharpParser.DELEGATE - 10)) | (1 << (CSharpParser.DESCENDING - 10)) | (1 << (CSharpParser.DOUBLE - 10)) | (1 << (CSharpParser.DYNAMIC - 10)) | (1 << (CSharpParser.EQUALS - 10)) | (1 << (CSharpParser.FALSE - 10)) | (1 << (CSharpParser.FLOAT - 10)) | (1 << (CSharpParser.FROM - 10)) | (1 << (CSharpParser.GET - 10)) | (1 << (CSharpParser.GROUP - 10)) | (1 << (CSharpParser.INT - 10)) | (1 << (CSharpParser.INTO - 10)) | (1 << (CSharpParser.JOIN - 10)) | (1 << (CSharpParser.LET - 10)) | (1 << (CSharpParser.LONG - 10)) | (1 << (CSharpParser.NAMEOF - 10)) | (1 << (CSharpParser.NEW - 10)) | (1 << (CSharpParser.NULL - 10)) | (1 << (CSharpParser.OBJECT - 10)) | (1 << (CSharpParser.ON - 10)) | (1 << (CSharpParser.ORDERBY - 10)))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CSharpParser.PARTIAL - 75)) | (1 << (CSharpParser.REMOVE - 75)) | (1 << (CSharpParser.SBYTE - 75)) | (1 << (CSharpParser.SELECT - 75)) | (1 << (CSharpParser.SET - 75)) | (1 << (CSharpParser.SHORT - 75)) | (1 << (CSharpParser.SIZEOF - 75)) | (1 << (CSharpParser.STRING - 75)) | (1 << (CSharpParser.THIS - 75)) | (1 << (CSharpParser.TRUE - 75)) | (1 << (CSharpParser.TYPEOF - 75)) | (1 << (CSharpParser.UINT - 75)) | (1 << (CSharpParser.ULONG - 75)) | (1 << (CSharpParser.UNCHECKED - 75)) | (1 << (CSharpParser.UNMANAGED - 75)) | (1 << (CSharpParser.USHORT - 75)) | (1 << (CSharpParser.VAR - 75)) | (1 << (CSharpParser.WHEN - 75)) | (1 << (CSharpParser.WHERE - 75)) | (1 << (CSharpParser.YIELD - 75)) | (1 << (CSharpParser.IDENTIFIER - 75)) | (1 << (CSharpParser.LITERAL_ACCESS - 75)) | (1 << (CSharpParser.INTEGER_LITERAL - 75)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 75)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 75)) | (1 << (CSharpParser.REAL_LITERAL - 75)) | (1 << (CSharpParser.CHARACTER_LITERAL - 75)) | (1 << (CSharpParser.REGULAR_STRING - 75)) | (1 << (CSharpParser.VERBATIUM_STRING - 75)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 75)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 75)) | (1 << (CSharpParser.OPEN_PARENS - 75)))) != 0):
                self.state = 1021
                self.member_declarator_list()
                self.state = 1023
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.COMMA:
                    self.state = 1022
                    self.match(CSharpParser.COMMA)




            self.state = 1027
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_declarator_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Member_declaratorContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Member_declaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_member_declarator_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_declarator_list" ):
                listener.enterMember_declarator_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_declarator_list" ):
                listener.exitMember_declarator_list(self)




    def member_declarator_list(self):

        localctx = CSharpParser.Member_declarator_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_member_declarator_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1029
            self.member_declarator()
            self.state = 1034
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,92,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1030
                    self.match(CSharpParser.COMMA)
                    self.state = 1031
                    self.member_declarator() 
                self.state = 1036
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,92,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_declaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expression(self):
            return self.getTypedRuleContext(CSharpParser.Primary_expressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_member_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_declarator" ):
                listener.enterMember_declarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_declarator" ):
                listener.exitMember_declarator(self)




    def member_declarator(self):

        localctx = CSharpParser.Member_declaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_member_declarator)
        try:
            self.state = 1042
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1037
                self.primary_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1038
                self.identifier()
                self.state = 1039
                self.match(CSharpParser.ASSIGNMENT)
                self.state = 1040
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unbound_type_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def DOUBLE_COLON(self):
            return self.getToken(CSharpParser.DOUBLE_COLON, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.DOT)
            else:
                return self.getToken(CSharpParser.DOT, i)

        def generic_dimension_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Generic_dimension_specifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Generic_dimension_specifierContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_unbound_type_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnbound_type_name" ):
                listener.enterUnbound_type_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnbound_type_name" ):
                listener.exitUnbound_type_name(self)




    def unbound_type_name(self):

        localctx = CSharpParser.Unbound_type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_unbound_type_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1044
            self.identifier()
            self.state = 1053
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.CLOSE_PARENS, CSharpParser.DOT, CSharpParser.LT]:
                self.state = 1046
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.LT:
                    self.state = 1045
                    self.generic_dimension_specifier()


                pass
            elif token in [CSharpParser.DOUBLE_COLON]:
                self.state = 1048
                self.match(CSharpParser.DOUBLE_COLON)
                self.state = 1049
                self.identifier()
                self.state = 1051
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.LT:
                    self.state = 1050
                    self.generic_dimension_specifier()


                pass
            else:
                raise NoViableAltException(self)

            self.state = 1062
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.DOT:
                self.state = 1055
                self.match(CSharpParser.DOT)
                self.state = 1056
                self.identifier()
                self.state = 1058
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.LT:
                    self.state = 1057
                    self.generic_dimension_specifier()


                self.state = 1064
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Generic_dimension_specifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(CSharpParser.LT, 0)

        def GT(self):
            return self.getToken(CSharpParser.GT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_generic_dimension_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneric_dimension_specifier" ):
                listener.enterGeneric_dimension_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneric_dimension_specifier" ):
                listener.exitGeneric_dimension_specifier(self)




    def generic_dimension_specifier(self):

        localctx = CSharpParser.Generic_dimension_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_generic_dimension_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1065
            self.match(CSharpParser.LT)
            self.state = 1069
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1066
                self.match(CSharpParser.COMMA)
                self.state = 1071
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1072
            self.match(CSharpParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IsTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def base_type(self):
            return self.getTypedRuleContext(CSharpParser.Base_typeContext,0)


        def rank_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Rank_specifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Rank_specifierContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.STAR)
            else:
                return self.getToken(CSharpParser.STAR, i)

        def INTERR(self):
            return self.getToken(CSharpParser.INTERR, 0)

        def isTypePatternArms(self):
            return self.getTypedRuleContext(CSharpParser.IsTypePatternArmsContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_isType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsType" ):
                listener.enterIsType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsType" ):
                listener.exitIsType(self)




    def isType(self):

        localctx = CSharpParser.IsTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_isType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1074
            self.base_type()
            self.state = 1079
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,101,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1077
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CSharpParser.OPEN_BRACKET]:
                        self.state = 1075
                        self.rank_specifier()
                        pass
                    elif token in [CSharpParser.STAR]:
                        self.state = 1076
                        self.match(CSharpParser.STAR)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 1081
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,101,self._ctx)

            self.state = 1083
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
            if la_ == 1:
                self.state = 1082
                self.match(CSharpParser.INTERR)


            self.state = 1086
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACE:
                self.state = 1085
                self.isTypePatternArms()


            self.state = 1089
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,104,self._ctx)
            if la_ == 1:
                self.state = 1088
                self.identifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IsTypePatternArmsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def isTypePatternArm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IsTypePatternArmContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IsTypePatternArmContext,i)


        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_isTypePatternArms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsTypePatternArms" ):
                listener.enterIsTypePatternArms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsTypePatternArms" ):
                listener.exitIsTypePatternArms(self)




    def isTypePatternArms(self):

        localctx = CSharpParser.IsTypePatternArmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_isTypePatternArms)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1091
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 1092
            self.isTypePatternArm()
            self.state = 1097
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1093
                self.match(CSharpParser.COMMA)
                self.state = 1094
                self.isTypePatternArm()
                self.state = 1099
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1100
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IsTypePatternArmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_isTypePatternArm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsTypePatternArm" ):
                listener.enterIsTypePatternArm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsTypePatternArm" ):
                listener.exitIsTypePatternArm(self)




    def isTypePatternArm(self):

        localctx = CSharpParser.IsTypePatternArmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_isTypePatternArm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1102
            self.identifier()
            self.state = 1103
            self.match(CSharpParser.COLON)
            self.state = 1104
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lambda_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def anonymous_function_signature(self):
            return self.getTypedRuleContext(CSharpParser.Anonymous_function_signatureContext,0)


        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def anonymous_function_body(self):
            return self.getTypedRuleContext(CSharpParser.Anonymous_function_bodyContext,0)


        def ASYNC(self):
            return self.getToken(CSharpParser.ASYNC, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_lambda_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambda_expression" ):
                listener.enterLambda_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambda_expression" ):
                listener.exitLambda_expression(self)




    def lambda_expression(self):

        localctx = CSharpParser.Lambda_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_lambda_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,106,self._ctx)
            if la_ == 1:
                self.state = 1106
                self.match(CSharpParser.ASYNC)


            self.state = 1109
            self.anonymous_function_signature()
            self.state = 1110
            self.right_arrow()
            self.state = 1111
            self.anonymous_function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Anonymous_function_signatureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def explicit_anonymous_function_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Explicit_anonymous_function_parameter_listContext,0)


        def implicit_anonymous_function_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Implicit_anonymous_function_parameter_listContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_anonymous_function_signature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnonymous_function_signature" ):
                listener.enterAnonymous_function_signature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnonymous_function_signature" ):
                listener.exitAnonymous_function_signature(self)




    def anonymous_function_signature(self):

        localctx = CSharpParser.Anonymous_function_signatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_anonymous_function_signature)
        try:
            self.state = 1124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,107,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1113
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1114
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1115
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1116
                self.explicit_anonymous_function_parameter_list()
                self.state = 1117
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1119
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1120
                self.implicit_anonymous_function_parameter_list()
                self.state = 1121
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1123
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explicit_anonymous_function_parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explicit_anonymous_function_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Explicit_anonymous_function_parameterContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Explicit_anonymous_function_parameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_explicit_anonymous_function_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicit_anonymous_function_parameter_list" ):
                listener.enterExplicit_anonymous_function_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicit_anonymous_function_parameter_list" ):
                listener.exitExplicit_anonymous_function_parameter_list(self)




    def explicit_anonymous_function_parameter_list(self):

        localctx = CSharpParser.Explicit_anonymous_function_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_explicit_anonymous_function_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1126
            self.explicit_anonymous_function_parameter()
            self.state = 1131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1127
                self.match(CSharpParser.COMMA)
                self.state = 1128
                self.explicit_anonymous_function_parameter()
                self.state = 1133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explicit_anonymous_function_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.refout = None # Token

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def OUT(self):
            return self.getToken(CSharpParser.OUT, 0)

        def IN(self):
            return self.getToken(CSharpParser.IN, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_explicit_anonymous_function_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicit_anonymous_function_parameter" ):
                listener.enterExplicit_anonymous_function_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicit_anonymous_function_parameter" ):
                listener.exitExplicit_anonymous_function_parameter(self)




    def explicit_anonymous_function_parameter(self):

        localctx = CSharpParser.Explicit_anonymous_function_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_explicit_anonymous_function_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 54)) & ~0x3f) == 0 and ((1 << (_la - 54)) & ((1 << (CSharpParser.IN - 54)) | (1 << (CSharpParser.OUT - 54)) | (1 << (CSharpParser.REF - 54)))) != 0):
                self.state = 1134
                localctx.refout = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 54)) & ~0x3f) == 0 and ((1 << (_la - 54)) & ((1 << (CSharpParser.IN - 54)) | (1 << (CSharpParser.OUT - 54)) | (1 << (CSharpParser.REF - 54)))) != 0)):
                    localctx.refout = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 1137
            self.type_()
            self.state = 1138
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_anonymous_function_parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_implicit_anonymous_function_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplicit_anonymous_function_parameter_list" ):
                listener.enterImplicit_anonymous_function_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplicit_anonymous_function_parameter_list" ):
                listener.exitImplicit_anonymous_function_parameter_list(self)




    def implicit_anonymous_function_parameter_list(self):

        localctx = CSharpParser.Implicit_anonymous_function_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_implicit_anonymous_function_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1140
            self.identifier()
            self.state = 1145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1141
                self.match(CSharpParser.COMMA)
                self.state = 1142
                self.identifier()
                self.state = 1147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Anonymous_function_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_anonymous_function_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnonymous_function_body" ):
                listener.enterAnonymous_function_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnonymous_function_body" ):
                listener.exitAnonymous_function_body(self)




    def anonymous_function_body(self):

        localctx = CSharpParser.Anonymous_function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_anonymous_function_body)
        try:
            self.state = 1150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.THROW, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1148
                self.throwable_expression()
                pass
            elif token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1149
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def from_clause(self):
            return self.getTypedRuleContext(CSharpParser.From_clauseContext,0)


        def query_body(self):
            return self.getTypedRuleContext(CSharpParser.Query_bodyContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_query_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_expression" ):
                listener.enterQuery_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_expression" ):
                listener.exitQuery_expression(self)




    def query_expression(self):

        localctx = CSharpParser.Query_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_query_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1152
            self.from_clause()
            self.state = 1153
            self.query_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class From_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(CSharpParser.FROM, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def IN(self):
            return self.getToken(CSharpParser.IN, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_from_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom_clause" ):
                listener.enterFrom_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom_clause" ):
                listener.exitFrom_clause(self)




    def from_clause(self):

        localctx = CSharpParser.From_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_from_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1155
            self.match(CSharpParser.FROM)
            self.state = 1157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,112,self._ctx)
            if la_ == 1:
                self.state = 1156
                self.type_()


            self.state = 1159
            self.identifier()
            self.state = 1160
            self.match(CSharpParser.IN)
            self.state = 1161
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select_or_group_clause(self):
            return self.getTypedRuleContext(CSharpParser.Select_or_group_clauseContext,0)


        def query_body_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Query_body_clauseContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Query_body_clauseContext,i)


        def query_continuation(self):
            return self.getTypedRuleContext(CSharpParser.Query_continuationContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_query_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_body" ):
                listener.enterQuery_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_body" ):
                listener.exitQuery_body(self)




    def query_body(self):

        localctx = CSharpParser.Query_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_query_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 48)) & ~0x3f) == 0 and ((1 << (_la - 48)) & ((1 << (CSharpParser.FROM - 48)) | (1 << (CSharpParser.JOIN - 48)) | (1 << (CSharpParser.LET - 48)) | (1 << (CSharpParser.ORDERBY - 48)) | (1 << (CSharpParser.WHERE - 48)))) != 0):
                self.state = 1163
                self.query_body_clause()
                self.state = 1168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1169
            self.select_or_group_clause()
            self.state = 1171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,114,self._ctx)
            if la_ == 1:
                self.state = 1170
                self.query_continuation()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_body_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def from_clause(self):
            return self.getTypedRuleContext(CSharpParser.From_clauseContext,0)


        def let_clause(self):
            return self.getTypedRuleContext(CSharpParser.Let_clauseContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(CSharpParser.Where_clauseContext,0)


        def combined_join_clause(self):
            return self.getTypedRuleContext(CSharpParser.Combined_join_clauseContext,0)


        def orderby_clause(self):
            return self.getTypedRuleContext(CSharpParser.Orderby_clauseContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_query_body_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_body_clause" ):
                listener.enterQuery_body_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_body_clause" ):
                listener.exitQuery_body_clause(self)




    def query_body_clause(self):

        localctx = CSharpParser.Query_body_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_query_body_clause)
        try:
            self.state = 1178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.FROM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1173
                self.from_clause()
                pass
            elif token in [CSharpParser.LET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1174
                self.let_clause()
                pass
            elif token in [CSharpParser.WHERE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1175
                self.where_clause()
                pass
            elif token in [CSharpParser.JOIN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1176
                self.combined_join_clause()
                pass
            elif token in [CSharpParser.ORDERBY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1177
                self.orderby_clause()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Let_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(CSharpParser.LET, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_let_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet_clause" ):
                listener.enterLet_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet_clause" ):
                listener.exitLet_clause(self)




    def let_clause(self):

        localctx = CSharpParser.Let_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_let_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1180
            self.match(CSharpParser.LET)
            self.state = 1181
            self.identifier()
            self.state = 1182
            self.match(CSharpParser.ASSIGNMENT)
            self.state = 1183
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(CSharpParser.WHERE, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_where_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_clause" ):
                listener.enterWhere_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_clause" ):
                listener.exitWhere_clause(self)




    def where_clause(self):

        localctx = CSharpParser.Where_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_where_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1185
            self.match(CSharpParser.WHERE)
            self.state = 1186
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Combined_join_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JOIN(self):
            return self.getToken(CSharpParser.JOIN, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def IN(self):
            return self.getToken(CSharpParser.IN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ExpressionContext,i)


        def ON(self):
            return self.getToken(CSharpParser.ON, 0)

        def EQUALS(self):
            return self.getToken(CSharpParser.EQUALS, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def INTO(self):
            return self.getToken(CSharpParser.INTO, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_combined_join_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCombined_join_clause" ):
                listener.enterCombined_join_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCombined_join_clause" ):
                listener.exitCombined_join_clause(self)




    def combined_join_clause(self):

        localctx = CSharpParser.Combined_join_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_combined_join_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1188
            self.match(CSharpParser.JOIN)
            self.state = 1190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,116,self._ctx)
            if la_ == 1:
                self.state = 1189
                self.type_()


            self.state = 1192
            self.identifier()
            self.state = 1193
            self.match(CSharpParser.IN)
            self.state = 1194
            self.expression()
            self.state = 1195
            self.match(CSharpParser.ON)
            self.state = 1196
            self.expression()
            self.state = 1197
            self.match(CSharpParser.EQUALS)
            self.state = 1198
            self.expression()
            self.state = 1201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.INTO:
                self.state = 1199
                self.match(CSharpParser.INTO)
                self.state = 1200
                self.identifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Orderby_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDERBY(self):
            return self.getToken(CSharpParser.ORDERBY, 0)

        def ordering(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.OrderingContext)
            else:
                return self.getTypedRuleContext(CSharpParser.OrderingContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_orderby_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderby_clause" ):
                listener.enterOrderby_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderby_clause" ):
                listener.exitOrderby_clause(self)




    def orderby_clause(self):

        localctx = CSharpParser.Orderby_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_orderby_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1203
            self.match(CSharpParser.ORDERBY)
            self.state = 1204
            self.ordering()
            self.state = 1209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1205
                self.match(CSharpParser.COMMA)
                self.state = 1206
                self.ordering()
                self.state = 1211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.dir = None # Token

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def ASCENDING(self):
            return self.getToken(CSharpParser.ASCENDING, 0)

        def DESCENDING(self):
            return self.getToken(CSharpParser.DESCENDING, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_ordering

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrdering" ):
                listener.enterOrdering(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrdering" ):
                listener.exitOrdering(self)




    def ordering(self):

        localctx = CSharpParser.OrderingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_ordering)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1212
            self.expression()
            self.state = 1214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.ASCENDING or _la==CSharpParser.DESCENDING:
                self.state = 1213
                localctx.dir = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==CSharpParser.ASCENDING or _la==CSharpParser.DESCENDING):
                    localctx.dir = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_or_group_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(CSharpParser.SELECT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ExpressionContext,i)


        def GROUP(self):
            return self.getToken(CSharpParser.GROUP, 0)

        def BY(self):
            return self.getToken(CSharpParser.BY, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_select_or_group_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_or_group_clause" ):
                listener.enterSelect_or_group_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_or_group_clause" ):
                listener.exitSelect_or_group_clause(self)




    def select_or_group_clause(self):

        localctx = CSharpParser.Select_or_group_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_select_or_group_clause)
        try:
            self.state = 1223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.SELECT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1216
                self.match(CSharpParser.SELECT)
                self.state = 1217
                self.expression()
                pass
            elif token in [CSharpParser.GROUP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1218
                self.match(CSharpParser.GROUP)
                self.state = 1219
                self.expression()
                self.state = 1220
                self.match(CSharpParser.BY)
                self.state = 1221
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_continuationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTO(self):
            return self.getToken(CSharpParser.INTO, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def query_body(self):
            return self.getTypedRuleContext(CSharpParser.Query_bodyContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_query_continuation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_continuation" ):
                listener.enterQuery_continuation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_continuation" ):
                listener.exitQuery_continuation(self)




    def query_continuation(self):

        localctx = CSharpParser.Query_continuationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_query_continuation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1225
            self.match(CSharpParser.INTO)
            self.state = 1226
            self.identifier()
            self.state = 1227
            self.query_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labeled_Statement(self):
            return self.getTypedRuleContext(CSharpParser.Labeled_StatementContext,0)


        def declarationStatement(self):
            return self.getTypedRuleContext(CSharpParser.DeclarationStatementContext,0)


        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = CSharpParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_statement)
        try:
            self.state = 1232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,121,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1229
                self.labeled_Statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1230
                self.declarationStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1231
                self.embedded_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_variable_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Local_variable_declarationContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def local_constant_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Local_constant_declarationContext,0)


        def local_function_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Local_function_declarationContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_declarationStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatement" ):
                listener.enterDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatement" ):
                listener.exitDeclarationStatement(self)




    def declarationStatement(self):

        localctx = CSharpParser.DeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_declarationStatement)
        try:
            self.state = 1241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,122,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1234
                self.local_variable_declaration()
                self.state = 1235
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1237
                self.local_constant_declaration()
                self.state = 1238
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1240
                self.local_function_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_function_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_function_header(self):
            return self.getTypedRuleContext(CSharpParser.Local_function_headerContext,0)


        def local_function_body(self):
            return self.getTypedRuleContext(CSharpParser.Local_function_bodyContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_local_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_function_declaration" ):
                listener.enterLocal_function_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_function_declaration" ):
                listener.exitLocal_function_declaration(self)




    def local_function_declaration(self):

        localctx = CSharpParser.Local_function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_local_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1243
            self.local_function_header()
            self.state = 1244
            self.local_function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_function_headerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_type(self):
            return self.getTypedRuleContext(CSharpParser.Return_typeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def local_function_modifiers(self):
            return self.getTypedRuleContext(CSharpParser.Local_function_modifiersContext,0)


        def type_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_listContext,0)


        def formal_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Formal_parameter_listContext,0)


        def type_parameter_constraints_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clausesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_local_function_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_function_header" ):
                listener.enterLocal_function_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_function_header" ):
                listener.exitLocal_function_header(self)




    def local_function_header(self):

        localctx = CSharpParser.Local_function_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_local_function_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,123,self._ctx)
            if la_ == 1:
                self.state = 1246
                self.local_function_modifiers()


            self.state = 1249
            self.return_type()
            self.state = 1250
            self.identifier()
            self.state = 1252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.LT:
                self.state = 1251
                self.type_parameter_list()


            self.state = 1254
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 1256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (CSharpParser.ADD - 10)) | (1 << (CSharpParser.ALIAS - 10)) | (1 << (CSharpParser.ARGLIST - 10)) | (1 << (CSharpParser.ASCENDING - 10)) | (1 << (CSharpParser.ASYNC - 10)) | (1 << (CSharpParser.AWAIT - 10)) | (1 << (CSharpParser.BOOL - 10)) | (1 << (CSharpParser.BY - 10)) | (1 << (CSharpParser.BYTE - 10)) | (1 << (CSharpParser.CHAR - 10)) | (1 << (CSharpParser.DECIMAL - 10)) | (1 << (CSharpParser.DESCENDING - 10)) | (1 << (CSharpParser.DOUBLE - 10)) | (1 << (CSharpParser.DYNAMIC - 10)) | (1 << (CSharpParser.EQUALS - 10)) | (1 << (CSharpParser.FLOAT - 10)) | (1 << (CSharpParser.FROM - 10)) | (1 << (CSharpParser.GET - 10)) | (1 << (CSharpParser.GROUP - 10)) | (1 << (CSharpParser.IN - 10)) | (1 << (CSharpParser.INT - 10)) | (1 << (CSharpParser.INTO - 10)) | (1 << (CSharpParser.JOIN - 10)) | (1 << (CSharpParser.LET - 10)) | (1 << (CSharpParser.LONG - 10)) | (1 << (CSharpParser.NAMEOF - 10)) | (1 << (CSharpParser.OBJECT - 10)) | (1 << (CSharpParser.ON - 10)) | (1 << (CSharpParser.ORDERBY - 10)) | (1 << (CSharpParser.OUT - 10)))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (CSharpParser.PARAMS - 74)) | (1 << (CSharpParser.PARTIAL - 74)) | (1 << (CSharpParser.REF - 74)) | (1 << (CSharpParser.REMOVE - 74)) | (1 << (CSharpParser.SBYTE - 74)) | (1 << (CSharpParser.SELECT - 74)) | (1 << (CSharpParser.SET - 74)) | (1 << (CSharpParser.SHORT - 74)) | (1 << (CSharpParser.STRING - 74)) | (1 << (CSharpParser.THIS - 74)) | (1 << (CSharpParser.UINT - 74)) | (1 << (CSharpParser.ULONG - 74)) | (1 << (CSharpParser.UNMANAGED - 74)) | (1 << (CSharpParser.USHORT - 74)) | (1 << (CSharpParser.VAR - 74)) | (1 << (CSharpParser.VOID - 74)) | (1 << (CSharpParser.WHEN - 74)) | (1 << (CSharpParser.WHERE - 74)) | (1 << (CSharpParser.YIELD - 74)) | (1 << (CSharpParser.IDENTIFIER - 74)) | (1 << (CSharpParser.OPEN_BRACKET - 74)) | (1 << (CSharpParser.OPEN_PARENS - 74)))) != 0):
                self.state = 1255
                self.formal_parameter_list()


            self.state = 1258
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 1260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHERE:
                self.state = 1259
                self.type_parameter_constraints_clauses()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_function_modifiersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASYNC(self):
            return self.getToken(CSharpParser.ASYNC, 0)

        def UNSAFE(self):
            return self.getToken(CSharpParser.UNSAFE, 0)

        def STATIC(self):
            return self.getToken(CSharpParser.STATIC, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_local_function_modifiers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_function_modifiers" ):
                listener.enterLocal_function_modifiers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_function_modifiers" ):
                listener.exitLocal_function_modifiers(self)




    def local_function_modifiers(self):

        localctx = CSharpParser.Local_function_modifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_local_function_modifiers)
        self._la = 0 # Token type
        try:
            self.state = 1268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ASYNC, CSharpParser.UNSAFE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1262
                _la = self._input.LA(1)
                if not(_la==CSharpParser.ASYNC or _la==CSharpParser.UNSAFE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 1264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.STATIC:
                    self.state = 1263
                    self.match(CSharpParser.STATIC)


                pass
            elif token in [CSharpParser.STATIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1266
                self.match(CSharpParser.STATIC)
                self.state = 1267
                _la = self._input.LA(1)
                if not(_la==CSharpParser.ASYNC or _la==CSharpParser.UNSAFE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_function_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_local_function_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_function_body" ):
                listener.enterLocal_function_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_function_body" ):
                listener.exitLocal_function_body(self)




    def local_function_body(self):

        localctx = CSharpParser.Local_function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_local_function_body)
        try:
            self.state = 1275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1270
                self.block()
                pass
            elif token in [CSharpParser.ASSIGNMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1271
                self.right_arrow()
                self.state = 1272
                self.throwable_expression()
                self.state = 1273
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Labeled_StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def statement(self):
            return self.getTypedRuleContext(CSharpParser.StatementContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_labeled_Statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeled_Statement" ):
                listener.enterLabeled_Statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeled_Statement" ):
                listener.exitLabeled_Statement(self)




    def labeled_Statement(self):

        localctx = CSharpParser.Labeled_StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_labeled_Statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1277
            self.identifier()
            self.state = 1278
            self.match(CSharpParser.COLON)
            self.state = 1279
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Embedded_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def simple_embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Simple_embedded_statementContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_embedded_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmbedded_statement" ):
                listener.enterEmbedded_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmbedded_statement" ):
                listener.exitEmbedded_statement(self)




    def embedded_statement(self):

        localctx = CSharpParser.Embedded_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_embedded_statement)
        try:
            self.state = 1283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1281
                self.block()
                pass
            elif token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BREAK, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.CONTINUE, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DO, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FIXED, CSharpParser.FLOAT, CSharpParser.FOR, CSharpParser.FOREACH, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GOTO, CSharpParser.GROUP, CSharpParser.IF, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LOCK, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.RETURN, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.SWITCH, CSharpParser.THIS, CSharpParser.THROW, CSharpParser.TRUE, CSharpParser.TRY, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.UNSAFE, CSharpParser.USHORT, CSharpParser.USING, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.WHILE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.SEMICOLON, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1282
                self.simple_embedded_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_embedded_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSharpParser.RULE_simple_embedded_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TryStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRY(self):
            return self.getToken(CSharpParser.TRY, 0)
        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)

        def catch_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Catch_clausesContext,0)

        def finally_clause(self):
            return self.getTypedRuleContext(CSharpParser.Finally_clauseContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryStatement" ):
                listener.enterTryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryStatement" ):
                listener.exitTryStatement(self)


    class CheckedStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHECKED(self):
            return self.getToken(CSharpParser.CHECKED, 0)
        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCheckedStatement" ):
                listener.enterCheckedStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCheckedStatement" ):
                listener.exitCheckedStatement(self)


    class ThrowStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def THROW(self):
            return self.getToken(CSharpParser.THROW, 0)
        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowStatement" ):
                listener.enterThrowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowStatement" ):
                listener.exitThrowStatement(self)


    class TheEmptyStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTheEmptyStatement" ):
                listener.enterTheEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTheEmptyStatement" ):
                listener.exitTheEmptyStatement(self)


    class UnsafeStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UNSAFE(self):
            return self.getToken(CSharpParser.UNSAFE, 0)
        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnsafeStatement" ):
                listener.enterUnsafeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnsafeStatement" ):
                listener.exitUnsafeStatement(self)


    class ForStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(CSharpParser.FOR, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.SEMICOLON)
            else:
                return self.getToken(CSharpParser.SEMICOLON, i)
        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)

        def for_initializer(self):
            return self.getTypedRuleContext(CSharpParser.For_initializerContext,0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def for_iterator(self):
            return self.getTypedRuleContext(CSharpParser.For_iteratorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)


    class BreakStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BREAK(self):
            return self.getToken(CSharpParser.BREAK, 0)
        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)


    class IfStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(CSharpParser.IF, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def if_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.If_bodyContext)
            else:
                return self.getTypedRuleContext(CSharpParser.If_bodyContext,i)

        def ELSE(self):
            return self.getToken(CSharpParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)


    class ReturnStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(CSharpParser.RETURN, 0)
        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)


    class GotoStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GOTO(self):
            return self.getToken(CSharpParser.GOTO, 0)
        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)
        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)

        def CASE(self):
            return self.getToken(CSharpParser.CASE, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def DEFAULT(self):
            return self.getToken(CSharpParser.DEFAULT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotoStatement" ):
                listener.enterGotoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotoStatement" ):
                listener.exitGotoStatement(self)


    class SwitchStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SWITCH(self):
            return self.getToken(CSharpParser.SWITCH, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)
        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)
        def switch_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Switch_sectionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Switch_sectionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)


    class FixedStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FIXED(self):
            return self.getToken(CSharpParser.FIXED, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def pointer_type(self):
            return self.getTypedRuleContext(CSharpParser.Pointer_typeContext,0)

        def fixed_pointer_declarators(self):
            return self.getTypedRuleContext(CSharpParser.Fixed_pointer_declaratorsContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixedStatement" ):
                listener.enterFixedStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixedStatement" ):
                listener.exitFixedStatement(self)


    class WhileStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(CSharpParser.WHILE, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)


    class DoStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DO(self):
            return self.getToken(CSharpParser.DO, 0)
        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)

        def WHILE(self):
            return self.getToken(CSharpParser.WHILE, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoStatement" ):
                listener.enterDoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoStatement" ):
                listener.exitDoStatement(self)


    class ForeachStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOREACH(self):
            return self.getToken(CSharpParser.FOREACH, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def local_variable_type(self):
            return self.getTypedRuleContext(CSharpParser.Local_variable_typeContext,0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)

        def IN(self):
            return self.getToken(CSharpParser.IN, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)

        def AWAIT(self):
            return self.getToken(CSharpParser.AWAIT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForeachStatement" ):
                listener.enterForeachStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForeachStatement" ):
                listener.exitForeachStatement(self)


    class UncheckedStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UNCHECKED(self):
            return self.getToken(CSharpParser.UNCHECKED, 0)
        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUncheckedStatement" ):
                listener.enterUncheckedStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUncheckedStatement" ):
                listener.exitUncheckedStatement(self)


    class ExpressionStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)


    class ContinueStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONTINUE(self):
            return self.getToken(CSharpParser.CONTINUE, 0)
        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)


    class UsingStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def USING(self):
            return self.getToken(CSharpParser.USING, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def resource_acquisition(self):
            return self.getTypedRuleContext(CSharpParser.Resource_acquisitionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsingStatement" ):
                listener.enterUsingStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsingStatement" ):
                listener.exitUsingStatement(self)


    class LockStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOCK(self):
            return self.getToken(CSharpParser.LOCK, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLockStatement" ):
                listener.enterLockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLockStatement" ):
                listener.exitLockStatement(self)


    class YieldStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def YIELD(self):
            return self.getToken(CSharpParser.YIELD, 0)
        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)
        def RETURN(self):
            return self.getToken(CSharpParser.RETURN, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def BREAK(self):
            return self.getToken(CSharpParser.BREAK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterYieldStatement" ):
                listener.enterYieldStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitYieldStatement" ):
                listener.exitYieldStatement(self)



    def simple_embedded_statement(self):

        localctx = CSharpParser.Simple_embedded_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_simple_embedded_statement)
        self._la = 0 # Token type
        try:
            self.state = 1415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,143,self._ctx)
            if la_ == 1:
                localctx = CSharpParser.TheEmptyStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1285
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 2:
                localctx = CSharpParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1286
                self.expression()
                self.state = 1287
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 3:
                localctx = CSharpParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1289
                self.match(CSharpParser.IF)
                self.state = 1290
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1291
                self.expression()
                self.state = 1292
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1293
                self.if_body()
                self.state = 1296
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,131,self._ctx)
                if la_ == 1:
                    self.state = 1294
                    self.match(CSharpParser.ELSE)
                    self.state = 1295
                    self.if_body()


                pass

            elif la_ == 4:
                localctx = CSharpParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1298
                self.match(CSharpParser.SWITCH)
                self.state = 1299
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1300
                self.expression()
                self.state = 1301
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1302
                self.match(CSharpParser.OPEN_BRACE)
                self.state = 1306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSharpParser.CASE or _la==CSharpParser.DEFAULT:
                    self.state = 1303
                    self.switch_section()
                    self.state = 1308
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1309
                self.match(CSharpParser.CLOSE_BRACE)
                pass

            elif la_ == 5:
                localctx = CSharpParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1311
                self.match(CSharpParser.WHILE)
                self.state = 1312
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1313
                self.expression()
                self.state = 1314
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1315
                self.embedded_statement()
                pass

            elif la_ == 6:
                localctx = CSharpParser.DoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1317
                self.match(CSharpParser.DO)
                self.state = 1318
                self.embedded_statement()
                self.state = 1319
                self.match(CSharpParser.WHILE)
                self.state = 1320
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1321
                self.expression()
                self.state = 1322
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1323
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 7:
                localctx = CSharpParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1325
                self.match(CSharpParser.FOR)
                self.state = 1326
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1328
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FIXED) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.USING - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.VOID - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)))) != 0):
                    self.state = 1327
                    self.for_initializer()


                self.state = 1330
                self.match(CSharpParser.SEMICOLON)
                self.state = 1332
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)))) != 0):
                    self.state = 1331
                    self.expression()


                self.state = 1334
                self.match(CSharpParser.SEMICOLON)
                self.state = 1336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)))) != 0):
                    self.state = 1335
                    self.for_iterator()


                self.state = 1338
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1339
                self.embedded_statement()
                pass

            elif la_ == 8:
                localctx = CSharpParser.ForeachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1341
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.AWAIT:
                    self.state = 1340
                    self.match(CSharpParser.AWAIT)


                self.state = 1343
                self.match(CSharpParser.FOREACH)
                self.state = 1344
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1345
                self.local_variable_type()
                self.state = 1346
                self.identifier()
                self.state = 1347
                self.match(CSharpParser.IN)
                self.state = 1348
                self.expression()
                self.state = 1349
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1350
                self.embedded_statement()
                pass

            elif la_ == 9:
                localctx = CSharpParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1352
                self.match(CSharpParser.BREAK)
                self.state = 1353
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 10:
                localctx = CSharpParser.ContinueStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1354
                self.match(CSharpParser.CONTINUE)
                self.state = 1355
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 11:
                localctx = CSharpParser.GotoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1356
                self.match(CSharpParser.GOTO)
                self.state = 1361
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BY, CSharpParser.DESCENDING, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.NAMEOF, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.UNMANAGED, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER]:
                    self.state = 1357
                    self.identifier()
                    pass
                elif token in [CSharpParser.CASE]:
                    self.state = 1358
                    self.match(CSharpParser.CASE)
                    self.state = 1359
                    self.expression()
                    pass
                elif token in [CSharpParser.DEFAULT]:
                    self.state = 1360
                    self.match(CSharpParser.DEFAULT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1363
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 12:
                localctx = CSharpParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1364
                self.match(CSharpParser.RETURN)
                self.state = 1366
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)))) != 0):
                    self.state = 1365
                    self.expression()


                self.state = 1368
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 13:
                localctx = CSharpParser.ThrowStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1369
                self.match(CSharpParser.THROW)
                self.state = 1371
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)))) != 0):
                    self.state = 1370
                    self.expression()


                self.state = 1373
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 14:
                localctx = CSharpParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1374
                self.match(CSharpParser.TRY)
                self.state = 1375
                self.block()
                self.state = 1381
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.CATCH]:
                    self.state = 1376
                    self.catch_clauses()
                    self.state = 1378
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpParser.FINALLY:
                        self.state = 1377
                        self.finally_clause()


                    pass
                elif token in [CSharpParser.FINALLY]:
                    self.state = 1380
                    self.finally_clause()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 15:
                localctx = CSharpParser.CheckedStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 1383
                self.match(CSharpParser.CHECKED)
                self.state = 1384
                self.block()
                pass

            elif la_ == 16:
                localctx = CSharpParser.UncheckedStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 1385
                self.match(CSharpParser.UNCHECKED)
                self.state = 1386
                self.block()
                pass

            elif la_ == 17:
                localctx = CSharpParser.LockStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 1387
                self.match(CSharpParser.LOCK)
                self.state = 1388
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1389
                self.expression()
                self.state = 1390
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1391
                self.embedded_statement()
                pass

            elif la_ == 18:
                localctx = CSharpParser.UsingStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 1393
                self.match(CSharpParser.USING)
                self.state = 1394
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1395
                self.resource_acquisition()
                self.state = 1396
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1397
                self.embedded_statement()
                pass

            elif la_ == 19:
                localctx = CSharpParser.YieldStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 1399
                self.match(CSharpParser.YIELD)
                self.state = 1403
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.RETURN]:
                    self.state = 1400
                    self.match(CSharpParser.RETURN)
                    self.state = 1401
                    self.expression()
                    pass
                elif token in [CSharpParser.BREAK]:
                    self.state = 1402
                    self.match(CSharpParser.BREAK)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1405
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 20:
                localctx = CSharpParser.UnsafeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 20)
                self.state = 1406
                self.match(CSharpParser.UNSAFE)
                self.state = 1407
                self.block()
                pass

            elif la_ == 21:
                localctx = CSharpParser.FixedStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 21)
                self.state = 1408
                self.match(CSharpParser.FIXED)
                self.state = 1409
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1410
                self.pointer_type()
                self.state = 1411
                self.fixed_pointer_declarators()
                self.state = 1412
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1413
                self.embedded_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(CSharpParser.Statement_listContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = CSharpParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1417
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 1419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BREAK) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.CONST) | (1 << CSharpParser.CONTINUE) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DO) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FIXED) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FOR) | (1 << CSharpParser.FOREACH) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GOTO) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IF) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LOCK) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.RETURN - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STATIC - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.SWITCH - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.THROW - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TRY - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.UNSAFE - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.USING - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.VOID - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.WHILE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)) | (1 << (CSharpParser.OPEN_BRACE - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.SEMICOLON - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)))) != 0):
                self.state = 1418
                self.statement_list()


            self.state = 1421
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_variable_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_variable_type(self):
            return self.getTypedRuleContext(CSharpParser.Local_variable_typeContext,0)


        def local_variable_declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Local_variable_declaratorContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Local_variable_declaratorContext,i)


        def USING(self):
            return self.getToken(CSharpParser.USING, 0)

        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def READONLY(self):
            return self.getToken(CSharpParser.READONLY, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def FIXED(self):
            return self.getToken(CSharpParser.FIXED, 0)

        def pointer_type(self):
            return self.getTypedRuleContext(CSharpParser.Pointer_typeContext,0)


        def fixed_pointer_declarators(self):
            return self.getTypedRuleContext(CSharpParser.Fixed_pointer_declaratorsContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_local_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_variable_declaration" ):
                listener.enterLocal_variable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_variable_declaration" ):
                listener.exitLocal_variable_declaration(self)




    def local_variable_declaration(self):

        localctx = CSharpParser.Local_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_local_variable_declaration)
        self._la = 0 # Token type
        try:
            self.state = 1442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.DECIMAL, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.STRING, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.USING, CSharpParser.VAR, CSharpParser.VOID, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.OPEN_PARENS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1427
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,145,self._ctx)
                if la_ == 1:
                    self.state = 1423
                    self.match(CSharpParser.USING)

                elif la_ == 2:
                    self.state = 1424
                    self.match(CSharpParser.REF)

                elif la_ == 3:
                    self.state = 1425
                    self.match(CSharpParser.REF)
                    self.state = 1426
                    self.match(CSharpParser.READONLY)


                self.state = 1429
                self.local_variable_type()
                self.state = 1430
                self.local_variable_declarator()
                self.state = 1435
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSharpParser.COMMA:
                    self.state = 1431
                    self.match(CSharpParser.COMMA)
                    self.state = 1432
                    self.local_variable_declarator()
                    self.state = 1437
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [CSharpParser.FIXED]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1438
                self.match(CSharpParser.FIXED)
                self.state = 1439
                self.pointer_type()
                self.state = 1440
                self.fixed_pointer_declarators()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_variable_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSharpParser.VAR, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_local_variable_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_variable_type" ):
                listener.enterLocal_variable_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_variable_type" ):
                listener.exitLocal_variable_type(self)




    def local_variable_type(self):

        localctx = CSharpParser.Local_variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_local_variable_type)
        try:
            self.state = 1446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,148,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1444
                self.match(CSharpParser.VAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1445
                self.type_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_variable_declaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def local_variable_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Local_variable_initializerContext,0)


        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_local_variable_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_variable_declarator" ):
                listener.enterLocal_variable_declarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_variable_declarator" ):
                listener.exitLocal_variable_declarator(self)




    def local_variable_declarator(self):

        localctx = CSharpParser.Local_variable_declaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_local_variable_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1448
            self.identifier()
            self.state = 1454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.ASSIGNMENT:
                self.state = 1449
                self.match(CSharpParser.ASSIGNMENT)
                self.state = 1451
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,149,self._ctx)
                if la_ == 1:
                    self.state = 1450
                    self.match(CSharpParser.REF)


                self.state = 1453
                self.local_variable_initializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_variable_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def array_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Array_initializerContext,0)


        def stackalloc_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Stackalloc_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_local_variable_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_variable_initializer" ):
                listener.enterLocal_variable_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_variable_initializer" ):
                listener.exitLocal_variable_initializer(self)




    def local_variable_initializer(self):

        localctx = CSharpParser.Local_variable_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_local_variable_initializer)
        try:
            self.state = 1459
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1456
                self.expression()
                pass
            elif token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1457
                self.array_initializer()
                pass
            elif token in [CSharpParser.STACKALLOC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1458
                self.stackalloc_initializer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_constant_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSharpParser.CONST, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def constant_declarators(self):
            return self.getTypedRuleContext(CSharpParser.Constant_declaratorsContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_local_constant_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_constant_declaration" ):
                listener.enterLocal_constant_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_constant_declaration" ):
                listener.exitLocal_constant_declaration(self)




    def local_constant_declaration(self):

        localctx = CSharpParser.Local_constant_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_local_constant_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1461
            self.match(CSharpParser.CONST)
            self.state = 1462
            self.type_()
            self.state = 1463
            self.constant_declarators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def simple_embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Simple_embedded_statementContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_if_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_body" ):
                listener.enterIf_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_body" ):
                listener.exitIf_body(self)




    def if_body(self):

        localctx = CSharpParser.If_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_if_body)
        try:
            self.state = 1467
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1465
                self.block()
                pass
            elif token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BREAK, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.CONTINUE, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DO, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FIXED, CSharpParser.FLOAT, CSharpParser.FOR, CSharpParser.FOREACH, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GOTO, CSharpParser.GROUP, CSharpParser.IF, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LOCK, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.RETURN, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.SWITCH, CSharpParser.THIS, CSharpParser.THROW, CSharpParser.TRUE, CSharpParser.TRY, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.UNSAFE, CSharpParser.USHORT, CSharpParser.USING, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.WHILE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.SEMICOLON, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1466
                self.simple_embedded_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_sectionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_list(self):
            return self.getTypedRuleContext(CSharpParser.Statement_listContext,0)


        def switch_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Switch_labelContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Switch_labelContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_switch_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_section" ):
                listener.enterSwitch_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_section" ):
                listener.exitSwitch_section(self)




    def switch_section(self):

        localctx = CSharpParser.Switch_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_switch_section)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1470 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1469
                    self.switch_label()

                else:
                    raise NoViableAltException(self)
                self.state = 1472 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,153,self._ctx)

            self.state = 1474
            self.statement_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_labelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(CSharpParser.CASE, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def case_guard(self):
            return self.getTypedRuleContext(CSharpParser.Case_guardContext,0)


        def DEFAULT(self):
            return self.getToken(CSharpParser.DEFAULT, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_switch_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_label" ):
                listener.enterSwitch_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_label" ):
                listener.exitSwitch_label(self)




    def switch_label(self):

        localctx = CSharpParser.Switch_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_switch_label)
        self._la = 0 # Token type
        try:
            self.state = 1485
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1476
                self.match(CSharpParser.CASE)
                self.state = 1477
                self.expression()
                self.state = 1479
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.WHEN:
                    self.state = 1478
                    self.case_guard()


                self.state = 1481
                self.match(CSharpParser.COLON)
                pass
            elif token in [CSharpParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1483
                self.match(CSharpParser.DEFAULT)
                self.state = 1484
                self.match(CSharpParser.COLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_guardContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHEN(self):
            return self.getToken(CSharpParser.WHEN, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_case_guard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase_guard" ):
                listener.enterCase_guard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase_guard" ):
                listener.exitCase_guard(self)




    def case_guard(self):

        localctx = CSharpParser.Case_guardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_case_guard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1487
            self.match(CSharpParser.WHEN)
            self.state = 1488
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.StatementContext)
            else:
                return self.getTypedRuleContext(CSharpParser.StatementContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_statement_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_list" ):
                listener.enterStatement_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_list" ):
                listener.exitStatement_list(self)




    def statement_list(self):

        localctx = CSharpParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1491 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1490
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 1493 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,156,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_variable_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Local_variable_declarationContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_for_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_initializer" ):
                listener.enterFor_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_initializer" ):
                listener.exitFor_initializer(self)




    def for_initializer(self):

        localctx = CSharpParser.For_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_for_initializer)
        self._la = 0 # Token type
        try:
            self.state = 1504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,158,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1495
                self.local_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1496
                self.expression()
                self.state = 1501
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSharpParser.COMMA:
                    self.state = 1497
                    self.match(CSharpParser.COMMA)
                    self.state = 1498
                    self.expression()
                    self.state = 1503
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_iteratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_for_iterator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_iterator" ):
                listener.enterFor_iterator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_iterator" ):
                listener.exitFor_iterator(self)




    def for_iterator(self):

        localctx = CSharpParser.For_iteratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_for_iterator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1506
            self.expression()
            self.state = 1511
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1507
                self.match(CSharpParser.COMMA)
                self.state = 1508
                self.expression()
                self.state = 1513
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Catch_clausesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def specific_catch_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Specific_catch_clauseContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Specific_catch_clauseContext,i)


        def general_catch_clause(self):
            return self.getTypedRuleContext(CSharpParser.General_catch_clauseContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_catch_clauses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatch_clauses" ):
                listener.enterCatch_clauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatch_clauses" ):
                listener.exitCatch_clauses(self)




    def catch_clauses(self):

        localctx = CSharpParser.Catch_clausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_catch_clauses)
        self._la = 0 # Token type
        try:
            self.state = 1525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,162,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1514
                self.specific_catch_clause()
                self.state = 1518
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,160,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 1515
                        self.specific_catch_clause() 
                    self.state = 1520
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,160,self._ctx)

                self.state = 1522
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.CATCH:
                    self.state = 1521
                    self.general_catch_clause()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1524
                self.general_catch_clause()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Specific_catch_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATCH(self):
            return self.getToken(CSharpParser.CATCH, 0)

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def class_type(self):
            return self.getTypedRuleContext(CSharpParser.Class_typeContext,0)


        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def exception_filter(self):
            return self.getTypedRuleContext(CSharpParser.Exception_filterContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_specific_catch_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecific_catch_clause" ):
                listener.enterSpecific_catch_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecific_catch_clause" ):
                listener.exitSpecific_catch_clause(self)




    def specific_catch_clause(self):

        localctx = CSharpParser.Specific_catch_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_specific_catch_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1527
            self.match(CSharpParser.CATCH)
            self.state = 1528
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 1529
            self.class_type()
            self.state = 1531
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BY) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)))) != 0):
                self.state = 1530
                self.identifier()


            self.state = 1533
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 1535
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHEN:
                self.state = 1534
                self.exception_filter()


            self.state = 1537
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class General_catch_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATCH(self):
            return self.getToken(CSharpParser.CATCH, 0)

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def exception_filter(self):
            return self.getTypedRuleContext(CSharpParser.Exception_filterContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_general_catch_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneral_catch_clause" ):
                listener.enterGeneral_catch_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneral_catch_clause" ):
                listener.exitGeneral_catch_clause(self)




    def general_catch_clause(self):

        localctx = CSharpParser.General_catch_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_general_catch_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1539
            self.match(CSharpParser.CATCH)
            self.state = 1541
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHEN:
                self.state = 1540
                self.exception_filter()


            self.state = 1543
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exception_filterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHEN(self):
            return self.getToken(CSharpParser.WHEN, 0)

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_exception_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterException_filter" ):
                listener.enterException_filter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitException_filter" ):
                listener.exitException_filter(self)




    def exception_filter(self):

        localctx = CSharpParser.Exception_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_exception_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1545
            self.match(CSharpParser.WHEN)
            self.state = 1546
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 1547
            self.expression()
            self.state = 1548
            self.match(CSharpParser.CLOSE_PARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Finally_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINALLY(self):
            return self.getToken(CSharpParser.FINALLY, 0)

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_finally_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinally_clause" ):
                listener.enterFinally_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinally_clause" ):
                listener.exitFinally_clause(self)




    def finally_clause(self):

        localctx = CSharpParser.Finally_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_finally_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1550
            self.match(CSharpParser.FINALLY)
            self.state = 1551
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Resource_acquisitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_variable_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Local_variable_declarationContext,0)


        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_resource_acquisition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResource_acquisition" ):
                listener.enterResource_acquisition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResource_acquisition" ):
                listener.exitResource_acquisition(self)




    def resource_acquisition(self):

        localctx = CSharpParser.Resource_acquisitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_resource_acquisition)
        try:
            self.state = 1555
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,166,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1553
                self.local_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1554
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Namespace_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.qi = None # Qualified_identifierContext

        def NAMESPACE(self):
            return self.getToken(CSharpParser.NAMESPACE, 0)

        def namespace_body(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_bodyContext,0)


        def qualified_identifier(self):
            return self.getTypedRuleContext(CSharpParser.Qualified_identifierContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_namespace_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace_declaration" ):
                listener.enterNamespace_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace_declaration" ):
                listener.exitNamespace_declaration(self)




    def namespace_declaration(self):

        localctx = CSharpParser.Namespace_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_namespace_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1557
            self.match(CSharpParser.NAMESPACE)
            self.state = 1558
            localctx.qi = self.qualified_identifier()
            self.state = 1559
            self.namespace_body()
            self.state = 1561
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.SEMICOLON:
                self.state = 1560
                self.match(CSharpParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Qualified_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.DOT)
            else:
                return self.getToken(CSharpParser.DOT, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_qualified_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualified_identifier" ):
                listener.enterQualified_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualified_identifier" ):
                listener.exitQualified_identifier(self)




    def qualified_identifier(self):

        localctx = CSharpParser.Qualified_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_qualified_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1563
            self.identifier()
            self.state = 1568
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.DOT:
                self.state = 1564
                self.match(CSharpParser.DOT)
                self.state = 1565
                self.identifier()
                self.state = 1570
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Namespace_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def extern_alias_directives(self):
            return self.getTypedRuleContext(CSharpParser.Extern_alias_directivesContext,0)


        def using_directives(self):
            return self.getTypedRuleContext(CSharpParser.Using_directivesContext,0)


        def namespace_member_declarations(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_member_declarationsContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_namespace_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace_body" ):
                listener.enterNamespace_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace_body" ):
                listener.exitNamespace_body(self)




    def namespace_body(self):

        localctx = CSharpParser.Namespace_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_namespace_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1571
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 1573
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,169,self._ctx)
            if la_ == 1:
                self.state = 1572
                self.extern_alias_directives()


            self.state = 1576
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.USING:
                self.state = 1575
                self.using_directives()


            self.state = 1579
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.CLASS) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.ENUM) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.INTERFACE) | (1 << CSharpParser.INTERNAL))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NAMESPACE - 65)) | (1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.OVERRIDE - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.PRIVATE - 65)) | (1 << (CSharpParser.PROTECTED - 65)) | (1 << (CSharpParser.PUBLIC - 65)) | (1 << (CSharpParser.READONLY - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.SEALED - 65)) | (1 << (CSharpParser.STATIC - 65)) | (1 << (CSharpParser.STRUCT - 65)) | (1 << (CSharpParser.UNSAFE - 65)) | (1 << (CSharpParser.VIRTUAL - 65)) | (1 << (CSharpParser.VOLATILE - 65)) | (1 << (CSharpParser.OPEN_BRACKET - 65)))) != 0):
                self.state = 1578
                self.namespace_member_declarations()


            self.state = 1581
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Extern_alias_directivesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def extern_alias_directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Extern_alias_directiveContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Extern_alias_directiveContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_extern_alias_directives

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtern_alias_directives" ):
                listener.enterExtern_alias_directives(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtern_alias_directives" ):
                listener.exitExtern_alias_directives(self)




    def extern_alias_directives(self):

        localctx = CSharpParser.Extern_alias_directivesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_extern_alias_directives)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1584 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1583
                    self.extern_alias_directive()

                else:
                    raise NoViableAltException(self)
                self.state = 1586 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,172,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Extern_alias_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTERN(self):
            return self.getToken(CSharpParser.EXTERN, 0)

        def ALIAS(self):
            return self.getToken(CSharpParser.ALIAS, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_extern_alias_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtern_alias_directive" ):
                listener.enterExtern_alias_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtern_alias_directive" ):
                listener.exitExtern_alias_directive(self)




    def extern_alias_directive(self):

        localctx = CSharpParser.Extern_alias_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_extern_alias_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1588
            self.match(CSharpParser.EXTERN)
            self.state = 1589
            self.match(CSharpParser.ALIAS)
            self.state = 1590
            self.identifier()
            self.state = 1591
            self.match(CSharpParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Using_directivesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def using_directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Using_directiveContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Using_directiveContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_using_directives

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsing_directives" ):
                listener.enterUsing_directives(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsing_directives" ):
                listener.exitUsing_directives(self)




    def using_directives(self):

        localctx = CSharpParser.Using_directivesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_using_directives)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1594 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1593
                self.using_directive()
                self.state = 1596 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSharpParser.USING):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Using_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSharpParser.RULE_using_directive

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class UsingAliasDirectiveContext(Using_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Using_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def USING(self):
            return self.getToken(CSharpParser.USING, 0)
        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)

        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)
        def namespace_or_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,0)

        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsingAliasDirective" ):
                listener.enterUsingAliasDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsingAliasDirective" ):
                listener.exitUsingAliasDirective(self)


    class UsingNamespaceDirectiveContext(Using_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Using_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def USING(self):
            return self.getToken(CSharpParser.USING, 0)
        def namespace_or_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,0)

        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsingNamespaceDirective" ):
                listener.enterUsingNamespaceDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsingNamespaceDirective" ):
                listener.exitUsingNamespaceDirective(self)


    class UsingStaticDirectiveContext(Using_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Using_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def USING(self):
            return self.getToken(CSharpParser.USING, 0)
        def STATIC(self):
            return self.getToken(CSharpParser.STATIC, 0)
        def namespace_or_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,0)

        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsingStaticDirective" ):
                listener.enterUsingStaticDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsingStaticDirective" ):
                listener.exitUsingStaticDirective(self)



    def using_directive(self):

        localctx = CSharpParser.Using_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_using_directive)
        try:
            self.state = 1613
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,174,self._ctx)
            if la_ == 1:
                localctx = CSharpParser.UsingAliasDirectiveContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1598
                self.match(CSharpParser.USING)
                self.state = 1599
                self.identifier()
                self.state = 1600
                self.match(CSharpParser.ASSIGNMENT)
                self.state = 1601
                self.namespace_or_type_name()
                self.state = 1602
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 2:
                localctx = CSharpParser.UsingNamespaceDirectiveContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1604
                self.match(CSharpParser.USING)
                self.state = 1605
                self.namespace_or_type_name()
                self.state = 1606
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 3:
                localctx = CSharpParser.UsingStaticDirectiveContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1608
                self.match(CSharpParser.USING)
                self.state = 1609
                self.match(CSharpParser.STATIC)
                self.state = 1610
                self.namespace_or_type_name()
                self.state = 1611
                self.match(CSharpParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Namespace_member_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace_member_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Namespace_member_declarationContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Namespace_member_declarationContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_namespace_member_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace_member_declarations" ):
                listener.enterNamespace_member_declarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace_member_declarations" ):
                listener.exitNamespace_member_declarations(self)




    def namespace_member_declarations(self):

        localctx = CSharpParser.Namespace_member_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_namespace_member_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1616 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1615
                self.namespace_member_declaration()
                self.state = 1618 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.CLASS) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.ENUM) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.INTERFACE) | (1 << CSharpParser.INTERNAL))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NAMESPACE - 65)) | (1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.OVERRIDE - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.PRIVATE - 65)) | (1 << (CSharpParser.PROTECTED - 65)) | (1 << (CSharpParser.PUBLIC - 65)) | (1 << (CSharpParser.READONLY - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.SEALED - 65)) | (1 << (CSharpParser.STATIC - 65)) | (1 << (CSharpParser.STRUCT - 65)) | (1 << (CSharpParser.UNSAFE - 65)) | (1 << (CSharpParser.VIRTUAL - 65)) | (1 << (CSharpParser.VOLATILE - 65)) | (1 << (CSharpParser.OPEN_BRACKET - 65)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Namespace_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_declarationContext,0)


        def type_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Type_declarationContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_namespace_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace_member_declaration" ):
                listener.enterNamespace_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace_member_declaration" ):
                listener.exitNamespace_member_declaration(self)




    def namespace_member_declaration(self):

        localctx = CSharpParser.Namespace_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_namespace_member_declaration)
        try:
            self.state = 1622
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.NAMESPACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1620
                self.namespace_declaration()
                pass
            elif token in [CSharpParser.ABSTRACT, CSharpParser.ASYNC, CSharpParser.CLASS, CSharpParser.DELEGATE, CSharpParser.ENUM, CSharpParser.EXTERN, CSharpParser.INTERFACE, CSharpParser.INTERNAL, CSharpParser.NEW, CSharpParser.OVERRIDE, CSharpParser.PARTIAL, CSharpParser.PRIVATE, CSharpParser.PROTECTED, CSharpParser.PUBLIC, CSharpParser.READONLY, CSharpParser.REF, CSharpParser.SEALED, CSharpParser.STATIC, CSharpParser.STRUCT, CSharpParser.UNSAFE, CSharpParser.VIRTUAL, CSharpParser.VOLATILE, CSharpParser.OPEN_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1621
                self.type_declaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_definition(self):
            return self.getTypedRuleContext(CSharpParser.Class_definitionContext,0)


        def struct_definition(self):
            return self.getTypedRuleContext(CSharpParser.Struct_definitionContext,0)


        def interface_definition(self):
            return self.getTypedRuleContext(CSharpParser.Interface_definitionContext,0)


        def enum_definition(self):
            return self.getTypedRuleContext(CSharpParser.Enum_definitionContext,0)


        def delegate_definition(self):
            return self.getTypedRuleContext(CSharpParser.Delegate_definitionContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def all_member_modifiers(self):
            return self.getTypedRuleContext(CSharpParser.All_member_modifiersContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_type_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_declaration" ):
                listener.enterType_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_declaration" ):
                listener.exitType_declaration(self)




    def type_declaration(self):

        localctx = CSharpParser.Type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_type_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1625
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1624
                self.attributes()


            self.state = 1628
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,178,self._ctx)
            if la_ == 1:
                self.state = 1627
                self.all_member_modifiers()


            self.state = 1635
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.CLASS]:
                self.state = 1630
                self.class_definition()
                pass
            elif token in [CSharpParser.READONLY, CSharpParser.REF, CSharpParser.STRUCT]:
                self.state = 1631
                self.struct_definition()
                pass
            elif token in [CSharpParser.INTERFACE]:
                self.state = 1632
                self.interface_definition()
                pass
            elif token in [CSharpParser.ENUM]:
                self.state = 1633
                self.enum_definition()
                pass
            elif token in [CSharpParser.DELEGATE]:
                self.state = 1634
                self.delegate_definition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Qualified_alias_memberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def DOUBLE_COLON(self):
            return self.getToken(CSharpParser.DOUBLE_COLON, 0)

        def type_argument_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_argument_listContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_qualified_alias_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualified_alias_member" ):
                listener.enterQualified_alias_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualified_alias_member" ):
                listener.exitQualified_alias_member(self)




    def qualified_alias_member(self):

        localctx = CSharpParser.Qualified_alias_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_qualified_alias_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1637
            self.identifier()
            self.state = 1638
            self.match(CSharpParser.DOUBLE_COLON)
            self.state = 1639
            self.identifier()
            self.state = 1641
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,180,self._ctx)
            if la_ == 1:
                self.state = 1640
                self.type_argument_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(CSharpParser.LT, 0)

        def type_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Type_parameterContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Type_parameterContext,i)


        def GT(self):
            return self.getToken(CSharpParser.GT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_type_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_parameter_list" ):
                listener.enterType_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_parameter_list" ):
                listener.exitType_parameter_list(self)




    def type_parameter_list(self):

        localctx = CSharpParser.Type_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_type_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1643
            self.match(CSharpParser.LT)
            self.state = 1644
            self.type_parameter()
            self.state = 1649
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1645
                self.match(CSharpParser.COMMA)
                self.state = 1646
                self.type_parameter()
                self.state = 1651
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1652
            self.match(CSharpParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_type_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_parameter" ):
                listener.enterType_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_parameter" ):
                listener.exitType_parameter(self)




    def type_parameter(self):

        localctx = CSharpParser.Type_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_type_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1655
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1654
                self.attributes()


            self.state = 1657
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_baseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def class_type(self):
            return self.getTypedRuleContext(CSharpParser.Class_typeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def namespace_or_type_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Namespace_or_type_nameContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_class_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_base" ):
                listener.enterClass_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_base" ):
                listener.exitClass_base(self)




    def class_base(self):

        localctx = CSharpParser.Class_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_class_base)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1659
            self.match(CSharpParser.COLON)
            self.state = 1660
            self.class_type()
            self.state = 1665
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1661
                self.match(CSharpParser.COMMA)
                self.state = 1662
                self.namespace_or_type_name()
                self.state = 1667
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_type_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace_or_type_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Namespace_or_type_nameContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_interface_type_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_type_list" ):
                listener.enterInterface_type_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_type_list" ):
                listener.exitInterface_type_list(self)




    def interface_type_list(self):

        localctx = CSharpParser.Interface_type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_interface_type_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1668
            self.namespace_or_type_name()
            self.state = 1673
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1669
                self.match(CSharpParser.COMMA)
                self.state = 1670
                self.namespace_or_type_name()
                self.state = 1675
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_parameter_constraints_clausesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_parameter_constraints_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Type_parameter_constraints_clauseContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clauseContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_type_parameter_constraints_clauses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_parameter_constraints_clauses" ):
                listener.enterType_parameter_constraints_clauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_parameter_constraints_clauses" ):
                listener.exitType_parameter_constraints_clauses(self)




    def type_parameter_constraints_clauses(self):

        localctx = CSharpParser.Type_parameter_constraints_clausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_type_parameter_constraints_clauses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1677 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1676
                self.type_parameter_constraints_clause()
                self.state = 1679 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSharpParser.WHERE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_parameter_constraints_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(CSharpParser.WHERE, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def type_parameter_constraints(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraintsContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_type_parameter_constraints_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_parameter_constraints_clause" ):
                listener.enterType_parameter_constraints_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_parameter_constraints_clause" ):
                listener.exitType_parameter_constraints_clause(self)




    def type_parameter_constraints_clause(self):

        localctx = CSharpParser.Type_parameter_constraints_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_type_parameter_constraints_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1681
            self.match(CSharpParser.WHERE)
            self.state = 1682
            self.identifier()
            self.state = 1683
            self.match(CSharpParser.COLON)
            self.state = 1684
            self.type_parameter_constraints()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_parameter_constraintsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constructor_constraint(self):
            return self.getTypedRuleContext(CSharpParser.Constructor_constraintContext,0)


        def primary_constraint(self):
            return self.getTypedRuleContext(CSharpParser.Primary_constraintContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def secondary_constraints(self):
            return self.getTypedRuleContext(CSharpParser.Secondary_constraintsContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_type_parameter_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_parameter_constraints" ):
                listener.enterType_parameter_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_parameter_constraints" ):
                listener.exitType_parameter_constraints(self)




    def type_parameter_constraints(self):

        localctx = CSharpParser.Type_parameter_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_type_parameter_constraints)
        self._la = 0 # Token type
        try:
            self.state = 1696
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1686
                self.constructor_constraint()
                pass
            elif token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BY, CSharpParser.CLASS, CSharpParser.DESCENDING, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.STRING, CSharpParser.STRUCT, CSharpParser.UNMANAGED, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1687
                self.primary_constraint()
                self.state = 1690
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,186,self._ctx)
                if la_ == 1:
                    self.state = 1688
                    self.match(CSharpParser.COMMA)
                    self.state = 1689
                    self.secondary_constraints()


                self.state = 1694
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.COMMA:
                    self.state = 1692
                    self.match(CSharpParser.COMMA)
                    self.state = 1693
                    self.constructor_constraint()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_type(self):
            return self.getTypedRuleContext(CSharpParser.Class_typeContext,0)


        def CLASS(self):
            return self.getToken(CSharpParser.CLASS, 0)

        def INTERR(self):
            return self.getToken(CSharpParser.INTERR, 0)

        def STRUCT(self):
            return self.getToken(CSharpParser.STRUCT, 0)

        def UNMANAGED(self):
            return self.getToken(CSharpParser.UNMANAGED, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_primary_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_constraint" ):
                listener.enterPrimary_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_constraint" ):
                listener.exitPrimary_constraint(self)




    def primary_constraint(self):

        localctx = CSharpParser.Primary_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_primary_constraint)
        self._la = 0 # Token type
        try:
            self.state = 1705
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,190,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1698
                self.class_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1699
                self.match(CSharpParser.CLASS)
                self.state = 1701
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.INTERR:
                    self.state = 1700
                    self.match(CSharpParser.INTERR)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1703
                self.match(CSharpParser.STRUCT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1704
                self.match(CSharpParser.UNMANAGED)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Secondary_constraintsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace_or_type_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Namespace_or_type_nameContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_secondary_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSecondary_constraints" ):
                listener.enterSecondary_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSecondary_constraints" ):
                listener.exitSecondary_constraints(self)




    def secondary_constraints(self):

        localctx = CSharpParser.Secondary_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_secondary_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1707
            self.namespace_or_type_name()
            self.state = 1712
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,191,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1708
                    self.match(CSharpParser.COMMA)
                    self.state = 1709
                    self.namespace_or_type_name() 
                self.state = 1714
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,191,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSharpParser.NEW, 0)

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_constructor_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructor_constraint" ):
                listener.enterConstructor_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructor_constraint" ):
                listener.exitConstructor_constraint(self)




    def constructor_constraint(self):

        localctx = CSharpParser.Constructor_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_constructor_constraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1715
            self.match(CSharpParser.NEW)
            self.state = 1716
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 1717
            self.match(CSharpParser.CLOSE_PARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def class_member_declarations(self):
            return self.getTypedRuleContext(CSharpParser.Class_member_declarationsContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_class_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_body" ):
                listener.enterClass_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_body" ):
                listener.exitClass_body(self)




    def class_body(self):

        localctx = CSharpParser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1719
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 1721
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CLASS) | (1 << CSharpParser.CONST) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.ENUM) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.EVENT) | (1 << CSharpParser.EXPLICIT) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IMPLICIT) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTERFACE) | (1 << CSharpParser.INTERNAL) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.OVERRIDE - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.PRIVATE - 64)) | (1 << (CSharpParser.PROTECTED - 64)) | (1 << (CSharpParser.PUBLIC - 64)) | (1 << (CSharpParser.READONLY - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SEALED - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.STATIC - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.STRUCT - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.UNSAFE - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.VIRTUAL - 64)) | (1 << (CSharpParser.VOID - 64)) | (1 << (CSharpParser.VOLATILE - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.OPEN_BRACKET - 64)))) != 0) or _la==CSharpParser.OPEN_PARENS or _la==CSharpParser.TILDE:
                self.state = 1720
                self.class_member_declarations()


            self.state = 1723
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_member_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_member_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Class_member_declarationContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Class_member_declarationContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_class_member_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_member_declarations" ):
                listener.enterClass_member_declarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_member_declarations" ):
                listener.exitClass_member_declarations(self)




    def class_member_declarations(self):

        localctx = CSharpParser.Class_member_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_class_member_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1726 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1725
                self.class_member_declaration()
                self.state = 1728 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CLASS) | (1 << CSharpParser.CONST) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.ENUM) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.EVENT) | (1 << CSharpParser.EXPLICIT) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IMPLICIT) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTERFACE) | (1 << CSharpParser.INTERNAL) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.OVERRIDE - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.PRIVATE - 64)) | (1 << (CSharpParser.PROTECTED - 64)) | (1 << (CSharpParser.PUBLIC - 64)) | (1 << (CSharpParser.READONLY - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SEALED - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.STATIC - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.STRUCT - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.UNSAFE - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.VIRTUAL - 64)) | (1 << (CSharpParser.VOID - 64)) | (1 << (CSharpParser.VOLATILE - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.OPEN_BRACKET - 64)))) != 0) or _la==CSharpParser.OPEN_PARENS or _la==CSharpParser.TILDE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def common_member_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Common_member_declarationContext,0)


        def destructor_definition(self):
            return self.getTypedRuleContext(CSharpParser.Destructor_definitionContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def all_member_modifiers(self):
            return self.getTypedRuleContext(CSharpParser.All_member_modifiersContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_class_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_member_declaration" ):
                listener.enterClass_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_member_declaration" ):
                listener.exitClass_member_declaration(self)




    def class_member_declaration(self):

        localctx = CSharpParser.Class_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_class_member_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1731
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1730
                self.attributes()


            self.state = 1734
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,195,self._ctx)
            if la_ == 1:
                self.state = 1733
                self.all_member_modifiers()


            self.state = 1738
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CLASS, CSharpParser.CONST, CSharpParser.DECIMAL, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.ENUM, CSharpParser.EQUALS, CSharpParser.EVENT, CSharpParser.EXPLICIT, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.IMPLICIT, CSharpParser.INT, CSharpParser.INTERFACE, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.READONLY, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.STRING, CSharpParser.STRUCT, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.VOID, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.OPEN_PARENS]:
                self.state = 1736
                self.common_member_declaration()
                pass
            elif token in [CSharpParser.TILDE]:
                self.state = 1737
                self.destructor_definition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_member_modifiersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_member_modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.All_member_modifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.All_member_modifierContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_all_member_modifiers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_member_modifiers" ):
                listener.enterAll_member_modifiers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_member_modifiers" ):
                listener.exitAll_member_modifiers(self)




    def all_member_modifiers(self):

        localctx = CSharpParser.All_member_modifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_all_member_modifiers)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1741 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1740
                    self.all_member_modifier()

                else:
                    raise NoViableAltException(self)
                self.state = 1743 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,197,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_member_modifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSharpParser.NEW, 0)

        def PUBLIC(self):
            return self.getToken(CSharpParser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(CSharpParser.PROTECTED, 0)

        def INTERNAL(self):
            return self.getToken(CSharpParser.INTERNAL, 0)

        def PRIVATE(self):
            return self.getToken(CSharpParser.PRIVATE, 0)

        def READONLY(self):
            return self.getToken(CSharpParser.READONLY, 0)

        def VOLATILE(self):
            return self.getToken(CSharpParser.VOLATILE, 0)

        def VIRTUAL(self):
            return self.getToken(CSharpParser.VIRTUAL, 0)

        def SEALED(self):
            return self.getToken(CSharpParser.SEALED, 0)

        def OVERRIDE(self):
            return self.getToken(CSharpParser.OVERRIDE, 0)

        def ABSTRACT(self):
            return self.getToken(CSharpParser.ABSTRACT, 0)

        def STATIC(self):
            return self.getToken(CSharpParser.STATIC, 0)

        def UNSAFE(self):
            return self.getToken(CSharpParser.UNSAFE, 0)

        def EXTERN(self):
            return self.getToken(CSharpParser.EXTERN, 0)

        def PARTIAL(self):
            return self.getToken(CSharpParser.PARTIAL, 0)

        def ASYNC(self):
            return self.getToken(CSharpParser.ASYNC, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_all_member_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_member_modifier" ):
                listener.enterAll_member_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_member_modifier" ):
                listener.exitAll_member_modifier(self)




    def all_member_modifier(self):

        localctx = CSharpParser.All_member_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_all_member_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1745
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.INTERNAL))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CSharpParser.NEW - 66)) | (1 << (CSharpParser.OVERRIDE - 66)) | (1 << (CSharpParser.PARTIAL - 66)) | (1 << (CSharpParser.PRIVATE - 66)) | (1 << (CSharpParser.PROTECTED - 66)) | (1 << (CSharpParser.PUBLIC - 66)) | (1 << (CSharpParser.READONLY - 66)) | (1 << (CSharpParser.SEALED - 66)) | (1 << (CSharpParser.STATIC - 66)) | (1 << (CSharpParser.UNSAFE - 66)) | (1 << (CSharpParser.VIRTUAL - 66)) | (1 << (CSharpParser.VOLATILE - 66)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Common_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Constant_declarationContext,0)


        def typed_member_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Typed_member_declarationContext,0)


        def event_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Event_declarationContext,0)


        def conversion_operator_declarator(self):
            return self.getTypedRuleContext(CSharpParser.Conversion_operator_declaratorContext,0)


        def body(self):
            return self.getTypedRuleContext(CSharpParser.BodyContext,0)


        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def constructor_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Constructor_declarationContext,0)


        def VOID(self):
            return self.getToken(CSharpParser.VOID, 0)

        def method_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Method_declarationContext,0)


        def class_definition(self):
            return self.getTypedRuleContext(CSharpParser.Class_definitionContext,0)


        def struct_definition(self):
            return self.getTypedRuleContext(CSharpParser.Struct_definitionContext,0)


        def interface_definition(self):
            return self.getTypedRuleContext(CSharpParser.Interface_definitionContext,0)


        def enum_definition(self):
            return self.getTypedRuleContext(CSharpParser.Enum_definitionContext,0)


        def delegate_definition(self):
            return self.getTypedRuleContext(CSharpParser.Delegate_definitionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_common_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommon_member_declaration" ):
                listener.enterCommon_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommon_member_declaration" ):
                listener.exitCommon_member_declaration(self)




    def common_member_declaration(self):

        localctx = CSharpParser.Common_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_common_member_declaration)
        try:
            self.state = 1766
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,199,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1747
                self.constant_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1748
                self.typed_member_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1749
                self.event_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1750
                self.conversion_operator_declarator()
                self.state = 1756
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.OPEN_BRACE, CSharpParser.SEMICOLON]:
                    self.state = 1751
                    self.body()
                    pass
                elif token in [CSharpParser.ASSIGNMENT]:
                    self.state = 1752
                    self.right_arrow()
                    self.state = 1753
                    self.throwable_expression()
                    self.state = 1754
                    self.match(CSharpParser.SEMICOLON)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1758
                self.constructor_declaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1759
                self.match(CSharpParser.VOID)
                self.state = 1760
                self.method_declaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1761
                self.class_definition()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1762
                self.struct_definition()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1763
                self.interface_definition()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1764
                self.enum_definition()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 1765
                self.delegate_definition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Typed_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def namespace_or_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,0)


        def DOT(self):
            return self.getToken(CSharpParser.DOT, 0)

        def indexer_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Indexer_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Method_declarationContext,0)


        def property_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Property_declarationContext,0)


        def operator_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Operator_declarationContext,0)


        def field_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Field_declarationContext,0)


        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def READONLY(self):
            return self.getToken(CSharpParser.READONLY, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_typed_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyped_member_declaration" ):
                listener.enterTyped_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyped_member_declaration" ):
                listener.exitTyped_member_declaration(self)




    def typed_member_declaration(self):

        localctx = CSharpParser.Typed_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_typed_member_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1773
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,200,self._ctx)
            if la_ == 1:
                self.state = 1768
                self.match(CSharpParser.REF)

            elif la_ == 2:
                self.state = 1769
                self.match(CSharpParser.READONLY)
                self.state = 1770
                self.match(CSharpParser.REF)

            elif la_ == 3:
                self.state = 1771
                self.match(CSharpParser.REF)
                self.state = 1772
                self.match(CSharpParser.READONLY)


            self.state = 1775
            self.type_()
            self.state = 1785
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,201,self._ctx)
            if la_ == 1:
                self.state = 1776
                self.namespace_or_type_name()
                self.state = 1777
                self.match(CSharpParser.DOT)
                self.state = 1778
                self.indexer_declaration()
                pass

            elif la_ == 2:
                self.state = 1780
                self.method_declaration()
                pass

            elif la_ == 3:
                self.state = 1781
                self.property_declaration()
                pass

            elif la_ == 4:
                self.state = 1782
                self.indexer_declaration()
                pass

            elif la_ == 5:
                self.state = 1783
                self.operator_declaration()
                pass

            elif la_ == 6:
                self.state = 1784
                self.field_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_declaratorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant_declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Constant_declaratorContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Constant_declaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_constant_declarators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant_declarators" ):
                listener.enterConstant_declarators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant_declarators" ):
                listener.exitConstant_declarators(self)




    def constant_declarators(self):

        localctx = CSharpParser.Constant_declaratorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_constant_declarators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1787
            self.constant_declarator()
            self.state = 1792
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1788
                self.match(CSharpParser.COMMA)
                self.state = 1789
                self.constant_declarator()
                self.state = 1794
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_declaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_constant_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant_declarator" ):
                listener.enterConstant_declarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant_declarator" ):
                listener.exitConstant_declarator(self)




    def constant_declarator(self):

        localctx = CSharpParser.Constant_declaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_constant_declarator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1795
            self.identifier()
            self.state = 1796
            self.match(CSharpParser.ASSIGNMENT)
            self.state = 1797
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declaratorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Variable_declaratorContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Variable_declaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_variable_declarators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declarators" ):
                listener.enterVariable_declarators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declarators" ):
                listener.exitVariable_declarators(self)




    def variable_declarators(self):

        localctx = CSharpParser.Variable_declaratorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_variable_declarators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1799
            self.variable_declarator()
            self.state = 1804
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1800
                self.match(CSharpParser.COMMA)
                self.state = 1801
                self.variable_declarator()
                self.state = 1806
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def variable_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Variable_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_variable_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declarator" ):
                listener.enterVariable_declarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declarator" ):
                listener.exitVariable_declarator(self)




    def variable_declarator(self):

        localctx = CSharpParser.Variable_declaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_variable_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1807
            self.identifier()
            self.state = 1810
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.ASSIGNMENT:
                self.state = 1808
                self.match(CSharpParser.ASSIGNMENT)
                self.state = 1809
                self.variable_initializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def array_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Array_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_variable_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_initializer" ):
                listener.enterVariable_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_initializer" ):
                listener.exitVariable_initializer(self)




    def variable_initializer(self):

        localctx = CSharpParser.Variable_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_variable_initializer)
        try:
            self.state = 1814
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1812
                self.expression()
                pass
            elif token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1813
                self.array_initializer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def VOID(self):
            return self.getToken(CSharpParser.VOID, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_return_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_type" ):
                listener.enterReturn_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_type" ):
                listener.exitReturn_type(self)




    def return_type(self):

        localctx = CSharpParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_return_type)
        try:
            self.state = 1818
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,206,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1816
                self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1817
                self.match(CSharpParser.VOID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace_or_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_member_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_name" ):
                listener.enterMember_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_name" ):
                listener.exitMember_name(self)




    def member_name(self):

        localctx = CSharpParser.Member_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_member_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1820
            self.namespace_or_type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_method_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_body" ):
                listener.enterMethod_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_body" ):
                listener.exitMethod_body(self)




    def method_body(self):

        localctx = CSharpParser.Method_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_method_body)
        try:
            self.state = 1824
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1822
                self.block()
                pass
            elif token in [CSharpParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1823
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Formal_parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_array(self):
            return self.getTypedRuleContext(CSharpParser.Parameter_arrayContext,0)


        def fixed_parameters(self):
            return self.getTypedRuleContext(CSharpParser.Fixed_parametersContext,0)


        def COMMA(self):
            return self.getToken(CSharpParser.COMMA, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_formal_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal_parameter_list" ):
                listener.enterFormal_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal_parameter_list" ):
                listener.exitFormal_parameter_list(self)




    def formal_parameter_list(self):

        localctx = CSharpParser.Formal_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_formal_parameter_list)
        self._la = 0 # Token type
        try:
            self.state = 1832
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,209,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1826
                self.parameter_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1827
                self.fixed_parameters()
                self.state = 1830
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.COMMA:
                    self.state = 1828
                    self.match(CSharpParser.COMMA)
                    self.state = 1829
                    self.parameter_array()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixed_parametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fixed_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Fixed_parameterContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Fixed_parameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_fixed_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixed_parameters" ):
                listener.enterFixed_parameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixed_parameters" ):
                listener.exitFixed_parameters(self)




    def fixed_parameters(self):

        localctx = CSharpParser.Fixed_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_fixed_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1834
            self.fixed_parameter()
            self.state = 1839
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,210,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1835
                    self.match(CSharpParser.COMMA)
                    self.state = 1836
                    self.fixed_parameter() 
                self.state = 1841
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,210,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixed_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Arg_declarationContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def parameter_modifier(self):
            return self.getTypedRuleContext(CSharpParser.Parameter_modifierContext,0)


        def ARGLIST(self):
            return self.getToken(CSharpParser.ARGLIST, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_fixed_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixed_parameter" ):
                listener.enterFixed_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixed_parameter" ):
                listener.exitFixed_parameter(self)




    def fixed_parameter(self):

        localctx = CSharpParser.Fixed_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_fixed_parameter)
        self._la = 0 # Token type
        try:
            self.state = 1850
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,213,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1843
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.OPEN_BRACKET:
                    self.state = 1842
                    self.attributes()


                self.state = 1846
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 54)) & ~0x3f) == 0 and ((1 << (_la - 54)) & ((1 << (CSharpParser.IN - 54)) | (1 << (CSharpParser.OUT - 54)) | (1 << (CSharpParser.REF - 54)) | (1 << (CSharpParser.THIS - 54)))) != 0):
                    self.state = 1845
                    self.parameter_modifier()


                self.state = 1848
                self.arg_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1849
                self.match(CSharpParser.ARGLIST)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_modifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def OUT(self):
            return self.getToken(CSharpParser.OUT, 0)

        def IN(self):
            return self.getToken(CSharpParser.IN, 0)

        def THIS(self):
            return self.getToken(CSharpParser.THIS, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_parameter_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_modifier" ):
                listener.enterParameter_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_modifier" ):
                listener.exitParameter_modifier(self)




    def parameter_modifier(self):

        localctx = CSharpParser.Parameter_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_parameter_modifier)
        try:
            self.state = 1860
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,214,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1852
                self.match(CSharpParser.REF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1853
                self.match(CSharpParser.OUT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1854
                self.match(CSharpParser.IN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1855
                self.match(CSharpParser.REF)
                self.state = 1856
                self.match(CSharpParser.THIS)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1857
                self.match(CSharpParser.IN)
                self.state = 1858
                self.match(CSharpParser.THIS)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1859
                self.match(CSharpParser.THIS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMS(self):
            return self.getToken(CSharpParser.PARAMS, 0)

        def array_type(self):
            return self.getTypedRuleContext(CSharpParser.Array_typeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_parameter_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_array" ):
                listener.enterParameter_array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_array" ):
                listener.exitParameter_array(self)




    def parameter_array(self):

        localctx = CSharpParser.Parameter_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_parameter_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1863
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1862
                self.attributes()


            self.state = 1865
            self.match(CSharpParser.PARAMS)
            self.state = 1866
            self.array_type()
            self.state = 1867
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Accessor_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.attrs = None # AttributesContext
            self.mods = None # Accessor_modifierContext

        def GET(self):
            return self.getToken(CSharpParser.GET, 0)

        def accessor_body(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_bodyContext,0)


        def SET(self):
            return self.getToken(CSharpParser.SET, 0)

        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def accessor_modifier(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_modifierContext,0)


        def set_accessor_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Set_accessor_declarationContext,0)


        def get_accessor_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Get_accessor_declarationContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_accessor_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessor_declarations" ):
                listener.enterAccessor_declarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessor_declarations" ):
                listener.exitAccessor_declarations(self)




    def accessor_declarations(self):

        localctx = CSharpParser.Accessor_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_accessor_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1870
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1869
                localctx.attrs = self.attributes()


            self.state = 1873
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 57)) & ~0x3f) == 0 and ((1 << (_la - 57)) & ((1 << (CSharpParser.INTERNAL - 57)) | (1 << (CSharpParser.PRIVATE - 57)) | (1 << (CSharpParser.PROTECTED - 57)))) != 0):
                self.state = 1872
                localctx.mods = self.accessor_modifier()


            self.state = 1885
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.GET]:
                self.state = 1875
                self.match(CSharpParser.GET)
                self.state = 1876
                self.accessor_body()
                self.state = 1878
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.INTERNAL or ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (CSharpParser.PRIVATE - 76)) | (1 << (CSharpParser.PROTECTED - 76)) | (1 << (CSharpParser.SET - 76)) | (1 << (CSharpParser.OPEN_BRACKET - 76)))) != 0):
                    self.state = 1877
                    self.set_accessor_declaration()


                pass
            elif token in [CSharpParser.SET]:
                self.state = 1880
                self.match(CSharpParser.SET)
                self.state = 1881
                self.accessor_body()
                self.state = 1883
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.GET or _la==CSharpParser.INTERNAL or ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (CSharpParser.PRIVATE - 76)) | (1 << (CSharpParser.PROTECTED - 76)) | (1 << (CSharpParser.OPEN_BRACKET - 76)))) != 0):
                    self.state = 1882
                    self.get_accessor_declaration()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Get_accessor_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GET(self):
            return self.getToken(CSharpParser.GET, 0)

        def accessor_body(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_bodyContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def accessor_modifier(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_modifierContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_get_accessor_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGet_accessor_declaration" ):
                listener.enterGet_accessor_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGet_accessor_declaration" ):
                listener.exitGet_accessor_declaration(self)




    def get_accessor_declaration(self):

        localctx = CSharpParser.Get_accessor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_get_accessor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1888
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1887
                self.attributes()


            self.state = 1891
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 57)) & ~0x3f) == 0 and ((1 << (_la - 57)) & ((1 << (CSharpParser.INTERNAL - 57)) | (1 << (CSharpParser.PRIVATE - 57)) | (1 << (CSharpParser.PROTECTED - 57)))) != 0):
                self.state = 1890
                self.accessor_modifier()


            self.state = 1893
            self.match(CSharpParser.GET)
            self.state = 1894
            self.accessor_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_accessor_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(CSharpParser.SET, 0)

        def accessor_body(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_bodyContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def accessor_modifier(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_modifierContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_set_accessor_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_accessor_declaration" ):
                listener.enterSet_accessor_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_accessor_declaration" ):
                listener.exitSet_accessor_declaration(self)




    def set_accessor_declaration(self):

        localctx = CSharpParser.Set_accessor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_set_accessor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1897
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1896
                self.attributes()


            self.state = 1900
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 57)) & ~0x3f) == 0 and ((1 << (_la - 57)) & ((1 << (CSharpParser.INTERNAL - 57)) | (1 << (CSharpParser.PRIVATE - 57)) | (1 << (CSharpParser.PROTECTED - 57)))) != 0):
                self.state = 1899
                self.accessor_modifier()


            self.state = 1902
            self.match(CSharpParser.SET)
            self.state = 1903
            self.accessor_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Accessor_modifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROTECTED(self):
            return self.getToken(CSharpParser.PROTECTED, 0)

        def INTERNAL(self):
            return self.getToken(CSharpParser.INTERNAL, 0)

        def PRIVATE(self):
            return self.getToken(CSharpParser.PRIVATE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_accessor_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessor_modifier" ):
                listener.enterAccessor_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessor_modifier" ):
                listener.exitAccessor_modifier(self)




    def accessor_modifier(self):

        localctx = CSharpParser.Accessor_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_accessor_modifier)
        try:
            self.state = 1912
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,225,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1905
                self.match(CSharpParser.PROTECTED)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1906
                self.match(CSharpParser.INTERNAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1907
                self.match(CSharpParser.PRIVATE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1908
                self.match(CSharpParser.PROTECTED)
                self.state = 1909
                self.match(CSharpParser.INTERNAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1910
                self.match(CSharpParser.INTERNAL)
                self.state = 1911
                self.match(CSharpParser.PROTECTED)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Accessor_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_accessor_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessor_body" ):
                listener.enterAccessor_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessor_body" ):
                listener.exitAccessor_body(self)




    def accessor_body(self):

        localctx = CSharpParser.Accessor_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_accessor_body)
        try:
            self.state = 1916
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1914
                self.block()
                pass
            elif token in [CSharpParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1915
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Event_accessor_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(CSharpParser.ADD, 0)

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def remove_accessor_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Remove_accessor_declarationContext,0)


        def REMOVE(self):
            return self.getToken(CSharpParser.REMOVE, 0)

        def add_accessor_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Add_accessor_declarationContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_event_accessor_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent_accessor_declarations" ):
                listener.enterEvent_accessor_declarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent_accessor_declarations" ):
                listener.exitEvent_accessor_declarations(self)




    def event_accessor_declarations(self):

        localctx = CSharpParser.Event_accessor_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_event_accessor_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1919
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1918
                self.attributes()


            self.state = 1929
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD]:
                self.state = 1921
                self.match(CSharpParser.ADD)
                self.state = 1922
                self.block()
                self.state = 1923
                self.remove_accessor_declaration()
                pass
            elif token in [CSharpParser.REMOVE]:
                self.state = 1925
                self.match(CSharpParser.REMOVE)
                self.state = 1926
                self.block()
                self.state = 1927
                self.add_accessor_declaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_accessor_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(CSharpParser.ADD, 0)

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_add_accessor_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_accessor_declaration" ):
                listener.enterAdd_accessor_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_accessor_declaration" ):
                listener.exitAdd_accessor_declaration(self)




    def add_accessor_declaration(self):

        localctx = CSharpParser.Add_accessor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_add_accessor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1932
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1931
                self.attributes()


            self.state = 1934
            self.match(CSharpParser.ADD)
            self.state = 1935
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Remove_accessor_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REMOVE(self):
            return self.getToken(CSharpParser.REMOVE, 0)

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_remove_accessor_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemove_accessor_declaration" ):
                listener.enterRemove_accessor_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemove_accessor_declaration" ):
                listener.exitRemove_accessor_declaration(self)




    def remove_accessor_declaration(self):

        localctx = CSharpParser.Remove_accessor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_remove_accessor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1938
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1937
                self.attributes()


            self.state = 1940
            self.match(CSharpParser.REMOVE)
            self.state = 1941
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Overloadable_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(CSharpParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CSharpParser.MINUS, 0)

        def BANG(self):
            return self.getToken(CSharpParser.BANG, 0)

        def TILDE(self):
            return self.getToken(CSharpParser.TILDE, 0)

        def OP_INC(self):
            return self.getToken(CSharpParser.OP_INC, 0)

        def OP_DEC(self):
            return self.getToken(CSharpParser.OP_DEC, 0)

        def TRUE(self):
            return self.getToken(CSharpParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSharpParser.FALSE, 0)

        def STAR(self):
            return self.getToken(CSharpParser.STAR, 0)

        def DIV(self):
            return self.getToken(CSharpParser.DIV, 0)

        def PERCENT(self):
            return self.getToken(CSharpParser.PERCENT, 0)

        def AMP(self):
            return self.getToken(CSharpParser.AMP, 0)

        def BITWISE_OR(self):
            return self.getToken(CSharpParser.BITWISE_OR, 0)

        def CARET(self):
            return self.getToken(CSharpParser.CARET, 0)

        def OP_LEFT_SHIFT(self):
            return self.getToken(CSharpParser.OP_LEFT_SHIFT, 0)

        def right_shift(self):
            return self.getTypedRuleContext(CSharpParser.Right_shiftContext,0)


        def OP_EQ(self):
            return self.getToken(CSharpParser.OP_EQ, 0)

        def OP_NE(self):
            return self.getToken(CSharpParser.OP_NE, 0)

        def GT(self):
            return self.getToken(CSharpParser.GT, 0)

        def LT(self):
            return self.getToken(CSharpParser.LT, 0)

        def OP_GE(self):
            return self.getToken(CSharpParser.OP_GE, 0)

        def OP_LE(self):
            return self.getToken(CSharpParser.OP_LE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_overloadable_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOverloadable_operator" ):
                listener.enterOverloadable_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOverloadable_operator" ):
                listener.exitOverloadable_operator(self)




    def overloadable_operator(self):

        localctx = CSharpParser.Overloadable_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_overloadable_operator)
        try:
            self.state = 1965
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,231,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1943
                self.match(CSharpParser.PLUS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1944
                self.match(CSharpParser.MINUS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1945
                self.match(CSharpParser.BANG)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1946
                self.match(CSharpParser.TILDE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1947
                self.match(CSharpParser.OP_INC)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1948
                self.match(CSharpParser.OP_DEC)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1949
                self.match(CSharpParser.TRUE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1950
                self.match(CSharpParser.FALSE)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1951
                self.match(CSharpParser.STAR)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1952
                self.match(CSharpParser.DIV)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 1953
                self.match(CSharpParser.PERCENT)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 1954
                self.match(CSharpParser.AMP)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 1955
                self.match(CSharpParser.BITWISE_OR)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 1956
                self.match(CSharpParser.CARET)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 1957
                self.match(CSharpParser.OP_LEFT_SHIFT)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 1958
                self.right_shift()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 1959
                self.match(CSharpParser.OP_EQ)
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 1960
                self.match(CSharpParser.OP_NE)
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 1961
                self.match(CSharpParser.GT)
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 1962
                self.match(CSharpParser.LT)
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 1963
                self.match(CSharpParser.OP_GE)
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 1964
                self.match(CSharpParser.OP_LE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conversion_operator_declaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(CSharpParser.OPERATOR, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def arg_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Arg_declarationContext,0)


        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def IMPLICIT(self):
            return self.getToken(CSharpParser.IMPLICIT, 0)

        def EXPLICIT(self):
            return self.getToken(CSharpParser.EXPLICIT, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_conversion_operator_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConversion_operator_declarator" ):
                listener.enterConversion_operator_declarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConversion_operator_declarator" ):
                listener.exitConversion_operator_declarator(self)




    def conversion_operator_declarator(self):

        localctx = CSharpParser.Conversion_operator_declaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_conversion_operator_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1967
            _la = self._input.LA(1)
            if not(_la==CSharpParser.EXPLICIT or _la==CSharpParser.IMPLICIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 1968
            self.match(CSharpParser.OPERATOR)
            self.state = 1969
            self.type_()
            self.state = 1970
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 1971
            self.arg_declaration()
            self.state = 1972
            self.match(CSharpParser.CLOSE_PARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def BASE(self):
            return self.getToken(CSharpParser.BASE, 0)

        def THIS(self):
            return self.getToken(CSharpParser.THIS, 0)

        def argument_list(self):
            return self.getTypedRuleContext(CSharpParser.Argument_listContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_constructor_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructor_initializer" ):
                listener.enterConstructor_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructor_initializer" ):
                listener.exitConstructor_initializer(self)




    def constructor_initializer(self):

        localctx = CSharpParser.Constructor_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_constructor_initializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1974
            self.match(CSharpParser.COLON)
            self.state = 1975
            _la = self._input.LA(1)
            if not(_la==CSharpParser.BASE or _la==CSharpParser.THIS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 1976
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 1978
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.OUT - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.VOID - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)))) != 0):
                self.state = 1977
                self.argument_list()


            self.state = 1980
            self.match(CSharpParser.CLOSE_PARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = CSharpParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_body)
        try:
            self.state = 1984
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1982
                self.block()
                pass
            elif token in [CSharpParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1983
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_interfacesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def interface_type_list(self):
            return self.getTypedRuleContext(CSharpParser.Interface_type_listContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_struct_interfaces

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct_interfaces" ):
                listener.enterStruct_interfaces(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct_interfaces" ):
                listener.exitStruct_interfaces(self)




    def struct_interfaces(self):

        localctx = CSharpParser.Struct_interfacesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_struct_interfaces)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1986
            self.match(CSharpParser.COLON)
            self.state = 1987
            self.interface_type_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def struct_member_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Struct_member_declarationContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Struct_member_declarationContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_struct_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct_body" ):
                listener.enterStruct_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct_body" ):
                listener.exitStruct_body(self)




    def struct_body(self):

        localctx = CSharpParser.Struct_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_struct_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1989
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 1993
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (CSharpParser.ABSTRACT - 9)) | (1 << (CSharpParser.ADD - 9)) | (1 << (CSharpParser.ALIAS - 9)) | (1 << (CSharpParser.ARGLIST - 9)) | (1 << (CSharpParser.ASCENDING - 9)) | (1 << (CSharpParser.ASYNC - 9)) | (1 << (CSharpParser.AWAIT - 9)) | (1 << (CSharpParser.BOOL - 9)) | (1 << (CSharpParser.BY - 9)) | (1 << (CSharpParser.BYTE - 9)) | (1 << (CSharpParser.CHAR - 9)) | (1 << (CSharpParser.CLASS - 9)) | (1 << (CSharpParser.CONST - 9)) | (1 << (CSharpParser.DECIMAL - 9)) | (1 << (CSharpParser.DELEGATE - 9)) | (1 << (CSharpParser.DESCENDING - 9)) | (1 << (CSharpParser.DOUBLE - 9)) | (1 << (CSharpParser.DYNAMIC - 9)) | (1 << (CSharpParser.ENUM - 9)) | (1 << (CSharpParser.EQUALS - 9)) | (1 << (CSharpParser.EVENT - 9)) | (1 << (CSharpParser.EXPLICIT - 9)) | (1 << (CSharpParser.EXTERN - 9)) | (1 << (CSharpParser.FIXED - 9)) | (1 << (CSharpParser.FLOAT - 9)) | (1 << (CSharpParser.FROM - 9)) | (1 << (CSharpParser.GET - 9)) | (1 << (CSharpParser.GROUP - 9)) | (1 << (CSharpParser.IMPLICIT - 9)) | (1 << (CSharpParser.INT - 9)) | (1 << (CSharpParser.INTERFACE - 9)) | (1 << (CSharpParser.INTERNAL - 9)) | (1 << (CSharpParser.INTO - 9)) | (1 << (CSharpParser.JOIN - 9)) | (1 << (CSharpParser.LET - 9)) | (1 << (CSharpParser.LONG - 9)) | (1 << (CSharpParser.NAMEOF - 9)) | (1 << (CSharpParser.NEW - 9)) | (1 << (CSharpParser.OBJECT - 9)) | (1 << (CSharpParser.ON - 9)) | (1 << (CSharpParser.ORDERBY - 9)))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (CSharpParser.OVERRIDE - 73)) | (1 << (CSharpParser.PARTIAL - 73)) | (1 << (CSharpParser.PRIVATE - 73)) | (1 << (CSharpParser.PROTECTED - 73)) | (1 << (CSharpParser.PUBLIC - 73)) | (1 << (CSharpParser.READONLY - 73)) | (1 << (CSharpParser.REF - 73)) | (1 << (CSharpParser.REMOVE - 73)) | (1 << (CSharpParser.SBYTE - 73)) | (1 << (CSharpParser.SEALED - 73)) | (1 << (CSharpParser.SELECT - 73)) | (1 << (CSharpParser.SET - 73)) | (1 << (CSharpParser.SHORT - 73)) | (1 << (CSharpParser.STATIC - 73)) | (1 << (CSharpParser.STRING - 73)) | (1 << (CSharpParser.STRUCT - 73)) | (1 << (CSharpParser.UINT - 73)) | (1 << (CSharpParser.ULONG - 73)) | (1 << (CSharpParser.UNMANAGED - 73)) | (1 << (CSharpParser.UNSAFE - 73)) | (1 << (CSharpParser.USHORT - 73)) | (1 << (CSharpParser.VAR - 73)) | (1 << (CSharpParser.VIRTUAL - 73)) | (1 << (CSharpParser.VOID - 73)) | (1 << (CSharpParser.VOLATILE - 73)) | (1 << (CSharpParser.WHEN - 73)) | (1 << (CSharpParser.WHERE - 73)) | (1 << (CSharpParser.YIELD - 73)) | (1 << (CSharpParser.IDENTIFIER - 73)) | (1 << (CSharpParser.OPEN_BRACKET - 73)) | (1 << (CSharpParser.OPEN_PARENS - 73)))) != 0):
                self.state = 1990
                self.struct_member_declaration()
                self.state = 1995
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1996
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def common_member_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Common_member_declarationContext,0)


        def FIXED(self):
            return self.getToken(CSharpParser.FIXED, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def all_member_modifiers(self):
            return self.getTypedRuleContext(CSharpParser.All_member_modifiersContext,0)


        def fixed_size_buffer_declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Fixed_size_buffer_declaratorContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Fixed_size_buffer_declaratorContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_struct_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct_member_declaration" ):
                listener.enterStruct_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct_member_declaration" ):
                listener.exitStruct_member_declaration(self)




    def struct_member_declaration(self):

        localctx = CSharpParser.Struct_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_struct_member_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1999
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1998
                self.attributes()


            self.state = 2002
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,236,self._ctx)
            if la_ == 1:
                self.state = 2001
                self.all_member_modifiers()


            self.state = 2014
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CLASS, CSharpParser.CONST, CSharpParser.DECIMAL, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.ENUM, CSharpParser.EQUALS, CSharpParser.EVENT, CSharpParser.EXPLICIT, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.IMPLICIT, CSharpParser.INT, CSharpParser.INTERFACE, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.READONLY, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.STRING, CSharpParser.STRUCT, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.VOID, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.OPEN_PARENS]:
                self.state = 2004
                self.common_member_declaration()
                pass
            elif token in [CSharpParser.FIXED]:
                self.state = 2005
                self.match(CSharpParser.FIXED)
                self.state = 2006
                self.type_()
                self.state = 2008 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 2007
                    self.fixed_size_buffer_declarator()
                    self.state = 2010 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BY) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)))) != 0)):
                        break

                self.state = 2012
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def base_type(self):
            return self.getTypedRuleContext(CSharpParser.Base_typeContext,0)


        def rank_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Rank_specifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Rank_specifierContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.STAR)
            else:
                return self.getToken(CSharpParser.STAR, i)

        def INTERR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.INTERR)
            else:
                return self.getToken(CSharpParser.INTERR, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_array_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_type" ):
                listener.enterArray_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_type" ):
                listener.exitArray_type(self)




    def array_type(self):

        localctx = CSharpParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2016
            self.base_type()
            self.state = 2024 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2020
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSharpParser.STAR or _la==CSharpParser.INTERR:
                    self.state = 2017
                    _la = self._input.LA(1)
                    if not(_la==CSharpParser.STAR or _la==CSharpParser.INTERR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 2022
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2023
                self.rank_specifier()
                self.state = 2026 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (CSharpParser.OPEN_BRACKET - 127)) | (1 << (CSharpParser.STAR - 127)) | (1 << (CSharpParser.INTERR - 127)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rank_specifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_rank_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRank_specifier" ):
                listener.enterRank_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRank_specifier" ):
                listener.exitRank_specifier(self)




    def rank_specifier(self):

        localctx = CSharpParser.Rank_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_rank_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2028
            self.match(CSharpParser.OPEN_BRACKET)
            self.state = 2032
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 2029
                self.match(CSharpParser.COMMA)
                self.state = 2034
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2035
            self.match(CSharpParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def variable_initializer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Variable_initializerContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Variable_initializerContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_array_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_initializer" ):
                listener.enterArray_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_initializer" ):
                listener.exitArray_initializer(self)




    def array_initializer(self):

        localctx = CSharpParser.Array_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_array_initializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2037
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 2049
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)) | (1 << (CSharpParser.OPEN_BRACE - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)))) != 0):
                self.state = 2038
                self.variable_initializer()
                self.state = 2043
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,242,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 2039
                        self.match(CSharpParser.COMMA)
                        self.state = 2040
                        self.variable_initializer() 
                    self.state = 2045
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,242,self._ctx)

                self.state = 2047
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.COMMA:
                    self.state = 2046
                    self.match(CSharpParser.COMMA)




            self.state = 2051
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variant_type_parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(CSharpParser.LT, 0)

        def variant_type_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Variant_type_parameterContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Variant_type_parameterContext,i)


        def GT(self):
            return self.getToken(CSharpParser.GT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_variant_type_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariant_type_parameter_list" ):
                listener.enterVariant_type_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariant_type_parameter_list" ):
                listener.exitVariant_type_parameter_list(self)




    def variant_type_parameter_list(self):

        localctx = CSharpParser.Variant_type_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_variant_type_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2053
            self.match(CSharpParser.LT)
            self.state = 2054
            self.variant_type_parameter()
            self.state = 2059
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 2055
                self.match(CSharpParser.COMMA)
                self.state = 2056
                self.variant_type_parameter()
                self.state = 2061
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2062
            self.match(CSharpParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variant_type_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def variance_annotation(self):
            return self.getTypedRuleContext(CSharpParser.Variance_annotationContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_variant_type_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariant_type_parameter" ):
                listener.enterVariant_type_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariant_type_parameter" ):
                listener.exitVariant_type_parameter(self)




    def variant_type_parameter(self):

        localctx = CSharpParser.Variant_type_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_variant_type_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2065
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 2064
                self.attributes()


            self.state = 2068
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.IN or _la==CSharpParser.OUT:
                self.state = 2067
                self.variance_annotation()


            self.state = 2070
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variance_annotationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN(self):
            return self.getToken(CSharpParser.IN, 0)

        def OUT(self):
            return self.getToken(CSharpParser.OUT, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_variance_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariance_annotation" ):
                listener.enterVariance_annotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariance_annotation" ):
                listener.exitVariance_annotation(self)




    def variance_annotation(self):

        localctx = CSharpParser.Variance_annotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_variance_annotation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2072
            _la = self._input.LA(1)
            if not(_la==CSharpParser.IN or _la==CSharpParser.OUT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_baseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def interface_type_list(self):
            return self.getTypedRuleContext(CSharpParser.Interface_type_listContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_interface_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_base" ):
                listener.enterInterface_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_base" ):
                listener.exitInterface_base(self)




    def interface_base(self):

        localctx = CSharpParser.Interface_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_interface_base)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2074
            self.match(CSharpParser.COLON)
            self.state = 2075
            self.interface_type_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def interface_member_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Interface_member_declarationContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Interface_member_declarationContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_interface_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_body" ):
                listener.enterInterface_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_body" ):
                listener.exitInterface_body(self)




    def interface_body(self):

        localctx = CSharpParser.Interface_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_interface_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2077
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 2081
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (CSharpParser.ADD - 10)) | (1 << (CSharpParser.ALIAS - 10)) | (1 << (CSharpParser.ARGLIST - 10)) | (1 << (CSharpParser.ASCENDING - 10)) | (1 << (CSharpParser.ASYNC - 10)) | (1 << (CSharpParser.AWAIT - 10)) | (1 << (CSharpParser.BOOL - 10)) | (1 << (CSharpParser.BY - 10)) | (1 << (CSharpParser.BYTE - 10)) | (1 << (CSharpParser.CHAR - 10)) | (1 << (CSharpParser.DECIMAL - 10)) | (1 << (CSharpParser.DESCENDING - 10)) | (1 << (CSharpParser.DOUBLE - 10)) | (1 << (CSharpParser.DYNAMIC - 10)) | (1 << (CSharpParser.EQUALS - 10)) | (1 << (CSharpParser.EVENT - 10)) | (1 << (CSharpParser.FLOAT - 10)) | (1 << (CSharpParser.FROM - 10)) | (1 << (CSharpParser.GET - 10)) | (1 << (CSharpParser.GROUP - 10)) | (1 << (CSharpParser.INT - 10)) | (1 << (CSharpParser.INTO - 10)) | (1 << (CSharpParser.JOIN - 10)) | (1 << (CSharpParser.LET - 10)) | (1 << (CSharpParser.LONG - 10)) | (1 << (CSharpParser.NAMEOF - 10)) | (1 << (CSharpParser.NEW - 10)) | (1 << (CSharpParser.OBJECT - 10)) | (1 << (CSharpParser.ON - 10)) | (1 << (CSharpParser.ORDERBY - 10)))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CSharpParser.PARTIAL - 75)) | (1 << (CSharpParser.READONLY - 75)) | (1 << (CSharpParser.REF - 75)) | (1 << (CSharpParser.REMOVE - 75)) | (1 << (CSharpParser.SBYTE - 75)) | (1 << (CSharpParser.SELECT - 75)) | (1 << (CSharpParser.SET - 75)) | (1 << (CSharpParser.SHORT - 75)) | (1 << (CSharpParser.STRING - 75)) | (1 << (CSharpParser.UINT - 75)) | (1 << (CSharpParser.ULONG - 75)) | (1 << (CSharpParser.UNMANAGED - 75)) | (1 << (CSharpParser.UNSAFE - 75)) | (1 << (CSharpParser.USHORT - 75)) | (1 << (CSharpParser.VAR - 75)) | (1 << (CSharpParser.VOID - 75)) | (1 << (CSharpParser.WHEN - 75)) | (1 << (CSharpParser.WHERE - 75)) | (1 << (CSharpParser.YIELD - 75)) | (1 << (CSharpParser.IDENTIFIER - 75)) | (1 << (CSharpParser.OPEN_BRACKET - 75)) | (1 << (CSharpParser.OPEN_PARENS - 75)))) != 0):
                self.state = 2078
                self.interface_member_declaration()
                self.state = 2083
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2084
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def VOID(self):
            return self.getToken(CSharpParser.VOID, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def EVENT(self):
            return self.getToken(CSharpParser.EVENT, 0)

        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def NEW(self):
            return self.getToken(CSharpParser.NEW, 0)

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def interface_accessors(self):
            return self.getTypedRuleContext(CSharpParser.Interface_accessorsContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def THIS(self):
            return self.getToken(CSharpParser.THIS, 0)

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def formal_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Formal_parameter_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def UNSAFE(self):
            return self.getToken(CSharpParser.UNSAFE, 0)

        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def READONLY(self):
            return self.getToken(CSharpParser.READONLY, 0)

        def type_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_listContext,0)


        def type_parameter_constraints_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clausesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_interface_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_member_declaration" ):
                listener.enterInterface_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_member_declaration" ):
                listener.exitInterface_member_declaration(self)




    def interface_member_declaration(self):

        localctx = CSharpParser.Interface_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_interface_member_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2087
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 2086
                self.attributes()


            self.state = 2090
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.NEW:
                self.state = 2089
                self.match(CSharpParser.NEW)


            self.state = 2155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,261,self._ctx)
            if la_ == 1:
                self.state = 2093
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.UNSAFE:
                    self.state = 2092
                    self.match(CSharpParser.UNSAFE)


                self.state = 2100
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,252,self._ctx)
                if la_ == 1:
                    self.state = 2095
                    self.match(CSharpParser.REF)

                elif la_ == 2:
                    self.state = 2096
                    self.match(CSharpParser.REF)
                    self.state = 2097
                    self.match(CSharpParser.READONLY)

                elif la_ == 3:
                    self.state = 2098
                    self.match(CSharpParser.READONLY)
                    self.state = 2099
                    self.match(CSharpParser.REF)


                self.state = 2102
                self.type_()
                self.state = 2130
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,256,self._ctx)
                if la_ == 1:
                    self.state = 2103
                    self.identifier()
                    self.state = 2105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpParser.LT:
                        self.state = 2104
                        self.type_parameter_list()


                    self.state = 2107
                    self.match(CSharpParser.OPEN_PARENS)
                    self.state = 2109
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (CSharpParser.ADD - 10)) | (1 << (CSharpParser.ALIAS - 10)) | (1 << (CSharpParser.ARGLIST - 10)) | (1 << (CSharpParser.ASCENDING - 10)) | (1 << (CSharpParser.ASYNC - 10)) | (1 << (CSharpParser.AWAIT - 10)) | (1 << (CSharpParser.BOOL - 10)) | (1 << (CSharpParser.BY - 10)) | (1 << (CSharpParser.BYTE - 10)) | (1 << (CSharpParser.CHAR - 10)) | (1 << (CSharpParser.DECIMAL - 10)) | (1 << (CSharpParser.DESCENDING - 10)) | (1 << (CSharpParser.DOUBLE - 10)) | (1 << (CSharpParser.DYNAMIC - 10)) | (1 << (CSharpParser.EQUALS - 10)) | (1 << (CSharpParser.FLOAT - 10)) | (1 << (CSharpParser.FROM - 10)) | (1 << (CSharpParser.GET - 10)) | (1 << (CSharpParser.GROUP - 10)) | (1 << (CSharpParser.IN - 10)) | (1 << (CSharpParser.INT - 10)) | (1 << (CSharpParser.INTO - 10)) | (1 << (CSharpParser.JOIN - 10)) | (1 << (CSharpParser.LET - 10)) | (1 << (CSharpParser.LONG - 10)) | (1 << (CSharpParser.NAMEOF - 10)) | (1 << (CSharpParser.OBJECT - 10)) | (1 << (CSharpParser.ON - 10)) | (1 << (CSharpParser.ORDERBY - 10)) | (1 << (CSharpParser.OUT - 10)))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (CSharpParser.PARAMS - 74)) | (1 << (CSharpParser.PARTIAL - 74)) | (1 << (CSharpParser.REF - 74)) | (1 << (CSharpParser.REMOVE - 74)) | (1 << (CSharpParser.SBYTE - 74)) | (1 << (CSharpParser.SELECT - 74)) | (1 << (CSharpParser.SET - 74)) | (1 << (CSharpParser.SHORT - 74)) | (1 << (CSharpParser.STRING - 74)) | (1 << (CSharpParser.THIS - 74)) | (1 << (CSharpParser.UINT - 74)) | (1 << (CSharpParser.ULONG - 74)) | (1 << (CSharpParser.UNMANAGED - 74)) | (1 << (CSharpParser.USHORT - 74)) | (1 << (CSharpParser.VAR - 74)) | (1 << (CSharpParser.VOID - 74)) | (1 << (CSharpParser.WHEN - 74)) | (1 << (CSharpParser.WHERE - 74)) | (1 << (CSharpParser.YIELD - 74)) | (1 << (CSharpParser.IDENTIFIER - 74)) | (1 << (CSharpParser.OPEN_BRACKET - 74)) | (1 << (CSharpParser.OPEN_PARENS - 74)))) != 0):
                        self.state = 2108
                        self.formal_parameter_list()


                    self.state = 2111
                    self.match(CSharpParser.CLOSE_PARENS)
                    self.state = 2113
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpParser.WHERE:
                        self.state = 2112
                        self.type_parameter_constraints_clauses()


                    self.state = 2115
                    self.match(CSharpParser.SEMICOLON)
                    pass

                elif la_ == 2:
                    self.state = 2117
                    self.identifier()
                    self.state = 2118
                    self.match(CSharpParser.OPEN_BRACE)
                    self.state = 2119
                    self.interface_accessors()
                    self.state = 2120
                    self.match(CSharpParser.CLOSE_BRACE)
                    pass

                elif la_ == 3:
                    self.state = 2122
                    self.match(CSharpParser.THIS)
                    self.state = 2123
                    self.match(CSharpParser.OPEN_BRACKET)
                    self.state = 2124
                    self.formal_parameter_list()
                    self.state = 2125
                    self.match(CSharpParser.CLOSE_BRACKET)
                    self.state = 2126
                    self.match(CSharpParser.OPEN_BRACE)
                    self.state = 2127
                    self.interface_accessors()
                    self.state = 2128
                    self.match(CSharpParser.CLOSE_BRACE)
                    pass


                pass

            elif la_ == 2:
                self.state = 2133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.UNSAFE:
                    self.state = 2132
                    self.match(CSharpParser.UNSAFE)


                self.state = 2135
                self.match(CSharpParser.VOID)
                self.state = 2136
                self.identifier()
                self.state = 2138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.LT:
                    self.state = 2137
                    self.type_parameter_list()


                self.state = 2140
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 2142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (CSharpParser.ADD - 10)) | (1 << (CSharpParser.ALIAS - 10)) | (1 << (CSharpParser.ARGLIST - 10)) | (1 << (CSharpParser.ASCENDING - 10)) | (1 << (CSharpParser.ASYNC - 10)) | (1 << (CSharpParser.AWAIT - 10)) | (1 << (CSharpParser.BOOL - 10)) | (1 << (CSharpParser.BY - 10)) | (1 << (CSharpParser.BYTE - 10)) | (1 << (CSharpParser.CHAR - 10)) | (1 << (CSharpParser.DECIMAL - 10)) | (1 << (CSharpParser.DESCENDING - 10)) | (1 << (CSharpParser.DOUBLE - 10)) | (1 << (CSharpParser.DYNAMIC - 10)) | (1 << (CSharpParser.EQUALS - 10)) | (1 << (CSharpParser.FLOAT - 10)) | (1 << (CSharpParser.FROM - 10)) | (1 << (CSharpParser.GET - 10)) | (1 << (CSharpParser.GROUP - 10)) | (1 << (CSharpParser.IN - 10)) | (1 << (CSharpParser.INT - 10)) | (1 << (CSharpParser.INTO - 10)) | (1 << (CSharpParser.JOIN - 10)) | (1 << (CSharpParser.LET - 10)) | (1 << (CSharpParser.LONG - 10)) | (1 << (CSharpParser.NAMEOF - 10)) | (1 << (CSharpParser.OBJECT - 10)) | (1 << (CSharpParser.ON - 10)) | (1 << (CSharpParser.ORDERBY - 10)) | (1 << (CSharpParser.OUT - 10)))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (CSharpParser.PARAMS - 74)) | (1 << (CSharpParser.PARTIAL - 74)) | (1 << (CSharpParser.REF - 74)) | (1 << (CSharpParser.REMOVE - 74)) | (1 << (CSharpParser.SBYTE - 74)) | (1 << (CSharpParser.SELECT - 74)) | (1 << (CSharpParser.SET - 74)) | (1 << (CSharpParser.SHORT - 74)) | (1 << (CSharpParser.STRING - 74)) | (1 << (CSharpParser.THIS - 74)) | (1 << (CSharpParser.UINT - 74)) | (1 << (CSharpParser.ULONG - 74)) | (1 << (CSharpParser.UNMANAGED - 74)) | (1 << (CSharpParser.USHORT - 74)) | (1 << (CSharpParser.VAR - 74)) | (1 << (CSharpParser.VOID - 74)) | (1 << (CSharpParser.WHEN - 74)) | (1 << (CSharpParser.WHERE - 74)) | (1 << (CSharpParser.YIELD - 74)) | (1 << (CSharpParser.IDENTIFIER - 74)) | (1 << (CSharpParser.OPEN_BRACKET - 74)) | (1 << (CSharpParser.OPEN_PARENS - 74)))) != 0):
                    self.state = 2141
                    self.formal_parameter_list()


                self.state = 2144
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 2146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.WHERE:
                    self.state = 2145
                    self.type_parameter_constraints_clauses()


                self.state = 2148
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.state = 2150
                self.match(CSharpParser.EVENT)
                self.state = 2151
                self.type_()
                self.state = 2152
                self.identifier()
                self.state = 2153
                self.match(CSharpParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_accessorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GET(self):
            return self.getToken(CSharpParser.GET, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.SEMICOLON)
            else:
                return self.getToken(CSharpParser.SEMICOLON, i)

        def SET(self):
            return self.getToken(CSharpParser.SET, 0)

        def attributes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.AttributesContext)
            else:
                return self.getTypedRuleContext(CSharpParser.AttributesContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_interface_accessors

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_accessors" ):
                listener.enterInterface_accessors(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_accessors" ):
                listener.exitInterface_accessors(self)




    def interface_accessors(self):

        localctx = CSharpParser.Interface_accessorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_interface_accessors)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 2157
                self.attributes()


            self.state = 2178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.GET]:
                self.state = 2160
                self.match(CSharpParser.GET)
                self.state = 2161
                self.match(CSharpParser.SEMICOLON)
                self.state = 2167
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.SET or _la==CSharpParser.OPEN_BRACKET:
                    self.state = 2163
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpParser.OPEN_BRACKET:
                        self.state = 2162
                        self.attributes()


                    self.state = 2165
                    self.match(CSharpParser.SET)
                    self.state = 2166
                    self.match(CSharpParser.SEMICOLON)


                pass
            elif token in [CSharpParser.SET]:
                self.state = 2169
                self.match(CSharpParser.SET)
                self.state = 2170
                self.match(CSharpParser.SEMICOLON)
                self.state = 2176
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.GET or _la==CSharpParser.OPEN_BRACKET:
                    self.state = 2172
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpParser.OPEN_BRACKET:
                        self.state = 2171
                        self.attributes()


                    self.state = 2174
                    self.match(CSharpParser.GET)
                    self.state = 2175
                    self.match(CSharpParser.SEMICOLON)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Enum_baseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_enum_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum_base" ):
                listener.enterEnum_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum_base" ):
                listener.exitEnum_base(self)




    def enum_base(self):

        localctx = CSharpParser.Enum_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_enum_base)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2180
            self.match(CSharpParser.COLON)
            self.state = 2181
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Enum_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def enum_member_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Enum_member_declarationContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Enum_member_declarationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_enum_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum_body" ):
                listener.enterEnum_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum_body" ):
                listener.exitEnum_body(self)




    def enum_body(self):

        localctx = CSharpParser.Enum_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_enum_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2183
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 2195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BY) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.OPEN_BRACKET - 64)))) != 0):
                self.state = 2184
                self.enum_member_declaration()
                self.state = 2189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,268,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 2185
                        self.match(CSharpParser.COMMA)
                        self.state = 2186
                        self.enum_member_declaration() 
                    self.state = 2191
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,268,self._ctx)

                self.state = 2193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.COMMA:
                    self.state = 2192
                    self.match(CSharpParser.COMMA)




            self.state = 2197
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Enum_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_enum_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum_member_declaration" ):
                listener.enterEnum_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum_member_declaration" ):
                listener.exitEnum_member_declaration(self)




    def enum_member_declaration(self):

        localctx = CSharpParser.Enum_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_enum_member_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 2199
                self.attributes()


            self.state = 2202
            self.identifier()
            self.state = 2205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.ASSIGNMENT:
                self.state = 2203
                self.match(CSharpParser.ASSIGNMENT)
                self.state = 2204
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_attribute_sectionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def global_attribute_target(self):
            return self.getTypedRuleContext(CSharpParser.Global_attribute_targetContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(CSharpParser.Attribute_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def COMMA(self):
            return self.getToken(CSharpParser.COMMA, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_global_attribute_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_attribute_section" ):
                listener.enterGlobal_attribute_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_attribute_section" ):
                listener.exitGlobal_attribute_section(self)




    def global_attribute_section(self):

        localctx = CSharpParser.Global_attribute_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_global_attribute_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2207
            self.match(CSharpParser.OPEN_BRACKET)
            self.state = 2208
            self.global_attribute_target()
            self.state = 2209
            self.match(CSharpParser.COLON)
            self.state = 2210
            self.attribute_list()
            self.state = 2212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COMMA:
                self.state = 2211
                self.match(CSharpParser.COMMA)


            self.state = 2214
            self.match(CSharpParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_attribute_targetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(CSharpParser.KeywordContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_global_attribute_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_attribute_target" ):
                listener.enterGlobal_attribute_target(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_attribute_target" ):
                listener.exitGlobal_attribute_target(self)




    def global_attribute_target(self):

        localctx = CSharpParser.Global_attribute_targetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_global_attribute_target)
        try:
            self.state = 2218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,274,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2216
                self.keyword()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2217
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Attribute_sectionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Attribute_sectionContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_attributes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributes" ):
                listener.enterAttributes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributes" ):
                listener.exitAttributes(self)




    def attributes(self):

        localctx = CSharpParser.AttributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_attributes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2221 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2220
                self.attribute_section()
                self.state = 2223 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSharpParser.OPEN_BRACKET):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_sectionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(CSharpParser.Attribute_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def attribute_target(self):
            return self.getTypedRuleContext(CSharpParser.Attribute_targetContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def COMMA(self):
            return self.getToken(CSharpParser.COMMA, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_attribute_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_section" ):
                listener.enterAttribute_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_section" ):
                listener.exitAttribute_section(self)




    def attribute_section(self):

        localctx = CSharpParser.Attribute_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_attribute_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2225
            self.match(CSharpParser.OPEN_BRACKET)
            self.state = 2229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,276,self._ctx)
            if la_ == 1:
                self.state = 2226
                self.attribute_target()
                self.state = 2227
                self.match(CSharpParser.COLON)


            self.state = 2231
            self.attribute_list()
            self.state = 2233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COMMA:
                self.state = 2232
                self.match(CSharpParser.COMMA)


            self.state = 2235
            self.match(CSharpParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_targetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(CSharpParser.KeywordContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_attribute_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_target" ):
                listener.enterAttribute_target(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_target" ):
                listener.exitAttribute_target(self)




    def attribute_target(self):

        localctx = CSharpParser.Attribute_targetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_attribute_target)
        try:
            self.state = 2239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,278,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2237
                self.keyword()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2238
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.AttributeContext)
            else:
                return self.getTypedRuleContext(CSharpParser.AttributeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_attribute_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_list" ):
                listener.enterAttribute_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_list" ):
                listener.exitAttribute_list(self)




    def attribute_list(self):

        localctx = CSharpParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_attribute_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2241
            self.attribute()
            self.state = 2246
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,279,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2242
                    self.match(CSharpParser.COMMA)
                    self.state = 2243
                    self.attribute() 
                self.state = 2248
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,279,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace_or_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def attribute_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Attribute_argumentContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Attribute_argumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)




    def attribute(self):

        localctx = CSharpParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2249
            self.namespace_or_type_name()
            self.state = 2262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_PARENS:
                self.state = 2250
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 2259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)))) != 0):
                    self.state = 2251
                    self.attribute_argument()
                    self.state = 2256
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CSharpParser.COMMA:
                        self.state = 2252
                        self.match(CSharpParser.COMMA)
                        self.state = 2253
                        self.attribute_argument()
                        self.state = 2258
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 2261
                self.match(CSharpParser.CLOSE_PARENS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_attribute_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_argument" ):
                listener.enterAttribute_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_argument" ):
                listener.exitAttribute_argument(self)




    def attribute_argument(self):

        localctx = CSharpParser.Attribute_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_attribute_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,283,self._ctx)
            if la_ == 1:
                self.state = 2264
                self.identifier()
                self.state = 2265
                self.match(CSharpParser.COLON)


            self.state = 2269
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pointer_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(CSharpParser.STAR, 0)

        def simple_type(self):
            return self.getTypedRuleContext(CSharpParser.Simple_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(CSharpParser.Class_typeContext,0)


        def rank_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Rank_specifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Rank_specifierContext,i)


        def INTERR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.INTERR)
            else:
                return self.getToken(CSharpParser.INTERR, i)

        def VOID(self):
            return self.getToken(CSharpParser.VOID, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_pointer_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointer_type" ):
                listener.enterPointer_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointer_type" ):
                listener.exitPointer_type(self)




    def pointer_type(self):

        localctx = CSharpParser.Pointer_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_pointer_type)
        self._la = 0 # Token type
        try:
            self.state = 2286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.DECIMAL, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.STRING, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2273
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.BOOL, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.DECIMAL, CSharpParser.DOUBLE, CSharpParser.FLOAT, CSharpParser.INT, CSharpParser.LONG, CSharpParser.SBYTE, CSharpParser.SHORT, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.USHORT]:
                    self.state = 2271
                    self.simple_type()
                    pass
                elif token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BY, CSharpParser.DESCENDING, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.STRING, CSharpParser.UNMANAGED, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER]:
                    self.state = 2272
                    self.class_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 2279
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSharpParser.OPEN_BRACKET or _la==CSharpParser.INTERR:
                    self.state = 2277
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CSharpParser.OPEN_BRACKET]:
                        self.state = 2275
                        self.rank_specifier()
                        pass
                    elif token in [CSharpParser.INTERR]:
                        self.state = 2276
                        self.match(CSharpParser.INTERR)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 2281
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2282
                self.match(CSharpParser.STAR)
                pass
            elif token in [CSharpParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2284
                self.match(CSharpParser.VOID)
                self.state = 2285
                self.match(CSharpParser.STAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixed_pointer_declaratorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fixed_pointer_declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Fixed_pointer_declaratorContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Fixed_pointer_declaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_fixed_pointer_declarators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixed_pointer_declarators" ):
                listener.enterFixed_pointer_declarators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixed_pointer_declarators" ):
                listener.exitFixed_pointer_declarators(self)




    def fixed_pointer_declarators(self):

        localctx = CSharpParser.Fixed_pointer_declaratorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_fixed_pointer_declarators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2288
            self.fixed_pointer_declarator()
            self.state = 2293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 2289
                self.match(CSharpParser.COMMA)
                self.state = 2290
                self.fixed_pointer_declarator()
                self.state = 2295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixed_pointer_declaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def fixed_pointer_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Fixed_pointer_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_fixed_pointer_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixed_pointer_declarator" ):
                listener.enterFixed_pointer_declarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixed_pointer_declarator" ):
                listener.exitFixed_pointer_declarator(self)




    def fixed_pointer_declarator(self):

        localctx = CSharpParser.Fixed_pointer_declaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_fixed_pointer_declarator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2296
            self.identifier()
            self.state = 2297
            self.match(CSharpParser.ASSIGNMENT)
            self.state = 2298
            self.fixed_pointer_initializer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixed_pointer_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def AMP(self):
            return self.getToken(CSharpParser.AMP, 0)

        def stackalloc_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Stackalloc_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_fixed_pointer_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixed_pointer_initializer" ):
                listener.enterFixed_pointer_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixed_pointer_initializer" ):
                listener.exitFixed_pointer_initializer(self)




    def fixed_pointer_initializer(self):

        localctx = CSharpParser.Fixed_pointer_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_fixed_pointer_initializer)
        try:
            self.state = 2305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2301
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,289,self._ctx)
                if la_ == 1:
                    self.state = 2300
                    self.match(CSharpParser.AMP)


                self.state = 2303
                self.expression()
                pass
            elif token in [CSharpParser.STACKALLOC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2304
                self.stackalloc_initializer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixed_size_buffer_declaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_fixed_size_buffer_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixed_size_buffer_declarator" ):
                listener.enterFixed_size_buffer_declarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixed_size_buffer_declarator" ):
                listener.exitFixed_size_buffer_declarator(self)




    def fixed_size_buffer_declarator(self):

        localctx = CSharpParser.Fixed_size_buffer_declaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_fixed_size_buffer_declarator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2307
            self.identifier()
            self.state = 2308
            self.match(CSharpParser.OPEN_BRACKET)
            self.state = 2309
            self.expression()
            self.state = 2310
            self.match(CSharpParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stackalloc_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STACKALLOC(self):
            return self.getToken(CSharpParser.STACKALLOC, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ExpressionContext,i)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_stackalloc_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStackalloc_initializer" ):
                listener.enterStackalloc_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStackalloc_initializer" ):
                listener.exitStackalloc_initializer(self)




    def stackalloc_initializer(self):

        localctx = CSharpParser.Stackalloc_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_stackalloc_initializer)
        self._la = 0 # Token type
        try:
            self.state = 2341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,295,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2312
                self.match(CSharpParser.STACKALLOC)
                self.state = 2313
                self.type_()
                self.state = 2314
                self.match(CSharpParser.OPEN_BRACKET)
                self.state = 2315
                self.expression()
                self.state = 2316
                self.match(CSharpParser.CLOSE_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2318
                self.match(CSharpParser.STACKALLOC)
                self.state = 2320
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (CSharpParser.ADD - 10)) | (1 << (CSharpParser.ALIAS - 10)) | (1 << (CSharpParser.ARGLIST - 10)) | (1 << (CSharpParser.ASCENDING - 10)) | (1 << (CSharpParser.ASYNC - 10)) | (1 << (CSharpParser.AWAIT - 10)) | (1 << (CSharpParser.BOOL - 10)) | (1 << (CSharpParser.BY - 10)) | (1 << (CSharpParser.BYTE - 10)) | (1 << (CSharpParser.CHAR - 10)) | (1 << (CSharpParser.DECIMAL - 10)) | (1 << (CSharpParser.DESCENDING - 10)) | (1 << (CSharpParser.DOUBLE - 10)) | (1 << (CSharpParser.DYNAMIC - 10)) | (1 << (CSharpParser.EQUALS - 10)) | (1 << (CSharpParser.FLOAT - 10)) | (1 << (CSharpParser.FROM - 10)) | (1 << (CSharpParser.GET - 10)) | (1 << (CSharpParser.GROUP - 10)) | (1 << (CSharpParser.INT - 10)) | (1 << (CSharpParser.INTO - 10)) | (1 << (CSharpParser.JOIN - 10)) | (1 << (CSharpParser.LET - 10)) | (1 << (CSharpParser.LONG - 10)) | (1 << (CSharpParser.NAMEOF - 10)) | (1 << (CSharpParser.OBJECT - 10)) | (1 << (CSharpParser.ON - 10)) | (1 << (CSharpParser.ORDERBY - 10)))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CSharpParser.PARTIAL - 75)) | (1 << (CSharpParser.REMOVE - 75)) | (1 << (CSharpParser.SBYTE - 75)) | (1 << (CSharpParser.SELECT - 75)) | (1 << (CSharpParser.SET - 75)) | (1 << (CSharpParser.SHORT - 75)) | (1 << (CSharpParser.STRING - 75)) | (1 << (CSharpParser.UINT - 75)) | (1 << (CSharpParser.ULONG - 75)) | (1 << (CSharpParser.UNMANAGED - 75)) | (1 << (CSharpParser.USHORT - 75)) | (1 << (CSharpParser.VAR - 75)) | (1 << (CSharpParser.VOID - 75)) | (1 << (CSharpParser.WHEN - 75)) | (1 << (CSharpParser.WHERE - 75)) | (1 << (CSharpParser.YIELD - 75)) | (1 << (CSharpParser.IDENTIFIER - 75)) | (1 << (CSharpParser.OPEN_PARENS - 75)))) != 0):
                    self.state = 2319
                    self.type_()


                self.state = 2322
                self.match(CSharpParser.OPEN_BRACKET)
                self.state = 2324
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)))) != 0):
                    self.state = 2323
                    self.expression()


                self.state = 2326
                self.match(CSharpParser.CLOSE_BRACKET)
                self.state = 2327
                self.match(CSharpParser.OPEN_BRACE)
                self.state = 2328
                self.expression()
                self.state = 2333
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,293,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 2329
                        self.match(CSharpParser.COMMA)
                        self.state = 2330
                        self.expression() 
                    self.state = 2335
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,293,self._ctx)

                self.state = 2337
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.COMMA:
                    self.state = 2336
                    self.match(CSharpParser.COMMA)


                self.state = 2339
                self.match(CSharpParser.CLOSE_BRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Right_arrowContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.first = None # Token
            self.second = None # Token

        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def GT(self):
            return self.getToken(CSharpParser.GT, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_right_arrow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRight_arrow" ):
                listener.enterRight_arrow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRight_arrow" ):
                listener.exitRight_arrow(self)




    def right_arrow(self):

        localctx = CSharpParser.Right_arrowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_right_arrow)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2343
            localctx.first = self.match(CSharpParser.ASSIGNMENT)
            self.state = 2344
            localctx.second = self.match(CSharpParser.GT)
            self.state = 2345
            if not (0 if localctx.first is None else localctx.first.tokenIndex) + 1 == (0 if localctx.second is None else localctx.second.tokenIndex):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$first.index + 1 == $second.index")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Right_shiftContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.first = None # Token
            self.second = None # Token

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.GT)
            else:
                return self.getToken(CSharpParser.GT, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_right_shift

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRight_shift" ):
                listener.enterRight_shift(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRight_shift" ):
                listener.exitRight_shift(self)




    def right_shift(self):

        localctx = CSharpParser.Right_shiftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_right_shift)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2347
            localctx.first = self.match(CSharpParser.GT)
            self.state = 2348
            localctx.second = self.match(CSharpParser.GT)
            self.state = 2349
            if not (0 if localctx.first is None else localctx.first.tokenIndex) + 1 == (0 if localctx.second is None else localctx.second.tokenIndex):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$first.index + 1 == $second.index")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Right_shift_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.first = None # Token
            self.second = None # Token

        def GT(self):
            return self.getToken(CSharpParser.GT, 0)

        def OP_GE(self):
            return self.getToken(CSharpParser.OP_GE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_right_shift_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRight_shift_assignment" ):
                listener.enterRight_shift_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRight_shift_assignment" ):
                listener.exitRight_shift_assignment(self)




    def right_shift_assignment(self):

        localctx = CSharpParser.Right_shift_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_right_shift_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2351
            localctx.first = self.match(CSharpParser.GT)
            self.state = 2352
            localctx.second = self.match(CSharpParser.OP_GE)
            self.state = 2353
            if not (0 if localctx.first is None else localctx.first.tokenIndex) + 1 == (0 if localctx.second is None else localctx.second.tokenIndex):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$first.index + 1 == $second.index")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean_literal(self):
            return self.getTypedRuleContext(CSharpParser.Boolean_literalContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(CSharpParser.String_literalContext,0)


        def INTEGER_LITERAL(self):
            return self.getToken(CSharpParser.INTEGER_LITERAL, 0)

        def HEX_INTEGER_LITERAL(self):
            return self.getToken(CSharpParser.HEX_INTEGER_LITERAL, 0)

        def BIN_INTEGER_LITERAL(self):
            return self.getToken(CSharpParser.BIN_INTEGER_LITERAL, 0)

        def REAL_LITERAL(self):
            return self.getToken(CSharpParser.REAL_LITERAL, 0)

        def CHARACTER_LITERAL(self):
            return self.getToken(CSharpParser.CHARACTER_LITERAL, 0)

        def NULL(self):
            return self.getToken(CSharpParser.NULL, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = CSharpParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_literal)
        try:
            self.state = 2363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.FALSE, CSharpParser.TRUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2355
                self.boolean_literal()
                pass
            elif token in [CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2356
                self.string_literal()
                pass
            elif token in [CSharpParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2357
                self.match(CSharpParser.INTEGER_LITERAL)
                pass
            elif token in [CSharpParser.HEX_INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2358
                self.match(CSharpParser.HEX_INTEGER_LITERAL)
                pass
            elif token in [CSharpParser.BIN_INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2359
                self.match(CSharpParser.BIN_INTEGER_LITERAL)
                pass
            elif token in [CSharpParser.REAL_LITERAL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 2360
                self.match(CSharpParser.REAL_LITERAL)
                pass
            elif token in [CSharpParser.CHARACTER_LITERAL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 2361
                self.match(CSharpParser.CHARACTER_LITERAL)
                pass
            elif token in [CSharpParser.NULL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 2362
                self.match(CSharpParser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CSharpParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSharpParser.FALSE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_boolean_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_literal" ):
                listener.enterBoolean_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_literal" ):
                listener.exitBoolean_literal(self)




    def boolean_literal(self):

        localctx = CSharpParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2365
            _la = self._input.LA(1)
            if not(_la==CSharpParser.FALSE or _la==CSharpParser.TRUE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interpolated_regular_string(self):
            return self.getTypedRuleContext(CSharpParser.Interpolated_regular_stringContext,0)


        def interpolated_verbatium_string(self):
            return self.getTypedRuleContext(CSharpParser.Interpolated_verbatium_stringContext,0)


        def REGULAR_STRING(self):
            return self.getToken(CSharpParser.REGULAR_STRING, 0)

        def VERBATIUM_STRING(self):
            return self.getToken(CSharpParser.VERBATIUM_STRING, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_string_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_literal" ):
                listener.enterString_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_literal" ):
                listener.exitString_literal(self)




    def string_literal(self):

        localctx = CSharpParser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_string_literal)
        try:
            self.state = 2371
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.INTERPOLATED_REGULAR_STRING_START]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2367
                self.interpolated_regular_string()
                pass
            elif token in [CSharpParser.INTERPOLATED_VERBATIUM_STRING_START]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2368
                self.interpolated_verbatium_string()
                pass
            elif token in [CSharpParser.REGULAR_STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2369
                self.match(CSharpParser.REGULAR_STRING)
                pass
            elif token in [CSharpParser.VERBATIUM_STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2370
                self.match(CSharpParser.VERBATIUM_STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interpolated_regular_stringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERPOLATED_REGULAR_STRING_START(self):
            return self.getToken(CSharpParser.INTERPOLATED_REGULAR_STRING_START, 0)

        def DOUBLE_QUOTE_INSIDE(self):
            return self.getToken(CSharpParser.DOUBLE_QUOTE_INSIDE, 0)

        def interpolated_regular_string_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Interpolated_regular_string_partContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Interpolated_regular_string_partContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_interpolated_regular_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpolated_regular_string" ):
                listener.enterInterpolated_regular_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpolated_regular_string" ):
                listener.exitInterpolated_regular_string(self)




    def interpolated_regular_string(self):

        localctx = CSharpParser.Interpolated_regular_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_interpolated_regular_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2373
            self.match(CSharpParser.INTERPOLATED_REGULAR_STRING_START)
            self.state = 2377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)) | (1 << (CSharpParser.DOUBLE_CURLY_INSIDE - 129)) | (1 << (CSharpParser.REGULAR_CHAR_INSIDE - 129)) | (1 << (CSharpParser.REGULAR_STRING_INSIDE - 129)))) != 0):
                self.state = 2374
                self.interpolated_regular_string_part()
                self.state = 2379
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2380
            self.match(CSharpParser.DOUBLE_QUOTE_INSIDE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interpolated_verbatium_stringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERPOLATED_VERBATIUM_STRING_START(self):
            return self.getToken(CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, 0)

        def DOUBLE_QUOTE_INSIDE(self):
            return self.getToken(CSharpParser.DOUBLE_QUOTE_INSIDE, 0)

        def interpolated_verbatium_string_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Interpolated_verbatium_string_partContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Interpolated_verbatium_string_partContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_interpolated_verbatium_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpolated_verbatium_string" ):
                listener.enterInterpolated_verbatium_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpolated_verbatium_string" ):
                listener.exitInterpolated_verbatium_string(self)




    def interpolated_verbatium_string(self):

        localctx = CSharpParser.Interpolated_verbatium_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_interpolated_verbatium_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2382
            self.match(CSharpParser.INTERPOLATED_VERBATIUM_STRING_START)
            self.state = 2386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)) | (1 << (CSharpParser.DOUBLE_CURLY_INSIDE - 129)) | (1 << (CSharpParser.VERBATIUM_DOUBLE_QUOTE_INSIDE - 129)) | (1 << (CSharpParser.VERBATIUM_INSIDE_STRING - 129)))) != 0):
                self.state = 2383
                self.interpolated_verbatium_string_part()
                self.state = 2388
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2389
            self.match(CSharpParser.DOUBLE_QUOTE_INSIDE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interpolated_regular_string_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interpolated_string_expression(self):
            return self.getTypedRuleContext(CSharpParser.Interpolated_string_expressionContext,0)


        def DOUBLE_CURLY_INSIDE(self):
            return self.getToken(CSharpParser.DOUBLE_CURLY_INSIDE, 0)

        def REGULAR_CHAR_INSIDE(self):
            return self.getToken(CSharpParser.REGULAR_CHAR_INSIDE, 0)

        def REGULAR_STRING_INSIDE(self):
            return self.getToken(CSharpParser.REGULAR_STRING_INSIDE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_interpolated_regular_string_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpolated_regular_string_part" ):
                listener.enterInterpolated_regular_string_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpolated_regular_string_part" ):
                listener.exitInterpolated_regular_string_part(self)




    def interpolated_regular_string_part(self):

        localctx = CSharpParser.Interpolated_regular_string_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_interpolated_regular_string_part)
        try:
            self.state = 2395
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2391
                self.interpolated_string_expression()
                pass
            elif token in [CSharpParser.DOUBLE_CURLY_INSIDE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2392
                self.match(CSharpParser.DOUBLE_CURLY_INSIDE)
                pass
            elif token in [CSharpParser.REGULAR_CHAR_INSIDE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2393
                self.match(CSharpParser.REGULAR_CHAR_INSIDE)
                pass
            elif token in [CSharpParser.REGULAR_STRING_INSIDE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2394
                self.match(CSharpParser.REGULAR_STRING_INSIDE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interpolated_verbatium_string_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interpolated_string_expression(self):
            return self.getTypedRuleContext(CSharpParser.Interpolated_string_expressionContext,0)


        def DOUBLE_CURLY_INSIDE(self):
            return self.getToken(CSharpParser.DOUBLE_CURLY_INSIDE, 0)

        def VERBATIUM_DOUBLE_QUOTE_INSIDE(self):
            return self.getToken(CSharpParser.VERBATIUM_DOUBLE_QUOTE_INSIDE, 0)

        def VERBATIUM_INSIDE_STRING(self):
            return self.getToken(CSharpParser.VERBATIUM_INSIDE_STRING, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_interpolated_verbatium_string_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpolated_verbatium_string_part" ):
                listener.enterInterpolated_verbatium_string_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpolated_verbatium_string_part" ):
                listener.exitInterpolated_verbatium_string_part(self)




    def interpolated_verbatium_string_part(self):

        localctx = CSharpParser.Interpolated_verbatium_string_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_interpolated_verbatium_string_part)
        try:
            self.state = 2401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2397
                self.interpolated_string_expression()
                pass
            elif token in [CSharpParser.DOUBLE_CURLY_INSIDE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2398
                self.match(CSharpParser.DOUBLE_CURLY_INSIDE)
                pass
            elif token in [CSharpParser.VERBATIUM_DOUBLE_QUOTE_INSIDE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2399
                self.match(CSharpParser.VERBATIUM_DOUBLE_QUOTE_INSIDE)
                pass
            elif token in [CSharpParser.VERBATIUM_INSIDE_STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2400
                self.match(CSharpParser.VERBATIUM_INSIDE_STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interpolated_string_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def FORMAT_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.FORMAT_STRING)
            else:
                return self.getToken(CSharpParser.FORMAT_STRING, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_interpolated_string_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpolated_string_expression" ):
                listener.enterInterpolated_string_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpolated_string_expression" ):
                listener.exitInterpolated_string_expression(self)




    def interpolated_string_expression(self):

        localctx = CSharpParser.Interpolated_string_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_interpolated_string_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2403
            self.expression()
            self.state = 2408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 2404
                self.match(CSharpParser.COMMA)
                self.state = 2405
                self.expression()
                self.state = 2410
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COLON:
                self.state = 2411
                self.match(CSharpParser.COLON)
                self.state = 2413 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 2412
                    self.match(CSharpParser.FORMAT_STRING)
                    self.state = 2415 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==CSharpParser.FORMAT_STRING):
                        break



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABSTRACT(self):
            return self.getToken(CSharpParser.ABSTRACT, 0)

        def AS(self):
            return self.getToken(CSharpParser.AS, 0)

        def BASE(self):
            return self.getToken(CSharpParser.BASE, 0)

        def BOOL(self):
            return self.getToken(CSharpParser.BOOL, 0)

        def BREAK(self):
            return self.getToken(CSharpParser.BREAK, 0)

        def BYTE(self):
            return self.getToken(CSharpParser.BYTE, 0)

        def CASE(self):
            return self.getToken(CSharpParser.CASE, 0)

        def CATCH(self):
            return self.getToken(CSharpParser.CATCH, 0)

        def CHAR(self):
            return self.getToken(CSharpParser.CHAR, 0)

        def CHECKED(self):
            return self.getToken(CSharpParser.CHECKED, 0)

        def CLASS(self):
            return self.getToken(CSharpParser.CLASS, 0)

        def CONST(self):
            return self.getToken(CSharpParser.CONST, 0)

        def CONTINUE(self):
            return self.getToken(CSharpParser.CONTINUE, 0)

        def DECIMAL(self):
            return self.getToken(CSharpParser.DECIMAL, 0)

        def DEFAULT(self):
            return self.getToken(CSharpParser.DEFAULT, 0)

        def DELEGATE(self):
            return self.getToken(CSharpParser.DELEGATE, 0)

        def DO(self):
            return self.getToken(CSharpParser.DO, 0)

        def DOUBLE(self):
            return self.getToken(CSharpParser.DOUBLE, 0)

        def ELSE(self):
            return self.getToken(CSharpParser.ELSE, 0)

        def ENUM(self):
            return self.getToken(CSharpParser.ENUM, 0)

        def EVENT(self):
            return self.getToken(CSharpParser.EVENT, 0)

        def EXPLICIT(self):
            return self.getToken(CSharpParser.EXPLICIT, 0)

        def EXTERN(self):
            return self.getToken(CSharpParser.EXTERN, 0)

        def FALSE(self):
            return self.getToken(CSharpParser.FALSE, 0)

        def FINALLY(self):
            return self.getToken(CSharpParser.FINALLY, 0)

        def FIXED(self):
            return self.getToken(CSharpParser.FIXED, 0)

        def FLOAT(self):
            return self.getToken(CSharpParser.FLOAT, 0)

        def FOR(self):
            return self.getToken(CSharpParser.FOR, 0)

        def FOREACH(self):
            return self.getToken(CSharpParser.FOREACH, 0)

        def GOTO(self):
            return self.getToken(CSharpParser.GOTO, 0)

        def IF(self):
            return self.getToken(CSharpParser.IF, 0)

        def IMPLICIT(self):
            return self.getToken(CSharpParser.IMPLICIT, 0)

        def IN(self):
            return self.getToken(CSharpParser.IN, 0)

        def INT(self):
            return self.getToken(CSharpParser.INT, 0)

        def INTERFACE(self):
            return self.getToken(CSharpParser.INTERFACE, 0)

        def INTERNAL(self):
            return self.getToken(CSharpParser.INTERNAL, 0)

        def IS(self):
            return self.getToken(CSharpParser.IS, 0)

        def LOCK(self):
            return self.getToken(CSharpParser.LOCK, 0)

        def LONG(self):
            return self.getToken(CSharpParser.LONG, 0)

        def NAMESPACE(self):
            return self.getToken(CSharpParser.NAMESPACE, 0)

        def NEW(self):
            return self.getToken(CSharpParser.NEW, 0)

        def NULL(self):
            return self.getToken(CSharpParser.NULL, 0)

        def OBJECT(self):
            return self.getToken(CSharpParser.OBJECT, 0)

        def OPERATOR(self):
            return self.getToken(CSharpParser.OPERATOR, 0)

        def OUT(self):
            return self.getToken(CSharpParser.OUT, 0)

        def OVERRIDE(self):
            return self.getToken(CSharpParser.OVERRIDE, 0)

        def PARAMS(self):
            return self.getToken(CSharpParser.PARAMS, 0)

        def PRIVATE(self):
            return self.getToken(CSharpParser.PRIVATE, 0)

        def PROTECTED(self):
            return self.getToken(CSharpParser.PROTECTED, 0)

        def PUBLIC(self):
            return self.getToken(CSharpParser.PUBLIC, 0)

        def READONLY(self):
            return self.getToken(CSharpParser.READONLY, 0)

        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def RETURN(self):
            return self.getToken(CSharpParser.RETURN, 0)

        def SBYTE(self):
            return self.getToken(CSharpParser.SBYTE, 0)

        def SEALED(self):
            return self.getToken(CSharpParser.SEALED, 0)

        def SHORT(self):
            return self.getToken(CSharpParser.SHORT, 0)

        def SIZEOF(self):
            return self.getToken(CSharpParser.SIZEOF, 0)

        def STACKALLOC(self):
            return self.getToken(CSharpParser.STACKALLOC, 0)

        def STATIC(self):
            return self.getToken(CSharpParser.STATIC, 0)

        def STRING(self):
            return self.getToken(CSharpParser.STRING, 0)

        def STRUCT(self):
            return self.getToken(CSharpParser.STRUCT, 0)

        def SWITCH(self):
            return self.getToken(CSharpParser.SWITCH, 0)

        def THIS(self):
            return self.getToken(CSharpParser.THIS, 0)

        def THROW(self):
            return self.getToken(CSharpParser.THROW, 0)

        def TRUE(self):
            return self.getToken(CSharpParser.TRUE, 0)

        def TRY(self):
            return self.getToken(CSharpParser.TRY, 0)

        def TYPEOF(self):
            return self.getToken(CSharpParser.TYPEOF, 0)

        def UINT(self):
            return self.getToken(CSharpParser.UINT, 0)

        def ULONG(self):
            return self.getToken(CSharpParser.ULONG, 0)

        def UNCHECKED(self):
            return self.getToken(CSharpParser.UNCHECKED, 0)

        def UNMANAGED(self):
            return self.getToken(CSharpParser.UNMANAGED, 0)

        def UNSAFE(self):
            return self.getToken(CSharpParser.UNSAFE, 0)

        def USHORT(self):
            return self.getToken(CSharpParser.USHORT, 0)

        def USING(self):
            return self.getToken(CSharpParser.USING, 0)

        def VIRTUAL(self):
            return self.getToken(CSharpParser.VIRTUAL, 0)

        def VOID(self):
            return self.getToken(CSharpParser.VOID, 0)

        def VOLATILE(self):
            return self.getToken(CSharpParser.VOLATILE, 0)

        def WHILE(self):
            return self.getToken(CSharpParser.WHILE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword" ):
                listener.enterKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword" ):
                listener.exitKeyword(self)




    def keyword(self):

        localctx = CSharpParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2419
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.AS) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BREAK) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CASE) | (1 << CSharpParser.CATCH) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.CLASS) | (1 << CSharpParser.CONST) | (1 << CSharpParser.CONTINUE) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DO) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.ELSE) | (1 << CSharpParser.ENUM) | (1 << CSharpParser.EVENT) | (1 << CSharpParser.EXPLICIT) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FINALLY) | (1 << CSharpParser.FIXED) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FOR) | (1 << CSharpParser.FOREACH) | (1 << CSharpParser.GOTO) | (1 << CSharpParser.IF) | (1 << CSharpParser.IMPLICIT) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTERFACE) | (1 << CSharpParser.INTERNAL) | (1 << CSharpParser.IS) | (1 << CSharpParser.LOCK) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NAMESPACE - 65)) | (1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.OPERATOR - 65)) | (1 << (CSharpParser.OUT - 65)) | (1 << (CSharpParser.OVERRIDE - 65)) | (1 << (CSharpParser.PARAMS - 65)) | (1 << (CSharpParser.PRIVATE - 65)) | (1 << (CSharpParser.PROTECTED - 65)) | (1 << (CSharpParser.PUBLIC - 65)) | (1 << (CSharpParser.READONLY - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.RETURN - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SEALED - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STACKALLOC - 65)) | (1 << (CSharpParser.STATIC - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.STRUCT - 65)) | (1 << (CSharpParser.SWITCH - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.THROW - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TRY - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.UNSAFE - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.USING - 65)) | (1 << (CSharpParser.VIRTUAL - 65)) | (1 << (CSharpParser.VOID - 65)) | (1 << (CSharpParser.VOLATILE - 65)) | (1 << (CSharpParser.WHILE - 65)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSharpParser.CLASS, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def class_body(self):
            return self.getTypedRuleContext(CSharpParser.Class_bodyContext,0)


        def type_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_listContext,0)


        def class_base(self):
            return self.getTypedRuleContext(CSharpParser.Class_baseContext,0)


        def type_parameter_constraints_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clausesContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_class_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_definition" ):
                listener.enterClass_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_definition" ):
                listener.exitClass_definition(self)




    def class_definition(self):

        localctx = CSharpParser.Class_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_class_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2421
            self.match(CSharpParser.CLASS)
            self.state = 2422
            self.identifier()
            self.state = 2424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.LT:
                self.state = 2423
                self.type_parameter_list()


            self.state = 2427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COLON:
                self.state = 2426
                self.class_base()


            self.state = 2430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHERE:
                self.state = 2429
                self.type_parameter_constraints_clauses()


            self.state = 2432
            self.class_body()
            self.state = 2434
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.SEMICOLON:
                self.state = 2433
                self.match(CSharpParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(CSharpParser.STRUCT, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def struct_body(self):
            return self.getTypedRuleContext(CSharpParser.Struct_bodyContext,0)


        def type_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_listContext,0)


        def struct_interfaces(self):
            return self.getTypedRuleContext(CSharpParser.Struct_interfacesContext,0)


        def type_parameter_constraints_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clausesContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def READONLY(self):
            return self.getToken(CSharpParser.READONLY, 0)

        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_struct_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct_definition" ):
                listener.enterStruct_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct_definition" ):
                listener.exitStruct_definition(self)




    def struct_definition(self):

        localctx = CSharpParser.Struct_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_struct_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.READONLY or _la==CSharpParser.REF:
                self.state = 2436
                _la = self._input.LA(1)
                if not(_la==CSharpParser.READONLY or _la==CSharpParser.REF):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 2439
            self.match(CSharpParser.STRUCT)
            self.state = 2440
            self.identifier()
            self.state = 2442
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.LT:
                self.state = 2441
                self.type_parameter_list()


            self.state = 2445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COLON:
                self.state = 2444
                self.struct_interfaces()


            self.state = 2448
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHERE:
                self.state = 2447
                self.type_parameter_constraints_clauses()


            self.state = 2450
            self.struct_body()
            self.state = 2452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.SEMICOLON:
                self.state = 2451
                self.match(CSharpParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(CSharpParser.INTERFACE, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def class_body(self):
            return self.getTypedRuleContext(CSharpParser.Class_bodyContext,0)


        def variant_type_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Variant_type_parameter_listContext,0)


        def interface_base(self):
            return self.getTypedRuleContext(CSharpParser.Interface_baseContext,0)


        def type_parameter_constraints_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clausesContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_interface_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_definition" ):
                listener.enterInterface_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_definition" ):
                listener.exitInterface_definition(self)




    def interface_definition(self):

        localctx = CSharpParser.Interface_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_interface_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2454
            self.match(CSharpParser.INTERFACE)
            self.state = 2455
            self.identifier()
            self.state = 2457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.LT:
                self.state = 2456
                self.variant_type_parameter_list()


            self.state = 2460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COLON:
                self.state = 2459
                self.interface_base()


            self.state = 2463
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHERE:
                self.state = 2462
                self.type_parameter_constraints_clauses()


            self.state = 2465
            self.class_body()
            self.state = 2467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.SEMICOLON:
                self.state = 2466
                self.match(CSharpParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Enum_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM(self):
            return self.getToken(CSharpParser.ENUM, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def enum_body(self):
            return self.getTypedRuleContext(CSharpParser.Enum_bodyContext,0)


        def enum_base(self):
            return self.getTypedRuleContext(CSharpParser.Enum_baseContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_enum_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum_definition" ):
                listener.enterEnum_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum_definition" ):
                listener.exitEnum_definition(self)




    def enum_definition(self):

        localctx = CSharpParser.Enum_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_enum_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2469
            self.match(CSharpParser.ENUM)
            self.state = 2470
            self.identifier()
            self.state = 2472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COLON:
                self.state = 2471
                self.enum_base()


            self.state = 2474
            self.enum_body()
            self.state = 2476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.SEMICOLON:
                self.state = 2475
                self.match(CSharpParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Delegate_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELEGATE(self):
            return self.getToken(CSharpParser.DELEGATE, 0)

        def return_type(self):
            return self.getTypedRuleContext(CSharpParser.Return_typeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def variant_type_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Variant_type_parameter_listContext,0)


        def formal_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Formal_parameter_listContext,0)


        def type_parameter_constraints_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clausesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_delegate_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelegate_definition" ):
                listener.enterDelegate_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelegate_definition" ):
                listener.exitDelegate_definition(self)




    def delegate_definition(self):

        localctx = CSharpParser.Delegate_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_delegate_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2478
            self.match(CSharpParser.DELEGATE)
            self.state = 2479
            self.return_type()
            self.state = 2480
            self.identifier()
            self.state = 2482
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.LT:
                self.state = 2481
                self.variant_type_parameter_list()


            self.state = 2484
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 2486
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (CSharpParser.ADD - 10)) | (1 << (CSharpParser.ALIAS - 10)) | (1 << (CSharpParser.ARGLIST - 10)) | (1 << (CSharpParser.ASCENDING - 10)) | (1 << (CSharpParser.ASYNC - 10)) | (1 << (CSharpParser.AWAIT - 10)) | (1 << (CSharpParser.BOOL - 10)) | (1 << (CSharpParser.BY - 10)) | (1 << (CSharpParser.BYTE - 10)) | (1 << (CSharpParser.CHAR - 10)) | (1 << (CSharpParser.DECIMAL - 10)) | (1 << (CSharpParser.DESCENDING - 10)) | (1 << (CSharpParser.DOUBLE - 10)) | (1 << (CSharpParser.DYNAMIC - 10)) | (1 << (CSharpParser.EQUALS - 10)) | (1 << (CSharpParser.FLOAT - 10)) | (1 << (CSharpParser.FROM - 10)) | (1 << (CSharpParser.GET - 10)) | (1 << (CSharpParser.GROUP - 10)) | (1 << (CSharpParser.IN - 10)) | (1 << (CSharpParser.INT - 10)) | (1 << (CSharpParser.INTO - 10)) | (1 << (CSharpParser.JOIN - 10)) | (1 << (CSharpParser.LET - 10)) | (1 << (CSharpParser.LONG - 10)) | (1 << (CSharpParser.NAMEOF - 10)) | (1 << (CSharpParser.OBJECT - 10)) | (1 << (CSharpParser.ON - 10)) | (1 << (CSharpParser.ORDERBY - 10)) | (1 << (CSharpParser.OUT - 10)))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (CSharpParser.PARAMS - 74)) | (1 << (CSharpParser.PARTIAL - 74)) | (1 << (CSharpParser.REF - 74)) | (1 << (CSharpParser.REMOVE - 74)) | (1 << (CSharpParser.SBYTE - 74)) | (1 << (CSharpParser.SELECT - 74)) | (1 << (CSharpParser.SET - 74)) | (1 << (CSharpParser.SHORT - 74)) | (1 << (CSharpParser.STRING - 74)) | (1 << (CSharpParser.THIS - 74)) | (1 << (CSharpParser.UINT - 74)) | (1 << (CSharpParser.ULONG - 74)) | (1 << (CSharpParser.UNMANAGED - 74)) | (1 << (CSharpParser.USHORT - 74)) | (1 << (CSharpParser.VAR - 74)) | (1 << (CSharpParser.VOID - 74)) | (1 << (CSharpParser.WHEN - 74)) | (1 << (CSharpParser.WHERE - 74)) | (1 << (CSharpParser.YIELD - 74)) | (1 << (CSharpParser.IDENTIFIER - 74)) | (1 << (CSharpParser.OPEN_BRACKET - 74)) | (1 << (CSharpParser.OPEN_PARENS - 74)))) != 0):
                self.state = 2485
                self.formal_parameter_list()


            self.state = 2488
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 2490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHERE:
                self.state = 2489
                self.type_parameter_constraints_clauses()


            self.state = 2492
            self.match(CSharpParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Event_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EVENT(self):
            return self.getToken(CSharpParser.EVENT, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def variable_declarators(self):
            return self.getTypedRuleContext(CSharpParser.Variable_declaratorsContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def member_name(self):
            return self.getTypedRuleContext(CSharpParser.Member_nameContext,0)


        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def event_accessor_declarations(self):
            return self.getTypedRuleContext(CSharpParser.Event_accessor_declarationsContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_event_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent_declaration" ):
                listener.enterEvent_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent_declaration" ):
                listener.exitEvent_declaration(self)




    def event_declaration(self):

        localctx = CSharpParser.Event_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_event_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2494
            self.match(CSharpParser.EVENT)
            self.state = 2495
            self.type_()
            self.state = 2504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,323,self._ctx)
            if la_ == 1:
                self.state = 2496
                self.variable_declarators()
                self.state = 2497
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.state = 2499
                self.member_name()
                self.state = 2500
                self.match(CSharpParser.OPEN_BRACE)
                self.state = 2501
                self.event_accessor_declarations()
                self.state = 2502
                self.match(CSharpParser.CLOSE_BRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declarators(self):
            return self.getTypedRuleContext(CSharpParser.Variable_declaratorsContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_field_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_declaration" ):
                listener.enterField_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_declaration" ):
                listener.exitField_declaration(self)




    def field_declaration(self):

        localctx = CSharpParser.Field_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_field_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2506
            self.variable_declarators()
            self.state = 2507
            self.match(CSharpParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Property_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_name(self):
            return self.getTypedRuleContext(CSharpParser.Member_nameContext,0)


        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def accessor_declarations(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_declarationsContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def variable_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Variable_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_property_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProperty_declaration" ):
                listener.enterProperty_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProperty_declaration" ):
                listener.exitProperty_declaration(self)




    def property_declaration(self):

        localctx = CSharpParser.Property_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 412, self.RULE_property_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2509
            self.member_name()
            self.state = 2523
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.state = 2510
                self.match(CSharpParser.OPEN_BRACE)
                self.state = 2511
                self.accessor_declarations()
                self.state = 2512
                self.match(CSharpParser.CLOSE_BRACE)
                self.state = 2517
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.ASSIGNMENT:
                    self.state = 2513
                    self.match(CSharpParser.ASSIGNMENT)
                    self.state = 2514
                    self.variable_initializer()
                    self.state = 2515
                    self.match(CSharpParser.SEMICOLON)


                pass
            elif token in [CSharpParser.ASSIGNMENT]:
                self.state = 2519
                self.right_arrow()
                self.state = 2520
                self.throwable_expression()
                self.state = 2521
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSharpParser.CONST, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def constant_declarators(self):
            return self.getTypedRuleContext(CSharpParser.Constant_declaratorsContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_constant_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant_declaration" ):
                listener.enterConstant_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant_declaration" ):
                listener.exitConstant_declaration(self)




    def constant_declaration(self):

        localctx = CSharpParser.Constant_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_constant_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2525
            self.match(CSharpParser.CONST)
            self.state = 2526
            self.type_()
            self.state = 2527
            self.constant_declarators()
            self.state = 2528
            self.match(CSharpParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexer_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THIS(self):
            return self.getToken(CSharpParser.THIS, 0)

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def formal_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Formal_parameter_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def accessor_declarations(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_declarationsContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_indexer_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexer_declaration" ):
                listener.enterIndexer_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexer_declaration" ):
                listener.exitIndexer_declaration(self)




    def indexer_declaration(self):

        localctx = CSharpParser.Indexer_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 416, self.RULE_indexer_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2530
            self.match(CSharpParser.THIS)
            self.state = 2531
            self.match(CSharpParser.OPEN_BRACKET)
            self.state = 2532
            self.formal_parameter_list()
            self.state = 2533
            self.match(CSharpParser.CLOSE_BRACKET)
            self.state = 2542
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.state = 2534
                self.match(CSharpParser.OPEN_BRACE)
                self.state = 2535
                self.accessor_declarations()
                self.state = 2536
                self.match(CSharpParser.CLOSE_BRACE)
                pass
            elif token in [CSharpParser.ASSIGNMENT]:
                self.state = 2538
                self.right_arrow()
                self.state = 2539
                self.throwable_expression()
                self.state = 2540
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TILDE(self):
            return self.getToken(CSharpParser.TILDE, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def body(self):
            return self.getTypedRuleContext(CSharpParser.BodyContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_destructor_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDestructor_definition" ):
                listener.enterDestructor_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDestructor_definition" ):
                listener.exitDestructor_definition(self)




    def destructor_definition(self):

        localctx = CSharpParser.Destructor_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 418, self.RULE_destructor_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2544
            self.match(CSharpParser.TILDE)
            self.state = 2545
            self.identifier()
            self.state = 2546
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 2547
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 2548
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def body(self):
            return self.getTypedRuleContext(CSharpParser.BodyContext,0)


        def formal_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Formal_parameter_listContext,0)


        def constructor_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Constructor_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_constructor_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructor_declaration" ):
                listener.enterConstructor_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructor_declaration" ):
                listener.exitConstructor_declaration(self)




    def constructor_declaration(self):

        localctx = CSharpParser.Constructor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 420, self.RULE_constructor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2550
            self.identifier()
            self.state = 2551
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 2553
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (CSharpParser.ADD - 10)) | (1 << (CSharpParser.ALIAS - 10)) | (1 << (CSharpParser.ARGLIST - 10)) | (1 << (CSharpParser.ASCENDING - 10)) | (1 << (CSharpParser.ASYNC - 10)) | (1 << (CSharpParser.AWAIT - 10)) | (1 << (CSharpParser.BOOL - 10)) | (1 << (CSharpParser.BY - 10)) | (1 << (CSharpParser.BYTE - 10)) | (1 << (CSharpParser.CHAR - 10)) | (1 << (CSharpParser.DECIMAL - 10)) | (1 << (CSharpParser.DESCENDING - 10)) | (1 << (CSharpParser.DOUBLE - 10)) | (1 << (CSharpParser.DYNAMIC - 10)) | (1 << (CSharpParser.EQUALS - 10)) | (1 << (CSharpParser.FLOAT - 10)) | (1 << (CSharpParser.FROM - 10)) | (1 << (CSharpParser.GET - 10)) | (1 << (CSharpParser.GROUP - 10)) | (1 << (CSharpParser.IN - 10)) | (1 << (CSharpParser.INT - 10)) | (1 << (CSharpParser.INTO - 10)) | (1 << (CSharpParser.JOIN - 10)) | (1 << (CSharpParser.LET - 10)) | (1 << (CSharpParser.LONG - 10)) | (1 << (CSharpParser.NAMEOF - 10)) | (1 << (CSharpParser.OBJECT - 10)) | (1 << (CSharpParser.ON - 10)) | (1 << (CSharpParser.ORDERBY - 10)) | (1 << (CSharpParser.OUT - 10)))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (CSharpParser.PARAMS - 74)) | (1 << (CSharpParser.PARTIAL - 74)) | (1 << (CSharpParser.REF - 74)) | (1 << (CSharpParser.REMOVE - 74)) | (1 << (CSharpParser.SBYTE - 74)) | (1 << (CSharpParser.SELECT - 74)) | (1 << (CSharpParser.SET - 74)) | (1 << (CSharpParser.SHORT - 74)) | (1 << (CSharpParser.STRING - 74)) | (1 << (CSharpParser.THIS - 74)) | (1 << (CSharpParser.UINT - 74)) | (1 << (CSharpParser.ULONG - 74)) | (1 << (CSharpParser.UNMANAGED - 74)) | (1 << (CSharpParser.USHORT - 74)) | (1 << (CSharpParser.VAR - 74)) | (1 << (CSharpParser.VOID - 74)) | (1 << (CSharpParser.WHEN - 74)) | (1 << (CSharpParser.WHERE - 74)) | (1 << (CSharpParser.YIELD - 74)) | (1 << (CSharpParser.IDENTIFIER - 74)) | (1 << (CSharpParser.OPEN_BRACKET - 74)) | (1 << (CSharpParser.OPEN_PARENS - 74)))) != 0):
                self.state = 2552
                self.formal_parameter_list()


            self.state = 2555
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 2557
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COLON:
                self.state = 2556
                self.constructor_initializer()


            self.state = 2559
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_member_name(self):
            return self.getTypedRuleContext(CSharpParser.Method_member_nameContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def method_body(self):
            return self.getTypedRuleContext(CSharpParser.Method_bodyContext,0)


        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def type_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_listContext,0)


        def formal_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Formal_parameter_listContext,0)


        def type_parameter_constraints_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clausesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_method_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_declaration" ):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_declaration" ):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = CSharpParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 422, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2561
            self.method_member_name()
            self.state = 2563
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.LT:
                self.state = 2562
                self.type_parameter_list()


            self.state = 2565
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 2567
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (CSharpParser.ADD - 10)) | (1 << (CSharpParser.ALIAS - 10)) | (1 << (CSharpParser.ARGLIST - 10)) | (1 << (CSharpParser.ASCENDING - 10)) | (1 << (CSharpParser.ASYNC - 10)) | (1 << (CSharpParser.AWAIT - 10)) | (1 << (CSharpParser.BOOL - 10)) | (1 << (CSharpParser.BY - 10)) | (1 << (CSharpParser.BYTE - 10)) | (1 << (CSharpParser.CHAR - 10)) | (1 << (CSharpParser.DECIMAL - 10)) | (1 << (CSharpParser.DESCENDING - 10)) | (1 << (CSharpParser.DOUBLE - 10)) | (1 << (CSharpParser.DYNAMIC - 10)) | (1 << (CSharpParser.EQUALS - 10)) | (1 << (CSharpParser.FLOAT - 10)) | (1 << (CSharpParser.FROM - 10)) | (1 << (CSharpParser.GET - 10)) | (1 << (CSharpParser.GROUP - 10)) | (1 << (CSharpParser.IN - 10)) | (1 << (CSharpParser.INT - 10)) | (1 << (CSharpParser.INTO - 10)) | (1 << (CSharpParser.JOIN - 10)) | (1 << (CSharpParser.LET - 10)) | (1 << (CSharpParser.LONG - 10)) | (1 << (CSharpParser.NAMEOF - 10)) | (1 << (CSharpParser.OBJECT - 10)) | (1 << (CSharpParser.ON - 10)) | (1 << (CSharpParser.ORDERBY - 10)) | (1 << (CSharpParser.OUT - 10)))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (CSharpParser.PARAMS - 74)) | (1 << (CSharpParser.PARTIAL - 74)) | (1 << (CSharpParser.REF - 74)) | (1 << (CSharpParser.REMOVE - 74)) | (1 << (CSharpParser.SBYTE - 74)) | (1 << (CSharpParser.SELECT - 74)) | (1 << (CSharpParser.SET - 74)) | (1 << (CSharpParser.SHORT - 74)) | (1 << (CSharpParser.STRING - 74)) | (1 << (CSharpParser.THIS - 74)) | (1 << (CSharpParser.UINT - 74)) | (1 << (CSharpParser.ULONG - 74)) | (1 << (CSharpParser.UNMANAGED - 74)) | (1 << (CSharpParser.USHORT - 74)) | (1 << (CSharpParser.VAR - 74)) | (1 << (CSharpParser.VOID - 74)) | (1 << (CSharpParser.WHEN - 74)) | (1 << (CSharpParser.WHERE - 74)) | (1 << (CSharpParser.YIELD - 74)) | (1 << (CSharpParser.IDENTIFIER - 74)) | (1 << (CSharpParser.OPEN_BRACKET - 74)) | (1 << (CSharpParser.OPEN_PARENS - 74)))) != 0):
                self.state = 2566
                self.formal_parameter_list()


            self.state = 2569
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 2571
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHERE:
                self.state = 2570
                self.type_parameter_constraints_clauses()


            self.state = 2578
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE, CSharpParser.SEMICOLON]:
                self.state = 2573
                self.method_body()
                pass
            elif token in [CSharpParser.ASSIGNMENT]:
                self.state = 2574
                self.right_arrow()
                self.state = 2575
                self.throwable_expression()
                self.state = 2576
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_member_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def DOUBLE_COLON(self):
            return self.getToken(CSharpParser.DOUBLE_COLON, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.DOT)
            else:
                return self.getToken(CSharpParser.DOT, i)

        def type_argument_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Type_argument_listContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Type_argument_listContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_method_member_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_member_name" ):
                listener.enterMethod_member_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_member_name" ):
                listener.exitMethod_member_name(self)




    def method_member_name(self):

        localctx = CSharpParser.Method_member_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 424, self.RULE_method_member_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2585
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,333,self._ctx)
            if la_ == 1:
                self.state = 2580
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 2581
                self.identifier()
                self.state = 2582
                self.match(CSharpParser.DOUBLE_COLON)
                self.state = 2583
                self.identifier()
                pass


            self.state = 2594
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,335,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2588
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpParser.LT:
                        self.state = 2587
                        self.type_argument_list()


                    self.state = 2590
                    self.match(CSharpParser.DOT)
                    self.state = 2591
                    self.identifier() 
                self.state = 2596
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,335,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operator_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(CSharpParser.OPERATOR, 0)

        def overloadable_operator(self):
            return self.getTypedRuleContext(CSharpParser.Overloadable_operatorContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def arg_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Arg_declarationContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Arg_declarationContext,i)


        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def body(self):
            return self.getTypedRuleContext(CSharpParser.BodyContext,0)


        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def IN(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.IN)
            else:
                return self.getToken(CSharpParser.IN, i)

        def COMMA(self):
            return self.getToken(CSharpParser.COMMA, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_operator_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator_declaration" ):
                listener.enterOperator_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator_declaration" ):
                listener.exitOperator_declaration(self)




    def operator_declaration(self):

        localctx = CSharpParser.Operator_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 426, self.RULE_operator_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2597
            self.match(CSharpParser.OPERATOR)
            self.state = 2598
            self.overloadable_operator()
            self.state = 2599
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 2601
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.IN:
                self.state = 2600
                self.match(CSharpParser.IN)


            self.state = 2603
            self.arg_declaration()
            self.state = 2609
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COMMA:
                self.state = 2604
                self.match(CSharpParser.COMMA)
                self.state = 2606
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.IN:
                    self.state = 2605
                    self.match(CSharpParser.IN)


                self.state = 2608
                self.arg_declaration()


            self.state = 2611
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 2617
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE, CSharpParser.SEMICOLON]:
                self.state = 2612
                self.body()
                pass
            elif token in [CSharpParser.ASSIGNMENT]:
                self.state = 2613
                self.right_arrow()
                self.state = 2614
                self.throwable_expression()
                self.state = 2615
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_arg_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_declaration" ):
                listener.enterArg_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_declaration" ):
                listener.exitArg_declaration(self)




    def arg_declaration(self):

        localctx = CSharpParser.Arg_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 428, self.RULE_arg_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2619
            self.type_()
            self.state = 2620
            self.identifier()
            self.state = 2623
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.ASSIGNMENT:
                self.state = 2621
                self.match(CSharpParser.ASSIGNMENT)
                self.state = 2622
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def argument_list(self):
            return self.getTypedRuleContext(CSharpParser.Argument_listContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_method_invocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_invocation" ):
                listener.enterMethod_invocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_invocation" ):
                listener.exitMethod_invocation(self)




    def method_invocation(self):

        localctx = CSharpParser.Method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 430, self.RULE_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2625
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 2627
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.OUT - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.VOID - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)))) != 0):
                self.state = 2626
                self.argument_list()


            self.state = 2629
            self.match(CSharpParser.CLOSE_PARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_creation_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def argument_list(self):
            return self.getTypedRuleContext(CSharpParser.Argument_listContext,0)


        def object_or_collection_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Object_or_collection_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_object_creation_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_creation_expression" ):
                listener.enterObject_creation_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_creation_expression" ):
                listener.exitObject_creation_expression(self)




    def object_creation_expression(self):

        localctx = CSharpParser.Object_creation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 432, self.RULE_object_creation_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2631
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 2633
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.OUT - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.VOID - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)) | (1 << (CSharpParser.LITERAL_ACCESS - 64)) | (1 << (CSharpParser.INTEGER_LITERAL - 64)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 64)) | (1 << (CSharpParser.REAL_LITERAL - 64)) | (1 << (CSharpParser.CHARACTER_LITERAL - 64)) | (1 << (CSharpParser.REGULAR_STRING - 64)) | (1 << (CSharpParser.VERBATIUM_STRING - 64)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 64)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 64)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (CSharpParser.OPEN_PARENS - 129)) | (1 << (CSharpParser.PLUS - 129)) | (1 << (CSharpParser.MINUS - 129)) | (1 << (CSharpParser.STAR - 129)) | (1 << (CSharpParser.AMP - 129)) | (1 << (CSharpParser.CARET - 129)) | (1 << (CSharpParser.BANG - 129)) | (1 << (CSharpParser.TILDE - 129)) | (1 << (CSharpParser.OP_INC - 129)) | (1 << (CSharpParser.OP_DEC - 129)) | (1 << (CSharpParser.OP_RANGE - 129)))) != 0):
                self.state = 2632
                self.argument_list()


            self.state = 2635
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 2637
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACE:
                self.state = 2636
                self.object_or_collection_initializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CSharpParser.IDENTIFIER, 0)

        def ADD(self):
            return self.getToken(CSharpParser.ADD, 0)

        def ALIAS(self):
            return self.getToken(CSharpParser.ALIAS, 0)

        def ARGLIST(self):
            return self.getToken(CSharpParser.ARGLIST, 0)

        def ASCENDING(self):
            return self.getToken(CSharpParser.ASCENDING, 0)

        def ASYNC(self):
            return self.getToken(CSharpParser.ASYNC, 0)

        def AWAIT(self):
            return self.getToken(CSharpParser.AWAIT, 0)

        def BY(self):
            return self.getToken(CSharpParser.BY, 0)

        def DESCENDING(self):
            return self.getToken(CSharpParser.DESCENDING, 0)

        def DYNAMIC(self):
            return self.getToken(CSharpParser.DYNAMIC, 0)

        def EQUALS(self):
            return self.getToken(CSharpParser.EQUALS, 0)

        def FROM(self):
            return self.getToken(CSharpParser.FROM, 0)

        def GET(self):
            return self.getToken(CSharpParser.GET, 0)

        def GROUP(self):
            return self.getToken(CSharpParser.GROUP, 0)

        def INTO(self):
            return self.getToken(CSharpParser.INTO, 0)

        def JOIN(self):
            return self.getToken(CSharpParser.JOIN, 0)

        def LET(self):
            return self.getToken(CSharpParser.LET, 0)

        def NAMEOF(self):
            return self.getToken(CSharpParser.NAMEOF, 0)

        def ON(self):
            return self.getToken(CSharpParser.ON, 0)

        def ORDERBY(self):
            return self.getToken(CSharpParser.ORDERBY, 0)

        def PARTIAL(self):
            return self.getToken(CSharpParser.PARTIAL, 0)

        def REMOVE(self):
            return self.getToken(CSharpParser.REMOVE, 0)

        def SELECT(self):
            return self.getToken(CSharpParser.SELECT, 0)

        def SET(self):
            return self.getToken(CSharpParser.SET, 0)

        def UNMANAGED(self):
            return self.getToken(CSharpParser.UNMANAGED, 0)

        def VAR(self):
            return self.getToken(CSharpParser.VAR, 0)

        def WHEN(self):
            return self.getToken(CSharpParser.WHEN, 0)

        def WHERE(self):
            return self.getToken(CSharpParser.WHERE, 0)

        def YIELD(self):
            return self.getToken(CSharpParser.YIELD, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = CSharpParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 434, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2639
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BY) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMEOF - 64)) | (1 << (CSharpParser.ON - 64)) | (1 << (CSharpParser.ORDERBY - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.REMOVE - 64)) | (1 << (CSharpParser.SELECT - 64)) | (1 << (CSharpParser.SET - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.VAR - 64)) | (1 << (CSharpParser.WHEN - 64)) | (1 << (CSharpParser.WHERE - 64)) | (1 << (CSharpParser.YIELD - 64)) | (1 << (CSharpParser.IDENTIFIER - 64)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[187] = self.right_arrow_sempred
        self._predicates[188] = self.right_shift_sempred
        self._predicates[189] = self.right_shift_assignment_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def right_arrow_sempred(self, localctx:Right_arrowContext, predIndex:int):
            if predIndex == 0:
                return (0 if localctx.first is None else localctx.first.tokenIndex) + 1 == (0 if localctx.second is None else localctx.second.tokenIndex)
         

    def right_shift_sempred(self, localctx:Right_shiftContext, predIndex:int):
            if predIndex == 1:
                return (0 if localctx.first is None else localctx.first.tokenIndex) + 1 == (0 if localctx.second is None else localctx.second.tokenIndex)
         

    def right_shift_assignment_sempred(self, localctx:Right_shift_assignmentContext, predIndex:int):
            if predIndex == 2:
                return (0 if localctx.first is None else localctx.first.tokenIndex) + 1 == (0 if localctx.second is None else localctx.second.tokenIndex)
         




