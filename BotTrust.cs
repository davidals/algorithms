//Google codejam 2011 https://code.google.com/codejam/contest/975485/dashboard
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GoogleCodeJam
{
    class Step
    {
        public String Robot { get; set; }
        public int Position { get; set; }
    }

    class Robot
    {
        public bool[] Hallway { get; set; }
        public int Position { get; set; }

        public Robot()
        {
            Hallway = new bool[101];
            Position = 1;
            Hallway[Position] = true;
        }

        public bool Move(Step nextStep, Step currentStep)
        {
            //Nothing More to do so wait until the other bot finishes
            if (nextStep == null)
                return false;
            //Time to Push Button
            if (Hallway[Position] && nextStep.Equals(currentStep) && nextStep.Position == Position)

                return true;
            //Arrived at the button before the other bot finished it's turn.
            else if (Hallway[Position] && nextStep.Position == Position) { }

            // Move Forward
            else if (nextStep.Position > Position)
            {
                Hallway[Position] = false;
                Position++;
                Hallway[Position] = true;
            }

            // Move Backwards
            else if (nextStep.Position < Position)
            {
                Hallway[Position] = false;
                Position--;
                Hallway[Position] = true;
            }
            return false;
        }

    }
    class BotTrust
    {
        public List<Step> Steps { get; set; }
        public int OPos { get; set; }
        public int BPos { get; set; }
        public bool[] O { get; set; }
        public bool[] B { get; set; }
        
        public BotTrust()
        {
            Steps = new List<Step>();
            O = new bool[101];
            B = new bool[101];
        }

        public void Answer(TextReader input)
        {
            string line = input.ReadLine();
            int nOfCases = Convert.ToInt32(line);
            for (int caseNo = 1; caseNo <= nOfCases; caseNo++)
            {
                //Read Credit amount
                line = input.ReadLine();
                var stuff = line.Split(' ');
                var nOfButtons = stuff[0];
                

                for (int i = 1; i < stuff.Length; i+=2)
                {
                    var robot = stuff[i];
                    var buttonPosition = stuff[i + 1];
                    Steps.Add(new Step { Robot = robot, Position = Convert.ToInt32(buttonPosition) });
                }

                Robot o = new Robot();
                Robot b = new Robot();
                int moves = 0;
                while (Steps.Count > 0)
                {
                    var currentStep = Steps.FirstOrDefault();
                    bool pushO = o.Move(FindNextStep("O"),currentStep);
                    bool pushB = b.Move(FindNextStep("B"),currentStep);
                    if(pushO || pushB)
                        Steps.RemoveAt(0);

                    moves++;
                }

                Console.Out.WriteLine("Case #{0}: {1} ", caseNo, moves);
                //Clear for next case
                Steps.Clear();
            }
        }

        
        
        private Step FindNextStep(string robot)
        {
            return Steps.FirstOrDefault(s => s.Robot.Equals(robot.ToUpper()));
        }
    }
}
