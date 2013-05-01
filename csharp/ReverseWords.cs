//Google Code Jam 2010 https://code.google.com/codejam/contest/351101/dashboard#s=p1
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GoogleCodeJam
{
    public class ReverseWords
    {
        public void Answer(TextReader input)
        {
            string line = input.ReadLine();
            int nOfCases = Convert.ToInt32(line);
            for (int caseNo = 1; caseNo <= nOfCases; caseNo++)
            {
                //Read Credit amount
                line = input.ReadLine();
                IEnumerable<String> words = line.Split(' ').Reverse();
                StringBuilder builder = new StringBuilder();
                foreach (var word in words)
                {
                    builder.Append(word);
                    builder.Append(" ");
                }

                Console.Out.WriteLine(
                    String.Format("Case #{0}: {1} ", caseNo, builder.ToString().Trim())
                    );
            }
        }
    }
}
