import sys
line1 = str(sys.argv[1]); 
line2 = str(sys.argv[2]);

newline="";
i = 0;
while i<len(line1):
   newline=newline+line1[i]+line2[i];
   i = i + 1;

print newline;
