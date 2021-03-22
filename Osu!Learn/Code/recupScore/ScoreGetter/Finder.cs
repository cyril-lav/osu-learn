using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace ScoreGetter
{
    class Finder : Reader
    {
        //0xA1,0,0,0,0,0x8D,0x56,0x0C,0xE8,0x00,0x00,0x00,0x00,0x8B,0x47,0x04
        private static readonly string s_acc_pattern = "\xA1\x0\x0\x0\x0\x8D\x56\x0C\xE8\x00\x00\x00\x00\x8B\x47\x04";
        private static readonly string s_acc_mask = "x????xxxx????xxx";

        //0x73,0x7a,0x8b,0x0d,0x0,0x0,0x0,0x0,0x85,0xc9,0x74,0x1f
        private static readonly string s_acc_pattern_fallback = "\x73\x7a\x8b\x0d\x0\x0\x0\x0\x85\xc9\x74\x1f\x8d\x55\xf0";
        private static readonly string s_acc_mask_fallback = "xxxx????xxxxxxx";

        //0x5e,0x5f,0x5d,0xc3,0xa1,0x0,0x0,0x0,0x0,0x89,0x0,0x04
        private static readonly string s_time_pattern = "\x5e\x5f\x5d\xc3\xa1\x0\x0\x0\x0\x89\x0\x04";
        private static readonly string s_time_mask = "xxxxx????x?x";


        private IntPtr m_acc_address;//acc,combo,hp,mods,300hit,100hit,50hit,miss Base Address

        
        public Finder(Process osu) : base(osu)
        {
        }

        public bool TryInit()
        {
            bool m_accuracy_address_success = false;

            SigScan.Reload();
            {

                //Find acc Address
                m_acc_address = SigScan.FindPattern(StringToByte(s_acc_pattern), s_acc_mask, 1);
                Console.WriteLine($"Playing Accuracy Base Address (0):0x{(int)m_acc_address:X8}");

                m_accuracy_address_success = TryReadIntPtrFromMemory(m_acc_address, out m_acc_address);
                Console.WriteLine($"Playing Accuracy Base Address (1):0x{(int)m_acc_address:X8}");

                if (!m_accuracy_address_success)//use s_acc_pattern_fallback
                {
                    Console.WriteLine("Use Fallback Accuracy Pattern");
                    m_acc_address = SigScan.FindPattern(StringToByte(s_acc_pattern_fallback), s_acc_mask_fallback, 4);
                    Console.WriteLine($"Playing Accuracy Base Address (0):0x{(int)m_acc_address:X8}");

                    m_accuracy_address_success = TryReadIntPtrFromMemory(m_acc_address, out m_acc_address);
                    Console.WriteLine($"Playing Accuracy Base Address (1):0x{(int)m_acc_address:X8}");
                }
            }
            return m_accuracy_address_success;
        }

        private IntPtr RulesetBaseAddress
        {
            get
            {
                TryReadIntPtrFromMemory(m_acc_address, out var tmp_ptr);
                return tmp_ptr;
            }
        }

        private IntPtr ScoreBaseAddress
        {
            get
            {
                TryReadIntPtrFromMemory(RulesetBaseAddress + 0x38, out var tmp_ptr);
                return tmp_ptr;
            }
        }

        public int GetMissCount()
        {
            TryReadShortFromMemory(ScoreBaseAddress + 0x92, out var value);
            return value;
        }

        public int Get300Count()
        {
            TryReadShortFromMemory(ScoreBaseAddress + 0x8a, out ushort value);
            return value;
        }

        public int Get100Count()
        {
            TryReadShortFromMemory(ScoreBaseAddress + 0x88, out var value);
            return value;
        }

        public int Get50Count()
        {
            TryReadShortFromMemory(ScoreBaseAddress + 0x8c, out var value);
            return value;
        }
        public int GetGekiCount()
        {
            TryReadShortFromMemory(ScoreBaseAddress + 0x8e, out var value);
            return value;
        }
        public int GetKatuCount()
        {
            TryReadShortFromMemory(ScoreBaseAddress + 0x90, out var value);
            return value;
        }
    }
}
