1. Study the following situations. In each of them, which of the main security objectives are probably not fulfilled?
   a. You have selected your favourite red filament for 3D printing in an e-shop, now entering your payment data and receiving an error message: “The transaction could not be completed, your bank is not responding, try later.”
   Answer: Availability

   b. You are sitting at a conference, listening to presentations of other researchers in the area you are keen on. You see one of them explaining your breakthrough ideas you never shared with anyone except that you have submitted them with a recent EU project proposal that happened to be rejected.
   Answer: Confidentiality

   c. Yesterday, you have completed the design of your new 3D model with Tinkercad. When you have logged into Tinkercad today, you found your model to be modified for unknown reasons.
   Answer: Integrity

2. An employee in the bank has been preparing 10 years for this beautiful day. The plan was perfect. Some large sum of money has been forgotten on some unused account—probably of a victim of a mafia war. Now they are safely moved to his private account in Belize. Unfortunately, a day after, the police knock on the door. You know why because you have programmed the information system for this bank. Which property does it have?
   Answer: Accountability

3. System calls are a typical example of a weak point of operating systems. They can be used by an adversary to take control over otherwise protected parts of memory, hardware, or other resources. It can be done, because an adversary program can offer a substitute routine to be called when user programs trap to system calls. Your comments.
   Answer: System calls create a privileged interface that must be strictly validated—any flaw in that boundary risks full compromise.

4. Under Linux, a user sometimes cannot hear anything when playing music with his favorite music player (mplayer program) even though it has speakers connected and volume up. This can happen for instance when that user is not member of the audio user group. We give him this privilege by adding him to that group. Fill in the following generic concepts with entities for this particular situation:
   a. Principal
   Answer: The end user

   b. Agent
   Answer: The OS’s group-management service

   c. Object
   Answer: The audio device resource

   d. Credential
   Answer: Membership in the “audio” group

5. A citizen who was banned from getting certain kind of permission from regulators notices that when the clerk in the office gives this permission to others, they always use certain URL address in this format: [https://permission-server.gov/give\_permission?personal\_id=####\&type\_of\_permission=####](https://permission-server.gov/give_permission?personal_id=####&type_of_permission=####). Therefore he tried to enter this URL to his web browser with his personal\_id, and the type of permission that he would like to have, but does not. Fortunately, it did not work out, because systems obey one of the core security principles? Which one?
   Answer: Complete mediation

6. What is the purpose of salt in hashing passwords process on a typical Linux system?
   Answer: To introduce unique per-user randomness so identical passwords produce distinct hashes and thwart precomputed attacks.

7. Provide 6 meaningful, useful, true and informative sentences about advantages and/or disadvantages of the three authentication methods:
   a) By what you know
   Answer: Passwords are easy to deploy and remember yet highly vulnerable to guessing and reuse across sites.
   Answer: Weak password policies enable brute-force and dictionary attacks if rate-limiting isn’t enforced.

   b) By what you have
   Answer: Tokens or devices greatly strengthen security as a second factor but can be lost, stolen, or require extra provisioning.
   Answer: Hardware tokens resist phishing but introduce logistics and cost for distribution and replacement.

   c) By what you are
   Answer: Biometric traits are unique and convenient but, if compromised, cannot be revoked like a password.
   Answer: Biometric matching risks false positives/negatives and often raises privacy and storage-security concerns.

8. When a user is logging in to a Linux desktop system on a text terminal, it sees the login: prompt first. After the user provides his username and password, the login process that runs with superuser privileges verifies the entered hashed password against a hashed password stored in /etc/shadow file. If they match, it forks a new process, changes the owner of that process to the user that is just logging in and starts a login shell as specified in /etc/passwd file. Your comments.
   Answer: This implements privilege separation—using elevated rights only to verify credentials, then dropping to user privilege to protect sensitive files.

9. Why do we typically start a webserver as some user and not as root?
   Answer: To minimize impact of any compromise by running with only the permissions needed, not full system control.

10. Somebody wanted to enter a hairdresser during pandemic and pulled out her covid-pass so that they let her in. Will her entry permission be based on capabilities or on access control list? Explain why.
    Answer: Capabilities—because the pass itself is a token granting the right, not a system-maintained ACL.

11. What is the relation between SSL and TLS and between HTTPS and SSL?
    Answer: TLS is the successor protocol to SSL with stronger cryptography; HTTPS is HTTP layered over SSL/TLS for secure web traffic.

12. What are the different ways to authenticate when using SSH?
    Answer: Password-based login, public-key authentication, host-based authentication, and GSSAPI/Kerberos methods.

13. A process P on a typical Linux system opens a file F, then reads from it 3 times, and finally closes it. Which of the following was used:
    a. Capabilities
    b. ACL
    Answer: Capabilities

14. Suppose you have a family bakery, and different people are working there: bakers, juniors, cleaning staff and others. Juniors have access to the flour, while bakers can get into the cabinet that contains hereditary recipes. In a corona crisis, some bakers were ill and trusted juniors temporarily received the privileges of the bakers until they could return. How is this access control method called and what basic security principle does this preserve?
    Answer: Role-Based Access Control (RBAC), preserving least privilege.

15. Can a similar access control be achieved somehow in Linux system? Using which technique and how does it work?
    Answer: Yes—via POSIX ACLs or supplementary groups to grant fine-grained, temporary permissions on files or resources.

16. What command on Linux could we use to start a process under a different user?
    Answer: sudo -u <username> <command>

17. You have installed some new program on your mobile phone and it asks you to let it use your microphone. What data structure will hold the decision of your approval?
    Answer: The OS’s permission database or settings store entry.

18. A browser is accessing a webserver that is providing the content in encrypted form to increase security. Why does the server need a certificate?
    Answer: To prove its identity to clients and enable establishment of a trusted encrypted channel.

19. How can that webserver obtain such certificate?
    Answer: By generating a CSR (Certificate Signing Request) and submitting it to a trusted CA for signing, then installing the returned certificate.

20. Suppose an adversary would like to cheat the web browser by recording traffic between the webserver and the browser first and then reusing this recorded communication to modify the content of the following communication. How is such wrongdoing called? What is done to prevent it?
    Answer: A replay attack; prevented using nonces, timestamps, and sequence numbers in TLS.

21. You have files A, B, C and users X, Y, Z, W. You would like to give read and write access to these files to the users as follows (other users should not have it):
    File A: read→ X, Y; write→ X, W
    File B: read→ X, Z; write→ Y, X
    File C: read→ Y, Z; write→ Z, W
    Can this be done in traditional 9-bit POSIX-like access control? If yes, how, if not why?
    Answer: No—POSIX permissions only allow one owner and one group per file, so you can’t express these arbitrary per-user rights.

22. One of the customers of a system you developed has ordered a Christmas tree to be brought right to his door using that system. Now he is refusing to pay for it, claiming he has not placed the order. However, you are 100% sure that he did that and you can provide a proof. It means that your system has the following property: (fill in)
    Answer: Non-repudiation

23. You have opened your program and commented-out lines 10-20 in it. Then you saved it, compiled it, and run it, surprisingly finding out that the program still executes those instructions at lines 10-20. You open the file and you see the lines are NOT commented-out. Which property is the system you are using lacking? (fill in)
    Answer: Integrity

24. A teacher has developed a special program to tacitly subscribe students to his elective course that nobody wanted to register for. Somehow he managed to start and keep that program running on a student computer, waiting until the student will have logged in to AIS. After that his program would just issue a few needed requests to AIS and the student would be silently registered. If this was possible, which core security principle was not obeyed by such AIS?
    Answer: Authorization

25. Under Linux, when you are trying to send a program to Arduino over serial cable, you run into a difficulty—you are missing the rights to file /dev/ttyUSB0 or similar. When we give a user this right, fill in the following generic concepts with entities in this situation:
    a. Principal
    Answer: The user

b. Agent
Answer: The udev/group-assignment mechanism

c. Object
Answer: The /dev/ttyUSB0 device node

d. Credential
Answer: Group-membership or file-mode permission

26. Why does an experienced attacker who has stolen password file from a machine you use, and who wants to guess your password has an easier job if the “salt” is not used?
    Answer: Because they can mount rainbow-table or dictionary attacks against all hashes at once without per-user randomness.

27. When a user is logging in to a Linux desktop system on a text terminal, it sees the login: prompt first. After the user provides his username and password, the login process changes its own user to the provided one so that it can read and verify the hashed password from a file, which is stored in an area that is readable only to that user. Your comments.
    Answer: This privilege switch isolates access to /etc/shadow, enforcing least-privilege and protecting secret data.

28. What is the main advantage and main disadvantage of using capabilities instead of ACL?
    Answer:
    Advantage: They grant fine-grained, per-process rights without global permission bits.
    Disadvantage: They add complexity in design, management, and reasoning about security state.

29. Capabilities allow both mandatory and discretionary access control, whereas ACL allow only mandatory. True?
    Answer: False

30. Suppose you have a family bakery, and different people are working there: bakers, juniors, cleaning staff and others. Juniors have access to the flour, while bakers can get into the cabinet that contains hereditary recipes. In a corona crisis, some bakers were ill and trusted juniors temporarily received the privileges of the bakers until they could return. How is this access control method called and what basic security principle does it preserve?
    Answer: Role-Based Access Control (RBAC), preserving least privilege.

