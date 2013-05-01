//Google Codejam 2011 https://code.google.com/codejam/contest/975485/dashboard#s=p1

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GoogleCodeJam
{
    class Combination
    {
        public String A { get; set; }
        public String B { get; set; }
        public String Result { get; set; }
    }

    public class Magicka
    {
        private String[] elements = {"Q", "W", "E", "R", "A", "S", "D", "F"};

        public void Answer(TextReader input)
        {
            string line = input.ReadLine();
            int nOfCases = Convert.ToInt32(line);
            for (int caseNo = 1; caseNo <= nOfCases; caseNo++)
            {

                var Combinations = new List<Combination>();
                var Opposing = new Dictionary<String, List<String>>();
                //Data
                line = input.ReadLine();

                var args = line.Split(' ');

                int index = 0;

                int C = Convert.ToInt32(args[index++]);
                for (int count = 0; count < C; count++ )
                {
                    String combs = args[index++];
                    for (int i = 0; i < combs.Length; i += 3)
                    {
                        Combinations.Add(new Combination
                                             {
                                                 A = combs[i].ToString(),
                                                 B = combs[i + 1].ToString(),
                                                 Result = combs[i + 2].ToString()
                                             });
                    }
                }
                int D = Convert.ToInt32(args[index++]);
                for (int count = 0; count < D; count++)
                {
                    String oppos = args[index++];
                    for (int i = 0; i < oppos.Length; i += 2)
                    {
                        String a = oppos[i].ToString();
                        String b = oppos[i+1].ToString();

                        CreateList(a, Opposing);
                        CreateList(b, Opposing);

                        Opposing[a].Add(b);
                        Opposing[b].Add(a);
                    }
                }

                int N = Convert.ToInt32(args[index++]);

                String invoke = args[index];

                var output = new List<String>();

                foreach (var element in invoke)
                {
                    output.Add(element.ToString());
                    Combine(output, Combinations);
                    if(ContainsOpposing(output,Opposing))
                        output.Clear();
                }

                Console.Out.WriteLine(CreateOutput(caseNo, output));

            }
        }

        private String CreateOutput(int caseNo, List<string> output)
        {
            StringBuilder builder = new StringBuilder();
            builder.Append(string.Format("Case #{0}: [", caseNo));
            bool hasSomething = false;
            foreach (var element in output)
            {
                builder.Append(element);
                builder.Append(", ");
                hasSomething = true;
            }
            if(hasSomething)
                builder.Remove(builder.Length - 2, 2);
            builder.Append("]");
            return builder.ToString();

        }

        private void Combine(List<string> output, List<Combination> combinations)
        {
            if (output.Count > 1)
            {
                String b = output[output.Count - 1];
                String a = output[output.Count - 2];

                foreach (var combination in combinations)
                {
                    if ((combination.A.Equals(a) && combination.B.Equals(b)) ||
                        (combination.A.Equals(b) && combination.B.Equals(a)))
                    {
                        output.RemoveAt(output.Count - 1);
                        output.RemoveAt(output.Count - 1);
                        output.Add(combination.Result);
                    }
                }
            }
        }

        private bool ContainsOpposing(List<string> output, Dictionary<string, List<string>> opposing)
        {
            foreach (var element in output)
            {
                if (opposing.ContainsKey(element))
                    if (opposing[element].Any(opposite => output.Contains(opposite)))
                    {
                        return true;
                    }
            }
            return false;
        }

        private void CreateList(string s, Dictionary<string, List<string>> map)
        {
            if(!map.ContainsKey(s))
                map[s] = new List<string>();
        }
    }
}

