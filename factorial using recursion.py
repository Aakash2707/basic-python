with open("in.txt", 'w') as f:
        text=input('Enter text:')
        f.write(text)
        f.close()
        with open("in.txt") as f:
                with open("out.txt", 'w') as f1:
                        for line in f:
                                if 'p' in line or 'P' in line:
                                        f1.write(line)

