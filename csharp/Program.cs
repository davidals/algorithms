using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GoogleCodeJam
{
    class Program
    {
       
        static void Main(string[] args)
        {
            TextReader reader = new StreamReader("/test.txt");
            //TextReader reader = Console.In;
            new Bullseye().Answer(reader);
            Console.Read();
        }
    }
}
