# -*- coding: utf-8 -*-

from .context import langsense

import unittest


ENGLISH_TEXT = [
  'The Simpsons is an American animated sitcom created by Matt Groening for the Fox Broadcasting Company',
  'The series is a satirical depiction of working-class life, epitomized by the Simpson family, which consists of Homer, Marge, Bart, Lisa, and Maggie',
  'The show is set in the fictional town of Springfield and parodies American culture and society, television, and the human condition',
  'The family was conceived by Groening shortly before a solicitation for a series of animated shorts with producer James L Brooks',
  'Groening created a dysfunctional family and named the characters after members of his own family, substituting Bart for his own name',
  'The shorts became a part of The Tracey Ullman Show on April 19, 1987',
  'After a three-season run, the sketch was developed into a half-hour prime time show and became an early hit for Fox, becoming the networks first series to land in the Top 30 ratings in a season',
  'Since its debut on December 17, 1989, 631 episodes of The Simpsons have been broadcast',
  'Its 29th season began on October 1, 2017',
  'It is the longest-running American sitcom and the longest-running American animated program, and, in 2009, it surpassed Gunsmoke as the longest-running American scripted primetime television series',
  'The Simpsons Movie, a feature-length film, was released in theaters worldwide on July 27, 2007, and grossed over $527 million',
  'On November 4, 2016, the series was renewed for a twenty-ninth and thirtieth season of 22 episodes each, extending the show to 2019',
  'The Simpsons received widespread critical acclaim throughout its first nine[5][6] or ten[7][8] seasons, which are generally considered its "Golden Age"',
  'Time named it the 20th centurys best television series,[9] and Erik Adams of The A Club named it televisions crowning achievement regardless of format',
  'On January 14, 2000, the Simpson family was awarded a star on the Hollywood Walk of Fame',
  'It has won dozens of awards since it debuted as a series, including 31 Primetime Emmy Awards, 30 Annie Awards, and a Peabody Award',
  'Homers exclamatory catchphrase "Doh!" has been adopted into the English language, while The Simpsons has influenced many other later adult-oriented animated sitcoms',
  'Despite this, the show has also been criticized for what many perceive as a decline in quality over the years, generally since about the late 1990s'
]

SPANISH_TEXT = [
  'Los Simpson (en ingl\xc3\xa9s, The Simpsons) es una serie estadounidense de comedia, en formato de animaci\xc3\xb3n, creada por Matt Groening para Fox Broadcasting Company y emitida en varios pa\xc3\xadses del mundo',
  'La serie es una s\xc3\xa1tira de la sociedad estadounidense que narra la vida y el d\xc3\xada a d\xc3\xada de una familia de clase media de ese pa\xc3\xads (cuyos miembros son Homer, Marge, Bart, Lisa y Maggie Simpson) que vive en un pueblo ficticio llamado Springfield',
  '1\xe2\x80\x8bLa familia fue concebida por Groening y poco despu\xc3\xa9s debut\xc3\xb3 en una serie de cortos de animaci\xc3\xb3n producidos por James L',
  'Brooks 2\xe2\x80\x8b Groening cre\xc3\xb3 una familia disfuncional y nombr\xc3\xb3 a sus personajes en honor a los miembros de su propia familia, sustituyendo su propio nombre por Bart',
  '2\xe2\x80\x8b3\xe2\x80\x8b Los cortos pasaron a formar parte de El show de Tracey Ullman el 19 de abril de 1987,4\xe2\x80\x8b pero despu\xc3\xa9s de tres temporadas se decidi\xc3\xb3 convertirlos en una serie de episodios de media hora en horario de m\xc3\xa1xima audiencia',
  ' Constituy\xc3\xb3 un \xc3\xa9xito de la cadena Fox y fue la primera serie de este canal en llegar a estar entre los 30 programas m\xc3\xa1s vistos en la temporada 1992-1993 en Estados Unidos',
  '5\xe2\x80\x8bDesde su debut el 17 de diciembre de 1989, se han emitido m\xc3\xa1s de 600 episodios, habiendo finalizado su vig\xc3\xa9simoctava temporada',
  '6\xe2\x80\x8b En el final de la decimoctava temporada, el 20 de mayo de 2007, se emiti\xc3\xb3 en Estados Unidos el episodio 400: You Kent Always Say What You Want',
  ' En la mayor\xc3\xada del mundo los d\xc3\xadas 26 y 27 de julio de 2007 se estren\xc3\xb3 Los Simpson: la pel\xc3\xadcula, la cual recaud\xc3\xb3 cerca de 526 millones de d\xc3\xb3lares en todo el mundo',
  '7\xe2\x80\x8bLos Simpson ha ganado numerosos premios desde su estreno como serie, incluyendo 25 premios Emmy, 24 premios Annie y un premio Peabody',
  ' La revista Time del 31 de diciembre de 1999 la calific\xc3\xb3 como la mejor serie del siglo XX,8\xe2\x80\x8b y el 14 de enero de 2000 recibi\xc3\xb3 una estrella en el Paseo de la Fama de Hollywood',
  ' Los Simpson es una de las series estadounidenses de dibujos animados de mayor duraci\xc3\xb3n9\xe2\x80\x8b y el programa estadounidense de animaci\xc3\xb3n m\xc3\xa1s largo',
  '10\xe2\x80\x8b El gru\xc3\xb1ido de fastidio de Homer \xc2\xabDoh!\xc2\xbb ha sido incluido en el diccionario Oxford English Dictionary, mientras que la serie ha influido en muchas comedias de situaci\xc3\xb3n animadas para adultos',
]

GERMAN_TEXT = [
  'James L Brooks wurde durch die Comicserie Life in Hell auf Matt Groening aufmerksam',
  ' Er rief Groening 1985 an und fragte, ob er etwas f\xc3\xbcr die Tracey Ullman Show zeichnen wolle',
  ' Bei dem vereinbarten Treffen soll Groening dann einigen Quellen zufolge erfahren haben, dass er etwas Neues und Au\xc3\x9fergew\xc3\xb6hnliches pr\xc3\xa4sentieren sollte',
  ' So zeichnete er in 15 Minuten die Figuren zur Serie',
  ' Hierbei soll ihm auch die Idee gekommen sein, dass Homer in einem Kernkraftwerk arbeitet',
  '[3] In einem Interview verriet er jedoch, dass er sich bei besagtem Treffen entschlossen habe, nicht, wie urspr\xc3\xbcnglich geplant, aus der Comicserie Life in Hell eine Fernsehserie zu machen, da dies, wie er erfahren musste, bedeutet h\xc3\xa4tte, die Rechte an Life in Hell abzugeben',
  ' Stattdessen entwickelte er dann spontan die Idee zur Serie Die Simpsons',
  '[4] Die Simpsons wurden erstmals am 19',
  ' April 1987 als Kurzfilm in der Tracey Ullman Show gesendet',
  ' Die Figuren waren zu diesem Zeitpunkt noch \xc3\xa4u\xc3\x9ferst krude gezeichnet, da Matt Groening die Rohentw\xc3\xbcrfe den Animatoren in der Hoffnung \xc3\xbcbergab, diese w\xc3\xbcrden f\xc3\xbcr den n\xc3\xb6tigen Feinschliff sorgen; stattdessen \xc3\xbcbertrugen sie die Skizzen ohne weitere Ver\xc3\xa4nderungen',
  '[5] 1989 wurde die Idee vom Fernsehsender FOX zu einer Fernsehserie ausgebaut, deren Pilotfolge Es weihnachtet schwer am 17',
  ' Dezember 1989 ausgestrahlt wurde und ein Publikum von knapp 27 Millionen Zuschauern erreichte',
  ' Als offiziell erste Folge der ersten Staffel sendete FOX am 14',
  ' Januar 1990 Bart wird ein Genie',
  ' Seitdem laufen Die Simpsons dort w\xc3\xb6chentlich',
  ' Bereits nach einem Jahr erreichte die Serie eine gro\xc3\x9fe, teilweise fanatische Anh\xc3\xa4ngerschar und genoss Kultstatus',
  '[6] Die Serie wurde in den ersten drei Staffeln von der Produktionsfirma Klasky Csupo produziert',
  ' Seit der vierten Produktionsstaffel ist Film Roman daf\xc3\xbcr verantwortlich',
  ' Ihre Erstausstrahlung im deutschen Sprachraum hatte die Serie 1991 im ZDF, seit 1994 wird sie auf ProSieben ausgestrahlt und war zudem auch bei Sat',
  '1 Comedy zu empfangen',
  ' In \xc3\x96sterreich l\xc3\xa4uft die Serie auf ORF 1 und in der Schweiz lief sie auf SF zwei im Zweikanalton, bis sie auf 3 Plus TV wechselte',
  ' In den USA sind Die Simpsons die langlebigste Prime-Time-Serie und zugleich die bisher erfolgreichste Zeichentrickserie',
  ' 1997 \xc3\xbcberholte die Serie die Familie Feuerstein im Rekord f\xc3\xbcr die am l\xc3\xa4ngsten laufende US-amerikanische Zeichentrickserie zur Prime Time und bekamen damit einen Eintrag im Guinness-Buch der Rekorde',
  '[7] 2004 wurden Die Simpsons von Scooby-Doo bei der Anzahl der Episoden \xc3\xbcberholt, konnten den Titel jedoch 2005 zur\xc3\xbcckerobern',
  ' Im Jahr 2009 wurde die Serie zudem f\xc3\xbcr die am l\xc3\xa4ngsten laufende Sitcom und die Serie mit den meisten Emmy-Awards mit weiteren Guinness-Rekorden ausgezeichnet und h\xc3\xa4lt somit vier Rekorde',
]


class EnglishTestSuite(unittest.TestCase):
  """Basic test cases."""

  def test_english(self):
    ls = langsense.LangSense()

    for sentence in ENGLISH_TEXT:
      assert ls.detect(sentence)[0][0] == 'en'

  def test_spanish(self):
    ls = langsense.LangSense()

    for sentence in SPANISH_TEXT:
      assert ls.detect(sentence)[0][0] == 'es'

  def test_german(self):
    ls = langsense.LangSense()

    for sentence in GERMAN_TEXT:
      assert ls.detect(sentence)[0][0] == 'de'


if __name__ == '__main__':
  unittest.main()