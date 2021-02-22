using ScoreGetter.OsuTools;
using System;
using System.Diagnostics;
using System.Threading;

namespace ScoreGetter
{
    class Program
    {
        public static int m_last_300 = 0;
        public static int m_last_100 = 0;
        public static int m_last_50 = 0;
        public static int m_last_miss = 0;

        public static int c300 = 0;
        public static int c100 = 0;
        public static int c50 = 0;
        public static int cmiss = 0;
        public static String sortie = "0";
        public static Process osu = GetId.FindOsuProcess();

        public static bool send = false;
        public static bool change = false;

        public static void getScore()
        {
            Finder finder = new Finder(osu);
            finder.TryInit();

            c300 = finder.Get300Count();
            c100 = finder.Get100Count();
            c50 = finder.Get50Count();
            cmiss = finder.GetMissCount();

            m_last_300 = c300;
            m_last_100 = c100;
            m_last_50 = c50;
            m_last_miss = cmiss;
            while (true)
            {


                if (c300 != m_last_300 && c300!=0 && !(m_last_300==0 && c300!=1) && !(c300!=1 && c300!=m_last_300+1))
                {
                    sortie="300";
                    m_last_300 = c300;
                    change = true;
                }

                if (c100 != m_last_100 && c100 != 0 && !(m_last_100 == 0 && c100 != 1))
                {
                    sortie="100";
                    m_last_100 = c100;
                    change = true;
                }


                if (c50 != m_last_50 && c50 != 0 && !(m_last_50 == 0 && c50 != 1))
                {
                    sortie="50";
                    m_last_50 = c50;
                    change = true;
                }

                if (cmiss != m_last_miss && cmiss != 0 && !(m_last_miss == 0 && cmiss != 1))
                {
                    sortie="0";
                    m_last_miss = cmiss;
                    change = true;
                }

                c300 = finder.Get300Count();
                c100 = finder.Get100Count();
                c50 = finder.Get50Count();
                cmiss = finder.GetMissCount();
                if (change)
                {
                    Console.WriteLine(sortie);
                    change = false;
                    send = false;
                }
            }
        }

        static void Main(string[] args)
        {
            //Attente ouverture OSU!
            while (osu == null)
            {
                Console.Out.Write("NULL\n");
                Thread.Sleep(5000);
                osu = GetId.FindOsuProcess();
            }

            Console.WriteLine("Trouvé");
            //OSU! ouvert

            Thread t = new Thread(new ThreadStart(getScore));
            t.Start();
            SocketManager.StartListening();
        }
    }
}
