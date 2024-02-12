<h1 align="center">Cyberpunk 2077 Breach Protocol Brute Force Solver</h1>

#### Ellijah Darrellshane Suryanegara
#### 13522097

Cyberpunk 2077 Breach Protocol Brute Force Solver is a program that solve Breach Protocol minigames in Cyberpunk 2077 by giving the most optimal solution available. This program uses a brute-force approach, meaning it finds all the possible solutions firsthand then searches for the solution which outputs the highest points. <br />
<br />
Components of this game include:
1. Token - consisting of two alphanumeric characters such as E9, BD, and 55.
2. Matrix - consisting of tokens that will be selected to form a code sequence.
3. Sequence - a series of tokens (two or more) that must be matched.
4. Buffer - the maximum number of tokens that can be arranged sequentially.
<br />

The rules of the Breach Protocol game include:
1. Players move in a pattern of horizontal, vertical, horizontal, vertical (alternating) until all sequences are successfully matched or the buffer is full.
2. Players start by selecting one token at the top row position of the matrix.
3. Sequences are matched to the tokens in the buffer.
4. A token in the buffer can be used in more than one sequence.
5. Each sequence has a varying reward or prize weight.
6. Sequences have a minimum length of two tokens. <br />

<br />To run this program, you would need Python installed on your device. If you haven't installed Python, you can easily install it on
<https://www.python.org/downloads/>

<br />
Once you've run the program, you would be given 2 input options. <br />
The first option is to input via a .txt file. The .txt file should be within the **test** directory. The content of the aforementioned .txt file should follow the following format:
<br />

```git
buffer_size
matrix_width matrix_height
matrix
number_of_sequences
sequences_1
sequences_1_reward
sequences_2
sequences_2_reward
…
sequences_n
sequences_n_reward
```

Example:
```git
7
6 6
7A 55 E9 E9 1C 55
55 7A 1C 7A E9 55
55 1C 1C 55 E9 BD
BD 1C 7A 1C 55 BD
BD 55 BD 7A 1C 1C
1C 55 55 7A 55 7A
3
BD E9 1C
15
BD 7A BD
20
BD 1C BD 55
30
```

The second option is to input via Command Line Interface (CLI). With this option, the matrix and sequence are randomly generated with the constraints given by the user. The user has to input the number_of_unique_tokens, tokens, buffer_size, number_of_sequences, and max_sequence_size. <br />
Example:
```git
Number of unique tokens: 5
Token 1: A1
Token 2: B2
Token 3: C3
Token 4: D4
Token 5: E5
Buffer size: 3
Number of matrix rows: 6
Number of matrix columns: 6
Number of sequences: 3
Maximum size of sequence: 3
```

<br />
Once you've finished, the program will output the optimal solution and execution time with the following format:

```git
max_reward
buffer_content
buffer_coordinate_1
buffer_coordinate_2
…
buffer_coordinate_n

execution_time_ms
```

Example:

```git
50
7A BD 7A BD 1C BD 55
1, 1
1, 4
3, 4
3, 5
6, 5
6, 4
5, 4

300 ms
```

Finally, the program would give a prompt for the user to decide whether to save the solution or not. If the user chooses to save, the solution would be stored in a .txt file in the **test** directory. The content of the .txt file would follow the same format as the output on the CLI.
