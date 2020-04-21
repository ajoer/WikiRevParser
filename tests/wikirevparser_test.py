import json
import unittest
from collections import Counter, OrderedDict
from wikirevparser import wikirevparser

mock_data_raw = {'user': 'Nordfra', 'timestamp': '2019-12-20T10:59:29Z', 'slots': {'main': {'contentmodel': 'wikitext', 'contentformat': 'text/x-wiki', '*': '[[Fil:BayeuxTapestryScene38.jpg|thumb|700px|Drageskibe på [[Bayeux-tapetet|Bayeuxtæppet]].]]\n[[Fil:Bergens Byvåpen 1299.jpg|thumb|[[Bergen]]s [[byvåben]] viser et drageskib, dvs. et skib med [[Drage (fabeldyr)|dragehoved]] i stavnen.]]\n\'\'\'Langskibe\'\'\' fra [[vikingetiden]] var meget hurtige og solide. Fra [[Danmark]] kendes [[Ladbyskibet]].\n\nFor at regnes som langskib, må længden være mindst 15 meter.<ref>Frode Sætran og May S. Rogne: "Otte andre skbisgrave", \'\'[[Aftenposten]]\'\' 26. marts 2019</ref> Langskibene var bygget, så de kunne sejle næsten helt ind til kysten. De var smalle, og dermed svære at manøvrere, men til gengæld hurtige. De havde [[mast]] og [[sejl]], samt huller hele vejen langs skibets [[ræling]] til de mange årer.\n\nDe norske langskibe kunne være 30-50 meter lange og havde en besætning på op til 60 mand. De danske eksemplarer var 17 og 28 meter lange, formodentlig med en besætning på henholdsvis 30 og 50 mand.\nDer er lavet mange [[rekonstruktion]]er af langskibe, som sejler med op til 20 kilometer i timen. \n\nTre af de mest kendte norske langskibe er udstillet på [[Bygdøy]] i [[Oslo]]: [[Osebergskibet]], [[Gokstadskibet]] og [[Tuneskibet]].\n \nDertil er der fundet fem andre norske langskibe, som var mindre godt bevaret: [[Myklebustskibet]], Borreskibet,<ref>https://snl.no/Borrehaugene</ref> Storhaugskibet,<ref>https://snl.no/Storhaugskipet</ref> Grønhaugskibet<ref>https://snl.no/Grønhaugskipet</ref> og Jellestadskibet.<ref>https://forskning.no/kronikk-arkeologi-historie/dette-haper-vi-jellestadskipet-kan-fortelle-oss-om-vikingtiden/1250872</ref>\n\n== Drageskibe ==\n[[Fil:Moragsoorm.jpg|thumb|Fuldskala polsk langskib.]]\n\'\'\'Drageskibe\'\'\' var langskibe med et udskåret [[Drage (fabeldyr)|dragehoved]] i [[stævn]]en<ref>https://www.naob.no/ordbok/drageskip</ref> for at markere [[status]]en til den [[konge]] eller [[høvding]], skibet tilhørte. De fleste langskibe var ikke udstyret med dragehoved.<ref>http://www.vikingskip.com/vikingskipstyper.htm</ref>\n\nOgså andre dyrehoveder kendes. [[Olav Haraldsson]]s skib [[Visund]]en fik sit navn fra det forgyldte "visundhoved" (dvs. [[bison]]hoved) i stævnen.<ref>https://www.nrk.no/sorlandet/oppdaget-hellig-olavs-langskip-1.7428766</ref> \n\nI \'\'[[Olav Tryggvasons saga]]\'\' omtales [[Ormen Lange]] som "\'\'en drage, gjort efter mønster af Ormen, som kongen havde med fra [[Hålogaland]]; men skibet var meget større og i alle dele gjort med mere omhu. Dette kaldte han Ormen Lange, men det andet blev hedende Ormen Skamme.\'\'"<ref>https://heimskringla.no/wiki/Olav_Tryggvessons_saga (kap. 88)</ref> \n\nI \'\'[[Håkon Håkonsson]]s saga\'\' omtales, at kongens skib \'\'hed\'\' Dragen. Det beskrives som udstyret med forgyldte hoveder og 25 rorbænke.<ref>https://heimskringla.no/wiki/Hakon_Hakonsøns_den_Gamles_Saga_(C.C.Rafn) (kap. 249)</ref>\n\nPå [[Bayeux-tapetet|Bayeuxtæppet]] skildres [[slaget ved Hastings]] med drageskibe i [[1066]].<ref>https://www.bbc.co.uk/blogs/ahistoryoftheworld/2010/08/the-bayeux-tapestry.shtml</ref>\n\n== Noter ==\n{{Reflist|2}}\n\n{{Krigsskibe}}\n{{Commonskat|Viking ships}}\n\n[[Kategori:Vikingeskibe]]\n[[Kategori:Skibstyper]]\n\n[[fr:Drakkar]]\n[[nl:Longschip]]'}}, 'comment': 'Drageskibe på Bayeuxtæppet.'}
mock_data_parsed = {'captions': ['Bergens byvåben viser et drageskib , dvs . et skib med dragehoved i stavnen .', 'Fuldskala polsk langskib .'], 'categories': ['Vikingeskibe', 'Skibstyper'], 'content': "Langskibe fra vikingetiden var meget hurtige og solide . Fra Danmark kendes Ladbyskibet . For at regnes som langskib , må længden være mindst 15 meter . Langskibene var bygget , så de kunne sejle næsten helt ind til kysten . De var smalle , og dermed svære at manøvrere , men til gengæld hurtige . De havde mast og sejl , samt huller hele vejen langs skibets ræling til de mange årer . De norske langskibe kunne være 30-50 meter lange og havde en besætning på op til 60 mand . De danske eksemplarer var 17 og 28 meter lange , formodentlig med en besætning på henholdsvis 30 og 50 mand . Der er lavet mange rekonstruktioner af langskibe , som sejler med op til 20 kilometer i timen . . Tre af de mest kendte norske langskibe er udstillet på Bygdøy i Oslo : Osebergskibet , Gokstadskibet og Tuneskibet . . Dertil er der fundet fem andre norske langskibe , som var mindre godt bevaret : Myklebustskibet , Borreskibet , Storhaugskibet , Grønhaugskibet og Jellestadskibet . Drageskibe var langskibe med et udskåret dragehoved i stævnen for at markere statusen til den konge eller høvding , skibet tilhørte . De fleste langskibe var ikke udstyret med dragehoved . Også andre dyrehoveder kendes . Olav Haraldssons skib Visunden fik sit navn fra det forgyldte `` visundhoved '' ( dvs . bisonhoved ) i stævnen . . I Olav Tryggvasons saga omtales Ormen Lange som `` en drage , gjort efter mønster af Ormen , som kongen havde med fra Hålogaland ; men skibet var meget større og i alle dele gjort med mere omhu . Dette kaldte han Ormen Lange , men det andet blev hedende Ormen Skamme . '' . I Håkon Håkonssons saga omtales , at kongens skib hed Dragen . Det beskrives som udstyret med forgyldte hoveder og 25 rorbænke . På Bayeuxtæppet skildres slaget ved Hastings med drageskibe i 1066 .", 'images': ['https://commons.wikimedia.org/wiki/File:BayeuxTapestryScene38.jpg', 'https://commons.wikimedia.org/wiki/File:Bergens_Byvåpen_1299.jpg', 'https://commons.wikimedia.org/wiki/File:Moragsoorm.jpg'], 'links': ['vikingetiden', 'danmark', 'ladbyskibet', 'mast', 'sejl', 'ræling', 'rekonstruktion', 'bygdøy', 'oslo', 'osebergskibet', 'gokstadskibet', 'tuneskibet', 'myklebustskibet', 'stævn', 'status', 'konge', 'høvding', 'olav haraldsson', 'visund', 'bison', 'olav tryggvasons saga', 'ormen lange', 'hålogaland', 'håkon håkonsson', 'bayeux-tapetet', 'slaget ved hastings', '1066', 'bergen', 'byvåben', 'drage (fabeldyr)'], 'reference_template_types': Counter({'_nill_': 11}), 'sections': [['Drageskibe', 'Noter'], [], []], 'urls': ['snl.no/Borrehaugene', 'snl.no/Storhaugskipet', 'snl.no/Grønhaugskipet', 'forskning.no/kronikk-arkeologi-historie/dette-haper-vi-jellestadskipet-kan-fortelle-oss-om-vikingtiden/1250872', 'naob.no/ordbok/drageskip', 'vikingskip.com/vikingskipstyper.htm', 'nrk.no/sorlandet/oppdaget-hellig-olavs-langskip-1.7428766', 'heimskringla.no/wiki/Olav_Tryggvessons_saga', 'heimskringla.no/wiki/Hakon_Hakonsøns_den_Gamles_Saga_(C.C.Rafn)', 'bbc.co.uk/blogs/ahistoryoftheworld/2010/08/the-bayeux-tapestry.shtml'], 'user': 'Nordfra'}

class WikiRevParserTest(unittest.TestCase):
    
    def setUp(self):
        self.parser = wikirevparser.ProcessRevisions("da", "Langskib")
        self.parser_fake = wikirevparser.ProcessRevisions("nl", "Jordskælvet i Elazığ 2020")

    def test_wikipedia_page(self):
        da_page = self.parser.wikipedia_page()
        fake_page = self.parser_fake.wikipedia_page()
        
        self.assertTrue(fake_page == None)
        self.assertEqual(self.parser_fake.revisions, {})
        self.assertEqual(self.parser.revisions[0], mock_data_raw)

    def test_get_caption(self):
        # data from https://da.wikipedia.org/wiki/Langskib
        input1 = "[[Fil:Bergens Byvåpen 1299.jpg|thumb|[[Bergen]]s [[byvåben]] viser et drageskib, dvs. et skib med [[Drage (fabeldyr)|dragehoved]] i stavnen.]]"
        target1 = "Bergens byvåben viser et drageskib , dvs . et skib med dragehoved i stavnen ."
        caption1 = self.parser.get_caption(input1)

        input2 = "Bergens byvåben viser et drageskib , dvs . et skib med dragehoved i stavnen ."
        target2 = None
        caption2 = self.parser.get_caption(input2)

        input3 = []
        target3 = None
        caption3 = self.parser.get_caption(input3)
        
        self.assertEqual(caption1, target1)
        self.assertEqual(caption2, target2)
        self.assertEqual(caption3, target3)

    def test_get_links(self):
        # data from https://da.wikipedia.org/wiki/Langskib
        input1 = """'''Drageskibe''' var langskibe med et udskåret [[Drage (fabeldyr)|dragehoved]] i [[stævn]]en<ref>https://www.naob.no/ordbok/drageskip</ref> for at markere [[status]]en til den [[konge]] eller [[høvding]], skibet tilhørte."""
        target1 = ['Drage (fabeldyr)', 'stævn', 'status', 'konge', 'høvding']
        links1, _other_ = self.parser.get_links(input1)
        
        input2 = 3
        target2 = None
        links2, _other_ = self.parser.get_links(input2)

        input3 = []
        target3 = None
        links3, _other_ = self.parser.get_links(input3)

        self.assertEqual(links1, target1)
        self.assertEqual(links2, target2)
        self.assertEqual(links3, target3)

    def test_get_reference_types(self):
        # data from https://da.wikipedia.org/wiki/Langskib
        input1 = ['>https://www.naob.no/ordbok/drageskip', '>http://www.vikingskip.com/vikingskipstyper.htm', '>https://www.nrk.no/sorlandet/oppdaget-hellig-olavs-langskip-1.7428766', '>https://heimskringla.no/wiki/Olav_Tryggvessons_saga (kap. 88)', '>https://heimskringla.no/wiki/Hakon_Hakonsøns_den_Gamles_Saga_(C.C.Rafn) (kap. 249)']
        target1 = Counter({'_nill_': 5})
        types1 = self.parser.get_reference_types(input1)    
        
        input2 = 3
        target2 = None
        types2 = self.parser.get_reference_types(input2)
        
        input3 = []
        target3 = None
        types3 = self.parser.get_reference_types(input3)

        self.assertEqual(types1, target1)
        self.assertEqual(types2, target2)
        self.assertEqual(types3, target3)

    def test_replace_link(self):
        # data from https://da.wikipedia.org/wiki/Langskib
        input1 = "Man har lavet [[rekonstruktion]]er af langskibe."
        target1 = "Man har lavet rekonstruktioner af langskibe."
        sub1 = "rekonstruktion"
        output1 = self.parser.replace_link(input1, sub1, sub1)

        input2 = 3
        target2 = None
        sub2 = "rekonstruktion"
        output2 = self.parser.replace_link(input2, sub2, sub2)
        
        input3 = "Man har lavet [[rekonstruktion]]er af langskibe."
        target3 = "Man har lavet [[rekonstruktion]]er af langskibe."
        sub3 = "vikingerne"
        output3 = self.parser.replace_link(input3, sub3, sub3)
        
        self.assertEqual(output1, target1)
        self.assertEqual(output2, target2)
        self.assertEqual(output3, target3)
            
    def test_get_image_link(self):
        # data from https://nl.wikipedia.org/wiki/Raymond_Poulidor
        input1 = "[[Afbeelding:Poulidor.jpg|thumb|250px|Raymond Poulidor eindelijk in het geel]]"
        target1 = "https://commons.wikimedia.org/wiki/File:Poulidor.jpg"
        output1 = self.parser.get_image_link(input1)

        input2 = "| lijst = [[Image:Jersey gold.svg|20px]]"
        target2 = "https://commons.wikimedia.org/wiki/File:Jersey_gold.svg"
        output2 = self.parser.get_image_link(input2)

        input3 = 3.4
        target3 = None
        output3 = self.parser.get_image_link(input3)

        self.assertEqual(output1, target1)
        self.assertEqual(output2, target2)
        self.assertEqual(output3, target3)
        self.assertNotEqual(output1, target2)

    def test_get_category(self):
        # data from https://da.wikipedia.org/wiki/Langskib
        input1 = "Kategori:skibstyper"
        target1 = "skibstyper"
        output1 = self.parser.get_category(input1)

        input2 = "ru:Драккар"
        target2 = None
        output2 = self.parser.get_category(input2)
        
        input3 = []
        target3 = None
        output3 = self.parser.get_category(input3)
        
        self.assertEqual(output1, target1)
        self.assertEqual(output2, target2)
        self.assertEqual(output3, target3)
        self.assertNotEqual(output1, target2)
        
    def test_proper_formatting(self):
        # data from https://da.wikipedia.org/wiki/Langskib
        input1 = "Fuldskala polsk langskib"
        target1 = "Fuldskala polsk langskib ."
        output1 = self.parser.proper_formatting(input1)

        input2 = [2, 3]
        target2 = None
        output2 = self.parser.proper_formatting(input2)

        input3 = "Langskibe også kaldet drageskibe, skibe fra vikingetiden, var meget hurtige og solide. De var bygget, så de kunne sejle næsten helt ind til kysten, hvilket var en fordel i krig og på plyndringstogter. Skibene var smalle, hvilket gjorde dem lette at manøvrere. Langskibene havde mast og sejl, samt huller hele vejen langs skibets ræling, til de mange årer som også blev taget i brug."
        target3 = "Langskibe også kaldet drageskibe , skibe fra vikingetiden , var meget hurtige og solide . De var bygget , så de kunne sejle næsten helt ind til kysten , hvilket var en fordel i krig og på plyndringstogter . Skibene var smalle , hvilket gjorde dem lette at manøvrere . Langskibene havde mast og sejl , samt huller hele vejen langs skibets ræling , til de mange årer som også blev taget i brug ."
        output3 = self.parser.proper_formatting(input3)

        self.assertEqual(output1, target1)
        self.assertEqual(output2, target2)
        self.assertEqual(output3, target3)
        self.assertNotEqual(output1, target2)

    def test_get_urls(self):
        # data from https://da.wikipedia.org/wiki/Langskib
        input_list = ['>https://www.naob.no/ordbok/drageskip', '>http://www.vikingskip.com/vikingskipstyper.htm', '>https://www.nrk.no/sorlandet/oppdaget-hellig-olavs-langskip-1.7428766', '>https://heimskringla.no/wiki/Olav_Tryggvessons_saga (kap. 88)', '>https://heimskringla.no/wiki/Hakon_Hakonsøns_den_Gamles_Saga_(C.C.Rafn) (kap. 249)', '[[Fil:Moragsoorm.jpg|thumb|Fuldskala', 'polsk', 'langskib.]]', '[[Fil:Bergens', 'Byvåpen', '1299.jpg|thumb|[[Bergen]]s', '[[byvåben]]', 'viser', 'et', 'drageskib,', 'dvs.', 'et', 'skib', 'med', '[[Drage', '(fabeldyr)|dragehoved]]', 'i', 'stavnen.]]', "'''Langskibe'''", 'fra', '[[vikingetiden]]', 'var', 'meget', 'hurtige', 'og', 'solide.', 'Fra', '[[Danmark]]', 'kendes', '[[Ladbyskibet]].', 'For', 'at', 'regnes', 'som', 'langskib,', 'må', 'længden', 'være', 'mindst', '15', 'meter.', 'Langskibene', 'var', 'bygget,', 'så', 'de', 'kunne', 'sejle', 'næsten', 'helt', 'ind', 'til', 'kysten.', 'De', 'var', 'smalle,', 'og', 'dermed', 'svære', 'at', 'manøvrere,', 'men', 'til', 'gengæld', 'hurtige.', 'De', 'havde', '[[mast]]', 'og', '[[sejl]],', 'samt', 'huller', 'hele', 'vejen', 'langs', 'skibets', '[[ræling]]', 'til', 'de', 'mange', 'årer.', 'De', 'norske', 'langskibe', 'kunne', 'være', '30-50', 'meter', 'lange', 'og', 'havde', 'en', 'besætning', 'på', 'op', 'til', '60', 'mand.', 'De', 'danske', 'eksemplarer', 'var', '17', 'og', '28', 'meter', 'lange,', 'formodentlig', 'med', 'en', 'besætning', 'på', 'henholdsvis', '30', 'og', '50', 'mand.', 'Der', 'er', 'lavet', 'mange', '[[rekonstruktion]]er', 'af', 'langskibe,', 'som', 'sejler', 'med', 'op', 'til', '20', 'kilometer', 'i', 'timen.', '==', 'Drageskibe', '==', "'''Drageskibe'''", 'var', 'langskibe', 'med', 'et', 'udskåret', '[[Drage', '(fabeldyr)|dragehoved]]', 'i', '[[stævn]]en', 'for', 'at', 'markere', '[[status]]en', 'til', 'den', '[[konge]]', 'eller', '[[høvding]],', 'skibet', 'tilhørte.', 'De', 'fleste', 'langskibe', 'var', 'ikke', 'udstyret', 'med', 'dragehoved.', 'Også', 'andre', 'dyrehoveder', 'kendes.', '[[Olav', 'Haraldsson]]s', 'skib', '[[Visund]]en', 'fik', 'sit', 'navn', 'fra', 'det', 'forgyldte', '"visundhoved"', '(dvs.', '[[bison]]hoved)', 'i', 'stævnen.', 'I', "''[[Olav", 'Tryggvasons', "saga]]''", 'omtales', '[[Ormen', 'Lange]]', 'som', '"\'\'en', 'drage,', 'gjort', 'efter', 'mønster', 'af', 'Ormen,', 'som', 'kongen', 'havde', 'med', 'fra', '[[Hålogaland]];', 'men', 'skibet', 'var', 'meget', 'større', 'og', 'i', 'alle', 'dele', 'gjort', 'med', 'mere', 'omhu.', 'Dette', 'kaldte', 'han', 'Ormen', 'Lange,', 'men', 'det', 'andet', 'blev', 'hedende', 'Ormen', 'Skamme.\'\'"', 'I', "''[[Håkon", 'Håkonsson]]s', "saga''", 'omtales,', 'at', 'kongens', 'skib', "''hed''", 'Dragen.', 'Det', 'beskrives', 'som', 'udstyret', 'med', 'forgyldte', 'hoveder', 'og', '25', 'rorbænke.', '==', 'Noter', '==', '{{Reflist|2}}', '{{Krigsskibe}}', '{{Commonskat|Viking', 'ships}}', '[[Kategori:Vikingeskibe]]', '[[Kategori:Skibstyper]]', '[[fr:Drakkar]]', '[[nl:Longschip]]']
        target_urls = ['naob.no/ordbok/drageskip', 'vikingskip.com/vikingskipstyper.htm', 'nrk.no/sorlandet/oppdaget-hellig-olavs-langskip-1.7428766', 'heimskringla.no/wiki/Olav_Tryggvessons_saga', 'heimskringla.no/wiki/Hakon_Hakonsøns_den_Gamles_Saga_(C.C.Rafn)']
        urls = self.parser.get_urls(input_list)

        self.assertEqual(urls, target_urls)


    