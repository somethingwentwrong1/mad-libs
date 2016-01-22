#Type a subject
print "What is your name?",
subj = raw_input("> ")
#Type a verb
print "What are you doing now?",
verb = raw_input("> ")
#Type a location
print "Where are you now?",
location = raw_input("> ")
#Type an adjective
print "How do you look now? (With Capitalization)"
adj = raw_input("> ")
#Insert everything in order
print "%r %r is %r in %r." % (
    adj, subj, verb, location)
