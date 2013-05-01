//Google code jam 2010 https://code.google.com/codejam/contest/351101/dashboard#s=p2
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GoogleCodeJam
{
    public class T9Spelling
    {
        public Dictionary<char, String> map;
        public void Answer(TextReader input)
        {
            BuildMap();
            string line = input.ReadLine();
            int nOfCases = Convert.ToInt32(line);
            for (int caseNo = 1; caseNo <= nOfCases; caseNo++)
            {
                //Read Credit amount
                line = input.ReadLine();
                StringBuilder builder = new StringBuilder();
                var last = '.';
                if (String.IsNullOrEmpty(line))
                    builder.Append("0");
                else
                    foreach (char c in line)
                    {
                        var digits = map[c];
                        var next = digits[0];
                        if (last.Equals(next))
                            builder.Append(" ");
                        builder.Append(map[c]);
                        last = digits[digits.Length - 1];
                    }

                Console.Out.WriteLine(
                    String.Format("Case #{0}: {1} ", caseNo, builder.ToString().Trim())
                    );
            }
        }

        private void BuildMap()
        {
            map= new Dictionary<char, String>();

            map['a'] = "2";
            map['b'] = "22";
            map['c'] = "222";

            map['d'] = "3";
            map['e'] = "33";
            map['f'] = "333";

            map['g'] = "4";
            map['h'] = "44";
            map['i'] = "444";

            map['j'] = "5";
            map['k'] = "55";
            map['l'] = "555";

            map['m'] = "6";
            map['n'] = "66";
            map['o'] = "666";

            map['p'] = "7";
            map['q'] = "77";
            map['r'] = "777";
            map['s'] = "7777";

            map['t'] = "8";
            map['u'] = "88";
            map['v'] = "888";

            map['w'] = "9";
            map['x'] = "99";
            map['y'] = "999";
            map['z'] = "9999";

            map[' '] = "0";
        }
    }
}
