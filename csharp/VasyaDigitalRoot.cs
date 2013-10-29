using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeForces
{
    class VasyaDigitalRoot
    {
         public static void Main()
        {
            //TextReader reader = new StreamReader("/test.txt");
            Answer(Console.In);
            Console.ReadLine();

        }

        public static void Answer(TextReader reader)
         {
             int[] array = reader.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
             int k = array[0];
             int d = array[1];

            if(d == 0 && k != 1)
                Console.WriteLine("No solution");

            else
            {
                Console.Write(d);
                for(int i = 1; i < k; i++)
                    Console.Write(0);
                Console.WriteLine();
            }
         }
    }
}
