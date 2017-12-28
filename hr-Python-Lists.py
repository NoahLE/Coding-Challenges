# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    # The number of commands to be submitted
    N = int(input())

    # Get other commands
    commands = []
    for command in range(N):
        commands.append(input())

    # The array which will be manipulated by the commands
    the_list = []

    # N = 12
    # commands = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'print ', 'remove 6', 'append 9', 'append 1', 'sort ',
    #             'print', 'pop', 'reverse', 'print']

    for command in commands:
        # Break the command into pieces
        full_command = command.split(sep=' ')

        # insert <location> <value>
        if full_command[0] == 'insert':
            the_list.insert(int(full_command[1]), int(full_command[2]))

        # print the array
        elif full_command[0] == 'print':
            print(the_list)

        # remove the first occurence of <value>
        elif full_command[0] == 'remove':
            the_list.remove(int(full_command[1]))

        # append <value> to the end of the list
        elif full_command[0] == 'append':
            the_list.append(int(full_command[1]))

        # sort the list
        elif full_command[0] == 'sort':
            the_list.sort()

        # pop the last element from the list
        elif full_command[0] == 'pop':
            the_list.pop()

        # reverse the list
        elif full_command[0] == 'reverse':
            the_list.reverse()

        else:
            pass
