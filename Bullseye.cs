using System;
using System.IO;


namespace GoogleCodeJam
{
    class Bullseye
    {
        public void Answer(TextReader input)
        {
            string line = input.ReadLine();
            int nOfCases = Convert.ToInt32(line);
            
            for (int caseNo = 1; caseNo <= nOfCases; caseNo++)
            {
                //Size
                line = input.ReadLine();
                long r = Convert.ToInt64(line.Split(' ')[0]);
                long t = Convert.ToInt64(line.Split(' ')[1]);

                var result = 1;
                var used = 0.0;
                while(used < t)
                {
                    used += Math.Pow(r + 1, 2) - Math.Pow(r, 2);
                    if(used > t) break;

                    result++;
                    r += 2;
                   
                }
               
                Console.Out.WriteLine("Case #{0}: {1}", caseNo, result);
            }

        }
    }
}
