//From google code jam: https://code.google.com/codejam/contest/2270488/dashboard#s=p1
class Lawnmower
{
    public void Answer(TextReader input)
    {
        string line = input.ReadLine();
        int nOfCases = Convert.ToInt32(line);
        for (int caseNo = 1; caseNo <= nOfCases; caseNo++)
        {
            //Size
            line = input.ReadLine();
            int rows = Convert.ToInt32(line.Split(' ')[0]);
            int cols = Convert.ToInt32(line.Split(' ')[1]);
            //Init pattern
            int[][] pattern = new int[rows][];
            for (int i = 0; i < rows; i++)
            {
                pattern[i] = new int[cols];
            }
 
            //Read pattern
            for (int row = 0; row < rows; row++)
            {
                line = input.ReadLine();
                var values = line.Split(' ');
                for(int col = 0; col < cols; col++)
                    pattern[row][col] = Convert.ToInt32(values[col]);
            }
 
            string result = "YES";
            for (int row = 0; row < rows; row++)
            {
                for (int col = 0; col < cols; col++)
                    {
                        if (RowHasGreaterThan(pattern[row][col],row,pattern)
                            && ColHasGreaterThan(pattern[row][col], col, pattern))
                            result = "NO";   
                    }
            }
            Console.Out.WriteLine("Case #{0}: {1}", caseNo, result);
        }
    }
 
    private bool ColHasGreaterThan(int value, int col, int[][] pattern)
    {
        for (int i = 0; i < pattern.Length; i++)
            if (pattern[i][col] > value)
                return true;
        return false;
    }
 
    private bool RowHasGreaterThan(int value, int row, int[][] pattern)
    {
        for (int j = 0; j < pattern[row].Length; j++)
            if (pattern[row][j] > value)
                return true;
        return false;
    }
}