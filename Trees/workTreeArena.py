from workTree import WorkTree

CEO = WorkTree("CEO","mehta")

CFO = WorkTree("CFO","sharma")
CHO = WorkTree("CHO","lakkad")
CTO = WorkTree("CTO","talpade")

CEO.add_child(CFO)
CEO.add_child(CHO)
CEO.add_child(CTO)

CFO.add_child(WorkTree("ACF1","aaa1"))
CFO.add_child(WorkTree("ACF2","aaa2"))
CFO.add_child(WorkTree("ACF2","aaa2"))

CHO.add_child(WorkTree("ACH1","bb1"))
CHO.add_child(WorkTree("ACH2","bb2"))


CTO.add_child(WorkTree("ACTO1","cc1"))


CEO.print_tree(only_name=True)
