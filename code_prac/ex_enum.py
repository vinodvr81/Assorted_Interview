import enum
class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1
print('\nMember name: {}'.format(BugStatus.wont_fix.name))
print('Member value: {}'.format(BugStatus.wont_fix.value))

print("*"*19)

for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))

#################################################################################

@enum.unique
class BugStatusNew(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1
    # This will trigger an error with unique applied.
    by_design = 4
    closed = 1

print("*"*19)

for status in BugStatusNew:
    print('{:15} = {}'.format(status.name, status.value))