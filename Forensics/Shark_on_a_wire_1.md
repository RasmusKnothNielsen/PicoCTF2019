# Shark on a wire 1

Q) We found this packet capture. Recover the flag. You can also find the file in /problems/shark-on-wire-1_0_13d709ec13952807e477ba1b5404e620.

A) 

Commentary:

Upen downloading the .pcap file, I open it with Wireshark, to get an estimation of the scope.

There is alot, so we have to use some automated tool to extract the flag.
The following terminal syntax does just that for us:

```
PCAP=capture.pcap; END=$(tshark -r $PCAP -T fields -e udp.stream | sort -n | 
tail -1); for ((i=0;i<=END;i++)); do tshark -r $PCAP -Y "udp.stream eq $i" 
-T fields -e data.text -o data.show_as_text:TRUE 2>/dev/null | tr -d '\n' | 
grep "picoCTF"; if [ $? -eq 0 ]; then echo "(Stream #$i)"; fi; done
```

Here we go through every packet, and prints out the string, if it starts with "picoCTF".
With this, we get the following:

```
picoCTF{StaT31355_636f6e6e}
(Stream #6)
picoCTF{N0t_a_fLag}
(Stream #7)
```

And we try the first flag, which is the correct flag.