using System;

namespace _03.StreamOfLetters
{
    class Program
    {
        static void Main(string[] args)
        {
/*Поток от букви
Напишете програма, която прочита скрито съобщение в поредица от символи. Те се получават по един на ред до получаване на командата "End". Думите се образуват от буквите в реда на четенето им. Символите, които не са латински букви трябва да бъдат игнорирани. Думите скрити в потока са разделени от тайна команда от три букви – "c", "o" и "n". При първото получаване на една от тези букви, тя се маркира като срещната, но не се запазва в думата. При всяко следващо нейно срещане се записва нормално в думата. След като са налични и трите символа от командата, се печата думата и интервал " ". Започва се нова дума, която по същия начин чака тайната команда, за да бъде отпечатана.
Вход
От конзолата се чете поредица от редове с един символ на всеки до получаване на командата "End".
Изход
На конзолата се печата на един ред всяка дума след тайната команда, следвана от интервал.
*/
            string word = "";
            int cCount = 0;
            int oCount = 0;
            int nCount = 0;
            int secretWordCount = 0;
            bool isFirstSecretLetter = false;

            string command = Console.ReadLine();

            while (command != "End")
            {
                char letter = char.Parse(command);

                if ((letter > 'a' && letter < 'z') || (letter > 'A' && letter < 'Z'))
                {
                    if (letter == 'c' && cCount < 1)
                    {
                        cCount++;
                        secretWordCount++;
                        isFirstSecretLetter = true;
                    }
                    else if (letter == 'o' && oCount < 1)
                    {
                        oCount++;
                        secretWordCount++;
                        isFirstSecretLetter = true;
                    }
                    else if (letter == 'n' && nCount < 1)
                    {
                        nCount++;
                        secretWordCount++;
                        isFirstSecretLetter = true;
                    }
                    if (secretWordCount == 3)
                    {
                        Console.Write($"{word} ");
                        secretWordCount = 0;
                        cCount = 0;
                        oCount = 0;
                        nCount = 0;
                        word = "";
                    }
                    else if (isFirstSecretLetter == false)
                    {
                        word += letter;
                    }
                    isFirstSecretLetter = false;
                }
                command = Console.ReadLine();
            }
            if (command == "End" && secretWordCount == 3)
            {
                Console.WriteLine($"{word}");
            }
        }
    }
}