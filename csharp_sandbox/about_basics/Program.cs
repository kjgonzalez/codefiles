/*
Basics of C# language, including some builtins

notes:
* the following is a complete hello world console program:
    public class Program { public static void Main() { Console.WriteLine("hello world"); } }
* unsafe code: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/unsafe-code
* nullable code: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-value-types



k260521: todo: 
* null coalescing operator (?? and ??=)
 * write & read file
* args in
* unsafe
* lib "File" and "Folder"(?)
* "Pack" : byte alignment, etc.
* class and inheritance
* about: lists
* about: arrays
* about: datatables
* about: collections
* (etc)


*/

#define MYSYM // a preprocessor define can't hold a value, only be defined or not defined. called a symbol

using ns_klib; // when you include/import a library, you usually just call its namespace explicitly.
using System.Runtime.CompilerServices;

class Shape
{
    public int color;
    public virtual double Area() { throw new Exception("not implemented"); }
}

class Rect : Shape
{
    double x = 0;
    double y = 0;
    public Rect(double x, double y) { this.x = x; this.y = y; }
    public override double Area() { return x * y; }
}

class Tri : Shape
{
    double b = 0;
    double h = 0;
    public Tri(double b, double h) { this.b = b; this.h = h; }
    public override double Area() { return b * h / 2; }
}

//"main" class which contains "Main" function, must always be "public static void Main"
public class Program {

    enum Season { Spring, Summer, Fall, Winter }

    public static void f01_core()
    {
        Console.WriteLine("hello world!");
        Console.WriteLine(Klib.add2(2, 3));
        Console.WriteLine($"is {3}bigger than {2}? {3 > 2}");

        // primitive types
        Console.WriteLine($"bool  : {sizeof(bool)}");
        Console.WriteLine($"byte  : {sizeof(byte)} (uchar)");
        Console.WriteLine($"sbyte : {sizeof(sbyte)}");
        Console.WriteLine($"char  : {sizeof(char)}");
        Console.WriteLine($"short : {sizeof(short)}");
        Console.WriteLine($"ushort: {sizeof(ushort)} (unsigned short)");
        Console.WriteLine($"int   : {sizeof(int)}");
        Console.WriteLine($"long  : {sizeof(long)}");
        Console.WriteLine($"UInt64: {sizeof(UInt64)} note: can specify UInt16 up to 128");
        Console.WriteLine($"float : {sizeof(float)}");
        Console.WriteLine($"double: {sizeof(double)}");
        unsafe { // enable via: Project settings >> Build >> General >> Unsafe code
            //nsole.WriteLine($"double: {sizeof(double)}");
            Console.WriteLine($"nint  : {sizeof(nint)} (\"native integer\")"); // not known before compilation
            Console.WriteLine($"nuint : {sizeof(nuint)} (\"native unsigned integer\")");
            Console.WriteLine($"enum  : {sizeof(Season)} (default)"); // variable?
        }

        // enums, dicts (maps)
        Season s = Season.Fall;
        Console.WriteLine($"season: {s} ({(int)s})");//prints name, can force to num
        Dictionary<Season, int[]> d = new Dictionary<Season, int[]>(); // "basic" way to instantiate an object
        Dictionary<Season, int[]> _tmp = new(); // "nice" way
        d.Add(Season.Spring, new int[] { 1, 2, 3 });
        d.Add(Season.Summer, new int[] { 1, 2, 3, 4 });
        d.Add(Season.Fall, new int[] { 1, 2, 3, 4, 5 });
        d.Add(Season.Winter, new int[] { 1, 2, 3, 4, 5, 6 });
        Console.WriteLine($"dict: nkeys={d.Count}, has <key>={d.ContainsKey(Season.Winter)}");

        // bit operations
        Console.WriteLine($"{1 << 3}");
        Console.WriteLine($"{8 << 3}");
        Console.WriteLine($"{2| 8}");
        Console.WriteLine($"");

        // math operations
        int x = 2;
        x += 2;
        x++;
        x = 6 % 4; // modulo
        x = (int) Math.Pow(2, 3); // note: pow uses double
        x = x > 10 ? 3 : 5; // ternary
        Console.WriteLine($"ternary: {(x > 4 ? 5 : 6)}"); // note: ternary in formatted ("interpolated") string requires parentheses

        // loops




    }



    public static void Main() 
    {
        f01_core();

    }
}//program




