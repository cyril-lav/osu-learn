using System;
using System.Collections.Generic;

namespace ScoreGetter
{
    [Flags]
    public enum ProvideDataMask : uint
    {
        Count300 = 1u << 3,
        Count100 = 1u << 4,
        Count50 = 1u << 5,
        CountMiss = 1u << 6,
        CountGeki = 1u << 7,
        CountKatu = 1u << 8,
    }

    public class ProvideData
    {

        public int Count300;
        public int Count100;
        public int Count50;
        public int CountMiss;
        public int CountGeki;
        public int CountKatu;

    }
}