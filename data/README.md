# Data
<!-- markdownlint-disable MD013 -->
## Content of folder

### Formatted files

- Columns ``uppsala_tm_1722-2022.dat``
    - Top part (no text!)

    1722  1 12   1.9   1.8 1
    1722  1 13   2.3   2.2 1
    1722  1 14   1.8   1.7 1
    1722  1 15    .9    .8 1
    1722  1 16  -1.8  -1.9 1
    1722  1 17    .5    .4 1
    ...

- Meta data ``uppsala_tm_1722-2022.txt``
    - Describes the data.

### Raw files

- Web portal: <https://www.smhi.se/data/hitta-data-for-en-plats/ladda-ner-vaderobservationer/airtemperatureInstant/>
- One can choose a station and further down one can download historical data "Ladda ner historisk data".
- These are combined cdata and meta data files
- So far there is just a couple of raw files down- and uploaded to this folder

- Uppsala: ``smhi-opendata_1_97530_20250122_131109.csv``
- Lund: ``smhi-opendata_1_53430_20251024_155957.csv``
- Kiruna: ``smhi-opendata_1_180960_20251024_160026.csv``

#### Example of content

   Stationsnamn;Stationsnummer;Stationsnät;Mäthöjd (meter över marken)
   Uppsala Flygplats;97530;SMHIs stationsnät;2.0

   Parameternamn;Beskrivning;Enhet
   Lufttemperatur;momentanvärde, 1 gång/tim;celsius

   Tidsperiod (fr.o.m);Tidsperiod (t.o.m);Höjd (meter över havet);Latitud (decimalgrader);Longitud (decimalgrader)
   1944-05-01 00:00:00;2025-01-01 06:20:10;20.6;59.9000;17.5930

   Datum;Tid (UTC);Lufttemperatur;Kvalitet;;Tidsutsnitt:
   1944-07-01;07:00:00;16.2;G;;Kvalitetskontrollerade historiska data (utom de senaste 3 mån)
   1944-07-01;13:00:00;23.0;G;;Tidsperiod (fr.o.m.) = 1944-07-01 00:00:00 (UTC)
   1944-07-01;18:00:00;20.2;G;;Tidsperiod (t.o.m.) = 2024-10-01 06:00:00 (UTC)
   1944-07-02;07:00:00;19.8;G;;Samplingstid = Ej angivet
   1944-07-02;13:00:00;25.8;G;;Kvalitetskoderna:
   1944-07-02;18:00:00;22.0;G;;Grön (G) = Kontrollerade och godkända värden.
   1944-07-03;07:00:00;21.0;G;;Gul (Y) = Misstänkta eller aggregerade värden. Grovt kontrollerade arkivdata och okontrollerade realtidsdata (senaste 2 tim).
   1944-07-03;13:00:00;24.2;G;;Nätinformation:
   1944-07-03;18:00:00;22.6;G;;SMHIs Stationsnät: Data samlas in och lagras i SMHIs databaser. Data kvalitetskontrolleras vilket innebär att felaktiga data korrigeras och att databortfall kompletteras utifrån expertbedömning där det är möjligt. De flesta stationerna övervakas, inspekteras och underhålls löpande av SMHI.
   1944-07-04;07:00:00;21.2;G;;Övriga stationer: Data samlas in och lagras i SMHIs databaser. Datakvaliteten är för SMHI okänd då SMHI varken utför kvalitetskontroll på data eller inspektioner på stationerna.
   1944-07-04;13:00:00;26.0;G;;Möjliga orsaker till saknade data:
   1944-07-04;18:00:00;21.8;G;;– stationen eller givaren har varit ur funktion.
   1944-07-05;07:00:00;22.4;G;;– stationen har endast levererat värden med kvalitetskod Röd (R). Dessa levereras ej.
   1944-07-05;13:00:00;27.6;G
   1944-07-05;18:00:00;25.6;G
   1944-07-06;07:00:00;24.0;G
   1944-07-06;13:00:00;26.4;G
   1944-07-06;18:00:00;27.6;G
   1944-07-07;07:00:00;24.4;G
   1944-07-07;13:00:00;29.1;G
   1944-07-07;18:00:00;25.6;G
   1944-07-08;07:00:00;23.3;G
