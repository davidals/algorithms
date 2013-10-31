using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;


namespace CodeForces
{
    public class DimaAndContinuousLine
    {
        private class Line
        {
            public int From { get; set; }
            public int To { get; set; }

        }
        public static void Main()
        {
            //TextReader reader = new StreamReader("/test.txt");
            Answer(Console.In);
            Console.ReadLine();

        }

        public static void Answer(TextReader reader)
        {
            int n = Convert.ToInt32(reader.ReadLine());
            int[] coordinates = reader.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
            List<Line> lines = new List<Line>();
            
            for (int index = 0; index < coordinates.Length - 1; index++)
            {
                int a = coordinates[index];
                int b = coordinates[index + 1];
                lines.Add(new Line {From = Math.Min(a,b), To = Math.Max(a,b)});
            }

            for (int i = 0; i < lines.Count; i++)
            {
                for(int j = 0; j< lines.Count; j++)
                {
                    if (intersect(lines[i], lines[j]))
                    {
                        Console.WriteLine("yes");
                        return;
                    }
                }
            }
            Console.WriteLine("no");
        }

        private static bool intersect(Line a, Line b)
        {
            return (IsBetween(a.From, b) && a.To > b.To) ||
                   (IsBetween(b.From, a) && b.To > a.To);
        }

        private static bool IsBetween(int a, Line l)
        {
            return a > l.From && a < l.To;
        }
    }
}
