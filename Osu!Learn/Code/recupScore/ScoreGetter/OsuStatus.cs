using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

namespace ScoreGetter
{
    public enum OsuStatus : UInt64
    {
        NoFoundProcess = 1ul << 0,
        Unkonwn = 1ul << 1,
        SelectSong = 1ul << 2,
        Playing = 1ul << 3,
        Editing = 1ul << 4,
        Rank = 1ul << 5,
        MatchSetup = 1ul << 6,
        Lobby = 1ul << 7,
        Idle = 1ul << 8,
    }
}
