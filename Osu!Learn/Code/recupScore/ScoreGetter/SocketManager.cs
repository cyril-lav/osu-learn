using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace ScoreGetter.OsuTools
{
    class SocketManager
    {
        // Incoming data from the client.  
        public static string dataret = null;
        public static string data = null;

        public static void StartListening()
        {
            byte[] buffer = new Byte[1024];
            
            IPEndPoint localEndPoint = new IPEndPoint(IPAddress.Parse("127.0.0.1"), int.Parse("12345"));
            Socket listener = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

            try
            {
                listener.Bind(localEndPoint);
                listener.Listen(10);

                while (true)
                {
                    Socket socket = listener.Accept();
                    data = null;
                    dataret = null;
                    int bytesRec = socket.Receive(buffer);

                    data += Encoding.ASCII.GetString(buffer, 0, bytesRec);
                    //Console.WriteLine("Text received : {0}", data);

                    byte[] msg = new Byte[1024];
                    if (!Program.send)
                    {
                        msg = Encoding.ASCII.GetBytes(Program.sortie);
                        socket.Send(msg);
                        Program.send = true;
                    }
                    
                    socket.Shutdown(SocketShutdown.Both);
                    socket.Close();
                }

            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }

            Console.WriteLine("\nPress ENTER to continue...");
            Console.Read();
        }
    }
}
