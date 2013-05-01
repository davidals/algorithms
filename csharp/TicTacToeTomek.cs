using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GoogleCodeJam
{
    class TicTacToeTomek
    {
        public void Answer(TextReader input)
        {
            string line = input.ReadLine();
            int nOfCases = Convert.ToInt32(line);
            for (int caseNo = 1; caseNo <= nOfCases; caseNo++)
            {
                //Init board
                char[][] board = new char[4][];
                for (int i = 0; i < 4; i++)
                {
                    board[i] = new char[4];    
                }
                //Read board
                for (int row = 0; row < 4; row++)
                {
                    line = input.ReadLine();
                    board[row][0] = line[0];
                    board[row][1] = line[1];
                    board[row][2] = line[2];
                    board[row][3] = line[3];
                }
                //Blank line
                input.ReadLine();
                string result = EvalBoard(board);
                Console.Out.WriteLine("Case #{0}: {1}", caseNo, result);
            }
        }

        private string EvalBoard(char[][] board)
        {
            
            if (HasWon('X', board))
                return "X won";
            
            if (HasWon('O', board))
                return "O won";

            if (HasEmptyCellInBoard(board))
                return "Game has not completed";

            return "Draw";
        }

        private bool HasWon(char player, char[][] board)
        {
            if (CheckForRows(player, board))
                return true;
            if (CheckForCols(player, board))
                return true;
            if (CheckForDiag(player, board))
                return true;
            return false;
        }

        private bool CheckForDiag(char player, char[][] board)
        {
            bool won = true;
            for(int i = 0; i < 4; i++)
            {
                won = won && (board[i][i].Equals(player) || board[i][i].Equals('T'));
            }
            if (!won)
            {
                won = true;
                for (int i = 0; i < 4; i++)
                {
                    won = won && (board[3 - i][i].Equals(player) || board[3 - i][i].Equals('T'));
                }
            }
            return won;
        }

        private bool CheckForCols(char player, char[][] board)
        {
            for (int j = 0; j < 4; j++)
            {
                bool rowCheck = true;
                for (int i = 0; i < 4; i++)
                {
                    rowCheck = rowCheck && (board[i][j].Equals(player) || board[i][j].Equals('T'));
                }
                if (rowCheck)
                    return true;
            }
            
            return false;
        }

        private bool CheckForRows(char player, char[][] board)
        {
            bool result = false;
            for (int i = 0; i < 4; i++)
            {
                result = result || PlayerWonInRow(player, board[i]);
            }
            
            return result;
        }

        private bool PlayerWonInRow(char player, char[] row)
        {
            bool won = true;
            for (int i = 0; i < 4; i++)
            {
                won = won && (row[i].Equals(player) || row[i].Equals('T'));
            }
            return won;
        }

        private bool HasEmptyCellInBoard(char[][] board)
        {
            bool empty = true;
            for (int i = 0; i < 4; i++)
            {
                empty = empty && HasEmptyCellInRow(board[i]);
            }
            return empty;
        }

        private bool HasEmptyCellInRow(char[] row)
        {
            for (int i = 0; i < 4; i++)
            {
                if (row[i].Equals('.'))
                    return true;
            }
            return false;
        }
    }
}
