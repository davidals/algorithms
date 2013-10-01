using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeForces
{
    /*
     * Answer to:
     * http://codeforces.com/contest/349/problem/B
     */ 
    public class ColorTheFence
    {
        public static void Answer(TextReader reader)
        {
            int liters;
            
            Dictionary<int, int> consumption = new Dictionary<int, int>();
            
            liters = Convert.ToInt32(reader.ReadLine());
            int[] array = reader.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
            
            for (int index = 0; index < array.Length; index++)
                 consumption[index+1] = array[index];


            if(liters < consumption.Values.Min()) Console.WriteLine("-1");
            
            

            //Finds the number with more digits
            int nOfDigits = liters/consumption.Values.Min();
            int maxDigit = consumption.Where(x => x.Value == consumption.Values.Min()).Max(x=> x.Key);

            StringBuilder number = new StringBuilder();
            for (int i = 0; i < nOfDigits; i++ )
            {
                number.Append(maxDigit);
                liters -= consumption[maxDigit];
            }

            StringBuilder result = new StringBuilder();
            //Maybe there is a greater number with the same amount of digits
            IOrderedEnumerable<KeyValuePair<int, int>> digitsReverseOrder = consumption.OrderByDescending(x => x.Key);
            if(liters > 0)
            {
                foreach (var c in number.ToString())
                {
                    int digit = Convert.ToInt32(c.ToString());
                    if (liters == 0) result.Append(digit);
                    else foreach (var pair in digitsReverseOrder)
                        {
                            if(liters + consumption[digit] >= pair.Value)
                            {
                                result.Append(pair.Key);
                                liters = liters + consumption[digit] - pair.Value;
                                break;
                            }
                        }
                }    
                
            }
            else
            {
                result = number;
            }
            
            Console.WriteLine(result.ToString());
        }
    }   
}
