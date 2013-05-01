//Google Code Jam 2010 https://code.google.com/codejam/contest/351101/dashboard#s=p0

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GoogleCodeJam
{
    public class StoreCredit
    {
        private class Mapping
        {
            public int OldPos { get; set; }
            public int Value { get; set; }
        }

        public void Answer(TextReader input)
        {
            string line = input.ReadLine();
            int nOfCases = Convert.ToInt32(line);
            for (int caseNo = 1; caseNo <= nOfCases; caseNo++)
            {
                //Read Credit amount
                line = input.ReadLine();
                int c = Convert.ToInt32(line);
                //Read itens number
                line = input.ReadLine();
                //Read itens
                line = input.ReadLine();
                String[] itens = line.Split(' ');
                int count = 1;
                Mapping[] intItens = (from x in itens
                                      select new Mapping {Value = Convert.ToInt32(x), OldPos = count++}).OrderBy(x => x.Value).ToArray();

                int[] solution = FindItens(intItens, c);
                
                Console.Out.WriteLine(
                    String.Format("Case #{0}: {1} {2}", caseNo, solution[0], solution[1])
                    );
            }
        }

        private int[] FindItens(Mapping[] itens, int c)
        {
            var result = new int[2];
            int i = 0;
            int j = itens.Length - 1;

            while (i < j)
            {
                if (itens[i].Value + itens[j].Value > c)
                    j--;
                else if (itens[i].Value + itens[j].Value < c)
                    i++;
                else
                    break;
                
            }
            result[0] = itens[i].OldPos;
            result[1] = itens[j].OldPos;
            return result;
        }


    }
}
