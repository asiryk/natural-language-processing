CONLLU_SENTENCE = """\
# sent_id = 2hkl
# text = Значно більше я відтворюю побачене й почуте, є своєрідним композитором того, що втілиться як мистецький твір.
# translit = Značno biľše ja vidtvoŕuju pobačene j počute, ě svoěridnym kompozytorom toho, ščo vtilyťśа jak mystećkyj tvir.
1	Значно	значно	ADV	Rp	Degree=Pos	2	advmod	2:advmod	Id=2hkm|LTranslit=značno|Translit=Značno
2	більше	більше	ADV	Rc	Degree=Cmp	4	advmod	4:advmod	Id=2hkn|LTranslit=biľše|Translit=biľše
3	я	я	PRON	Pp-1-ysnn	Animacy=Anim|Case=Nom|Number=Sing|Person=1|PronType=Prs	4	nsubj	4:nsubj|11:nsubj	Id=2hko|LTranslit=ja|Translit=ja
4	відтворюю	відтворювати	VERB	Vmpip1s	Aspect=Imp|Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	0:root	Id=2hkp|LTranslit=vidtvoŕuvaty|Translit=vidtvoŕuju
5	побачене	побачене	NOUN	Ap-nsas-	Animacy=Inan|Case=Acc|Gender=Neut|Number=Sing	4	obj	4:obj	Id=2hkq|LTranslit=pobačene|Translit=pobačene
6	й	й	CCONJ	Ccs	_	7	cc	7:cc	Id=2hkr|LTranslit=j|Translit=j
7	почуте	почуте	NOUN	Ap-nsas-	Animacy=Inan|Case=Acc|Gender=Neut|Number=Sing	5	conj	4:obj|5:conj	Id=2hks|LTranslit=počute|SpaceAfter=No|Translit=počute
8	,	,	PUNCT	U	_	11	punct	11:punct	Id=2hkt|LTranslit=,|Translit=,
9	є	бути	AUX	Vapip1s	Aspect=Imp|Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	11	cop	11:cop	Id=2hku|LTranslit=buty|Translit=ě
10	своєрідним	своєрідний	ADJ	Afpmsif	Case=Ins|Degree=Pos|Gender=Masc|Number=Sing	11	amod	11:amod	Id=2hkv|LTranslit=svoěridnyj|Translit=svoěridnym
11	композитором	композитор	NOUN	Ncmsiy	Animacy=Anim|Case=Ins|Gender=Masc|Number=Sing	4	conj	0:root|4:conj	Id=2hkw|LTranslit=kompozytor|Translit=kompozytorom
12	того	те	PRON	Pd--nnsgn	Animacy=Inan|Case=Gen|Gender=Neut|Number=Sing|PronType=Dem	11	nmod	11:nmod|15:nsubj:rel	Id=2hkx|LTranslit=te|SpaceAfter=No|Translit=toho
13	,	,	PUNCT	U	_	15	punct	15:punct	Id=2hky|LTranslit=,|Translit=,
14	що	що	SCONJ	Css	_	15	mark	15:mark|18:nsubj:sp	Id=2hkz|LTranslit=ščo|Translit=ščo
15	втілиться	втілитися	VERB	Vmeif3s	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin	12	acl:relcl	12:acl:relcl	Id=2hl0|LTranslit=vtilytyśа|Translit=vtilyťśа
16	як	як	SCONJ	Css	_	18	mark	18:mark	Id=2hl1|LTranslit=jak|Translit=jak
17	мистецький	мистецький	ADJ	Ao-msnf	Case=Nom|Gender=Masc|Number=Sing	18	amod	18:amod	Id=2hl2|LTranslit=mystećkyj|Translit=mystećkyj
18	твір	твір	NOUN	Ncmsnn	Animacy=Inan|Case=Nom|Gender=Masc|Number=Sing	15	xcomp:sp	15:xcomp:sp	Id=2hl3|LTranslit=tvir|SpaceAfter=No|Translit=tvir
19	.	.	PUNCT	U	_	4	punct	4:punct	Id=2hl4|LTranslit=.|Translit=.
"""
