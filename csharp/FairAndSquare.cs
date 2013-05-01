using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GoogleCodeJam
{
    class FairAndSquare
    {
        public void Answer(TextReader input)
        {
            string line = input.ReadLine();
            int nOfCases = Convert.ToInt32(line);
            bool[] DP = new bool[100000000000000];
            for (int caseNo = 1; caseNo <= nOfCases; caseNo++)
            {
                //Size
                line = input.ReadLine();
                long low = Convert.ToInt64(line.Split(' ')[0]);
                long hi = Convert.ToInt64(line.Split(' ')[1]);
                long result = 0;
                for (long i = 1; i * i <= hi; i++)
                {
                    if(i * i >= low)
                    {
                        if (IsPalindrome(i) && IsPalindrome(i * i))
                        {
                            DP[i] = true;
                            result++;
                        }

                    }
                }
                 Console.Out.WriteLine("Case #{0}: {1}", caseNo, result);
            }

        }

        private bool IsPalindrome(long value)
        {
            string valueString = value.ToString();
            int i = 0;
            int j = valueString.Length -1;

            while(j > i && j > 0)
            {
                if(!valueString[i].Equals(valueString[j]))
                    return false;
                i++;
                j--;
            }
            return true;
        }
    }
}
