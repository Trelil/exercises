# Programflöde, primtal och den magiska modulo operatorn

I denna uppgift får du undersöka hur loopar fungerar samt grundläggande logiska satser

- **Svårighetsgrad:** <1-3>

## Delmoment

1. Undersök loop.py, if.py, if_else.py,
	I de ovan nämnda filerna finns kod som demonstrerar hur loopar och if-satser fungerar.
	
	Börja med att köra loop.py
	Undersök nu vad som händer om du ändrar parametern till range funktonen från 10 till något annat tal.

	Fortsätt nu med att köra de två filerna if.py och if_else.py.
	Se till att du förstår skillnaden mellan flera påvartanna följande if-satse och en stor if-else sats.
	Diskutera det gärna med en handledare om du är osäker.
	
2. Undersök fizzbuzz.py,
	Läs igenom specifikationen i fizzbuzz.py för hur fizzbuss ska fungera.
	Testa att köra fizzbuzz.py. Notera att "FizzBuzz" aldrig skrivs ut.
	Det är något som är fel på if-else satsen. Försök lösa problemet.
	Tips: programmet exekveras linjärt. Tänk rad för rad vad som händer.

3. Funktioner
	Funktioner har du redan sett och använt, exempelvis print("Hello, World!") eller range(10), dock är det här första gången som du ser hela definitionen på en.
	Du kan själv definiera funktioner genom att skriva

	def funktionsnamn(parameter1, parameter2):
		funktionskropp

	funktionsnamnet får innehålla små och stora bokstäver samt '_'.
	parameterlistan (det innanför parenteserna) kan innehålla hur många parametrar som helst men behöver heller inte ha några alls. parametrar separeras med ','
	
	Var som helst i en funktion kan man använda 'return x', funktionen returnerar då x och avbryts direkt. programmet körs vidare där funktionen kallades
	
	När man skriver små program kanske man inte behöver funktioner. Men när det börjar bli större så är de väldigt användbara för att strukturera upp koden och göra abstraktioner. Man kan tänka på en funktion som en låda där du stoppar in något på ena sidan och får ut något på den andra. Lådan brukar ofta kallas "black box" då vi inte vet hur beräkningarna görs. Däremot vet vi vad vi kan stoppa in och vad vi förväntar oss att få ut.

	I functions.py ser du några exempel på hur funktioner fungerar. Du behöver inte memorera allt nu, du kan återkomma och se hur syntaxen ser ut, det viktiga är att du förstår vilka möjligheter det ger dig.


4. Funktionen "contains" och listor.
	Listor är likt funktoner väldigt användbart, här används listor för att visa ett exempel på en användbar funktion. Därför går vi nu bara igenom basen för hur listor fungerar.

	lists.py innehåller exempel och övningar på hur listor kan användas.

	När du är nöjd och har fått lite förståelse för hur listor fungerar gå vidare till contains.py.

5. Härnäst ska vi kolla på beräkning av primtal.
	prime.py innehåller en funktion för att kolla om ett tal är ett primtal. Funktionen är dock inte helt färdigskriven.


	

## Utbyggnad

	Det saknas lite logik, t.ex accepterar funktionen alla tal under 2 då 'range(2, x)', där x < 2, ger en tom lista och därmed returnerar funktionen True
	Lägg till en if-sats som returnerar 'False' om integer är mindre än eller lika med 1. Kör programmet och kolla om funktionen ger korrekt svar för talen 0 och 1.


	Nu är din uppgift att skriva ut all primtal under 100.
	Skriv en for loop för att iterera över alla tal mellon 0 och 100,
	använd sedan en if-sats som kollar resultatet från is_prime funktionen och skriver ut talet om det är ett primtal.