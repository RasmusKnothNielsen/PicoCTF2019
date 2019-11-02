# Where is the file
###Q) I've used a super secret mind trick to hide this file. Maybe something lies in /problems/where-is-the-file_2_f1aa319cafd4b55ee4a60c1ba65255e2.

###A) picoCTF{w3ll_that_d1dnt_w0RK_30444bc6}

##Commentary:
Navigate to the specific folder:
```
cd /problems/where-is-the-file_2_f1aa319cafd4b55ee4a60c1ba65255e2
```
When we do a ls here, there is nothing, and since the assignment talked about hidden files, lets try to use the show hidden files flag:

```
ls -a
```

This reveals the file .cant_see_me, so now we can read the content of said file
```
cat .cant_see_me
```