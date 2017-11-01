# Project Wallflower
Project Wallflower is a chat software that encrypts communications
using a one time pad, which is provably secure, and unbreakable.
This software will remain secure as long as the crpyto.pad file is
kept safe. ONLY TRANSFER THE CRYPTO.PAD FILE OFFLINE, AND TO PEOPLE
YOU WANT TO CHAT WITH.

This software includes a cryptographically secure random number
generator for creating a one-time pad.

To run simply get a copy of crypto_random.py, PadGen.py, and Wallflower_Client.py; run
the PadGen.py program in a Linux terminal and distribute the generated file to
everyone you want to chat with. Then chat by running the Wallflower_Client.py
software in the same directory as the crypto.pad file generated using PadGen.py.

You will need to change the IP address in the client to match your server address.

You will be dropped into a room unique to your one-time pad.

# PLEASE NOTE
This was written when I was is high school. I would make a ton of changes if I was working on this now (I may fix it soon).
For one, I would create a server that pushes updates to clients instead of clients pulling updates. I would also use a
combination of a ont-time pad and a bitwise XOR cipher as this would allow any type of data to be passed through, rather than
just text. This system is secure, it just has a not-so-good design in terms of server software, and data encoding.
