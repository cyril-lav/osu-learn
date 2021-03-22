using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

namespace ScoreGetter
{
    class GetId
    {
        private readonly int m_osu_id = 0;
        private static Process m_osu_process;
        public static Process FindOsuProcess()
        {
                Process[] process_list;

                process_list = Process.GetProcesses();
                        foreach (var p in process_list)
                        {
                            if (p.ProcessName =="osu!")
                            {
                                m_osu_process = p;
                                break;
                            }
                    }
            return m_osu_process;
        }
    }
}
