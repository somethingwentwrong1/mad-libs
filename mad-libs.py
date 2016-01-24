# Type a subject
print "What is your name?",
subj = raw_input("> ")
# Type a verb
print "What are you doing now?",
verb = raw_input("> ")
# Type a location
print "Where are you now?",
location = raw_input("> ")
# Type an adjective
print "How do you look now?"
adj = raw_input("> ")
# Insert everything in order
print "One day, there was a monster named %r." % (subj)
print "%r was %r and scary." % (subj, adj)
print "When %r %r appears, the girls ran away because %r %r was %r in %r." % (
    adj, subj, adj, subj, verb, location)
