//Google Codejam 2011 https://code.google.com/codejam/contest/975485/dashboard#s=p2
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GoogleCodeJam
{
    class CandySplitting
    {
        public void Answer(TextReader input)
        {
            string line = input.ReadLine();
            int nOfCases = Convert.ToInt32(line);
            for (int caseNo = 1; caseNo <= nOfCases; caseNo++)
            {
                //N of candies
                line = input.ReadLine();
                //Candies
                line = input.ReadLine();
                var candies = line.Split(' ').Select(x => Convert.ToInt32(x)).OrderBy(x => x).ToArray();

                if (XorUpTo(candies, candies.Length) == 0)
                    Console.Out.WriteLine("Case #{0}: {1} ", caseNo, SumFrom(candies,1));        
                else
                    Console.Out.WriteLine("Case #{0}: {1} ", caseNo, "NO");        
            }
        }

        private int SumFrom(int[] candies, int index)
        {
            int result = 0;
            for (int i = index; i < candies.Length; i++)
            {
                var candy = candies[i];
                result = result + candy;
            }
            return result;
        }
        
        private int XorUpTo(int[] candies, int index)
        {
            int result = 0;
            for (int i = 0; i < index; i++)
            {
                var candy = candies[i];
                result = result ^ candy;
            }
            return result;
        }
    }

}
