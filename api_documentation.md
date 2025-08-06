```
NAV Online Számla rendszer
```
# NAV Online Számla rendszer

## Számlaadat-szolgáltatás REST API

## interfészleírás és fejlesztői dokumentáció


## NAV Online Számla rendszer





NAV Online Számla rendszer


- BEVEZETÉS Tartalomjegyzék
   - CÉL
   - ADÓZÓKRA VONATKOZÓ HASZNÁLATI KÖVETELMÉNYEK
   - A KAPCSOLÓDÁSHOZ IMPLEMENTÁLANDÓ TECHNOLÓGIÁK
   - SZÁMLÁZÓ PROGRAMOKRA VONATKOZÓ TECHNIKAI KÖVETELMÉNYEK
- 1 SZÁMLAADAT-SZOLGÁLTATÁS REST API ISMERTETÉSE
   - 1.1 A SZÁMLAADAT-SZOLGÁLTATÁS FOLYAMATA
   - 1.2 AZ XML-ÜZENETEK ÁLTALÁNOS FELÉPÍTÉSE
   - 1.3 BASICONLINEINVOICEREQUESTTYPE
      - 1.3.1 BasicHeaderType
      - 1.3.2 UserHeaderType............................................................................................................................
      - 1.3.3 SoftwareType
   - 1.4 BASICONLINEINVOICERESPONSETYPE
      - 1.4.1 BasicResultType
   - 1.5 A REQUESTSIGNATURE SZÁMÍTÁSA
      - 1.5.1 Számítás manageInvoice és manageAnnulment operáció esetén
      - 1.5.2 Számítás manageInvoice és manageAnnulment operáción kívül
      - 1.5.3 Helyi idő konvertálása UTC időre
   - 1.6 A SZOLGÁLTATÁS TECHNIKAI LEÍRÁSA
      - 1.6.1 Általános technikai adatok
      - 1.6.2 Erőforrások..................................................................................................................................
      - 1.6.3 HTTP fejlécek
      - 1.6.4 HTTP státuszkódok
      - 1.6.5 Tömörítés és méretkorlát
      - 1.6.6 Válaszidő, timeout
      - 1.6.7 Szerveróra, NTP
      - 1.6.8 Karbantartási mód
      - 1.6.9 Verziókezelés
      - 1.6.10 Karakterkonverzió
      - 1.6.11 Forgalomkorlátozás
   - 1.7 AZ API SÉMALEÍRÓ FŐBB ELEMEI
   - 1.8 ÜZLETI OPERÁCIÓK
      - 1.8.1 A /manageAnnulment operáció
      - 1.8.2 A /manageInvoice operáció
      - 1.8.3 A /queryInvoiceChainDigest operáció
      - 1.8.4 A /queryInvoiceCheck operáció
      - 1.8.5 A /queryInvoiceData operáció
      - 1.8.6 A /queryInvoiceDigest operáció
      - 1.8.7 A /queryTransactionList operáció
      - 1.8.8 A /queryTransactionStatus operáció...........................................................................................
      - 1.8.9 A /queryTaxpayer operáció
      - 1.8.10 A /tokenExchange operáció
   - 1.9 LOGIKAI REFERENCIA IMPLEMENTÁCIÓ
      - 1.9.1 Azonnaliság kezelése, adatszolgáltatások kötegelése
      - 1.9.2 Elveszett tranzakció azonosító kezelése, dupla adatszolgáltatások megelőzése
   - 1.10 JOGELŐDRE VONATKOZÓ MŰVELETEK............................................................................................................
      - 1.10.1 Lekérdező operációk
      - 1.10.2 Számlaadat-szolgáltatás beküldése
      - 1.10.3 Jogelőd adatszolgáltatásainak technikai érvénytelenítése
- 2 SZÁMLAADAT-SZOLGÁLTATÁS ÜZLETI TARTALOM LEÍRÁSA NAV Online Számla rendszer
   - 2.1 A SZÁMLA/MÓDOSÍTÁS SÉMA ÁLTALÁNOS JELLEMZŐI
      - 2.1.1 Az InvoiceDataType komplex típus szerkezete
      - 2.1.2 Adatok kötelezősége
      - 2.1.3 Címadatok a sémában
      - 2.1.4 Adószámok a sémában
      - 2.1.5 Előre nem nevesített adatok szerepeltetése
      - 2.1.6 Egyezményes, nevesített adatok szerepeltetése
      - 2.1.7 Tizedes elválasztó........................................................................................................................
   - 2.2 A SZÁMLA/MÓDOSÍTÁS SÉMA RÉSZLETES TARTALMA
      - 2.2.1 invoiceReference
      - 2.2.2 invoiceHead
      - 2.2.3 invoiceLines
      - 2.2.4 productFeeSummary
      - 2.2.5 invoiceSummary
   - 2.3 AZ ÜZLETI TARTALOMBAN SZEREPLŐ TÍPUSOK LEÍRÁSA
      - 2.3.1 BankAccountNumberType (Bankszámlaszám típus)
      - 2.3.2 Boolean (Logikai érték)
      - 2.3.3 InvoiceDateType (Dátum típus).................................................................................................
      - 2.3.4 ExchangeRateType (Árfolyam típus)
      - 2.3.5 InvoiceAppearanceType (Megjelenési forma típus)
      - 2.3.6 InvoiceCategoryType (Számla típusa)
      - 2.3.7 MarginSchemeType (Különbözet szerinti adózás típus)
      - 2.3.8 MonetaryType (Pénzösszeg típus)
      - 2.3.9 PaymentMethodType (Fizetés módja típus)
      - 2.3.10 ProductCodeCategoryType (Termékkódfajta típus)
      - 2.3.11 ProductStreamType (Termékáram típus)
      - 2.3.12 QuantityType (Mennyiség típus)
      - 2.3.13 RateType (Arány típus)
      - 2.3.14 TakeoverType (Termékdíj átvállalás típus)
      - 2.3.15 InvoiceTimestampType (időbélyeg típus)
      - 2.3.16 UnitOfMeasureType (mennyiségi egység típus)
      - 2.3.17 LineNatureIndicatorType (termék/szolgáltatás jelölő típus)
   - 2.4 KORÁBBI ADATSZOLGÁLTATÁS TECHNIKAI ÉRVÉNYTELENÍTÉSE
      - 2.4.1 Adatszolgáltatás technikai érvénytelenítésére vonatkozó szabályok
   - 2.5 ADATSZOLGÁLTATÁS SZÁMLÁVAL EGY TEKINTET ALÁ ESŐ OKIRATOKRÓL
      - 2.5.1 Adatszolgáltatás számla érvénytelenítéséről
      - 2.5.2 Adatszolgáltatás számla módosításáról
      - 2.5.3 Módosuló adatok a tételsorokban
      - 2.5.4 Módosításkor szolgáltatandó adatok
      - 2.5.5 Számla összegzés adatok módosításkor
      - 2.5.6 Adatszolgáltatás több számlát módosító okiratról
      - 2.5.7 Adatszolgáltatás többszöri módosításokról
      - 2.5.8 Értelmezést segítő példák
   - 2.6 ELEKTRONIKUS SZÁMLÁZÁS TÁMOGATÁSA
      - 2.6.1 Archiválás
      - 2.6.2 Adatszolgáltatás elektronikus számla beküldésével
   - 2.7 NAGYMÉRETŰ SZÁMLÁKRÓL TÖRTÉNŐ ADATSZOLGÁLTATÁS
   - 2.8 KÖZMŰ ELSZÁMOLÓ SZÁMLÁJÁNAK ADATSZOLGÁLTATÁSA
   - 2.9 ELŐLEGSZÁMLA, VÉGSZÁMLA ADATSZOLGÁLTATÁSA
- 3 HIBAKEZELÉS
   - 3.1 ÁLTALÁNOS HIBAKÓDOK NAV Online Számla rendszer
      - 3.1.1 GeneralExceptionResponseType
      - 3.1.2 GeneralErrorResponseType
   - 3.2 TECHNIKAI HIBAKÓDOK
   - 3.3 VALIDÁCIÓS HIBAKÓDOK
      - 3.3.1 Technikai validációs hibakódok
      - 3.3.2 Blokkoló validációs hibakódok
      - 3.3.3 Figyelmeztetések
- 4 TÖRZSEK
   - 4.1 AZ ILLETÉKES ÁLLAMI ADÓHATÓSÁGOT JELZŐ ILLETÉKESSÉGI KÓDOK (COUNTYCODE)
   - 4.2 ORSZÁGKÓD TÍPUS ISO 3166 ALPHA- 2 SZABVÁNY SZERINT
   - 4.3 IRÁNYÍTÓSZÁM TÖRZS ELÉRHETŐSÉGE
   - 4.4 VTSZ TÖRZS ELÉRHETŐSÉGE
   - 4.5 SZJ TÖRZS ELÉRHETŐSÉGE
   - 4.6 KN TÖRZS ELÉRHETŐSÉGE
   - 4.7 CSK TÖRZS ELÉRHETŐSÉGE
   - 4.8 KT TÖRZS ELÉRHETŐSÉGE
   - 4.9 EJ TÖRZS ELÉRHETŐSÉGE
   - 4.10 TESZOR TÖRZS ELÉRHETŐSÉGE
- 5 VERZIÓKÖVETÉS
   - 5.1 1.0-ÁS XSD-VERZIÓ
   - 5.2 1.1-ES XSD-VERZIÓ
   - 5.3 2.0-ÁS XSD-VERZIÓ
   - 5.4 3.0-ÁS XSD-VERZIÓ
- 6 KÖRNYEZETEK ELÉRHETŐSÉGEI
   - 6.1 FELHASZNÁLÓI TESZTKÖRNYEZET
   - 6.2 ÉLES KÖRNYEZET
- 7 HELPDESK ÉS TECHNIKAI SEGÍTSÉGNYÚJTÁS
   - 7.1 ÖNELLENŐRZÉS
   - 7.2 HELPDESK ELÉRHETŐSÉG
   - 7.3 GITHUB ELÉRHETŐSÉG
      - 7.3.1 Common repository
      - 7.3.2 Online-Invoice repository
      - 7.3.3 Online-Invoice-Test-Tool repository
- 8 RENDSZERDIAGNOSZTIKA
   - 8.1 A SZOLGÁLTATÁS TECHNIKAI LEÍRÁSA
      - 8.1.1 Általános technikai adatok
      - 8.1.2 Erőforrások................................................................................................................................
      - 8.1.3 HTTP fejlécek
      - 8.1.4 HTTP válaszkódok
      - 8.1.5 Válaszidő, timeout
      - 8.1.6 Elérhetőségek
   - 8.2 A SZOLGÁLTATÁS ÉS AZ ÜZLETI METRIKÁK MŰKÖDÉSE
      - 8.2.1 Metrikák típusai
      - 8.2.2 Metrikák leírása
   - 8.3 ÜZLETI OPERÁCIÓK
      - 8.3.1 A /queryServiceMetrics operáció
- 9 MELLÉKLETEK NAV Online Számla rendszer
- I. AZ ONLINE SZÁMLA RENDSZER ÁLTAL KÜLDÖTT FIGYELMEZTETŐ ÜZENETEK
   - I.1 A SZÁMLA FEJLÉC ADATAIVAL KAPCSOLATOS FIGYELMEZTETÉSEK
   - I.2 TÉTELSOROKBAN SZEREPLŐ ADATOKRA VONATKOZÓ FIGYELMEZTETÉSEK
   - I.3 TERMÉKDÍJADATOKHOZ KAPCSOLÓDÓ FIGYELMEZTETÉSEK
   - I.4 AZ ÖSSZESÍTŐ ADATOKRA VONATKOZÓ FIGYELMEZTETÉSEK
   - I.5 INKONZISZTENS SZÁMLAMÓDOSÍTÁSI ADATOK CSOPORT
- II. AZ ONLINE SZÁMLA RENDSZER ÁLTAL KÜLDÖTT INFORMÁCIÓS ÜZENETEK
- III. AZ ONLINE SZÁMLA RENDSZER ADATSZÓTÁRA................................................................................
   - III.1 MEGFELELTETÉS
   - III.2 KÖTELEZŐSÉGEK
- IV. AZ ONLINE SZÁMLA ÉS AZ ONLINE PÉNZTÁRGÉP RENDSZER KAPCSOLATA
   - IV. I. BIZONYLAT TÍPUSOK
      - IV. 1. 1. Pénztárgépi bizonylat típusok
   - IV.2. ÁTADÁSI FOLYAMAT
      - IV. 2.1. Bizonylatok szétválasztása
      - IV.2.2 Deduplikáció..............................................................................................................................
      - IV.2.3 Adószám forgatás ÁFA csoport tagok esetén
   - IV.3 SZÁRMAZTATOTT ADATOK
      - IV.3.1 Vevői adószámra illesztés
      - IV.3.2 Előzményre illesztés
      - IV.3.3 Számlasor pozíció illesztése
      - IV.3.4 Karakter konverziós műveletek
      - IV.3.5 Összesítő adatok kiszámítása
   - IV.4 XML TRANSZFORMÁCIÓ
      - IV.4.1 invoiceOperation értékadás
      - IV.4.2 XML root értékadás
      - IV.4.3 invoiceMain csomópont választás....................................................................................................
      - IV.4.4 invoice/invoiceReference értékadás
      - IV.4.5 invoice/invoiceHead csomópont értékadás
      - IV.4.6 invoice/invoiceLines csomópont értékadás
      - IV.4.7 invoice/ProductFeeSummary csomópont értékadás
      - IV.4.8 invoice/invoiceSummary csomópont értékadás
   - IV.5 TRANZAKCIÓS MŰVELETEK
      - IV.5.1 Adatszolgáltatások
      - IV.5.2 Feldolgozási műveletek
      - IV.5.3 Módosítás, annulálás
      - IV.5.4 Statisztika, notifikáció
- 1. ábra A BasicOnlineInvoiceRequestType felépítése Ábrajegyzék
- 2. ábra A BasicHeaderType felépítése
- 3. ábra A UserHeaderType felépítése......................................................................................................
- 4. ábra A SoftwareType felépítése
- 5. ábra A BasicOnlineInvoiceResponseType felépítése
- 6. ábra A BasicResultType felépítése
- 7. ábra A ManageAnnulmentRequest felépítése
- 8. ábra A ManageAnnulmentResponse felépítése
- 9. ábra A ManageInvoiceRequest felépítése
- 10. ábra A ManageInvoiceResponse felépítése
- 11. ábra A QueryInvoiceChainDigestRequest felépítése
- 12. ábra A QueryInvoiceChainDigestResponse felépítése
- 13. ábra Az InvoiceChainElementType felépítése
- 14. ábra A QueryInvoiceCheckRequest felépítése
- 15. ábra A QueryInvoiceCheckResponse felépítése
- 16. ábra A QueryInvoiceDataRequest felépítése
- 17. ábra A QueryInvoiceDataResponse felépítése
- 18. ábra Az AuditDataType felépítése
- 19. ábra A QueryInvoiceDigestRequest felépítése
- 20. ábra A MandatoryQueryParamsType felépítése
- 21. ábra Az AdditionalQueryParamsType felépítése
- 22. ábra A RelationalQueryParamsType felépítése
- 23. ábra A TransactionQueryParamsType felépítése
- 24. ábra A QueryInvoiceDigestResponse felépítése
- 25. ábra Az InvoiceDigestType felépítése..............................................................................................
- 26. ábra A QueryTransactionListRequest felépítése
- 27. ábra A QueryTransactionListResponse felépítése
- 28. ábra A QueryTransactionStatusRequest felépítése.........................................................................
- 29. ábra A QueryTransactioneStatusResponse felépítése
- 30. ábra A ProcessingResultType felépítése..........................................................................................
- 31. ábra Az AnnulmentDataType felépítése..........................................................................................
- 32. ábra A QueryTaxpayerRequest felépítése
- 33. ábra A QueryTaxpayerResponse felépítése
- 34. ábra A TaxpayerAddressListType felépítése
- 35. ábra A DetailedAddressType felépítése
- 36. ábra A TokenExchangeRequest felépítése
- 37. ábra A TokenExchangeResponse felépítése
- 38. ábra Az InvoiceDataType
- 39. ábra Az AddressType felépítése
- 40. ábra A SimpleAddressType felépítése
- 41. ábra A DetailedAddressType felépítése
- 42. ábra A TaxNumberType felépítése
- 43. ábra A CustomerVatDataType felépítése
- 44. ábra Az AdditionalDataType felépítése
- 45. ábra A ConventionalInvoiceInfoType felépítése
- 46. ábra Az InvoiceType felépítése NAV Online Számla rendszer
- 47. ábra Az InvoiceReferenceType felépítése
- 48. ábra Az InvoiceHeadType felépítése
- 49. ábra A SupplierInfoType felépítése
- 50. ábra A CustomerInfoType felépítése
- 51. ábra A FiscalRepresentativeType felépítése
- 52. ábra Az InvoiceDetailType felépítése
- 53. ábra A LinesType felépítése
- 54. ábra A LineType felépítése
- 55. ábra A LineModificationReferenceType felépítése
- 56. ábra A ReferencesToOtherLinesType felépítése
- 57. ábraAz AdvanceDataType felépítése
- 58. ábra A ProductCodesType felépítése
- 59. ábra A ProductCodeType felépítése
- 60. ábra A DiscountDataType felépítése
- 61. ábra A LineAmountsNormalType felépítése
- 62. ábra A VatRateType felépítése
- 63. ábra A LineAmountsSimplifiedType felépítése
- 64. ábra Az AggregateInvoiceLineDataType felépítése
- 65. ábra A NewTransportMeanType felépítése
- 66. ábra A VehicleType felépítése
- 67. ábra A VesselType felépítése
- 68. ábra Az AircraftType felépítése
- 69. ábra A DieselOilPurchaseType felépítése
- 70. ábra A ProductFeeClauseType felépítése
- 71. ábra A ProductFeeTakeoverDataType felépítése
- 72. ábra A CustomerDeclarationType felépítése
- 73. ábra A ProductFeeDataType felépítése
- 74. ábra A ProductFeeSummaryType felépítése
- 75. ábra A PaymentEvidenceDocumentDataType felépítése
- 76. ábra A SummaryType felépítése
- 77. ábra A SummaryNormalType felépítése
- 78. ábra A SummaryByVatRate felépítése
- 79. ábra A SummarySimplifiedType felépítése
- 80. ábra Az InvoiceAnnulmentType felépítése
- 81 ábra A BatchInvoiceType felépítése
- 82. ábra A GeneralExceptionResponseType felépítése
- 83 ábra A GeneralErrorResponseType felépítése
- 84. ábra A QueryServiceMetricsResponse felépítése
- 85. ábra A QueryServiceMetricsListResponse felépítése


```
NAV Online Számla rendszer
```
**Kifejezések, rövidítések
Kifejezés Leírás**
Adatexport A számla és a nyugta adóigazgatási azonosításáról, valamint az elektronikus formában
megőrzött számlák adóhatósági ellenőrzéséről szóló 23/2014. (VI. 30.) NGM rendelet
11/A. §-ában előírtak szerinti adóhatósági ellenőrzési adatszolgáltatás.
Adózó Az a Magyarországon nyilvántartásba vett adóalany, aki, vagy amely a jogszabályok
alapján az online számlaadat-szolgáltatásra kötelezett.
AES- 128 Szimmetrikus titkosítási algoritmus (Advanced Encryption Cypher, RFC3826).
Adatszolgáltató Az a természetes vagy jogi személy, aki az adózó adatszolgáltatási kötelezettségét
ténylegesen teljesíti. Lehet maga az adózó, annak az Áfa tv. szerinti meghatalmazottja
(meghatalmazotti számlázás), az adózó vevője (önszámlázás).
Aláírókulcs Jelen dokumentum értelmében egy karaktersorozat, mely segítségével más karakter
vagy jelsorozat kiegészítésre, “aláírásra” kerül.
API Alkalmazásprogramozási interfész.
Áfa tv. Az általános forgalmi adóról szóló 2007. évi CXXVII. törvény.
Air. tv. Az adóigazgatási rendtartásról szóló 2017.évi CLI. törvény.
BASE64 64 karakterből álló ábécén alapuló tartalomkódolási forma, melynek segítségével bináris,
illetve speciális karaktereket tartalmazó adatokból ASCII karaktersorozat állítható elő
(Binary-to-text encoding, RFC3548).
Elsődleges
felhasználó

```
Az Online Számla rendszer azon felhasználója, aki az adózó törvényes képviselője vagy
állandó meghatalmazottja, és ezáltal jogosult az adózó regisztrálására és ezen felül is
teljes körű jogosultsággal rendelkezik a rendszer használata tekintetében. Ez alól csak a
REST API-n keresztüli adatszolgáltatás a kivétel, mely az elsődleges felhasználó által
létrehozott technikai felhasználóval teljesíthető.
Endpoint Olyan elérési út, amelyen keresztül az operáció által nyújtott szolgáltatás elérhető.
Eredeti számla Az az Áfa tv. szerinti számla, amire az adott módosító okirat (módosítás) vonatkozik.
Gyermekelem Szülőelem által tartalmazott elem.
Gyártó A Számlázó programot, vagy ennek adatszolgáltatást végrehajtó modulját fejlesztő
természetes vagy jogi személy, vagy helyette az adott Számlázó program felhasználója.
Jövedéki törvény A jövedéki adóról szóló 2016. évi LXVIII. törvény.
Módosító okirat
(módosítás)
```
```
Az Áfa tv. 170. §-ában meghatározott feltételeknek megfelelő, kétséget kizáróan az adott
eredeti számlára hivatkozó, annak adattartalmát módosító vagy érvénytelenítő okirat.
NAV Nemzeti Adó- és Vámhivatal.
Operáció Azon informatikai eljárások, szolgáltatások, amelyek a meghívhatók a kiajánlott REST
webszolgáltatáson keresztül.
REST Representational state transfer (REST) vagy másnéven RESTful webszolgáltatás.
SHA- 256 256 bites Biztonságos HASH algoritmus (Secure Hash Algorithm 3, RFC6234).
SHA- 512 512 bites Biztonságos HASH algoritmus (Secure Hash Algorithm 3, RFC6234).
SHA3- 512 512 bites Keccak titkosítású Biztonságos HASH algoritmus (FIPS-202)^1
Számla Ezen dokumentum vonatkozásában a számlázó program által kiállított Áfa tv.
rendelkezései szerinti számla, ide nem értve a számlával egy tekintet alá eső okiratot.
```
(^1) https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf


```
NAV Online Számla rendszer
```
```
Számlázó program Az Adatszolgáltató által használt szoftver vagy szoftverek csoportja, amely az adózó, mint
a termék vagy szolgáltatás szállítója érdekében a számla kiállítását elvégzi, ezzel együtt a
jogszabály szerinti adatszolgáltatást teljesíti.
Szülőelem A sémaállományban szereplő olyan elem, ami további elemeket tartalmaz.
Technikai
felhasználó
```
```
A REST API-n keresztül történő adatszolgáltatáshoz szükséges user, melyet az Elsődleges
felhasználó hozhat létre a rendszerben.
Termékdíj törvény A környezetvédelmi termékdíjról szóló 2011. évi LXXXV. törvény.
Token Adatszolgáltatás teljesítéséhez használatos egyszeri jegy.
XML Kiterjeszthető Jelölő Nyelv (eXtensible Markup Language, W3C standard
https://www.w3.org/TR/xml/).
XSD XML -séma definíciós fájl (XML Schema Definition, W3C standard
https://www.w3.org/TR/xmlschema11-1/).
Webszolgáltatás Alkalmazások közötti adatcserére szolgáló protokollok és szabványok gyűjteménye.
Egyenes adózás Olyan termékértékesítések és szolgáltatásnyújtások, amelynek tekintetében a termék
értékesítője, a szolgáltatás nyújtója az adófizetésre kötelezett.
Fordított adózás Olyan termékértékesítések és szolgáltatás nyújtások, amelyek tekintetében a termék
beszerzője, szolgáltatás igénybevevője az adófizetésre kötelezett.
```
**Dokumentum történet
Dátum Szerző Verzió Változtatás**
2018.01.11. KCS, RD, MA 1.0 Első kiadás

2018. 0 1.22 KCS 1.0 Szövegjavítások, pontosítások
2018.03.11 KCS, MA 1.0 Új választípusok bevezetése, pontosítás,
    egyértelműsítés, adózói visszajelzések átvezetése
2018.04.19 KCS 1.0 Tömörítés, queryInvoiceData átalakítás, lapozás,
    pontosítások
2018.05.23 KCS 1.0 Figyelmeztetések átvezetése, pontosítások
2018.05.30 KCS 1.0 Publikált sémaváltozás átvezetése, szerveróra,
    karbantartási üzenet, új WARN -üzenetek
2018.06.14 KCS 1.0 Hatályba lépett jogszabály átvezetése,
    szövegjavítások
2018.12.06 KCS, CZ, MA 1.1 1.1-es interfészverzió változások átvezetése,
    változáskövetés, lásd: 5.2 fejezet
2019.02.05 KCS 1.1 INVALID_UNIT_OF_MEASURE_OWN validáció
    kivezetése, gyűjtőszámlában exchangeRate
    megadás pontosítása
2019.07.12 KCS 1.1 Új blokkoló validáció bevezetése, mennyiségi
    egység és WARN -elírások javítása
2019. 08. 29 KCS 2.0 2.0-ás interfészverzió változások átvezetése a teljes
    dokumentumon, változáskövetés, lásd: 5.3 fejezet
2019.09.18 KCS 2.0 5.3-as fejezet tartalmi javításai
2019.10.14 KCS 2.0 GitHub-os javítási észrevételek átvezetése, 1 új
    batchInvoice feldolgozáshoz kapcsolódó ERROR és
    2.0-ás új WARN -üzenetek beépítése,
    processingResult tag számosságának módosítása új
    API XSD miatt


```
NAV Online Számla rendszer
```
2019.12. 11 KCS 2.0 GitHub-os javítási észrevételek átvezetése,
technikai érvénytelenítés jóváhagyás állapotainak
leírása

2020. 02. 06 HS, KCS 2.0 2.0 default értékek kivezetése,
    queryInvoiceChainDigest és queryTransactionList
    lekérdező szolgáltatások bevezetése,
    queryTaxpayerResponse kiegészítése,
    queryInvoiceDigestRequest adószám keresési
    lehetőség mindkét irányú lekérdezésnél,
    queryServiceMetrics metrikaszolgáltatás
    bevezetése
2020.09.30 HS 3.0 3.0-ás interfészverzió változások átvezetése a teljes
    dokumentumon, változáskövetés, lásd: 5.4 fejezet
2020.11.02 HS 3.0 Új blokkoló szinkron validáció
    (INVALID_TIMESTAMP) bevezetése, rate limiting és
    referencia implementációk hozzáadása, jogszabályi
    környezet aktualizálása, elírások javítása
2020.12.03 HS 3.0 Sémamódosítások (CustomerVatStatusType,
    vatRateType), új validációk, SHA-512 pontosítás,
    adószámos magánszemély megkülönböztetés
2021.01.22 HS 3.0 INVALID_INVOICE_NUMBER,
    DOMESTIC_TAXNUMBER_EXPECTED_REVERSE_CH
    ARGE blokkoló validációk bevezetése, WARN
    aktualizálás 3.0 verzióra
2021.03.25 HS 3.0 WARN leírások pótlása,
    INCORRECT_LINE_DATA_UOM WARN kivezetése
2021.11.02 HS, KCS 3.0 OPG blokkoló validációk, WARN pontosítások, III.
    melléklet hozzáadása az OPG-s számlák
    integrációjáról
2021.11.24 HS 3.0 Új ERROR és WARN üzenetek bevezetése
2022.03.31 HS 3.0 Új ERROR, WARN és INFO üzenetek
2022.12.08 NÁ, HS, KF 3.0 INVALID_LINE_OPERATION blokkoló validáció
    bevezetése; 2.5.7 és 2.5.8 pontok tartalmának
    módosítása
2023.10.25. NÁ 3.0 Új áfakulcs miatti ERROR és WARN módosítások
    Módosult error sorszámok: 14, 48, 49
    Módosult warn sorszámok: 910
2023.12.08. NÁ 3.0 RequestId egyediségvizsgálat módosítása
    OPG számlák számlaszám képzésének pontosítása
2024.12.11 EA, NÁ 3.0 Jogelőd kezelés miatti funkció változások
    Részletesen ld 1.10-es fejezet


## BEVEZETÉS

Az általános forgalmi adóról szóló 2007. évi CXXVII. törvény 10. mellékletének 20 21. január 4 - től
hatályos 1. és 6. pontja szerint:

_„ 1. Az adóalany köteles adatot szolgáltatni az adó- és vámhatóság részére azon általa teljesített
termékértékesítésekről, szolgáltatásnyújtásokról kibocsátott vagy kiállított számláról, számlával egy
tekintet alá eső okiratról, amelyre e törvény rendelkezéseit kell alkalmazni a 158/A. § értelmében,_

_kivéve azon szolgáltatásnyújtásról, melynek teljesítési helye a Közösség másik tagállama, és amely
tekintetében az adóalany adófizetési kötelezettségének az Art. távolról is nyújtható szolgáltatásokat
nyújtó adózókra vonatkozó különös szabályai szerint tesz eleget._

_„ 6. Az 1-5. pont szerinti adatszolgáltatást az állami adó- és vámhatóság által erre a célra biztosított
elektronikus felületen kell teljesíteni. Az elektronikus felület az adóalany egyedi azonosítására szolgáló
adatok igénylését követően használható. Az azonosító adatokat az adóalany vagy annak Air. szerinti
állandó meghatalmazottja igényli.”_

### CÉL

A dokumentum célja az online számlaadat-szolgáltatás interfész üzleti funkcionalitásaiért felelős
/invoiceService működésének, illetve az általa használt XML üzenetstruktúrának bemutatása, valamint
a számlázó programok interfészhez történő integrációjának támogatása.

Jelen dokumentum a következő sémaleírók üzleti és műszaki tartalmát foglalja magába.

```
Séma Tartalom
common.xsd Generikus, NAV kommunkiációt leíró típusok, katalógus
elemek és primitívek
invoiceBase.xsd Online Számla rendszer specifikus adattípusai
invoiceApi.xsd A REST API operációi (beküldési és lekérdező funkciók)
invoiceData.xsd A számlaadat-szolgáltatás üzleti tartalma
invoiceAnnulment.xsd A technikai érvénytelenítés üzleti tartalma
serviceMetrics.xsd Az Online Számla rendszer működési metrikáinak
szerkezete, tartalma
```
Az InvoiceApi sémaleíróra vonatkozó szabályok az „ **SZÁMLAADAT-SZOLGÁLTATÁS REST API
ISMERTETÉSE”** fejezetben, míg az InvoiceData és invoiceAnnulment sémaleíróra vonatkozó szabályok
a „ **SZÁMLAADAT-SZOLGÁLTATÁS ÜZLETI TARTALOM LEÍRÁSA”** fejezetben találhatók meg.

A rendszer diagnosztikai adatainak lekérésére szolgáló /metricService működése, a serviceMetrics
sémaleíróra vonatkozó szabályok és az XML -üzenetek struktúrája a „ **Rendszerdiagnosztika”**
fejezetben található.

### ADÓZÓKRA VONATKOZÓ HASZNÁLATI KÖVETELMÉNYEK

**1)** Az adatszolgáltatásra kötelezett adózónak érvényes regisztrációval kell rendelkeznie az Online
Számla rendszerben. A regisztráció az Online Számla web felületen kezdeményezhető.


**2)** Az adatszolgáltatási interfész használatához az adatszolgáltatásra kötelezett adózónak technikai

felhasználót kell létrehoznia az Online Számla rendszerben. A számlabejelentő interfész webes
felhasználóval (elsődleges vagy másodlagos) nem vehető igénybe. A technikai felhasználó létrehozását
csak elsődleges felhasználó végezheti el az Online Számla web felületen. Az adózó tetszőlegesen
megválaszthatja, hogy adatszolgáltatásai teljesítéséhez hány technikai felhasználót igényel.

**3)** A technikai felhasználó számára aláírókulcsot és cserekulcsot kell generáltatni az Online Számla
rendszerben. A kulcsok generálását csak elsődleges felhasználó jogosult elvégezni az Online Számla
web felületen. Az aláírókulcs az üzenetek aláírására szolgáló requestSignature számításában játszik
szerepet, míg a cserekulcs az adatszolgáltatási token szerveroldali elkódolásához és a kliensoldali
dekódolásához szükséges.

4) A technikai felhasználók kapcsán az elsődleges felhasználónak meg kell határoznia, hogy jogosult-e

a beküldött számlaadatok utólagos lekérdezésére.

A felsorolt követelmények rendszersíkonként értendők, azaz a tesztkörnyezetben elvégzett
regisztráció nem helyettesíti az éles környezetben elvégzett regisztrációt, illetve a tesztkörnyezetben
létrehozott technikai felhasználók és kulcsok sem használhatók az éles környezetben!

### A KAPCSOLÓDÁSHOZ IMPLEMENTÁLANDÓ TECHNOLÓGIÁK

- HTTPS – Biztonságos HTTP
- Webservice - Webszolgáltatás
- WADL – Webalkalmazás Leíró Nyelv
- REST API – Adatszolgáltatáshoz szükséges REST interfész
- XML – Kiterjeszthető Jelölő Nyelv
- Kódolási és titkosítási algoritmusok

### SZÁMLÁZÓ PROGRAMOKRA VONATKOZÓ TECHNIKAI KÖVETELMÉNYEK

**1)** Az adatszolgáltatási interfészt bármely számlázó program igénybe veheti, amely képes a jelen
specifikációban meghatározott HTTP üzenet küldésére és séma-konform XML összeállításra.

**2)** A számlázó programnak minden adatszolgáltatáskor a számlaadatok mellett az adózó technikai
felhasználójának hitelesítési adatait is küldenie kell. Az ehhez szükséges implementációt a számlázó
program szabadon meghatározhatja, azonban elvárás, hogy az adatszolgáltatás automatikusan, a

folyamaton belül külön emberi beavatkozás nélkül történjen.

**3)** A számlázó programnak a sikeres authentikáció elvégzéséhez a következő kódolási és titkosítási
algoritmusokat kell implementálnia:

- BASE64 encode/decode (RFC3548)
- SHA-512 encode (RFC6234)
- SHA3-512 encode (FIPS 202)
- AES-128 ECB decode (RFC3826)
- GZIP compress/decompress (RFC1952) (opcionális)


## 1 SZÁMLAADAT-SZOLGÁLTATÁS REST API ISMERTETÉSE

A számlaadat-szolgáltatás interfész a következő operációkat implementálja.

- **/manageAnnulment:** a technikai érvénytelenítés beküldésére szolgáló operáció
- **/manageInvoice:** a számlaadat-szolgáltatás beküldésre szolgáló operáció, ezen keresztül van
    lehetőség számla vagy módosító okirat adatait a NAV-nak beküldeni
- **/queryInvoiceChainDigest:** számlalánc kivonatos lekérdezésére szolgáló operáció
- **/queryInvoiceCheck:** sikeres számlaadat-szolgáltatás ellenőrzésére szolgáló operáció
- **/queryInvoiceData:** a számlaadatok teljes adattartalmú lekérdezésére szolgáló operáció
    számlasorszám alapján
- **/queryInvoiceDigest:** számlaadatok kivonatos lekérdezésére szolgáló operáció, kötelező és
    opcionális keresőparaméterek alapján
- **/queryTransactionList:** beküldött tranzakciók lekérdezése megadott időintervallum alapján
- **/queryTransactionStatus:** számlaadat-szolgáltatás és technikai érvénytelenítés feldolgozási
    eredményének lekérdezésére szolgáló operáció
- **/queryTaxpayer:** belföldi adószám validáló operáció, mely a számlakiállítás folyamatába
    építve képes a megadott adószám valódiságáról és érvényességéről a NAV adatbázisa alapján
    adatot szolgáltatni
- **/tokenExchange:** a számlaadat-szolgáltatás és a technikai érvénytelenítés beküldését
    megelőző egyszer használatos adatszolgáltatási token kiadását végző operáció

Az egyes operációk részletes működéséről, kérés-válasz struktúrájáról az „ **Üzleti operációk”** fejezet
tartalmaz információkat.

### 1.1 A SZÁMLAADAT-SZOLGÁLTATÁS FOLYAMATA

Az adatszolgáltatásra kötelezett adózó tetszőleges technikai felhasználójával a számlázó programnak
egyszer használatos adatszolgáltatási tokent kell igényelnie az erre szolgáló endpointon. A tokent
minden adatszolgáltatás előtt meg kell igényelni az adatszolgáltatás befogadásához. Az
adatszolgáltatási token adózóra szól, és a válaszban visszaadott időpontig – jelenleg a kiállítást
követően 5 percig – érvényes. Az érvényesség időtartama később változhat. Az adatszolgáltatási tokent
a rendszer a kérvényező technikai felhasználó cserekulcsával kódolva adja ki. A tokent felhasználni csak
akkor lehet, ha az a helyes, dekódolt értékkel kerül a szervernek visszaküldésre.

A számlák beküldése történhet egyenként vagy kötegelve. Egy adatszolgáltatás jelenlegi beküldési

limitje a sémaleíró szerint 100 számlára vonatkozó adatszolgáltatás, tehát egy HTTP requestben és egy
adatszolgáltatási tokennel egyszerre legfeljebb ennyi számlaadat-szolgáltatás küldhető be. Javasolt a
kliensoldali implementáció közben ezt az értéket paraméterezhetővé tenni. Az adatszolgáltatást a
token lejárati idejéig vagy a beküldési limit eléréséig - ha az előbb következik be - lehet beküldeni. A
token lejárati idejének megállapításában egzakt módon a szerveridő fog dönteni, ezért az esetleges
kliensoldali időeltérést érdemes a kötegelt beküldéskor figyelembe venni. Kötegelt beküldésként
elfogadott megoldás az is, ha az adatszolgáltatással érintett számla kiállításakor az adatszolgáltatási
token azonnal megkérésre kerül, azonban a token érvényességi idején belül kiállításra kerülő,
adatszolgáltatással érintett további számlák adatai összegyűjtésre kerülnek és ugyanazzal a tokennel,
a token érvényességi idején belül egyben kerülnek beküldésre.


A számlaadatok az adatszolgáltatási XML-en belül BASE64 formátumra kódolva kerülnek beágyazásra,

ezért a szerveroldali feldolgozás egy része (a kérés ellenőrzése és az authentikáció) szinkron módon,
míg a tényleges számlaadat feldolgozás már aszinkron módon történik meg.

A sikeresen befogadott adatszolgáltatásra a szerver tranzakcióazonosítót ad vissza. A kapott
tranzakcióazonosítóval a kliens tetszőleges számban és gyakorisággal lekérdezheti a tranzakció
feldolgozási státuszát. Ha a tranzakció feldolgozása megtörtént, a szerver a kérésben szereplő minden
számlára tételes feldolgozási eredményt ad vissza. Az egyes számlákra vonatkozó feldolgozási státusz
tartalmazhat:

- blokkoló hibát (olyan technikai vagy súlyos üzleti hibát, amely az adatszolgáltatás befogadását
    megakadályozza => ERROR típusú visszajelzés)
- figyelmeztetést (olyan üzleti hiba, amely az adatszolgáltatás befogadását nem blokkolja,
    azonban a számla, vagy az erről nyújtott adatszolgáltatás tartalmilag helytelen vagy helytelen
    lehet => WARN típusú visszajelzés)
- tájékoztató üzenetet (INFO típusú visszajelzés)
- nyugtaüzenetet (az adatszolgáltatás helyes és a befogadása megtörtént => OK típusú
    visszajelzés)

Az adatszolgáltatás addig nem tekinthető teljesítettnek, amíg a kliens az aszinkronfeldolgozás
sikerességéről meg nem győződött és az adott számlához tartozó nyugtaüzenetet meg nem kapta.

### 1.2 AZ XML-ÜZENETEK ÁLTALÁNOS FELÉPÍTÉSE

A számlaadat-szolgáltatás interfész az „ **Üzleti operációk”** fejezetben meghatározott számú root
element párral rendelkezik. A párok egyik része request, míg a másik része response típusú element,
és a vonatkozó operáció kérés-válasz struktúráját írja le.

### 1.3 BASICONLINEINVOICEREQUESTTYPE

Minden request element kötelező része a BasicOnlineInvoiceRequestType. A komplex típus header és
user csomópontjai a common.xsd-ből származnak, míg a software csomópont az invoiceApi.xsd-ben
szereplő típus. A típuson belül a header az üzenetváltással kapcsolatos általános technikai adatokat, a
user az authentikációval kapcsolatos adatokat, míg a software a műveletet végző számlázó program
adatait tartalmazza.


```
1. ábra A BasicOnlineInvoiceRequestType felépítése
```
#### 1.3.1 BasicHeaderType

A kérésekben a header elementet a BasicHeaderType implementálja.

## 2. ábra A BasicHeaderType felépítése

```
Tag Típus Kötelező Tartalma
requestId xs:string igen A kérés egyedi azonosítója
timestamp xs:dateTime igen A kérés kliensoldali időpontja UTC-ben
requestVersion xs:string igen A kérés verziószáma
headerVersion xs:string nem A header verziószáma
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
requestId EntityIdType [+a-zA-Z0-9_]{1,30} - -
```

```
timestamp GenericTimestampType \d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.\d{1,3})?Z
```
##### - -

```
requestVersion AtomicStringType15 - - -
headerVersion AtomicStringType15 - - -
```
**Leírás és kapcsolódó követelmények**

```
1) A requestId a kérés azonosítója. Értéke bármi lehet, ami a pattern szerint érvényes és az
egyediséget nem sérti. A requestId-nak - az adott adózó vonatkozásában és a timestamp tűrési
toleranciáján belül - kérésenként egyedinek kell lennie. Az egyediségbe minden olyan kérés
beleszámít amely átesik az egyediségvizsgálaton. Az egyediségbe minden sikeresen
feldolgozott kérés, valamint az INVALID_REQUEST_SIGNATURE és FORBIDDEN hibakóddal
elutasított kérés azonosítója számít bele. Ezen kérések azonosítói (requestId) nem
használhatók fel újra. A tag értéke beleszámít a requestSignature értékébe.
2) A timestamp a kérés beküldésének időpontja a kliens órája szerint. A timestamp-nak a
kérésben UTC időben és megfelelő formátum szerint kell érkeznie. Ez magyarországi időzóna
esetén:
```
```
DT (téli időszámítás) idején GMT+1 órát
DST (nyári időszámítás) esetén GMT+2 órát jelent. A tag értéke beleszámít a requestSignature
értékébe.
```
```
A timestamp értékének megengedett toleranciája a szerveridőhöz képest +- 1 nap.
```
```
A dátumokkal kapcsolatosan a „ Helyi idő konvertálása UTC időre” fejezet ad felvilágosítást.
```
```
3) A requestVersion a kérés struktúráját azonosítja. A későbbi interfészváltozások erre a tagra
lesznek visszavezetve, így a requestVersion a kérés és a válasz struktúráját, az ahhoz
kapcsolódó validációkat, ellenőrzéseket is meghatározza. Értéke a támogatott verzió
értékének megfelelően töltendő. Üzleti validáció vizsgálja az értékét, nincs xsd szintű enum
értékkészlete. Jelenleg elfogadott egyetlen érték: 3.
4) A headerVersion opcionális elem a kérésben. Arra szolgál, hogy ha a jövőben a kérések
struktúrája is alapvetően megváltozna, akkor a különböző struktúrák és az ahhoz kapcsolódó
ellenőrzések erre a tagra lesznek visszavezetve. Üzleti validáció vizsgálja az értékét, nincs xsd
szintű enum értékkészlete. Jelenleg elfogadott egyetlen érték: 1.
```
#### 1.3.2 UserHeaderType............................................................................................................................

A kérésekben a user elementet a UserHeaderType implementálja.


## 3. ábra A UserHeaderType felépítése......................................................................................................

```
Tag Típus Kötelező Tartalma
login xs:string igen A technikai felhasználó login neve
passwordHash xs:complexType igen A technikai felhasználó jelszóhash
értéke
taxNumber xs:string igen Azon adózó adószámának első 8 jegye,
aki az interfész szolgáltatását igénybe
veszi, és akihez a technikai felhasználó
tartozik
predecessorTaxNumber xs:string nem A jogelőd adózó adószámának első 8
jegye
requestSignature xs:complexType igen A kérés aláírásának hash értéke
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
login LoginType [a-zA-Z0-9]{6,15} - -
passwordHash CryptoType - - -
taxNumber TaxpayerIdType [0-9]{8} - -
predecessorTaxNumber TaxpayerIdType [0-9]{8} - -
requestSignature CryptoType - - -
```

**Leírás és kapcsolódó követelmények**

```
1) A login tag a technikai felhasználó nevét tartalmazza. A login nevet a rendszer véletlenszerűen
generálja a technikai felhasználó létrehozásakor 15 karakter hosszan. A login tag az
authentikáció egyik eleme.
2) A passwordHash a login tagban szereplő technikai felhasználó jelszavának nagybetűs SHA- 512
hash értéke. A literál jelszót a technikai felhasználót létrehozó elsődleges felhasználó adja meg
az Online Számla webfelületen. A passwordHash az authentikáció egyik eleme.
3) A taxNumber azon adózó adószámának első 8 száma, aki nevében a technikai felhasználó
tevékenykedik, és akihez tartozik. Csak magyar adószám az elfogadott.
4) A requestSignature a kliens által generált aláírása az üzenetnek. Minden kéréshez kötelezően
tartoznia kell egy requestSignature-nek. A szerver a kérésben szereplő adatok alapján elvégzi
a saját requestSignature számítását és csak akkor hajtja végre a kérést, ha a tárolt és kapott
adatokból a helyes érték ténylegesen előállítható. A requestSignature számításáról a
„requestSignature számítása” fejezet nyújt tájékoztatást.
5) A passwordHash és requestSignature komplex típusa a cryptoType. A típusnak kötelező
attribútuma a cryptoType, melyben a hash-képző algoritmust kell megadni. Üzleti validáció
vizsgálja az értékét, nincs xsd szintű enum értékkészlete.
6) A passwordHash tag a típusából adódóan kiegészül egy új, kötelező attribútummal: cryptoType
néven. Egyetlen elfogadott értéke: SHA- 512
7) A requestSignature tag a típusából adódóan kiegészül egy új, kötelező attribútummal:
cryptoType néven. Egyetlen elfogadott értéke: SHA3- 512
8) A predecessorTaxNumber amennyiben megadásra kerül, akkor validálásra kerül, hogy a
taxNumber tagben megadott adózóval jogelőd viszonyban áll-e. A jogelőd viszony rekurzívan
kerül ellenőrzésre, közvetett jogelőd megadása is elfogadott. A predecessorTaxNumber
megadása befolyásolja az operációk üzleti logikáját, ez alól kivételt képez és nincs kihatással az
alábbi operációk működésére: ManageInvoice, TokenExchange, QueryTaxpayer.
```

#### 1.3.3 SoftwareType

A kérésekben a software elementet a SoftwareType implementálja.

## 4. ábra A SoftwareType felépítése

```
Tag Típus Kötelező Tartalma
softwareId xs:string igen A számlázó program azonosítója
softwareName xs:string igen A számlázó program neve
softwareOperation xs:string igen A számlázó program működési típusa
softwareMainVersion xs:string igen A számlázó program fő verziója
softwareDevName xs:string igen A számlázó program fejlesztőjének
neve
softwareDevContact xs:string igen A számlázó program fejlesztőjének
működő email címe
softwareDevCountryCode xs:string nem A számlázó program fejlesztőjének
országkódja
softwareDevTaxNumber xs:string nem A számlázó program fejlesztőjének
adószáma
```

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
softwareId SoftwareIdType [0-9A-
Z\-]{18}
```
##### - -

```
softwareName SimpleText50NotBlankType .*[^\s].* - -
softwareOperation SoftwareOperationType LOCAL_SOFTWARE
ONLINE_SERVICE
```
##### -

```
softwareMainVersion SimpleText15NotBlankType .*[^\s].* - -
softwareDevName SimpleText512NotBlankType .*[^\s].* - -
softwareDevContact SimpleText200NotBlankType .*[^\s].* - -
softwareDevCountryCode CountryCodeType [A-Z]{2} - -
softwareDevTaxNumber SimpleText50NotBlankType .*[^\s].* - -
```
**Leírás és kapcsolódó követelmények**

A típus az adatszolgáltatást végző szoftverre vonatkozó információkat tartalmazza.

A softwareId az adott számlázó program azonosítására szolgáló 18 elemű karaktersorozat.

A softwareId képzésére vonatkozó ajánlás: az azonosító első két karaktere a szoftvert fejlesztő cég
országkódja ISO 3166 alpha-2 szabvány szerint. Az azonosító további karakterei a fejlesztő cég adószám
törzsszáma, megfelelő számú számjegyen (egyes országokban az adószám hosszúsága lényegesen
eltérhet a Magyarországon megszokott 8 számjegytől).

Az azonosító további karaktereit a Gyártó saját maga képezi meg úgy, hogy az azonosító egyedisége
biztosított legyen. A Gyártó dönthet arról, hogy egy adott szoftvertermék különböző verzióihoz, vagy

a különböző ügyfeleinél működő példányokhoz külön-külön azonosítót képez-e. Ugyanazon
szoftververzió ugyanazon példányának az adatszolgáltatáskor ugyanazt a softwareId-t kell közölnie
magáról.

Ha a számlázó program (vagy az egyes modulok) fejlesztésében több fejlesztő cég is részt vesz, akkor
megegyezéses alapon az egyik adatait szükséges megadni.

A softwareId-t és a fejlesztő cég e-mail címét (sofwareDevContact) az esetleges működési problémák
azonosítására, illetve a fejlesztő erről történő tájékoztatására használatos.

### 1.4 BASICONLINEINVOICERESPONSETYPE

Minden response element kötelező része a BasicOnlineInvoiceResponseType. A komplex típus header
és user csomópontjai a common.xsd-ből származnak, míg a software csomópont az invoiceApi.xsd-ben
szereplő típus. A típuson belül a header a válasz tranzakcionális adatait, a result a feldolgozás
eredményét, míg a software a műveletet végző számlázó program adatait tartalmazza.

A válaszban adott header és software szerkezetileg és tartalmilag mindig meg fog egyezni a kérésben
szereplő header és software tagek adataival.


## 5. ábra A BasicOnlineInvoiceResponseType felépítése

#### 1.4.1 BasicResultType

A válaszokban a feldolgozási eredményt a BasicResultType implementálja.

## 6. ábra A BasicResultType felépítése

```
Tag Típus Kötelező Tartalma
funcCode xs:string igen A feldolgozás eredménye
errorCode xs:string nem A feldolgozás hibakódja
message xs:string nem A feldolgozási eredményhez vagy
hibakódhoz tartozó szöveges üzenet
notification/notificationCode xs:string nem Értesítés kód
notification/notificationText xs:string nem Értesítés szöveg
```

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
funcCode FunctionCodeType - OK
ERROR
```
##### -

```
errorCode SimpleText50NotBlankType .*[^\s].* - -
message SimpleText1024NotBlankType .*[^\s].* - -
notification/
notificationCode
```
```
SimpleText1 00 NotBlankType .*[^\s].* - -
```
```
notification/notificationText SimpleText1024NotBlankType .*[^\s].* - -
```
**Leírás és kapcsolódó követelmények**

```
1) A funcCode a szerver által adott státusz a requestben szereplő művelet végrehajtására. Az
értelmezése az üzleti operációk szerint eltérő lehet, mindig a teljes válasszal együtt
értelmezendő!
2) Az errodCode akkor kerül visszaadásra, ha a funcCode értéke ERROR volt. A hiba egyedi kódját
tartalmazza, a kliens oldalon ezt a taget lehet használni a hibaüzenet mappelésére. Az
errorCode értékkészletéről a „ HIBAKEZELÉS” fejezetben lévő hibakód táblázat tájékoztat.
3) A message opcionális szöveges üzenet, ami a funcCode-ot vagy az errorCode-ot kíséri. Az
emberi megértést segíti olvasható üzenet közvetítésével.
4) A notification csomópontot a NAV a jövőben egyéb, API hívásokban értelmezhető tájékoztató
üzenetek közlésére fogja használni, kulcs-érték struktúrában.
```
### 1.5 A REQUESTSIGNATURE SZÁMÍTÁSA

A requestSignature az interfész-authentikáció egyik fő eleme. A szerepe, hogy illetéktelenek ne
tudjanak a rendszerben változtatásokat végrehajtani. A hash értéket a szerver oldal minden operáció
minden kérésénél ellenőrzi, és csak akkor hajtja végre a műveletet, ha a tárolt és kapott adatokból a
helyes érték ténylegesen előállítható.

#### 1.5.1 Számítás manageInvoice és manageAnnulment operáció esetén

A requestSignature alapját manageInvoice és manageAnnulment operáció esetén a requestSignature
egy parciális hitelesítésből, illetve 1-100 közötti index hash értékek összefűzéséből és további SHA3-
512 hash műveletből számítódik. A parciális hitelesítést a következő értékek összefűzéséből lehet

megállapítani:

- a requestId értéke
- a timestamp tag értéke YYYYMMDDhhmmss maszkkal, UTC időben
- a technikai felhasználó aláírókulcsának literál értéke

Az összefűzéskor a timestamp maszkoláshoz ki kell venni a dátum- és időpontszeparátorokat, valamint
az időzónát.

Az index hash értékeket az egyes indexek alatt álló operation és base64 tartalom összefűzését követő
nagybetűs SHA3- 512 hash értékéből lehet megállapítani:

- invoiceOperation vagy annulmentOperation literál értéke
- az invoiceData vagy invoiceAnnulment tagban található base64 tartalom


A kiszámított index hash-eket a parciális hash mögé kell fűzni az indexek által leírt sorrendben. Az így

és sorrendben konkatenált string nagybetűs SHA 3 - 512 hash eredménye lesz a requestSignature értéke.

Egy fiktív példa request adatai:

- requestId = TSTKFT1222564
- timestamp = 201 7 - 12 - 30 T1 8 :25:45.000Z
- a technikai felhasználó aláírókulcsa = ce-8f5e-215119fa7dd621DLMRHRLH2S
- az 1-es indexen lévő számlaadatok
    o invoiceOperation = CREATE
    o invoiceData = QWJjZDEyMzQ=
- a 2-es indexen lévő számlaadatok
    o invoiceOperation = MODIFY
    o invoiceData = RGNiYTQzMjE=
- a parciális hitelesítés értéke = TSTKFT122256420171230182545ce-8f5e-
    215119fa7dd621DLMRHRLH2S
- az első index hash =
    o hash alapja = CREATEQWJjZDEyMzQ=
    o lowercase hash =
       4317798460962869bc67f07c48ea7e4a3afa301513ceb87b8eb94ecf92bc220a89c480f
       87f0860e85e29a3b6c0463d4f29712c5ad48104a6486ce839dc2f24cb
    o uppercase hash =
       4317798460962869BC67F07C48EA7E4A3AFA301513CEB87B8EB94ECF92BC220A89C
       480F87F0860E85E29A3B6C0463D4F29712C5AD48104A6486CE839DC2F24CB
- a második index hash =
    o hash alapja = MODIFYRGNiYTQzMjE=
    o lowercase hash =
       a881218238933f6ffb9e167445cb4daa9749bcf484fde48ab7649fd25e8b634a4736a65
       a7c4a8e2831119f739837e006566f97370415aad55e268605206f2a6c
    o uppercase hash =
       A881218238933F6FFB9E167445CB4DAA9749BCF484FDE48AB7649FD25E8B634A473
       6A65A7C4A8E2831119F739837E006566F97370415AAD55E268605206F2A6C

A teljes requestSignature alapja így:

TSTKFT1222564 20171230182545 ce-8f5e-
215119fa7dd621DLMRHRLH2S4317798460962869BC67F07C48EA7E4A3AFA301513CEB87B8EB94ECF

92BC220A89C480F87F0860E85E29A3B6C0463D4F29712C5AD48104A6486CE839DC2F24CBA881218
238933F6FFB9E167445CB4DAA9749BCF484FDE48AB7649FD25E8B634A4736A65A7C4A8E2831119F7
39837E006566F97370415AAD55E268605206F2A6C

A requestSignature értéke SHA 3 - 512 hashelést és nagybetűsítést követően:

60BC80609EE3B8F42FE904200A49A1921A1DADA08D55319ACD40C59F626514B74EEA49011D37260
0A10DBCF8199D590DA9C2841D987308F2D83DAE17C2470C42


A requestSignature tag a típusából adódóan kiegészül egy új, kötelező attribútummal: cryptoType

néven. Egyetlen elfogadott értéke: SHA3- 512

#### 1.5.2 Számítás manageInvoice és manageAnnulment operáción kívül

A manageInvoice és manageAnnulment operáció kivételével minden más operációban – mivel ezekben
nem merül fel adatbeküldés – a requestSignature egyenlő a parciális hitelesítés SHA3-512 hash
értékével, amelyet a következő értékek összefűzéséből lehet megállapítani:

- a requestId értéke
- a timestamp tag értéke yyyyMMddHHmmss maszkkal, UTC időben
- a technikai felhasználó aláírókulcsának literál értéke

Az így és sorrendben konkatenált string nagybetűs SHA 3 - 512 hash eredménye lesz a requestSignature
értéke.

A requestSignature tag a típusából adódóan kiegészül egy új, kötelező attribútummal: cryptoType
néven. Egyetlen elfogadott értéke: SHA3- 512

#### 1.5.3 Helyi idő konvertálása UTC időre

A helyes kliensoldali requestSignature előállításához a helyi időt UTC időre kell konvertálni. Ez úgy
tehető meg, hogy a kliensnél érvényes időzóna szerinti helyi idő értékéhez hozzá kell adni vagy ki kell
vonni annyi egész órát, amennyivel az időzóna az UTC középidőtől eltér. Amelyik időzónában van
téli/nyári időszámítás, ott a kivonásnál/összeadásnál erre is figyelni kell.

A helyes UTC idő megállapításához az „ **Önellenőrzés”** fejezet nyújt további információkat.

### 1.6 A SZOLGÁLTATÁS TECHNIKAI LEÍRÁSA

Az /invoiceService egy RESTful típusú állapottalan (stateless) webszerviz. A szolgáltatás technikai
jellemzői a következők.

#### 1.6.1 Általános technikai adatok

A szolgáltatásnak HTTP POST metódussal kell a body-ban a megfelelő XML kérést elküldeni, melyre a
szerver a response body-ban XML-t ad vissza. A kérésben az elvégzendő műveletet a hívó a megfelelő

endpoint címzésével és a megfelelő struktúrájú XML összeállításával definiálja. A kérés helyességétől
függően a szerver vagy üzleti XML választ, vagy csupán standard HTTP választ ad vissza.

**Context root:**

/invoiceService/v 3

**XSD:**

common.xsd
invoiceBase.xsd
invoiceApi.xsd
invoiceData.xsd
invoiceAnnulment.xsd


Az általános elemek definíciója a common.xsd-ben, illetve az invoiceBase-xsd-ben található. A

kommunikációhoz használt elemek definíciója az invoiceApi sémaleíróban, a számlák üzleti modellje
és elemei definíciója az invoiceData sémaleíróban, míg a technikai érvénytelenítés adatainak
definíciója az invoiceAnnulment sémaleíróban található.

#### 1.6.2 Erőforrások..................................................................................................................................

/manageAnnulment
/manageInvoice
/queryInvoiceChainDigest
/queryInvoiceCheck
/queryInvoiceData
/queryInvoiceDigest
/queryTransactionList
/queryTransactionStatus
/queryTaxpayer
/tokenExchange

#### 1.6.3 HTTP fejlécek

A kérésben a következő HTTP fejléc mezőket kötelező megadni:

content-type=application/xml
accept=application/xml

Az adatbázisba mentés és a válasz a kérésben megadott encodingtól függetlenül mindig UTF-8 lesz,
ezért javasolt a kérésben is ennek a kódolásnak a használata.

#### 1.6.4 HTTP státuszkódok

A szolgáltatás a hívónak helyes kérés esetén minden esetben HTTP 200-as választ ad. Ez nem feltétlenül
jelzi, hogy a megfogalmazott kérés tartalmán az üzleti végrehajtás sikeresen lefutott, csak azt, hogy a
kérés informatikai tekintetben jól formázott volt, a hívott erőforrás el tudta olvasni, be tudta fogadni.
A mivel a szolgáltatás által kezelt hibakódok fel vannak mappelve, így az azokra visszaadott hibakód is
sikeres válasznak számít. Tehát egy HTTP 200-as válaszban is lehet hibakódokat tartalmazó üzenet.

A helytelen kérés vagy egyéb technikai hiba esetén visszaadott eredményekről a „ **Hibakezelés”**
fejezetben lévő hibakód táblázat tájékoztat.

#### 1.6.5 Tömörítés és méretkorlát

A szolgáltatásnak küldött HTTP POST body mérete nem haladhatja meg a 10 megabájtot egyik
operációban sem.

Ha az adatszolgáltatásban ennél nagyobb belső XML-t kell elküldeni, akkor a számla XML-t a BASE64
kódolást megelőzően tömöríteni kell. A tömörítés a GZIP formátum szerint lehetséges. A tömörített
tartalmak kezelésekor legfejlebb 15 megabájtos tömörítetlen méretet enged meg a szerver
számlánként. A szerveroldali BASE64 dekódolás után, ha a belső számla XML tömörítetlen mérete

meghaladja a szerveroldali toleranciát, az adott számla feldolgozása technikai hibával eldobásra kerül.
Kérjük, hogy a kliensoldali tömörítéskor a leggyorsabb, legkevésbé tömörítő, 1-es compression ratio
kerüljön alkalmazásra („gzip -1 [FILE]”)! Azon kérések, amik ennél nagyobb tömörítési rátát
alkalmaznak, automatikusan a feldolgozási sor legvégére kerülnek.

A tömörítve beküldött számlákat a /queryInvoiceData operációban a szerver is mindig tömörítetten
adja vissza (a nem tömörítetteket pedig hasonlóképp mindig tömörítetlenül). Így, a tömörítés


implementálása opcionális ugyan, de ha az adózó a saját üzleti folyamataiban használja a bejövő

számlák lekérdezését (például gépi vagy gépileg segített könyvelést valósít meg), akkor javasolt
felkészíteni az adott rendszert a tömörített tartalmú válasz fogadására.

Azon számlák esetén, amelyek a tömörítés után is méretkorláton kívül esnek, lehetséges a tételek
adattartalmának összevonása. Részletes leírás a „ **Nagyméretű számlákról történő adatszolgáltatás”**
fejezetben található az eljárással kapcsolatban.

#### 1.6.6 Válaszidő, timeout

A szerver jellemzően 200ms alatti válaszidőkkel szolgál ki. A szinkronhívások blokkoló timeout értéke

5000 ms. Kérjük, hogy kliens oldalon a fenti értéket meghaladó válaszidőt kezeljék csak
időtúllépésként!

Az abszolút timeout értéke 60 sec. Ha egy adatszolgáltatásra nem érkezik válasz a 60 másodperces
timeout miatt, még nem jelenti a beküldés sikertelenségét.

Az ilyen válasz nélküli (timeout) szélsőséges esetek utókövetésére használható a queryTransactionList
operáció. A lekérdezés segítségével lekérdezhető az összes, sikeresen befogadott adatszolgáltatás a
megadott időintervallumban. Ha kliens oldalon valamelyik beküldött adatszolgáltatáshoz nincs meg a
válaszként kapott tranzakcióazonosító, akkor így azonosítható be. A lekérdező operáció részletes
leírása a „ **A /queryTransactionList** operáció **”** fejezetben található. Ha az adatszolgáltatás ilyen esetben
nem található a lekérdező operáció válaszában, akkor megismételhető a beküldés.

#### 1.6.7 Szerveróra, NTP

A szerver az időbeállításokat egy zárt, a külvilág számára nem hozzáférhető NTP szervertől kapja. Kliens
oldalon a szerveridőhöz szinkronizálás nem követelmény, azonban opcionálisan a következő
időszinkronizáció lehetséges: [http://www.pool.ntp.org/zone/hu](http://www.pool.ntp.org/zone/hu) (a csatlakozáshoz NTP kliensre van
szükség).

#### 1.6.8 Karbantartási mód

A szerver kétfajta karbantartási üzemmódban futhat. Az első jellemzően olyan verzióváltások esetén
lesz alkalmazva, amelynek feltétele, hogy ne legyen a rendszerben függőben lévő, feldolgozatlan
adatszolgálatás (pl: sémaváltozás, új kötelező validációk stb.). Ez az üzemmód a számlabejelentő
interfészen csak a tokenkérést fékezi, az interfész többi operációja továbbra is kiszolgál. Ez lehetővé
teszi, hogy a már kikért tokenek felhasználásra kerüljenek, de azok lejártával újabb
adatszolgáltatásokat nem lehet a rendszerbe beküldeni. A másik mód az interfész összes operációjának
működését fékezi. Karbantartási módban a „ **Hibakezelés”** fejezetben jelzett hiba kerül visszaadásra.

#### 1.6.9 Verziókezelés

A szolgáltatás szempontjából a verziót az URL, míg az üzleti adatmodell szempontjából a verziót a HTTP
body-ban megadott requestVersion tag értéke definiálja.

Főverziónak azon verziókat nevezzük, amelyekben az üzleti adatmodell visszafelé kompatibilitása az
egyes verziók között nem biztosítható. Kisverziónak azok a verziók számítanak, amelyekben adott
főverzión belül az üzleti adatok kompatibilisek maradnak.

Új főverzióhoz minden esetben új URL-ek és az új XML namespace tartozik. A kisverziók öröklik annak
a főverziónak az URL és namespace adatait, amelynek a részét képezik.


```
Tekintettel arra, hogy az átállási idő alatt az XML API két eltérő verziója is egymás mellett működik,
szükséges néhány verziókkal kapcsolatos összefüggést általánosságban is kikötni. Ezen összefüggések
a következők.
```
```
1) Az egyes főverziók tokenjei között nincs átjárás. (például létező 2 .x-es tokennel nem lehet 3 .x-
es számlaadatot beküldeni és fordítva sem)
2) Minden beküldött /manageInvoice és /manageAnnulment kérés feldolgozási státuszát
minimum a beküldéshez tartozó requestVersion értékű lekérdezéssel lehet csak lekérdezni,
alacsonyabbal sosem (például 2.0-es /manageInvoice feldolgozási státusza lekérdezhető 3 .0-
ás lekérdezéssel, fordítva viszont nem).
3) Minden sikeresen befogadott számla lekérdezhető teljes adattartalmában, ha a lekérdezés
requestVersion értéke azonos az aktuálisan támogatott főverzió értékével. Az egyes főverziók
között viszont alulról nincs átjárás, az alacsonyabb verziók csak a saját beküldéseiket
kereshetik (például 3 .x-es lekérdezések rálátnak teljeskörűen az 1.x, 2 .x és 3 .x-es
számlaadatokra is, míg a 2 .x-es lekérdezések a 3.x-es adataikat nem látják).
4) Minden alapszámlához csak olyan módosító vagy sztornó számláról szóló adatszolgáltatás
fűzhető, amelynek a requestVersion értéke minimum azonos az alapszámla requestVersion
értékével, alacsonyabbal sosem (például 2.0-ás alapszámlához beküldhető 3 .0-ás sztornó
adatszolgáltatás, fordítva viszont nem).
```
#### 1.6.10 Karakterkonverzió

```
A beküldött számlák mentésekor 2.0-ás xsd verzióig bezárólag az egyes tagekben szereplő adatokon a
rendszer uppercase konverziót végzett, melyek a következők voltak:
```
```
o supplierName, customerName, fiscalRepresentativeName, obligatedName
o minden AddressType típus által leírt cím minden eleme
o minden productCodeOwnValue tag értéke
o lineDescription
o unitOfMeasure
o discountDescription
o minden vatExemption tag értéke
o brand, serialNum, engineNum
o minden EkaerIdsType típus által leírt EKÁER szám
```
```
A 2.0-ás vagy kisebb verziójú számlák esetén a válaszban a fenti mezők a beküldött értéktől függetlenül
mindig uppercase formátumban kerülnek visszaadásra. A 3.0 verziótól kezdve ez az uppercase
konverzió kivezetésre kerül.
```
#### 1.6.11 Forgalomkorlátozás

```
A forgalomkorlátozás az XML API meghatározott végpontjait érinti. A forgalomkorlátozás alá eső
végponton minden kliens 1 adott IP címről másodpercenként 1 kérést küldhet be a szervernek. Minden
további kérés +4000 ms késleltetést kap a hálózati rétegben, az előző kérés késleltetéséhez számítva.
Ha 1 kliens várakozó kérései elérik a 60 másodperces küszöbértéket, minden 60 másodpercnél tovább
várakozó kérés terminálásra kerül szerver oldalról közvetlenül a beérkezést követően. A
forgalomkorlátozás alá eső végpontok listája:
```
- v1-es végpontok
    o /tokenExchange


```
o /manageInvoice
o /queryInvoiceData
o /queryInvoiceStatus
o /queryTaxpayer
```
### 1.7 AZ API SÉMALEÍRÓ FŐBB ELEMEI

A felsorolt element node-ok a szolgáltatás fontosabb és összetettebb csomópontjai. Jellemzően több
atomi elemet és complex type node-ot tartalmaznak magukon belül, hogy az operációk által használt
kérés- és válaszüzenetek rugalmasan felépíthetők legyenek.

**Request elemek**

ManageAnnulmentRequest - a POST /manageAnnulment REST operáció kérésének root elementje
ManageInvoiceRequest – a POST /manageInvoice REST operáció kérésének root elementje
QueryInvoiceChainDigestRequest - a POST /queryInvoiceChainDigest REST operáció kérésének root
elementje
QueryInvoiceCheckRequest - a POST /queryInvoiceCheck REST operáció kérésének root elementje
QueryInvoiceDataRequest – a POST /queryInvoiceData REST operáció kérésének root elementje
QueryInvoiceDigestRequest - a POST /queryInvoiceDigest REST operáció kérésének root elementje
QueryTransactionListRequest – a POST /queryTransactionList REST operáció kérésének root
elementje
QueryTransactionStatusRequest – a POST /queryTransactionStatus REST operáció kérésének root
elementje
QueryTaxpayerRequest – a POST /queryTaxpayer REST operáció kérésének root elementje
TokenExchangeRequest – a POST /tokenExchange REST operáció kérésének root elementje

**Response elemek**

ManageAnnulmentResponse - a POST /manageAnnulment REST operáció válaszának root elementje
ManageInvoiceResponse – a POST /manageInvoice REST operáció válaszának root elementje
QueryInvoiceChainDigestResponse - a POST /queryInvoiceChainDigest REST operáció válaszának root
elementje
QueryInvoiceCheckResponse - a POST /queryInvoiceCheck REST operáció válaszának root elementje
QueryInvoiceDataResponse – a POST /queryInvoiceData REST operáció válaszának root elementje
QueryInvoiceDigestResponse – a POST / queryInvoiceDigest REST operáció válaszának root elementje
QueryTransactionListResponse – a POST /queryTransactionList REST operáció válaszának root
elementje
QueryTransactionStatusResponse – a POST /queryTransactionStatus REST operáció válaszának root
elementjeQueryTaxpayerResponse – a POST /queryTaxpayer REST operáció válaszának root
elementje
TokenExchangeResponse – a POST /tokenExchange REST operáció válaszának root elementje

### 1.8 ÜZLETI OPERÁCIÓK

Jelen fejezetben a számlaadat-szolgáltatás interfész funkcionalitásait megvalósító /invoiceService
szolgáltatás technikai leírása és az egyes operációkat és kérés-válasz struktúrákat leíró root elementek

bemutatása található.


#### 1.8.1 A /manageAnnulment operáció

A /manageAnnulment operáció a technikai érvénytelenítések beküldésére szolgáló operáció. Technikai
érvénytelenítés csak olyan adatszolgáltatásra küldhető, amelynek a befogadása a NAV oldalon DONE
státusszal megtörtént.

**1.8.1.1 ManageAnnulmentRequest**
A /manageAnnulment operáció kérésének struktúráját a ManageAnnulmentRequest element
tartalmazza.

## 7. ábra A ManageAnnulmentRequest felépítése

A típus a BasicOnlineInvoiceRequestType-ot terjeszti ki, így az abban foglalt elemeken kívül az
adatszolgáltatási tokent és egy listatípust tartalmaz, melyben a beküldendő technikai
érvénytelenítések adatai találhatók.

```
Tag Típus Kötelező Tartalma
exchangeToken xs:string igen Adatszolgáltatási token
index xs:int igen A technikai érvénytelenítés pozíciója a
kérésen belül
annulmentOperation xs:string igen A kért technikai érvénytelenítési
művelet megjelölése
invoiceAnnulment xs:base64Binary igen A technikai érvénytelenítés adatai
BASE64 kódolásban
```

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
exchangeToken SimpleText50NotBlankType .*[^\s].* - -
index InvoiceIndexType minInclusive = 1
maxInclusive =
100
```
##### - -

```
annulmentOperation ManageAnnulmentOperationType - ANNUL -
invoiceAnnulment - - - -
```
**Leírás és kapcsolódó követelmények**

```
1) Az exchangeToken tagban az adatbeküldést megelőzően a /tokenExchange operációban
igényelt token dekódolt értékét kell küldeni. A dekódolást a tokent igénylő technikai
felhasználó cserekulcsával kell elvégezni, AES-128 ECB titkosítási algoritmus alapján. A küldés
időpontjában a tokennek a szerver oldalon érvényesnek kell lennie, lejárt vagy nem helyesen
dekódolt tokennel adatszolgáltatás nem teljesíthető. Mivel a token nem technikai
felhasználóra, hanem adózóra szól, más technikai felhasználó által igényelt token az
adatszolgáltatásban felhasználható, feltéve, hogy a dekódolást annak a felhasználónak a
cserekulcsával végezték, aki a tokent korábban igényelte.
2) Az index egy adott adatbeküldés pozícióját jelöli a kérésen belül. A feldolgozási válasz ez
alapján lesz összekapcsolható az egyes adatbeküldésekkel. Mivel az index implicit befolyásolja
a requestSignature generálását, így elvárás, hogy az sorfolytonosan növekvő és hézagmentes
legyen. A nem ennek megfelelően indexelt kérések feldolgozását a szerver visszautasítja.
3) Az annulmentOperation tag jelöli, hogy az adott pozíción lévő adatbeküldés technikai
érvénytelenítésnek számít-e (a tag jelenleg csak egy értéket vehet fel). A technikai
érvénytelenítés részletszabályairól a „ Korábbi adatszolgáltatás technikai érvénytelenítése”
fejezet tartalmaz információkat.
4) Az invoiceAnnulment tag egy különálló XML-t tartalmaz, BASE64 formátumra elkódolva. A
belül lévő XML-nek jól formázottnak és séma-konformnak kell lennie az invoiceAnnulment.xsd-
re. A technikai érvénytelenítés feldolgozása aszinkron módon történik, a feldolgozási
eredmény lekérése a /queryTransactionStatus operációban lehetséges.
5) A ManageAnnulmentRequest/user/ predecessorTaxNumber tag megadása esetén a technikai
érvénytelenítési kérést az alkalmazás a jogelődre vonatkozóan dolgozza fel. Vagyis a technikai
érvénytelenítés során megadott számlaszám (InvoiceAnnulment/annulmentReference)
azonosítása a megadott jogelődre történik.
```
1.8.1.2 ManageAnnulmentResponse
A /manageAnnulment operáció válaszának struktúráját a ManageAnnulmentResponse element
tartalmazza.


## 8. ábra A ManageAnnulmentResponse felépítése

A típus a TransactionResponseType-ot terjeszti ki. A típus a BasicOnlineInvoiceResponseType-on kívül
egy tranzakcióazonosítót tartalmaz.

```
Tag Típus Kötelező Tartalma
transactionId xs:string igen A befogadott adatszolgáltatás azonosítója
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
transactionId EntityIdType [+a-zA-Z0-9_]{1,30} - -
```
**Leírás és kapcsolódó követelmények**

```
1) A transactionId egy adatbeküldést (számlaadat-szolgáltatás vagy technikai érvénytelenítés)
tartalmazó kérés egyedi, szerveroldali azonosítója. Tranzakcióazonosító csak akkor kerül
kiadásra, ha a kérés szinkron feldolgozása sikeresen megtörtént. Azonban a
tranzakcióazonosító kiadása önmagában nem jelenti a feldolgozás sikerességét is, hiszen a
beküldött adatok vizsgálata és feldolgozása csak ezt követően fog megtörténni. Az
adatbeküldés feldolgozási eredményét ezzel a tranzakcióazonosítóval lehet lekérdezni a
/queryTransactionStatus operációban.
```
#### 1.8.2 A /manageInvoice operáció

A /manageInvoice a számlaadat-szolgáltatás beküldésére szolgáló operáció, ezen keresztül van
lehetőség számla, módosító vagy sztornó számlaadat-szolgáltatást a NAV-nak beküldeni.

**1.8.2.1 ManageInvoiceRequest**
A /manageInvoice operáció kérésének struktúráját a ManageInvoiceRequest element tartalmazza.


## 9. ábra A ManageInvoiceRequest felépítése

A típus a BasicOnlineInvoiceRequestType-ot terjeszti ki, így az abban foglalt elemeken kívül az
adatszolgáltatási tokent és egy listatípust tartalmaz, melyben a beküldendő üzleti számlaadatok
találhatók.

```
Tag Típus Kötelező Tartalma
exchangeToken xs:string igen Adatszolgáltatási token
compressedContent xs:boolean igen Tömörített tartalom jelzése a
feldolgozási folyamat számára
index xs:int igen A számla pozíciója a kérésen belül
invoiceOperation xs:string igen A számlaművelet megjelölése
invoiceData xs:base64Binary igen A számla adatai BASE64 kódolásban
electronicInvoiceHash xs:string nem Számlaállomány hash-lenyomata
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
exchangeToken SimpleText50NotBlankType .*[^\s].* - -
compressedContent - - - false
```

```
index InvoiceIndexType minInclusive = 1
maxInclusive =
100
```
##### - -

```
invoiceOperation ManageInvoiceOperationType - CREATE
MODIFY
STORNO
```
##### -

```
invoiceData - - - -
electronicInvoiceHash CryptoType .*[^\s].* - -
```
**Leírás és kapcsolódó követelmények**

```
1) Az exchangeToken tagban az adatszolgáltatást megelőzően a /tokenExchange operációban
igényelt token dekódolt értékét kell küldeni. A dekódolást a tokent igénylő technikai
felhasználó cserekulcsával kell elvégezni, AES-128 ECB titkosítási algoritmus alapján. A küldés
időpontjában a tokennek a szerver oldalon érvényesnek kell lennie, lejárt vagy nem helyesen
dekódolt tokennel adatszolgáltatás nem teljesíthető. Mivel a token nem technikai
felhasználóra, hanem adózóra szól, más technikai felhasználó által igényelt token az
adatszolgáltatásban felhasználható, feltéve, hogy a dekódolást annak a felhasználónak a
cserekulcsával végezték, aki a tokent korábban igényelte.
2) A compressedContent tag annak a jelölője, hogy a kérésben szereplő számlaadat-
szolgáltatások tömörített XML-t tartalmaznak-e. Mivel a tag kérés szintű, a kérésben szereplő
adatszolgáltatásoknak egységesen kell vagy tömörített, vagy tömörítetlen formátumban
szerepelniük. A tömörítés pontos alkalmazásáról a „ Tömörítés és méretkorlát” fejezet ad
tájékoztatást.
3) Az index egy adott számlára vonatkozó adatszolgáltatás pozícióját jelöli a kérésen belül. A
feldolgozási válasz ez alapján lesz összekapcsolható az egyes számlaadat-szolgáltatásokkal.
Mivel az index implicit befolyásolja a requestSignature generálását, így elvárás, hogy az
sorfolytonosan növekvő és hézagmentes legyen. A nem ennek megfelelően indexelt kérések
feldolgozását a szerver visszautasítja.
4) Az invoiceOperation tag jelöli, hogy az adott pozíción lévő számla számlának, módosító
számlának, sztornó számlának tekintendő-e. A módosítás, sztornírozás és az érvénytelenítés
részletszabályairól a z „Adatszolgáltatás számlával egy tekintet alá eső okiratokról” fejezet
tartalmaz információkat.
5) Az invoiceData tag egy különálló XML-t tartalmaz, BASE64 formátumra elkódolva. A belül lévő
XML-nek jól formázottnak és séma-konformnak kell lennie az invoiceData.xsd-re. A
számlaadatok feldolgozása aszinkron módon történik, a feldolgozási eredmény lekérése a
/queryTransactionStatus operációban lehetséges.
6) Az electronicInvoiceHash tag az InvoiceOperationType komplex típusban szerepel. A hash-
lenyomat megadása opcionális sémaszinten, azonban completenessIndicator jelölő true
értéke esetén kötelező. Az electronicInvoiceHash tag a típusából adódóan kiegészül egy új,
kötelező attibútummal: cryptoType néven. Elfogadott értéke az adott számla
completenessIndicator (adatszolgáltatás maga a számla) tag értékétől függ.
Ha a completenessIndicator értéke true, az egyetlen elfogadott érték az SHA3-512. Ilyen
esetben a hash értékének nagybetűs változatát kell beküldeni. Ha a completenessIndicator
jelölő értéke false, az elfogadott értékek: SHA3-512, SHA-256.
7) A ManageInvoiceRequest/user/ predecessorTaxNumber tag megadása esetén validálásra
kerül a jogelőd adószáma, azonban további hatása nincs az operációra.
```

**1.8.2.2 ManageInvoiceResponse**

A /manageInvoice operáció válaszának struktúráját a ManageInvoiceResponse element tartalmazza.

## 10. ábra A ManageInvoiceResponse felépítése

A típus a TransactionResponseType-ot terjeszti ki. A típus a BasicOnlineInvoiceResponseType-on kívül
egy tranzakcióazonosítót tartalmaz.

```
Tag Típus Kötelező Tartalma
transactionId xs:string igen A befogadott adatszolgáltatás azonosítója
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
transactionId EntityIdType [+a-zA-Z0-9_]{1,30} - -
```
**Leírás és kapcsolódó követelmények**

```
1) A transactionId egy adatbeküldést (számlaadat-szolgáltatás vagy technikai érvénytelenítés)
tartalmazó kérés egyedi, szerveroldali azonosítója. Tranzakcióazonosító csak akkor kerül
kiadásra, ha a kérés szinkron feldolgozása sikeresen megtörtént. Azonban a
tranzakcióazonosító kiadása önmagában nem jelenti a feldolgozás sikerességét is, hiszen a
beküldött adatok vizsgálata és feldolgozása csak ezt követően fog megtörténni. Az
adatbeküldés feldolgozási eredményét ezzel a tranzakcióazonosítóval lehet lekérdezni a
/queryTransactionStatus operációban.
```
#### 1.8.3 A /queryInvoiceChainDigest operáció

A /queryInvoiceChainDigest egy számlaszám alapján működő lekérdező operáció, amely a számlán
szereplő kiállító és a vevő oldaláról is használható. Az operáció a megadott keresőfeltételeknek
megfelelő, lapozható számlalistát ad vissza a válaszban. A lista elemei a megadott alapszámlához
tartozó számlalánc elemei. A válasz nem tartalmazza a számlák összes üzleti adatát, hanem csak egy
kivonatot (digest-et), elsősorban a módosításra és tételsorok számára vonatkozóan.


**1.8.3.1 QueryInvoiceChainDigestRequest**

A /queryInvoiceChainDigest operáció kérésének struktúráját a QueryInvoiceChainDigestRequest
element tartalmazza.

## 11. ábra A QueryInvoiceChainDigestRequest felépítése

A típus a BasicOnlineInvoiceRequestType-ot terjeszti ki, így az abban foglalt elemeken kívül kötelező
keresőparaméterként várja a keresendő alapszámla számát, a keresés irányát, illetve opcionálisan a
kiállító/vevő adószámát.

```
Tag Típus Kötelező Tartalma
page xs:int igen A lekérdezni kívánt lap száma
invoiceNumber xs:string igen A keresett számla száma
invoiceDirection xs:string igen A keresés iránya, a keresés elvégezhető
kiállítóként és vevőként is
taxNumber xs:string nem A kiállító/vevő adószáma
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
page RequestPageType minInclusive = 1 - -
invoiceNumber SimpleText50NotBlankType .*[^\s].* - -
invoiceDirection InvoiceDirectionType - OUTBOUND
INBOUND
```
##### -

```
taxNumber TaxpayerIdType [0-9]{8} - -
```

**Leírás és kapcsolódó követelmények**

```
1) Az invoiceNumber tagban a keresett alapszámla számát kell megadni. Az operáció fel van
készítve az előzmény nélküli módosítások listázására is, ezért nem követelmény, hogy a
megadott számlaszám ténylegesen létezzen is a rendszerben, de az előzmény nélküli módosító
számláknak hivatkozni kell a keresett értékre.
2) A keresés irányát az invoiceDirection tagban kell kötelezően jelölni. A keresés iránya lehet
kiállító oldali (OUTBOUND) vagy vevő oldali (INBOUND). Kiállítókénti keresés esetén a
lekérdezést végző technikai felhasználóhoz tartozó adószámnak kell szerepelnie a számlán a
kiállítói oldalon. Hasonlóképpen, vevőkénti keresés esetén a lekérdezést végző technikai
felhasználóhoz tartozó adószámnak kell szerepelnie a számlán a vevői oldalon. Azon számlák,
amelyek nem tartalmazzák a vevő adószámát, vevői oldalról nem kereshetők, csak a saját
kiállítói oldalukról.
3) A QueryInvoiceChainDigestRequest/user/ predecessorTaxNumber tag megadása esetén a
számlalánc tagok keresése a megadott jogelődnél történik.
```
**1.8.3.2 QueryInvoiceChainDigestResponse**
A /queryInvoiceChainDigest operáció válaszának struktúráját a QueryInvoiceChainDigestResponse
element tartalmazza.

## 12. ábra A QueryInvoiceChainDigestResponse felépítése


## 13. ábra Az InvoiceChainElementType felépítése

A típus a BasicOnlineInvoiceResponseType-ot terjeszti ki, így az abban foglalt elemeken kívül legalább
1 keresési találat esetén a számlalánc elemeinek kivonatos adatait tartalmazza. A kivonat a számlák


alapvető adatai mellett elsősorban a számlák sorainak sorszámát, illetve a módosításra vonatkozó

adatokat tartalmazza.

```
Tag Típus Kötelező Tartalma
currentPage xs:int igen A jelenleg lekérdezett lap értéke
availablePage xs:int igen Az elérhető legnagyobb lap értéke
```
invoiceChainElement/invoiceChainDigest szint

```
Tag Típus Kötelező Tartalma
invoiceNumber xs:string igen Számla vagy módosító okirat sorszáma -
Áfa tv. 169. § b) vagy 170. § (1) bek. b)
pont
batchIndex xs:int nem A módosító okirat sorszáma kötegelt
módosítás esetén
invoiceOperation xs:string igen Számlaművelet
supplierTaxNumber xs:string igen Számla kiállítójának adószáma
customerTaxNumber xs:string nem A vevő adószáma
insDate xs:dateTime igen A számlaadat-szolgáltatás mentésének
időpontja
originalRequestVersion xs:string igen Az adatszolgáltatás requestVersion értéke
```
invoiceChainElement/invoiceLines szint

```
Tag Típus Kötelező Tartalma
maxLineNumber xs:nonNegativeInteger igen A sorok száma közül a
legmagasabb, amit a
számla tartalmaz
newCreatedLines/lineNumberIntervalStart xs:nonNegativeInteger igen Hozzáadott számla sor
intervallum kezdete
newCreatedLines/lineNumberIntervalEnd xs:nonNegativeInteger igen Hozzáadott számla sor
intervallum inkluzív vége
```
invoiceChainElement/invoiceReferenceData szint

```
Tag Típus Kötelező Tartalma
originalInvoiceNumber xs:string igen Az eredeti számla sorszáma,
amelyre a módosítás
vonatkozik
modifyWithoutMaster xs:boolean igen Alapszámla nélküli módosítás
jelölése
modificationTimestamp xs:dateTime igen A módosítás időbélyege
modificationIndex xs:int igen A számlára vonatkozó
módosító okirat egyedi
sorszáma
```

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
currentPage ResponsePageType minInclusive = 0 - -
availablePage ResponsePageType minInclusive = 0 - -
```
invoiceChainElement/invoiceChainDigest szint

```
Tag SimpleType Pattern Enum Defau
lt
invoiceNumber SimpleText50NotBlankTy
pe
```
```
.*[^\s].* - -
```
```
batchIndex InvoiceUnboundedIndex
Type
```
```
minInclusive = 1 - -
```
```
invoiceOperation ManageInvoiceOperation
Type
```
##### - CREAT

##### E

##### MODIF

##### Y

##### STORN

##### O

```
supplierTaxNumbe
r
```
```
TaxpayerIdType [0-9]{8} - -
```
```
customerTaxNumb
er
```
```
TaxpayerIdType [0-9]{8} - -
```
```
insDate InvoiceTimestampType \d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.\d{1,3})?ZminI
nclusive = 2010 - 01 - 01T00:00:00Z
```
##### - -

```
originalRequestVer
sion
```
```
OriginalRequestVersionT
ype
```
##### - 1.0

##### 1.1

##### 2.0

##### 3.0

##### -

invoiceChainElement/invoiceLines szint

```
Tag SimpleType Pattern Enum Default
maxLineNumber LineNumberType - - -
newCreatedLines/lineNumberIntervalStart LineNumberType - - -
newCreatedLines/lineNumberIntervalEnd LineNumberType - - -
```
invoiceChainElement/invoiceReferenceData szint

```
Tag SimpleType Pattern Enu
m
```
```
Defaul
t
originalInvoiceNumber SimpleText50NotBlankType .*[^\s].* - -
modifyWithoutMaster - - - false
modificationTimestam
p
```
```
InvoiceTimestampType \d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.\d{1,3})?
Z minInclusive = 2010 - 01 -
01T00:00:00Z
```

```
modificationIndex InvoiceUnboundedIndexTyp
e
```
```
minInclusive = 1 - -
```
**Leírás és kapcsolódó követelmények**

```
1) A currentPage tagban mindig a kérésben megadott page paraméter értéke kerül visszaadásra.
Az availablePage tag tartalmazza a lekérdezhető további lapokat is. Ha a keresés nem ad
eredményt, úgy az availablePage értéke 0 és az invoiceChainElement tag üres. Az egyes
lapokon legfeljebb 100 tétel szerepelhet.
2) A maxLineNumber tag az adott számlához tartozó legmagasabb lineNumber értéket
tartalmazza (nem összekeverendő a /line/lineModificationReference/lineNumberReference
értékkel).
3) A newCreatedLines csomópont csak módosító és sztornó számláknál képződik, és csak abban
az esetben, ha az adott számla tartalmaz új sorokat (ahol lineOperation = CREATE). Mivel a
sorfolytonosság nem garantált egy számlán belül, így annyi newCreatedLines fog képződni,
ahány releváns intervallumot tartalmaz a számla. Az intervallum vége inkluzív, tehát a
lineNumberIntervalEnd tag értéke még beletartozik a meghatározott sorok számába.
4) Az invoiceReferenceData szintén csak módosító és sztornó számláknál képződik, a
csomóponton belül a modificationTimestamp és modificationIndex elemek töltése az adott
számla verziójától függ. 1.0 és 1.1 verzióknál a modificationTimestamp, míg 2.0 verziótól
kezdve a modificationIndex fog töltődni.
```
#### 1.8.4 A /queryInvoiceCheck operáció

A /queryInvoiceCheck egy számlaszám alapján működő lekérdező operáció, amely a számlán szereplő
kiállító és a vevő oldaláról is használható. Az operáció a megadott számlaszámról szóló adatszolgáltatás

létezését ellenőrzi a rendszerben, a számla teljes adattartalmának visszaadása nélkül.

**1.8.4.1 QueryInvoiceCheckRequest**
A /queryInvoiceCheck operáció kérésének struktúráját a QueryInvoiceCheckRequest element
tartalmazza.


## 14. ábra A QueryInvoiceCheckRequest felépítése

A típus a BasicOnlineInvoiceRequestType-ot terjeszti ki, így az abban foglalt elemeken kívül kötelező
keresőparaméterként várja a keresendő számla számát, a keresés irányát, illetve opcionálisan a
módosító okirat sorszámát kötegelt módosítás esetén, valamint a kiállító adószámát.

```
Tag Típus Kötelező Tartalma
invoiceNumber xs:string igen A keresett számla száma
invoiceDirection xs:string igen A keresés iránya, a keresés elvégezhető
kiállítóként és vevőként is
batchIndex xs:int nem A módosító okirat sorszáma kötegelt
módosítás esetén
supplierTaxNumber xs:string nem A kiállító adószáma vevő oldali keresés
esetén
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
invoiceNumber SimpleText50NotBlankType .*[^\s].* - -
invoiceDirection InvoiceDirectionType - OUTBOUND
INBOUND
```
##### -


```
batchIndex InvoiceUnboundedIndexType minInclusive = 1 - -
supplierTaxNumber TaxpayerIdType [0-9]{8} - -
```
**Leírás és kapcsolódó követelmények**

```
1) Az invoiceNumber tagban a keresett számla vagy módosító okirat számát kell megadni.
2) A keresés irányát az invoiceDirection tagban kell kötelezően jelölni. A keresés iránya lehet
kiállító oldali (OUTBOUND) vagy vevő oldali (INBOUND). Kiállítókénti keresés esetén a
lekérdezést végző technikai felhasználóhoz tartozó adószámnak kell szerepelnie a számlán a
kiállítói oldalon. Hasonlóképpen, vevőkénti keresés esetén a lekérdezést végző technikai
felhasználóhoz tartozó adószámnak kell szerepelnie a számlán a vevői oldalon. Azon számlák,
amelyek nem tartalmazzák a vevő adószámát, vevői oldalról nem kereshetők, csak a saját
kiállítói oldalukról.
3) Kötegelt módosítás esetén a keresés opcionálisan szűkíthető a batchIndex által leírt pozíción
lévő számlára. Ha a keresett számlaszám egy kötegelt módosítást leíró számlát jelöl, úgy vevő
oldali keresés esetén csak a helyes számlaszám és batchIndex pár megadásával végezhető el.
Ha a keresett számlaszám nem kötegelt módosítás és a batchIndex tag ki van töltve, vagy
ellenkezőleg, a keresett számlaszám kötegelt módosítás és vevő oldali keresés esetén a
batchIndex kitöltetlen, a rendszer külön hibakódot ad vissza. A hibakódról a „ Hibakezelés”
fejezet tartalmaz további információkat.
4) A supplierTaxNumber tag csak vevő oldali lekérdezés esetén adható meg. Ha több kiállító is
kiállította azonos sorszámmal a keresett számlát, akkor a tag megadásával van lehetőség a
megtalált halmazt egy eleműre szűkíteni. Ha vevő oldali lekérdezés esetén a tag nincs kitöltve
és a válasz több elemű, a rendszer külön hibakódot ad vissza. A lehetséges kiállítói adószámok
listája a /queryInvoiceDigest operációban kapható vissza. Ha a keresést nem vevőként végzik
és a supplierTaxNumber tag ki van töltve, a rendszer külön hibakódot ad vissza. A hibakódról
a „ Hibakezelés” fejezet tartalmaz további információkat.
5) A QueryInvoiceCheckRequest/user/ predecessorTaxNumber tag megadása esetén a megadott
jogelődhöz tartozó számlákon történik a keresés.
```
**1.8.4.2 QueryInvoiceCheckResponse**
A /queryInvoiceCheck operáció válaszának struktúráját a QueryInvoiceCheckResponse element

tartalmazza.


## 15. ábra A QueryInvoiceCheckResponse felépítése

A típus a BasicOnlineInvoiceResponseType-ot terjeszti ki, így az abban foglalt elemeken kívül egy
invoiceCheckResult nevű logikai értéket tartalmaz.

```
Tag Típus Kötelező Tartalma
invoiceCheckResult xs:boolean igen Az ellenőrzés logikai értékét tartalmazza
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
invoiceCheckResult - - - false
```
**Leírás és kapcsolódó követelmények**

```
1) Az invoiceCheckResult tag tartalmazza az ellenőrzés eredményét. A tag értéke abban az
esetben true (igaz), ha a lekérdezett számlaszám pontosan egyszer szerepel érvényesként a
rendszerben. Ha a lekérdezett számlaszám hiba miatt többször szerepel érvényesként a
rendszerben, úgy a válaszban a rendszer új hibakódot ad vissza. A hibakódról a „ Hibakezelés”
fejezet tartalmaz további információkat. A tag értéke minden más esetben false (hamis).
```
#### 1.8.5 A /queryInvoiceData operáció

A /queryInvoiceData egy számlaszám alapján működő lekérdező operáció, amely a számlán szereplő

kiállító és a vevő oldaláról is használható. Az operáció a megadott számlaszám teljes adattartalmát adja
vissza a válaszban.


**1.8.5.1 QueryInvoiceDataRequest**

A /queryInvoiceData operáció kérésének struktúráját a QueryInvoiceDataRequest element
tartalmazza.

## 16. ábra A QueryInvoiceDataRequest felépítése

A típus a BasicOnlineInvoiceRequestType-ot terjeszti ki, így az abban foglalt elemeken kívül kötelező
keresőparaméterként várja a keresendő számla számát, a keresés irányát, illetve opcionálisan a
módosító okirat sorszámát kötegelt módosítás esetén, valamint a kiállító adószámát.

```
Tag Típus Kötelező Tartalma
invoiceNumber xs:string igen A keresett számla száma
invoiceDirection xs:string igen A keresés iránya, a keresés elvégezhető
kiállítóként és vevőként is
batchIndex xs:int nem A módosító okirat sorszáma kötegelt
módosítás esetén
supplierTaxNumber xs:string nem A kiállító adószáma vevő oldali keresés
esetén
```
**Facetek és leírók**


```
Tag SimpleType Pattern Enum Default
invoiceNumber SimpleText50NotBlankType .*[^\s].* - -
invoiceDirection InvoiceDirectionType - OUTBOUND
INBOUND
```
##### -

```
batchIndex InvoiceUnboundedIndexType minInclusive = 1 - -
supplierTaxNumber TaxpayerIdType [0-9]{8} - -
```
**Leírás és kapcsolódó követelmények**

```
1) Minden keresőparaméter jelentése és működése azonos a /queryInvoiceCheck operáció
kérésében szereplő tagekkel.
2) A QueryInvoiceDataRequest/user/ predecessorTaxNumber tag megadása esetén a megadott
jogelődhöz tartozó számlákon történik a keresés.
```
**1.8.5.2 QueryInvoiceDataResponse**
A /queryInvoiceData operáció válaszának struktúráját a QueryInvoiceDataResponse element
tartalmazza.

## 17. ábra A QueryInvoiceDataResponse felépítése


## 18. ábra Az AuditDataType felépítése

A típus a BasicOnlineInvoiceResponseType-ot terjeszti ki. Találat esetén az abban foglalt elemeken
kívül tartalmazza számlaadatokat base64 kódolásban, egy auditData nevű csomópontot a számla audit
adataival, illetve a számlaadatok tömörítettségének logikai jelölését.

```
Tag Típus Kötelező Tartalma
invoiceData xs:base64Binary igen A számla adatai BASE64
kódolásban
auditData/insDate xs:dateTime igen A számlaadat-szolgáltatás
mentésének időpontja
auditData/insCusUser xs:string igen A számlaadat-szolgáltatást
beküldő technikai felhasználó
neve
auditData/source xs:string igen A számlaadat-szolgáltatás forrása
auditData/transactionId xs:string nem A számlaadat-szolgáltatás
tranzakcióazonosítója, ha az gépi
interfészen került beküldésre
auditData/index xs:int nem A számlaadat-szolgáltatás
tranzakciójának indexe
auditData/batchIndex xs:int nem A módosító okirat száma a
kötegen belül
auditData/originalRequestVersion xs:string igen Az adatszolgáltatás
requestVersion értéke
```

```
compressedContentIndicator xs:boolean igen Jelöli, ha az invoiceData tartalmát
a BASE64 dekódolást követően
még ki kell tömöríteni az
olvasáshoz
electronicInvoiceHash xs:complexType nem Elektronikus számla- vagy
módosító okirat állomány hash-
lenyomata
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enu
m
```
```
Defau
lt
invoiceData - - - -
auditData/insDate InvoiceTimestampType \d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.\d{1,
3})?Z
minInclusive = 2010 - 01 -
01T00:00:00Z
```
##### - -

```
auditData/insCusUser LoginType [a-zA-Z0-9]{6,15} - -
auditData/source SourceType - WEB
XML
M2
M
OPG
```
##### -

```
auditData/transactionId EntityIdType [+a-zA-Z0-9_]{1,30} - -
auditData/index InvoiceIndexType minInclusive =1
maxInclusive = 100
```
##### - -

```
auditData/batchIndex
InvoiceUnboundedIndexT
ype
```
```
minInclusive =1
```
```
auditData/originalRequestVer
sion
```
```
OriginalRequestVersionTy
pe
```
##### - 1.0

##### 1.1

##### 2.0

##### 3.0

##### -

```
compressedContentIndicator - - - false
electronicInvoiceHash CryptoType - - -
```
**Leírás és kapcsolódó követelmények**

```
1) A számla üzleti adatait tartalmazó invoiceDataResult csomópont csak akkor kerül a válaszba,
ha a kiállítói vagy vevői oldalon keresett számla pontosan egyszer, érvényesként szerepel a
rendszerben. Ha nincs találat, vagy a keresést végző adószám nem szerepel a számlán az
invoiceDirection által leírt helyen, a rendszer üres üzleti választ
(BasicOnlineInvoiceResponseType) és egy <funcCode>OK</funcCode> üzenetet ad vissza. Ha
a keresett számlaszám egynél többször szerepel a rendszerben érvényesként, a rendszer külön
hibakódot ad vissza (MULTIPLE_QUERY_RESULT_FOUND). A hibakódról a „ Hibakezelés”
fejezet tartalmaz további információkat.
```

```
2) Az electronicInvoiceHash az invoiceData csomóponton kívül szerepel a beküldésben. Emiatt a
queryInvoiceData válaszban szintén az invoiceData csomóponton kívül szerepel, mivel az
invoiceData csomópont BASE64 értékéből számolódik a hash-érték.
```
#### 1.8.6 A /queryInvoiceDigest operáció

A /queryInvoiceDigest üzleti keresőparaméterek alapján működő lekérdező operáció, amely a számlán
szereplő kiállító és a vevő oldaláról is használható. Az operáció a megadott keresőfeltételeknek
megfelelő, lapozható számla listát ad vissza a válaszban. A válasz nem tartalmazza a számlák összes
üzleti adatát, hanem csak egy kivonatot (digest-et). Ha szükség van a listában szereplő valamely számla

teljes adattartalmára, úgy azt a számlaszám birtokában a /queryInvoiceData operációban lehet
lekérdezni.

**1.8.6.1 QueryInvoiceDigestRequest**
A /queryInvoiceDigest operáció kérésének struktúráját a QueryInvoiceDigestRequest element
tartalmazza.

## 19. ábra A QueryInvoiceDigestRequest felépítése


## 20. ábra A MandatoryQueryParamsType felépítése


## 21. ábra Az AdditionalQueryParamsType felépítése


## 22. ábra A RelationalQueryParamsType felépítése


## 23. ábra A TransactionQueryParamsType felépítése

A típus a BasicOnlineInvoiceRequestType-ot terjeszti ki, így az abban foglalt elemeken kívül kötelező
keresőparaméterként várja a keresett lapszámot, a keresés irányát, valamint a kötelező
keresőparaméterek valamelyikét. A szolgáltatásnak ezen kívül megadhatók opcionális
keresőparaméterek, melyek a kötelező keresőparaméterek alapján meghatározott eredményhalmazt

tovább szűkítik. Minden keresőfeltétel konjuktív, logikai vagy nem adható meg.

**Root element szint**

```
Tag Típus Kötelező Tartalma
page xs:int igen A lekérdezni kívánt lap száma
invoiceDirection xs:string igen A keresés iránya, a keresés elvégezhető
kiállítóként és vevőként is
invoiceQueryParams xs:complexType igen A kérés keresőparaméterek
```
**invoiceQueryParams szint**

```
Tag Típus Kötelező Tartalma
mandatoryQueryParams xs:complexType igen Kötelező keresőparaméterek
additionalQueryParams nem Kiegészítő keresőparaméterek
relationalQueryParams nem Relációs keresőparaméterek
transactionQueryParams nem Tranzakciós keresőparaméterek
```
**mandatoryQueryParams szint**

```
Tag Típus Kötelező Tartalma
invoiceIssueDate/dateFrom xs:date igen Számla kiállításának
nagyobb vagy egyenlő
keresőparamétere
invoiceIssueDate/dateTo xs:date igen Számla kiállításának kisebb
vagy egyenlő
keresőparamétere
insDate/dateTimeFrom xs:dateTime igen Számla feldolgozásának
időbélyeges, nagyobb vagy
egyenlő keresőparamétere
UTC idő szerint
```

```
insDate/dateTimeTo xs:dateTime igen Számla feldolgozásának
időbélyeges, kisebb vagy
egyenlő keresőparamétere
UTC idő szerint
originalInvoiceNumber/originalInvoiceNumber xs:string igen Számlalánc
keresőparaméter az
alapszámla számával
```
**additionalQueryParams szint**

```
Tag Típus Kötelező Tartalma
taxNumber xs:string nem A számla kiállítójának vagy vevőjének
adószáma
groupMemberTaxNumber xs:string nem A számla kiállítójának vagy vevőjének
csoporttag adószáma
name xs:string nem A számla kiállítójának vagy vevőjének
keresőparamétere szó eleji egyezőségre
invoiceCategory xs:string nem A számla típusa
paymentMethod xs:string nem Fizetés módja
invoiceAppearance xs:string nem A számla megjelenési formája
source xs:string nem Az adatszolgálatás forrása
currency xs:string nem A számla pénzneme
```
**relationalQueryParams szint**

```
Tag Típus Kötelező Tartalma
invoiceDelivery/queryOperator xs:string igen Relációs kereső operátor
invoiceDelivery/queryValue xs:date igen A keresett érték
paymentDate/queryOperator xs:string igen Relációs kereső operátor
paymentDate/queryValue xs:date igen A keresett érték
invoiceNetAmount/queryOperator xs:string igen Relációs kereső operátor
invoiceNetAmount/queryValue xs:decimal igen A keresett érték
invoiceNetAmountHUF/queryOperator xs:string igen Relációs kereső operátor
invoiceNetAmountHUF/queryValue xs:decimal igen A keresett érték
invoiceVatAmount/queryOperator xs:string igen Relációs kereső operátor
invoiceVatAmount/queryValue xs:decimal igen A keresett érték
invoiceVatAmountHUF/queryOperator xs:string igen Relációs kereső operátor
invoiceVatAmountHUF/queryValue xs:decimal igen A keresett érték
```
**transactionQueryParams szint**

```
Tag Típus Kötelező Tartalma
transactionId xs:string nem A keresett tranzakció azonosítója
index xs:int nem A keresett számla sorszáma a tranzakción
belül
invoiceOperation xs:string nem Számlaművelet keresőparamétere
```
**Facetek és leírók**


**Root element szint**

```
Tag SimpleType Pattern Enum Default
page RequestPageType minInclusive = 1 - -
invoiceDirection InvoiceDirectionType - OUTBOUND
INBOUND
```
##### -

```
invoiceQueryParams -
```
**invoiceQueryParams szint**

```
Tag SimpleType Pattern Enum Default
mandatoryQueryParams -
additionalQueryParams
relationalQueryParams
transactionQueryParams
```
**mandatoryQueryParams szint**

```
Tag SimpleType Pattern Enu
m
```
```
Defau
lt
invoiceIssueDate/dateFrom InvoiceDateType minInclusive = 2010- 01 - 01
\d{4}-\d{2}-\d{2}
```
##### - -

```
invoiceIssueDate/dateTo InvoiceDateType minInclusive = 2010- 01 - 01
\d{4}-\d{2}-\d{2}
```
##### - -

```
insDate/dateTimeFrom InvoiceTimestampTyp
e
```
```
\d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.\d{
1,3})?Z
minInclusive = 2010 - 01 -
01T00:00:00Z
```
##### - -

```
insDate/dateTimeTo InvoiceTimestampTyp
e
```
```
\d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.\d{
1,3})?Z
minInclusive = 2010 - 01 -
01T00:00:00Z
```
##### - -

```
originalInvoiceNumber/originalInvoic
eNumber
```
```
SimpleText50NotBlan
kType
```
```
.*[^\s].* - -
```
**additionalQueryParams szint**

```
Tag SimpleType Pattern Enum Default
taxNumber TaxpayerIdType [0-9]{8} - -
groupMemberTaxNumber TaxpayerIdType [0-9]{8} - -
name QueryNameType minlength = 5
.*[^\s].*
```
##### - -

```
invoiceCategory InvoiceCategoryType - NORMAL
SIMPLIFIED
AGGREGATE
```
##### -

```
paymentMethod PaymentMethodType - TRANSFER
CASH
CARD
```
##### -


##### VOUCHER

##### OTHER

```
invoiceAppearance InvoiceAppearanceType - PAPER
ELECTRONIC
EDI
UNKNOWN
```
##### -

```
source SourceType - WEB
XML
MGM
OPG
```
##### -

```
currency CurrencyType [A-Z]{3} - -
```
**relationalQueryParams szint**

```
Tag SimpleType Pattern Enum Default
invoiceDelivery/queryOperator QueryOperatorType - EQ
GT
GTE
LT
LTE
```
##### -

```
invoiceDelivery/queryValue InvoiceDateType minInclusive =
2010 - 01 - 01
\d{4}-\d{2}-
\d{2}
```
##### - -

```
paymentDate/queryOperator QueryOperatorType - EQ
GT
GTE
LT
LTE
```
##### -

```
paymentDate/queryValue InvoiceDateType minInclusive =
2010 - 01 - 01
\d{4}-\d{2}-
\d{2}
```
##### - -

```
invoiceNetAmount/queryOperator QueryOperatorType - EQ
GT
GTE
LT
LTE
```
##### -

```
invoiceNetAmount/queryValue MonetaryType totalDigits = 18,
fractionDigits =
2
```
##### - -

```
invoiceNetAmountHUF/queryOperator QueryOperatorType - EQ
GT
GTE
LT
LTE
```
##### -

```
invoiceNetAmountHUF/queryValue MonetaryType totalDigits = 18,
fractionDigits =
2
```
##### - -

```
invoiceVatAmount/queryOperator QueryOperatorType - EQ
GT
```
##### -


##### GTE

##### LT

##### LTE

```
invoiceVatAmount/queryValue MonetaryType totalDigits = 18,
fractionDigits =
2
```
##### - -

```
invoiceVatAmountHUF/queryOperator QueryOperatorType - EQ
GT
GTE
LT
LTE
```
##### -

```
invoiceVatAmountHUF/queryValue MonetaryType totalDigits = 18,
fractionDigits =
2
```
##### - -

**transactionQueryParams szint**

```
Tag SimpleType Pattern Enum Default
transactionId EntityIdType [+a-zA-Z0-9_]{1,30} - -
index InvoiceIndexType minInclusive =1
maxInclusive = 100
```
##### - -

```
invoiceOperation ManageInvoiceOperationType - CREATE
MODIFY
STORNO
```
##### -

**Leírás és kapcsolódó követelmények**

```
1) A page tagban a lekérdezés lapszámát kell megadni. Kötelező legkisebb értéke 1. A lekérdezés
válaszában visszaadásra kerül, hogy az adott lekérdezési eredmény hány lapszámon keresztül
ad eredményt. A lekérdezést hasonló paraméterekkel, de magasabb lapszámon megismételve,
a rendszer mindig a következő lapra eső eredményeket adja vissza. A kliens nem választhatja
meg sem a lapok méretét, sem a rendezés feltételeit, arról minden esetben a szerver dönt.
2) A mandatoryQueryParams típusban kötelező a 3 fő keresési feltétel közül egyet választani. A
keresés történhet:
a. invoiceIssueDate megadása esetén a számla vagy módosító okirat kiállításának naptári
napjára
b. insDate megadása esetén a számla vagy módosító okirat szerveroldali feldolgozásának
időpontjára, UTC időben
c. originalInvoiceNumber megadása esetén számlaláncra
3) invoiceIssueDate és insDate keresőfeltétel megadásakor a két időpont közötti távolság nem
lehet nagyobb 35 napnál (vagy 840 óránál), az ennek nem megfelelő kérésekre a rendszer
külön hibakódot ad vissza. A hibakódról a „ Hibakezelés” fejezet tartalmaz további
információkat.
4) invoiceIssueDate és insDate keresőfeltétel megadásakor a két belső keresőparaméter (from-
to) egyenlősége esetén, a rendszer invoiceIssueDate esetén, az adott nap 24 óráját, insDate
esetén a pontos időpontot keresi. A két belső keresőparaméter (from-to) egymással
átfedésben nem lehet. Az ennek nem megfelelő kérésekre a rendszer külön hibakódot ad
vissza. A hibakódról a „ Hibakezelés” fejezet tartalmaz további információkat.
```

```
5) originalInvoiceNumber keresőfeltétel megadásakor a rendszer a megadott számlaszámmal
keresi az alapszámlát, illetve minden olyan módosító okiratot, amelynek a hivatkozása a
keresőfeltételben megadott számlaszámra mutat. A megtalált halmaz lehet teljes számlalánc
vagy olyan részleges lánc is, ahol az alapszámla hiányzik, és minden módosító okirat előzmény
nélküliként van megjelölve.
6) Az additionalQueryParams típusban szűkíthető a megtalált számlák listája az egyes
keresőparaméterek megadásával. A szűkítés a megtalált halmaz azon üzleti adataira
vonatkozik, amelyeknek az azonos nevű keresőparaméterei ki lettek töltve a kérésben. A
típuson belül a taxNumber, groupMemberTaxNumber és a name tagek „kétértékű”
keresőparaméterek. Ez azt jelenti, hogy az invoiceDirection értékétől függően kiállítói oldali
keresés esetén (invoiceDirection = OUTBOUND) a mezők a vevő oldali adatokban, míg vevő
oldali keresés esetén (invoiceDirection = INBOUND) a mezők a kiállító oldali adatokban
keresnek.
7) A name keresőparaméter szó eleji egyezőségre keres, ha a megadott keresőparaméter
legalább 5 hosszú. A rendszer a keresés előtt a keresőparamétert uppercase értékre
konvertálja, ezért uppercase-lowercase eltérésre a kliens oldalnak nem kell tekintettel lennie.
8) A relationalQueryParams típusban szűkíthető a megtalált számlák listája az egyes
keresőparaméterek megadásával. Minden keresés a külső típusban található üzleti adat (pl:
invoiceDelivery, paymentDate stb.) keresését végzi.
9) A relationalQueryParams típusban a keresés történhet egyenlőségre vagy tartományra, az
alábbiak szerint:
a. ha a keresés egyenlőségre történik, a külső csomópontot csak egyszer szabad képezni
és a queryOperatorban EQ értéket kell szerepeltetni, ekkor a keresett érték a
queryValue tagban definiált érték lesz
b. ha a keresés tartományra történik, akkor a külső csomópontot kétszer kell képezni, és
a queryOperator tagekben csak LT vagy LTE, illetve GT vagy GTE pároknak kell állnia,
ekkor a keresett tartományt az LT vagy LTE, illetve GT vagy GTE párokhoz tartozó
queryValue tagban definiált értékek határozzák meg
c. minden olyan kérésre, amely a fenti megkötéseket nem teljesíti a rendszer külön
hibakódot ad vissza. A hibakódról a „ Hibakezelés” fejezet tartalmaz további
információkat.
10) A transactionQueryParams típusban szűkíthető a megtalált számlák listája az egyes
keresőparaméterek megadásával. A szűkítés a megtalált halmaz azon tranzakciós adataira
vonatkozik, amelyeknek az azonos nevű keresőparaméterei ki lettek töltve a kérésben.
11) A QueryInvoiceDigestRequest/user/ predecessorTaxNumber tag megadása esetén a megadott
jogelődhöz tartozó számlákon történik a keresés.
```
**1.8.6.2 QueryInvoiceDigestResponse**
A /queryInvoiceDigest operáció válaszának struktúráját a QueryInvoiceDigestResponse element
tartalmazza.


## 24. ábra A QueryInvoiceDigestResponse felépítése


## 25. ábra Az InvoiceDigestType felépítése..............................................................................................


A típus a BasicOnlineInvoiceResponseType-ot terjeszti ki, így az abban foglalt elemeken kívül legalább

1 keresési találat esetén, a számla kivonatos adatait tartalmazza. A kivonat fő szabályként minden
olyan elemet tartalmaz, amire a kérésben keresni lehet.

```
Tag Típus Kötelező Tartalma
currentPage xs:int igen A jelenleg lekérdezett lap
értéke
availablePage xs:int igen Az elérhető legnagyobb
lap értéke
invoiceDigest/invoiceNumber xs:string igen Számla vagy módosító
okirat sorszáma
invoiceDigest/batchIndex xs:int nem Kötegelt módosítás
esetén a számla sorszáma
a kötegen belül
invoiceDigest/invoiceOperation xs:string igen Számlaművelet típusa
invoiceDigest/invoiceCategory xs:string igen Számla típusa
invoiceDigest/invoiceIssueDate xs:date igen Számla vagy módosító
okirat kiállítási dátuma
invoiceDigest/supplierTaxNumber xs:string igen Számla kiállítójának
adószáma
invoiceDigest/supplierGroupMemberTaxNumber xs:string nem Számla kiállítójának
áfacsoport azonosító
száma
invoiceDigest/supplierName xs:string igen A számla kiállítójának
neve
invoiceDigest/customerTaxNumber xs:string nem A vevő adószáma
invoiceDigest/customerGroupMemberTaxNumber xs:string nem A vevő áfacsoport
azonosító száma
invoiceDigest/customerName xs:string nem A vevő neve
invoiceDigest/paymentMethod xs:string nem Fizetési mód
invoiceDigest/paymentDate xs:date nem Fizetési határidő
invoiceDigest/invoiceAppearance xs:string nem A számla megjelenési
formája
invoiceDigest/source xs:string nem Az adatszolgáltatás
forrása
invoiceDigest/invoiceDeliveryDate xs:date nem A számla teljesítési
dátuma
invoiceDigest/currency xs:string nem A számla pénzneme
invoiceDigest/invoiceNetAmount xs:decimal nem A számla nettó összege a
számla pénznemében
invoiceDigest/invoiceNetAmountHUF xs:decimal nem A számla nettó összege
forintban
invoiceDigest/invoiceVatAmount xs:decimal nem A számla áfa összege a
számla pénznemében
invoiceDigest/invoiceVatAmountHUF xs:decimal nem A számla áfa összege
forintban
invoiceDigest/transactionId xs:string nem Az adatszolgáltatás
tranzakcióazonosítója
invoiceDigest/index xs:int nem A számla sorszáma a
kérésen belül
```

```
invoiceDigest/originalInvoiceNumber xs:string nem Az eredeti számla
sorszáma, amelyre a
módosítás vonatkozik
invoiceDigest/modificationIndex xs:int nem A számlára vonatkozó
módosító okirat egyedi
sorszáma
invoiceDigest/insDate xs:dateTime igen A rendszerbe történő
beérkezés időpontja UTC
időben
invoiceDigest/completenessIndicator xs:boolean nem Az adatszolgáltatás maga
az elektronikus számla
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Defa
ult
currentPage ResponsePageType minInclusive = 0 - -
availablePage ResponsePageType minInclusive = 0 - -
invoiceDigest/invoiceNumber SimpleText50NotBlan
kType
```
```
.*[^\s].* - -
```
```
invoiceDigest/batchIndex InvoiceUnboundedIn
dexType
```
```
minInclusive = 1 - -
```
```
invoiceDigest/invoiceOperation ManageInvoiceOpera
tionType
```
##### - CREATE

##### MODIFY

##### STORNO

##### -

```
invoiceDigest/invoiceCategory InvoiceCategoryType - NORMA
L
SIMPLIFI
ED
AGGREG
ATE
```
##### -

```
invoiceDigest/invoiceIssueDate InvoiceDateType minInclusive = 2010- 01 -
01
```
##### - -

```
invoiceDigest/supplierTaxNumber TaxpayerIdType [0-9]{8} - -
invoiceDigest/supplierGroupMembe
rTaxNumber
```
```
TaxpayerIdType [0-9]{8} - -
```
```
invoiceDigest/supplierName SimpleText512NotBla
nkType
```
```
.*[^\s].* - -
```
```
invoiceDigest/customerTaxNumber TaxpayerIdType [0-9]{8} - -
invoiceDigest/customerGroupMemb
erTaxNumber
```
```
TaxpayerIdType [0-9]{8} - -
```
```
invoiceDigest/customerName SimpleText512NotBla
nkType
```
```
.*[^\s].* - -
```
```
invoiceDigest/paymentMethod PaymentMethodType - TRANSFE
R
CASH
CARD
VOUCHE
R
OTHER
```
##### -


```
invoiceDigest/paymentDate InvoiceDateType minInclusive = 2010- 01 -
01
```
##### - -

```
invoiceDigest/invoiceAppearance InvoiceAppearanceTy
pe
```
##### - PAPER

##### ELECTRO

##### NIC

##### EDI

##### UNKNO

##### WN

##### -

```
invoiceDigest/source SourceType - WEB
XML
MGM
OPG
```
##### -

```
invoiceDigest/invoiceDeliveryDate InvoiceDateType minInclusive = 2010- 01 -
01
```
##### - -

```
invoiceDigest/currency CurrencyType [A-Z]{3} - -
invoiceDigest/invoiceNetAmount MonetaryType totalDigits = 18,
fractionDigits = 2
```
##### - -

```
invoiceDigest/invoiceNetAmountHU
F
```
```
MonetaryType totalDigits = 18,
fractionDigits = 2
```
##### - -

```
invoiceDigest/invoiceVatAmount MonetaryType totalDigits = 18,
fractionDigits = 2
```
##### - -

```
invoiceDigest/invoiceVatAmountHU
F
```
```
MonetaryType totalDigits = 18,
fractionDigits = 2
```
##### - -

```
invoiceDigest/transactionId EntityIdType [+a-zA-Z0-9_]{1,30} - -
invoiceDigest/index InvoiceIndexType minInclusive = 1
maxInclusive = 100
```
##### - -

```
invoiceDigest/originalInvoiceNumbe
r
```
```
SimpleText50NotBlan
kType
```
```
.*[^\s].* - -
```
```
invoiceDigest/modificationIndex InvoiceUnboundedIn
dexType
```
```
minInclusive = 1 - -
```
```
invoiceDigest/insDate InvoiceTimestampTyp
e
```
```
\d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.
\d{1,3})?Z minInclusive =
2010 - 01 - 01T00:00:00Z
```
##### - -

```
invoiceDigest/completenessIndicato
r
```
- - - false

**Leírás és kapcsolódó követelmények**

```
1) A currentPage tagban mindig a kérésben megadott page paraméter értéke kerül visszaadásra.
Az availablePage tag tartalmazza a lekérdezhető további lapokat is. Ha a keresés nem ad
eredményt, úgy az availablePage értéke 0 és az invoiceDigest tag üres. Az egyes lapokon
legfeljebb 100 tétel szerepelhet.
2) Az operáció - egyedül a lekérdező operációk között - listázza az egynél többször érvényesként
előforduló számlákat is. Az egyes tételek között a transactionId értéke alapján lehet
különbséget tenni, figyelemmel arra, hogy duplikált adatszolgáltatás csak külön
tranzakciókban érkezhet. Ez minden esetben kliensoldali hiba, az így megtalált számlák
számára technikai érvénytelenítést kell feladni, majd jóváhagyás után megismételni az
adatszolgáltatást a helyes adatokkal.
```

#### 1.8.7 A /queryTransactionList operáció

A /queryTransactionList a kérésben megadott időintervallumban, a technikai felhasználóhoz tartozó
adószámhoz beküldött számlaadat-szolgáltatások listázására szolgál.

**1.8.7.1 QueryTransactionListRequest**
A /queryTransactionList operáció kérésének struktúráját a QueryTransactionListRequest element
tartalmazza.

## 26. ábra A QueryTransactionListRequest felépítése

A típus a BasicOnlineInvoiceRequestType-ot terjeszti ki, így az abban foglalt elemeken kívül a
lekérdezni kívánt intervallum kezdő és végdátuma szerepel.

```
Tag Típus Kötelező Tartalma
dateTimeFrom xs:dateTime igen Időpontos intervallum nagyobb vagy
egyenlő paramétere UTC idő szerint
```

```
dateTimeTo xs:dateTime igen Időpontos intervallum kisebb vagy
egyenlő paramétere UTC idő szerint
requestStatus xs:string nem A tranzakció státusza
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
dateTimeFrom InvoiceTimestampType \d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.\d{1,3})?Z
minInclusive = 2010 - 01 -
01T00:00:00Z
```
##### - -

```
dateTimeTo InvoiceTimestampType \d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.\d{1,3})?Z
minInclusive = 2010 - 01 -
01T00:00:00Z
```
##### - -

```
requestStatus RequestStatusType - RECEIVED,
PROCESSING,
SAVED,
FINISHED,
NOTIFIED
```
##### -

**Leírás és kapcsolódó követelmények**

```
1) dateTimeFrom és dateTimeTo keresőfeltétel megadásakor a két időpont közötti távolság nem
lehet nagyobb 35 napnál (vagy 840 óránál), az ennek nem megfelelő kérésekre a rendszer
külön hibakódot ad vissza. A hibakódról a „ Hibakezelés” fejezet tartalmaz további
információkat.
2) A kérésben lehetőség van a tranzakció státuszára szűrni, a requestStatus tagben, melynek
lehetséges értékei:
a. RECEIVED: befogadva
b. PROCESSING: feldolgozás alatt
c. SAVED: elmentve
d. FINISHED: feldolgozás befejezve
e. NOTIFIED: lekérdezve
3) A QueryTransactionListRequest/user/ predecessorTaxNumber tag megadása esetén a
megadott jogelődhöz tartozó számlaadat-szolgáltatások között történik a keresés.
```
**1.8.7.2 QueryTransactionListResponse**
A /queryTransactionList operáció válaszának struktúráját a QueryTransactionListResponse element
tartalmazza.


## 27. ábra A QueryTransactionListResponse felépítése

A típus a BasicOnlineInvoiceResponseType-ot terjeszti ki, így az abban foglalt elemeken kívül a
kérésben megadott intervallumon belül létrejött számlaadat-szolgáltatások főbb adatait tartalmazza.

```
Tag Típus Kötelező Tartalma
currentPage xs:int igen A jelenleg lekérdezett lap értéke
availablePage xs:int igen Az elérhető legnagyobb lap értéke
transaction/insDate xs:dateTime igen A számlaadat-szolgáltatás
mentésének időpontja
transaction/insCusUser xs:string igen A számlaadat-szolgáltatást beküldő
technikai felhasználó neve
transaction/source xs:string igen A számlaadat-szolgáltatás forrása
transaction/transactionId xs:string igen A számlaadat-szolgáltatás
tranzakcióazonosítója
```

```
transaction/requestStatus xs:string igen A tranzakció státusza
transaction/technicalAnnulment xs:boolean igen Jelöli, hogy a tranzakció technikai
érvénytelenítést tartalmaz
transaction/originalRequestVersion xs:string igen A számlaadat-szolgáltatás
requestVersion értéke
transaction/itemCount xs:int igen A számlaadat-szolgáltatás
tételeinek száma
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Defau
lt
currentPage ResponsePageType minInclusive = 0 - -
availablePage ResponsePageType minInclusive = 0
transaction/insDate InvoiceTimestampType \d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.\d{
1,3})?Z minInclusive = 2010 -
01 - 01T00:00:00Z
```
##### - -

```
transaction/insCusUser LoginType [a-zA-Z0-9]{6,15} - -
transaction/source SourceType - WEB
XML
M2M
OPG
```
##### -

```
transaction/transactionId EntityIdType [+a-zA-Z0-9_]{1,30} - -
transaction/requestStatus RequestStatusType - RECEIVED,
PROCESSI
NG,
SAVED,
FINISHED,
NOTIFIED
```
##### -

```
transaction/technicalAnnulm
ent
```
- - - false

```
transaction/originalRequestV
ersion
```
```
OriginalRequestVersio
nType
```
##### - 1.0

##### 1.1

##### 2.0

##### 3.0

##### -

```
transaction/itemCount InvoiceIndexType minInclusive =1
maxInclusive = 100
```
##### - -

**Leírás és kapcsolódó követelmények**

```
1) A lista minden adatszolgáltatási tranzakciót visszaad, amit az adózó beküldött, forrástól
függetlenül.
2) A válaszban visszaadott requestStatus értékeinek jelentése:
```
- RECEIVED: befogadva
- PROCESSING: feldolgozás alatt
- SAVED: elmentve
- FINISHED: feldolgozás befejezve
- NOTIFIED: lekérdezve


#### 1.8.8 A /queryTransactionStatus operáció...........................................................................................

A /queryTransactionStatus a számlaadat-szolgáltatás feldolgozás aktuális állapotának és
eredményének lekérdezésére szolgáló operáció.

**1.8.8.1 QueryTransactionStatusRequest**
A /queryTransactionStatus operáció kérésének struktúráját a QueryTransactionStatusRequest
element tartalmazza.

## 28. ábra A QueryTransactionStatusRequest felépítése.........................................................................

A típus a BasicOnlineInvoiceRequestType-ot terjeszti ki, így az abban foglalt elemeken kívül a
lekérdezni kívánt tranzakció azonosítója szerepel.

```
Tag Típus Kötelező Tartalma
transactionId xs:string igen A lekérdezni kívánt tranzakció azonosítója
returnOriginalRequest xs:boolean nem Az eredeti tartalom lekérdezésének
jelölője
```

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
transactionId EntityIdType [+a-zA-Z0-9_]{1,30} - -
returnOriginalRequest - - - false
```
**Leírás és kapcsolódó követelmények**

```
1) A transactionId a keresett tranzakció egyedi, szerver által adott azonosítója. A transactionId
tartozhat technikai érvénytelenítéshez vagy számlaadat-szolgáltatáshoz is.
2) Az operáció – már feldolgozott státuszú kérések esetén is – biztosítja az eredeti, kliens által
beküldött számlaadat-szolgáltatás visszaadásának lehetőségét, ha erre szükség volna. Ennek
tényét a kérésben a returnOriginalRequest tagban kell jelölni.
3) A QueryTransactionStatusRequest/user/ predecessorTaxNumber tag megadása esetén a
megadott jogelődhöz tartozó számlaadat-szolgáltatások történik a keresés.
```
**1.8.8.2 QueryTransactionStatusResponse**
A /queryTransactionStatus operáció válaszának struktúráját a QueryTransactionStatusResponse

element tartalmazza.

## 29. ábra A QueryTransactioneStatusResponse felépítése


## 30. ábra A ProcessingResultType felépítése..........................................................................................

## 31. ábra Az AnnulmentDataType felépítése..........................................................................................


A típus a BasicOnlineInvoiceResponseType-ot terjeszti ki, így az abban foglalt elemeken kívül a

kérésben megadott tranzakcióazonosítóhoz tartozó számlák tételes feldolgozási eredményét, valamint
opcionálisan a technikai érvénytelenítés jóváhagyási adatait tartalmazza.

```
Tag Típus Kötele-
ző
```
```
Tartalma
```
```
index xs:int igen A számlaadat-
szolgáltatás
tranzakciójának
indexe
batchIndex xs:int nem Kötegelt
módosítás
esetén a számla
sorszáma a
kötegen belül
invoiceStatus xs:string igen A számla
feldolgozási
státusza
technicalValidationMessages/validationResultCode xs:string igen Technikai
validáció
eredménye
technicalValidationMessages/validationErrorCode xs:string nem Validációs
hibakód
technicalValidationMessages/message xs:string nem Feldolgozási
üzenet
businessValidationMessages/validationResultCode xs:string igen Üzleti validáció
eredménye
businessValidationMessages/validationErrorCode xs:string nem Validációs
hibakód
businessValidationMessages/message xs:string nem Feldolgozási
üzenet
businessValidationMessages/pointer/tag xs:string nem Tag hivatkozás
businessValidationMessages/pointer/value xs:string nem Érték hivatkozás
businessValidationMessages/pointer/line xs:nonNegativeInt
eger
```
```
nem Sorhivatkozás
```
```
businessValidationMessages/pointer/originalInvoiceNu
mber
```
```
xs:string nem Kötegelt számla
művelet esetén
az eredeti
számla
sorszáma,
melyre a
módosítás
vonatkozik
compressedContent xs:boolean igen Jelöli, ha az
originalRequest
tartalmát a
BASE64
dekódolást
követően még
ki kell
```

```
tömöríteni az
olvasáshoz
originalRequest xs:base64Binary nem Az eredeti
számlaadat
originalRequestVersion xs:string igen Az
adatszolgáltatás
requestVersion
értéke
annulmentData/annulmentVerificationStatus xs:string igen A technikai
érvénytelenítő
kérések
jóváhagyási
státusza
annulmentData/annulmentDecisionDate xs:dateTime nem A technikai
érvénytelenítés
jóváhagyásának
vagy
elutasításának
időpontja UTC
időben
annulmentData/annulmentDecisionUser xs:string nem A technikai
érvénytelenítést
jóváhagyó vagy
elutasító
felhasználó
neve
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Def
ault
index InvoiceIndexType minInclusive =1
maxInclusive = 100
```
##### - -

```
batchIndex InvoiceUnboundedI
ndexType
```
##### - - -

```
invoiceStatus InvoiceStatusType - RECEIVED
PROCESSING
SAVED
DONE
ABORTED
```
##### -

```
technicalValidationMessages/validat
ionResultCode
```
```
TechnicalResultCod
eType
```
##### - CRITICAL

##### ERROR

##### -

```
technicalValidationMessages/validat
ionErrorCode
```
```
SimpleText 10 0NotBl
ankType
```
```
.*[^\s].* - -
```
```
technicalValidationMessages/messa
ge
```
```
SimpleText1024Not
BlankType
```
```
.*[^\s].* - -
```
```
businessValidationMessages/validati
onResultCode
```
```
BusinessResultCode
Type
```
##### - ERROR

##### WARN

##### INFO

##### -


```
businessValidationMessages/validati
onErrorCode
```
```
SimpleText 10 0NotBl
ankType
```
##### - - -

```
businessValidationMessages/messag
e
```
```
SimpleText1024Not
BlankType
```
```
.*[^\s].* - -
```
```
businessValidationMessages/pointer
/tag
```
```
SimpleText 1024 Not
BlankType
```
```
.*[^\s].* - -
```
```
businessValidationMessages/pointer
/value
```
```
SimpleText1024Not
BlankType
```
```
.*[^\s].* - -
```
```
businessValidationMessages/pointer
/line
```
```
LineNumberType minInclusive =1
```
- -

```
businessValidationMessages/pointer
/originalInvoiceNumber
```
```
SimpleText50NotBla
nkType
```
```
.*[^\s].* - -
```
```
compressedContentIndicator - - - fals
e
originalRequest InvoiceType - - -
originalRequestVersion OriginalRequestVers
ionType
```
##### - 1.0

##### 1.1

##### 2.0

##### 3.0

##### -

```
annulmentData/annulmentVerificati
onStatus
```
```
AnnulmentVerificati
onStatusType
```
##### - NOT_VERIFIAB

##### LE

##### VERIFICATION

##### _PENDING

##### VERIFICATION

##### _DONE

##### VERIFICATION

##### _REJECTED

##### -

```
annulmentData/annulmentDecision
Date
```
```
InvoiceTimestampT
ype
```
```
\d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{
2}(.\d{1,3})?Z
minInclusive = 2010 -
01 - 01T00:00:00Z
```
##### - -

```
annulmentData/annulmentDecision
User
```
```
LoginType [a-zA-Z0-9]{6,15} - -
```
**Leírás és kapcsolódó követelmények**

```
1) Ha az adózónak nincs a lekérdezési feltételeknek megfelelő adatszolgáltatási tranzakciója, a
szolgáltatás csak egy <funcCode>OK</funcCode> üzenetet ad vissza.
2) Kötegelt beküldés esetén a kérésben szereplő index pozíció alapján lehet az adott számlára
vonatkozó adatszolgáltatáshoz tartozó feldolgozási eredményt megfeleltetni a válaszban lévő
adatokkal.
3) Az invoiceStatus jelzi az egyes számlákra vonatkozó adatszolgáltatások feldolgozási állapotát.
```
```
RECEIVED = az adott indexen lévő számlaadat-szolgáltatás befogadása megtörtént
```
```
PROCESSING = az adott indexen lévő számlaadat-szolgáltatás feldolgozása megkezdődött
```
```
SAVED = az adott indexen lévő számlaadat-szolgáltatás feldolgozásakor blokkoló hiba nem
lépett fel, a számla mentésre került, de a feldolgozás még nem fejeződött be
```

```
DONE = az adott indexen lévő számlaadat-szolgáltatás feldolgozása sikeresen befejeződött
```
```
ABORTED = az adott indexen lévő számlaadat-szolgáltatás feldolgozása sikertelen volt
```
Csak azon számlaadat-szolgáltatás tekinthető teljesítettnek, melyre vonatkozóan az invoiceStatus =
DONE. Ezen körön belül csak azon számlaadat-szolgáltatás tekinthető üzletileg helyesnek, melyre
vonatkozóan a válaszban nincs businessValidationMessages listaelem.

```
4) Figyelemmel arra, hogy az egyes számlaadat-szolgáltatási adatok séma-validitásának vizsgálata
aszinkron történik, az operáció biztosítja ezen adatok körére is a séma sértések és egyéb
technikai hibák tételes visszadását, csakúgy, mint a szinkron feldolgozásnál. A node értéke és
értékkészlete mindenben megegyezik a hivatkozott GeneralErrorResponseType típusban
található értékészlettel.
5) Az esetlegesen lekérdezett eredeti adatszolgáltatást a rendszer BASE64 encoded
formátumban adja vissza. Ha a tartalom tömörítve érkezett a rendszerbe, akkor a válasz is
tömörítetten kerül visszaadásra. Ennek a tényéről a compressedContentIndicator tag
tájékoztat.
6) A message tagban technikai validáció esetén technikai hibaüzenet, üzleti validáció esetén
pedig a blokkoló hibának (ERROR) vagy figyelmezetésnek (WARN) az üzleti leírása kerül
visszaadásra. A validációs eredmény lokalizációja figyelembe veszi a lekérdező technikai
felhasználó kapcsolattartási nyelvét.
7) A pointer tagban a vonatkozó tag, érték és opcionálisan tétel sorszám kerül visszaadásra,
amelyre az esetleges figyelmeztetés (WARN) vonatkozik.
8) Az annulmentVerificationStatus jelzi az egyes technikai érvénytelenítésekre vonatkozó
adatszolgáltatások jóváhagyási állapotát.
```
```
NOT_VERIFIABLE = az annulment kérés aszinkron feldolgozásakor bármely index ERROR
értéket kapott (ilyen esetben a teljes technikai érvénytelenítés elutasításra kerül a többi
indexre is, a beküldést meg kell ismételni a szükséges javítások után).
```
```
VERIFICATION_PENDING = az annulment kérés aszinkron feldolgozása minden indexen DONE
eredményt adott, ekkortól lehet a technikai érvénytelenítést a felületen
jóváhagyni/elutasítani.
```
```
VERIFICATION_DONE = ha már sikeresen jóváhagyták a kérést a felületen (ez a státusz jelzi,
hogy a technikailag érvénytelenített számlaszámok újra beküldhetőek az adott adózónál).
```
```
VERIFICATION_REJECTED = ha az elsődleges felhasználó nem jóváhagyta, hanem elutasította a
technikai érvénytelenítést (ilyen esetben ismét nem történt semmi, minden visszaállt az
eredeti állapotba, a tartalmazó számlaszámok továbbra is érvényesek a rendszerben).
```
A businessValidationMessages értékkészletéről a „ **Validációs hibakódok”** fejezetben található
információ.

#### 1.8.9 A /queryTaxpayer operáció

A /queryTaxpayer belföldi adószám validáló operáció, mely a számlakiállítás folyamatába építve képes
a megadott adószám valódiságáról és érvényességéről a NAV adatbázisa alapján adatot szolgáltatni.


**1.8.9.1 QueryTaxpayerRequest**

A /queryTaxpayer operáció kérésének struktúráját a QueryTaxpayerRequest element tartalmazza.

## 32. ábra A QueryTaxpayerRequest felépítése

A típus a BasicOnlineInvoiceRequestType-ot terjeszti ki, így az abban foglalt elemeken kívül a
lekérdezni kívánt magyar adószámot tartalmazza.

```
Tag Típus Kötelező Tartalma
taxNumber xs:string igen A lekérdezni kívánt magyar adószám első
8 jegye
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
taxNumber TaxpayerIdType [0-9]{8} - -
```
**Leírás és kapcsolódó követelmények**

```
1) A szolgáltatás csak magyar adószámok vizsgálatát támogatja, ez technikailag a pattern
megkötésen keresztül van kényszerítve.
2) A QueryTaxpayerRequest/user/ predecessorTaxNumber tag megadása esetén validálásra
kerül a megadott érték, azonban további hatása nincs az operációra.
```
**1.8.9.2 QueryTaxpayerResponse**
A /queryTaxpayer operáció válaszának struktúráját a QueryTaxpayerResponse element tartalmazza.


## 33. ábra A QueryTaxpayerResponse felépítése

## 34. ábra A TaxpayerAddressListType felépítése


## 35. ábra A DetailedAddressType felépítése

A típus a BasicOnlineInvoiceResponseType-ot terjeszti ki, így az abban foglalt elemeken kívül
opcionálisan a lekérdezett adószám státuszát, találat esetén pedig az adózó nevét, áfacsoport és
címadatait tartalmazza.

```
Tag Típus Kötelező Tartalma
infoDate xs:dateTime nem A lekérdezett
adószám utolsó
változásának
időpontja
```

```
taxpayerValidity xs:boolean nem A lekérdezett
adószám
érvényességének
státusza (ha az
adószám létezik)
taxpayerData/taxpayerName xs:string igen A lekérdezett
adózó neve
taxpayerData/taxpayerShortName xs:string nem Az adózó rövid
neve
taxNumberDetail/taxpayerId xs:string igen Az adóalany adó
törzsszáma
taxNumberDetail/vatCode xs:string nem Áfakód az
adóalanyiság
típusának jelzésére
taxNumberDetail/countyCode xs:string nem Megyekód
taxpayerData/incorporation xs:string igen Gazdasági típus
taxpayerData/vatGroupMembership xs:string nem Az adózó
áfacsoport tagsága
taxpayerAddressItem/taxpayerAddressType xs:string igen Adózói címtípus
taxpayerAddressItem/taxpayerAddress/countryCode xs:string igen Országkód ISO
3166 alpha- 2
szabvány szerint
taxpayerAddressItem/taxpayerAddress/region xs:string nem Tartománykód ISO
3166 alpha- 2
szabvány szerint
taxpayerAddressItem/taxpayerAddress/postalCode xs:string igen Irányítószám
taxpayerAddressItem/taxpayerAddress/city xs:string igen Város
taxpayerAddressItem/taxpayerAddress/streetName xs:string igen Közterület neve
taxpayerAddressItem/taxpayerAddress/publicPlaceCategory xs:string igen Közterület jellege
taxpayerAddressItem/taxpayerAddress/number xs:string nem Házszám
taxpayerAddressItem/taxpayerAddress/building xs:string nem Épület
taxpayerAddressItem/taxpayerAddress/staircase xs:string nem Lépcsőház
taxpayerAddressItem/taxpayerAddress/floor xs:string nem Emelet
taxpayerAddressItem/taxpayerAddress/door xs:string nem Ajtó
taxpayerAddressItem/taxpayerAddress/lotNumber xs:string nem Helyrajzi szám
```
**Facetek és leírók**

```
Tag SimpleType Patter
n
```
```
Enum Defa
ult
infoDate - - - -
taxpayerValidity - - - -
taxpayerData/taxpayerName SimpleText512NotBlan
kType
```
```
.*[^\s]
.*
```
##### - -

```
taxpayerData/taxpayerShortName SimpleText200NotBlan
kType
```
```
.*[^\s]
.*
```
##### - -

```
taxNumberDetail/taxpayerId TaxpayerIdType [0-
9]{8}
```
##### - -

```
taxNumberDetail/vatCode VatCodeType [1-
5]{1}
```
##### - -


```
taxNumberDetail/countyCode CountyCodeType [0-
9]{2}
```
##### - -

```
taxpayerData/incorporation IncorporationType - ORGANIZATIO
N,
SELF_EMPLOY
ED,
TAXABLE_PER
SON
taxpayerData/vatGroupMembership TaxpayerIdType [0-
9]{8}
```
##### - -

```
taxpayerAddressItem/taxpayerAddressType TaxpayerAddressType
Type
```
##### - HQ, SITE,

##### BRANCH

##### -

```
taxpayerAddressItem/taxpayerAddress/country
Code
```
```
CountryCodeType [A-
Z]{2}
```
##### - -

```
taxpayerAddressItem/taxpayerAddress/region SimpleText50NotBlank
Type
```
```
.*[^\s]
.*
```
##### - -

```
taxpayerAddressItem/taxpayerAddress/postalC
ode
```
```
PostalCodeType [A-Z0-
9]{4,1
0}
```
##### - -

```
taxpayerAddressItem/taxpayerAddress/city SimpleText255NotBlan
kType
```
```
.*[^\s]
.*
```
##### - -

```
taxpayerAddressItem/taxpayerAddress/streetN
ame
```
```
SimpleText255NotBlan
kType
```
```
.*[^\s]
.*
```
##### - -

```
taxpayerAddressItem/taxpayerAddress/publicPl
aceCategory
```
```
SimpleText50NotBlank
Type
```
```
.*[^\s]
.*
```
##### - -

```
taxpayerAddressItem/taxpayerAddress/number SimpleText50NotBlank
Type
```
```
.*[^\s]
.*
```
##### - -

```
taxpayerAddressItem/taxpayerAddress/buildin
g
```
```
SimpleText50NotBlank
Type
```
```
.*[^\s]
.*
```
##### - -

```
taxpayerAddressItem/taxpayerAddress/staircas
e
```
```
SimpleText50NotBlank
Type
```
```
.*[^\s]
.*
```
##### - -

```
taxpayerAddressItem/taxpayerAddress/floor SimpleText50NotBlank
Type
```
```
.*[^\s]
.*
```
##### - -

```
taxpayerAddressItem/taxpayerAddress/door SimpleText50NotBlank
Type
```
```
.*[^\s]
.*
```
##### - -

```
taxpayerAddressItem/taxpayerAddress/lotNum
ber
```
```
SimpleText50NotBlank
Type
```
```
.*[^\s]
.*
```
##### - -

**Leírás és kapcsolódó követelmények**

```
1) A taxpayerValidity tag értéke akkor true, ha a lekérdezett adószám létezik. Nem érvényes vagy
nem létező adószámra false érték kerül visszaadásra.
2) A válaszban a taxpayerData csomópont akkor képződik, ha a lekérdezett adószám létezik. Az
adózó teljes neve minden esetben ismert.
3) Az adózó rövid nevét a taxpayerShortName tag jelöli a válaszban.
4) A vatGroupMembership tag tartalmazza a lekérdezett adózó áfacsoport tagságát, ha az adózó
tagja áfacsoportnak.
5) A kliens oldalán diszkrecionális, hogy a visszakapott információt hogyan és milyen mértékben
építi be a számlakiállítás folyamatába.
6) Az infoDate az adózó adatainak utolsó változását mutatja.
```

```
7) A taxNumberDetail csomópont tartalmazza a lekérdezett adózó teljes adószámát, az
invoiceData sémaleíró szerinti formátumban.
8) Az adózói címadatok listaként szerepelnek, mivel egy adózóhoz több címadat is tartozhat. A
címtípus megfeleltetése: HQ=Székhely, SITE=Telephely, BRANCH=Fióktelep
9) Az incorporation tag jelöli a lekérdezett adózó gazdasági típusát. Lehetséges értékei:
```
- ORGANIZATION: gazdasági társaság,
- SELF_EMPLOYED: egyéni vállalkozó
- TAXABLE_PERSON: adószámos magánszemély.

#### 1.8.10 A /tokenExchange operáció

A /tokenExchange a számlaadat-szolgáltatás beküldését megelőző egyszer használatos
adatszolgáltatási token kiadását végző operáció.

**1.8.10.1 TokenExchangeRequest**
A /tokenExchange operáció kérésének struktúráját a TokenExchangeRequest element tartalmazza.

## 36. ábra A TokenExchangeRequest felépítése

A típus a BasicOnlineInvoiceRequestType-ot terjeszti ki, azonban az operáció azon kívül semmilyen

kiegészítő paraméter megadását nem igényli. A kliens egyszerűen az endpoint címzésével és egy
authentikáció elvégzésével jelzi az adatszolgáltatási token igénylésre vonatkozó kérését.

A TokenExchangeRequest/user/ **predecessorTaxNumber** tag megadása esetén validálásra kerül a
jogelőd adószáma, azonban további hatása nincs az operációra.

**1.8.10.2 TokenExchangeResponse**
A /tokenExchange operáció válaszának struktúráját a TokenExchangeResponse element tartalmazza.


## 37. ábra A TokenExchangeResponse felépítése

A típus a BasicOnlineInvoiceResponseType-ot terjeszti ki, így az abban foglalt elemeken kívül az AES-
128 ECB titkosítási algoritmussal elkódolt adatszolgáltatási tokent, valamint annak érvényességi
intervallumát tartalmazza.

```
Tag Típus Kötelező Tartalma
encodedExchangeToken xs:base64Binary igen Az elkódolt adatszolgáltatási token
tokenValidityFrom xs:dateTime igen Az adatszolgáltatási token
érvényességének kezdete
tokenValidityTo xs:dateTime igen Az adatszolgáltatási token
érvényességének vége
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
encodedExchangeToken - - - -
tokenValidityFrom InvoiceTimestampType \d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.\d{1,3})?Z
minInclusive = 2010 - 01 -
01T00:00:00Z
```
##### - -

```
tokenValidityTo InvoiceTimestampType \d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.\d{1,3})?Z
minInclusive = 2010 - 01 -
01T00:00:00Z
```
##### - -


**Leírás és kapcsolódó követelmények**

```
1) Az AES-128 szimmetrikus kulcsú titkosítás. A kiadott adatszolgáltatási token azonosítója a
műveletet kérvényező technikai felhasználó cserekulcsával kerül kódolásra, és a hívó
ugyanezen kulcs ismeretében dekódolhatja azt. A /manageInvoice operáció a dekódolt token
értékét várja, az elkódolt token önmagában semmilyen művelet elvégzésére nem jogosít!
2) A kiadott adatszolgáltatási token érvényességének kezdete és vége UTC időzónában van
meghatározva, hogy minden időzónában lévő kliens egyértelműen tudja az érvényességi
intervallumot meghatározni. Kötegelt küldés esetén erre az érvényességi intervallumra kell
fokozottan figyelemmel lenni.
```
### 1.9 LOGIKAI REFERENCIA IMPLEMENTÁCIÓ

Jelen fejezetben találhatók azon ajánlások, amelyek az adatszolgáltatás jogilag és/vagy műszakilag
komplex kérdéskörére egy lehetséges és jogszabályszerű megoldást tartalmaznak.

#### 1.9.1 Azonnaliság kezelése, adatszolgáltatások kötegelése

A számla abban az időpontban minősül kiállítottnak, amely időponttal a számlázó program az előállított
számla adatait lezárja. Az adatszolgáltatásnak tehát abban az időpontban kell teljesülnie, amely
időponttól kezdődően az adott sorszámú számla egyetlen adata sem írható felül, adattartalmát már
csak egy új számlasorszámon kibocsátott módosító vagy érvénytelenítő számlával lehet módosítani.

Természetesen az azonnaliság az észszerűség határain belül értelmezendő. Így például, ha egy adózó
úgy alakította ki a saját ügyviteli rendszerét, hogy abban több száz számla adatának jóváhagyása és
lezárása egyszerre valósul meg, és az adatok továbbítása a számlák lezárásakor megkezdődik, akkor az
azonnali továbbítás megvalósul akkor is, ha a továbbítás több órát vesz igénybe.

Hasonlóképpen elfogadott megoldás, ha az első adatszolgáltatásra kötelezett számla lezárásakor a
számlázóprogram azonnal, emberi beavatkozás nélkül tokent kér (/tokenExchange hívás) az Online
számla rendszertől, de az adaszolgáltatás beküldését (/manageInvoice hívás) késlelteti a token
érvényességének végéig vagy a séma szerint meghatározott maximális darabszám eléréséig a célból,
hogy az érvényességi idő alatt lezáruló további adatszolgáltatásra kötelezett számlák jelentése egy
kötegben megtörténhessen. A leírt megoldás kizárólag akkor jogszabályszerű, ha a folyamatban
emberi közreműködés nem történik, valamint az ütemezést szoftver logika végzi, amely az
adatszolgáltást legfeljebb az első tokenkérés érvényességi ideje alatt megkísérli beküldeni. Ha a
beküldési kísérlet sikertelen, akkor az adatszolgáltatást azonnal meg kell ismételni.

#### 1.9.2 Elveszett tranzakció azonosító kezelése, dupla adatszolgáltatások megelőzése

Az Online számla rendszer határvédelmi eszközén 60 másodperc az időtúllépés értéke. Ez azt jelenti,

hogy azon beküldött adatszolgáltatásokra, amelyekre a rendszer lassulás vagy túlterhelődés esetén
nem képes 60 másodperc alatt válaszolni, azokra a kliensek nem fognak tranzakció azonosítót
visszakapni. Ez pedig ellehetetleníti a feldolgozási eredmény lekérdezését. Mindazonáltal, a beküldött
adatok ekkor még (a beküldéstől számított 60. másodperc végén) még élnek szerver oldalon, és ott
feldolgozásra, mentésre várnak. Az adatbázisba mentésre pedig 5 perc áll rendelkezésre, ezért a
művelet sorsa (commit vagy rollback) ekkor még nem dőlt el véglegesen.

Ha a számlázóprogram nem kapott az adatszolgáltatásra timeout miatt választ, akkor ebben az esetben
az adatszolgáltatást nem szükséges azonnal megismételnie. Elfogadott az a megoldás, ha a számlázó


program a hiányzó tranzakció azonosító esetén a beküldésől (/manageInvoice vagy

/manageAnnulment hívás) számított 5 percig várakozik, majd az 5 perces várakozás leteltével listázza
az elmúlt időszakra a tranzakcióit (/queryTransactionList hívás). A listázásra vonatkozó keresési
intervallumot javasolt kellően kicsire venni (figyelemmel arra, hogy maga a kiváltó ok is jellemzően
lassuláskor következik be, ily módon a listázás gyorsabban lefuthat), de sysdate- 5
percnélmindenképpen kicsit nagyobbra, például az elmúlt 10 percre. Ha a listában szerepel olyan
tranzakció azonosító, amelyet a kliens nem ismer, akkor ott a feldolgozási eredmény lekérdezésével
(/queryTransactionStatus, ügyelve arra, hogy a returnOriginalRequest tag értéke legyen true) vissza
lehet kérni a beküldött számla adatokat is, amely által a válasz adatai alapján a számlázóprogram
adatbázisában összevezethető, hogy mely számlák mely tranzakció azonosítóhoz tartoznak. Ezt
követően a feldolgozási eredmény lekérdezése a megszokott módon ismétlődhet, ha szükséges. Ha a

tranzakció listázás eredménye szerint nincs ismeretlen tranzakció azonosító a kérdéses időszakban
(mely esetben a tranzakció szinkron hiba miatt elutasításra került) akkor a kérdéses
adatszolgáltatásokat azonnal meg kell ismételni. A leírt megoldás kizárólag akkor jogszabályszerű, ha
a folyamatban emberi közreműködés nem történik, valamint az ütemezést szoftver logika végzi, amely
a tranzakció listázást, az összevezetést, továbbá az adatszolgáltatás megismétlését a feltételek
fennállása esetén azonnal elvégzi.

### 1.10 JOGELŐDRE VONATKOZÓ MŰVELETEK............................................................................................................

#### 1.10.1 Lekérdező operációk

A számlaadat-szolgáltatással kapcsolatos lekérdező operációkon keresztül lekérdezhetőek adott adózó
jogelődjeire vonatkozó adatok, azonban a jogutódlás formájától függően bizonyos korlátozások

lehetnek érvényben (lásd 1.1.10.1. fejezet).

Amennyiben a jogelődre vonatkozik a lekérdezés, akkor az operáció kérésének struktúrájában a
predecessorTaxNumber mezőben szükséges megadni a jogelőd adószámát. Az érintett operációk és a
pontos felépítés a 1.8-as fejezetben kifejtésre került.

```
Tag Típus Kötelező Tartalma
predecessorTaxNumber xs:string nem A jogelőd adózó adószámának első 8
jegye
```
A predecessorTaxNumber töltése esetén nem a technikai felhasználóhoz tartozó adózó adataiban
történik a keresés, hanem a tagben megadott jogelőd adataiban. Tehát ebben az esetben, csak a
jogelődre vonatkozó adatok kerülnek visszaadásra a válaszban. A lekérdező operációk további
keresőparaméterei változatlanul használhatóak. A paraméter hibás megadása esetén
INVALID_PREDECESSOR_TAX_NUMBER hibakód kerül visszaadásra.

1.10.1.1 Jogelődre vonatkozó lekérdezések korlátozása

A jogutódlás formájától függően az alábbi korlátozások vannak érvényben a lekérdező operációknál.

Amennyiben a jogutódlási forma **kiválás vagy leválás** , akkor a jogutód számára:


- Kizárólag azon számlaadatok kérdezhetőek le a queryInvoiceCheck, queryInvoiceData,
    queryInvoiceDigest, queryInvoiceChainDigest operációkkal, ahol a számlán megadott
    teljesítési vagy kiállítási dátum a jogutódlás időpontjával megegyező vagy azelőtti.
- A QueryTransactionStatus és QueryTransactionList operációknál kizárólag azon tranzakciók
    kérdezhetőek le, amelyek beküldési időpontja a jogutódlás időpontjával megegyező vagy
    azelőtti. Továbbá az ilyen típusú jogelődökre vonatkozóan a QueryTransactionStatus
    operációnál tilos a returnOriginalRequest paraméter használata.

**Áfacsoportból kivált adózó** esetén az áfacsoportra vonatkozóan:

- Kizárólag azon számlaadatok kérdezhetőek le a queryInvoiceCheck, queryInvoiceData,
    queryInvoiceDigest, queryInvoiceChainDigest operációkkal, ahol a számlán megadott
    teljesítési vagy kiállítási dátum a kilépés időpontjával megegyező vagy azelőtti, illetve azon
    számlaadatok lekérdezése tilos, amelyeken a groupMemberTaxNumber mező kitöltött és eltér
    a lekérdező adószámától.
- A QueryTransactionStatus és QueryTransactionList operáció használata nem támogatott.

A fenti korlátozások megszűnt áfacsoport esetén a kijelölt képviselőre nem vonatkoznak.

#### 1.10.2 Számlaadat-szolgáltatás beküldése

A jogelőd-jogutód adózók viszonylatában kettő műveletet különböztethetünk meg:

- számlaadat-szolgáltatás pótlása
- jogelőd számlájára való hivatkozás érvénytelenítő / módosító számla esetén

1.10.2.1 Számlaadat-szolgáltatás pótlásának jelölése

A jogutód szerepkörben lévő adózó a jogelődjei tekintetében pótolhat számlaadat-szolgáltatást. Ilyen
esetben a ManageInvoiceRequest beküldője a jogutód, a számlán kiállítói pozícióban szereplő adózó
pedig valamely jogelőd.

A pótlást a következő módon szükséges jelölni az adatszolgáltatásban:

A jelzést az előre nem nevesített adatok közt szükséges szerepeltetni, mint a számla egészére
vonatkozó extra adat. A vonatkozó csomópont: **invoiceHead/invoiceDetail/additionalInvoiceData** ,

amely felépítésének részletes leírása a 2.1.5-ös fejezetben olvasható.

Pótlás esetén az additionalInvoiceData csomópont töltésénél az elvárás az alábbi:

```
Tag Típus Kötelező Tartalma
additionalInvoiceData/dataName xs:string Igen A10000_JOGELOD_POTLAS
additionalInvoiceData/dataDescription xs:string Igen Tetszőleges, pl. jogelőd nevében
pótlás
additionalInvoiceData/dataValue xs:string Igen Tetszőleges, pl. A jogutód adózó
adószámának első 8 jegye
```
A A10000_JOGELOD_POTLAS kód feltüntetése a pótlás szándékának jelölésére szolgál, helyes
megadását validáció ellenőrzi.


A kód maximum egyszer szerepelhet az additionalInvoiceData listában. Amennyiben a kód szerepel a

számlaadat-szolgáltatásban, akkor a kiállítói adószám mezőben egy jogelőd adószámának megadása
az elvárt. (a beküldő jogutód saját adószámának megadása error hibát eredményez.)

**Számlaadat-szolgáltatás pótlásának korlátozása:**

- Amennyiben a jogutódlási forma **kiválás vagy leválás** , akkor a levált vagy kivált jogutód
    számára nem engedélyezett a pótlás. Kiválás (ide értve az áfacsoportból való kiválást is) és
    leválás esetén a kiválást, leválást megelőzően kiállított számláról teljesítendő
    adatszolgáltatást csak a fennmaradó adóalany (amelyből a kiválás, leválás történt)
    pótolhatja.
- **Csoportos áfaalany** (áfakód = 5) számára tiltott a pótlás művelete.

1.10.2.2 Jogelőd számlájára való hivatkozás jelölése

Ebben az esetben a jogutód szerepkörben lévő adózó küld be egy módosító / érvénytelenítő számlát.
Kiállítói pozícióban a jogutód szerepel. Az eredeti számla sorszámának feltüntetése az
invoiceReference/originalInvoiceNumber csomópontban tehető meg. A jogelőd számlájára való
hivatkozás feltüntetésével jelezhető, hogy nem a kiállító adózó saját, hanem egy jogelőd számlájára
történik a módosítás/érvénytelenítés beküldése. Előfordulhat, hogy ugyanazon sorszámú számlát,
mind a jogelőd és mind a jogutód kiállította. Ezért egyértelműen jelezni kell, hogy melyik számlának az

adatai kerülnek módosításra.

A modifyWithoutMaster tag töltése a saját számlákhoz hasonlóan az eredeti számlaadat-szolgáltatás
létezőségének megfelelően töltendő. Ezt validáció ellenőrzi
(MODIFY_WITHOUT_MASTER_MISMATCH, INVALID_INVOICE_REFERENCE).

Jogelődre való hivatkozás során továbbá elvárt a jogelőd és jogutódhoz tartozó számlalánc elemeken
a modificationIndex és a lineNumber egyediség biztosítása, amelyet szintén validáció kényszerít ki
(MODIFICATION_INDEX_NOT_UNIQUE, INVOICE_LINE_ALREADY_EXIST).

A jogelőd számlájára való hivatkozás jelzését az előre nem nevesített adatok közt szükséges
szerepeltetni az **invoiceHead/invoiceDetail/additionalInvoiceData** csomópontban, amelyet a
következők szerint kell tölteni:

```
Tag Típus Kötelező Tartalma
additionalInvoiceData/dataName xs:string Igen A10000_JOGELOD_ADOSZAM
additionalInvoiceData/dataDescription xs:string Igen Tetszőleges leírás, pl. jogelőd
számlájára való hivatkozás
additionalInvoiceData/dataValue xs:string Igen A jogelőd adózó adószámának
törzsszáma (első 8 számjegye), akinek
a számlájára hivatkozás történik
```
A kékkel jelölt adatok helyes megadását validáció ellenőrzi. A A10000_JOGELOD_ADOSZAM kód
maximum egyszer szerepelhet az additionalInvoiceData listában.


#### 1.10.3 Jogelőd adatszolgáltatásainak technikai érvénytelenítése

Jogelőd(ök) adatszolgáltatásának technikai érvénytelenítéséhez a ManageAnnulmentRequest
kérésben szükséges szerepeltetni a user/predecessorTaxNumber mezőt, ezzel jelezve, hogy a technikai
érvénytelenítésben megjelölt számlaszám nem az autentikált adózó számlái között keresendő, hanem
a megjelölt jogelőd számlái között.

A jogelődnél a referenciaként megadott számla létezőségét validáció ellenőrzi.
(INVALID_ANNULMENT_REFERENCE). Egy adott számlára továbbra is maximum 1 elbírálás alatt lévő

technikai érvénytelenítési kérés létezhet, amelyet validáció kényszerít ki
(ANNULMENT_IN_PROGRESS).

Amennyiben a technikai érvénytelenítés olyan számla adatszolgáltatására érkezik, amelyhez
kapcsolódóan már történt módosításról/érvénytelenítésről is adatszolgáltatás, akkor a technikai
érvénytelenítés automatikusan, külön kérés nélkül vonatkozik mindegyik módosításról történő
adatszolgáltatásra is, de csak az adott adózó viszonylatában. Abban az esetben, ha a technikai
érvénytelenítéssel érintett számlára vonatkozóan létezik az adózó valamely jogutódjánál arra
hivatkozó módosításról/érvénytelenítésről adatszolgáltatás, akkor a jogelőd számlájáról teljesített
számlaadat-szolgáltatás technikai érvénytelenítése NEM érinti a jogutód(ok) arra hivatkozó
adatszolgáltatásait.

1.10.3.1 Jogelőd számlaadat-szolgáltatására vonatkozó technikai érvénytelenítés korlátozása

A jogelőd számlaadat-szolgáltatására vonatkozó technikai érvénytelenítés beküldéséreaz alábbi
korlátozások vannak érvényben:

- Amennyiben a jogutódlási forma **kiválás vagy leválás** , akkor a kivált/levált jogutód számára
    nem engedélyezett a jogelőd adatszolgáltatásainak technikai érvénytelenítése (kiválás, leválás
    esetében a számlaadat-szolgáltatás technikai érvénytelenítését, illetve az adatszolgáltatás
    javítását a tovább működő adóalany végzi).
- **Csoportos áfaalany** (áfakód = 5) számára tilos a jogelődök adatszolgáltatásainak technikai
    érvénytelenítése (a csoportos adóalanyiság előtti időszakra a számlaadat-szolgáltatás
    technikai érvénytelenítését, illetve az adatszolgáltatás javítását a tag végzi).

## 2 SZÁMLAADAT-SZOLGÁLTATÁS ÜZLETI TARTALOM LEÍRÁSA

Ez a fejezet a számlázó programok online adatszolgáltatásán belül a számla vagy a módosítás leírására

szolgáló Invoice elem (típusa: InvoiceDataType) elvárt tartalmát mutatja be részletesen.

Az adatszolgáltatás keretében beküldött számlaadatokat a
ManageInvoiceRequest/invoiceoperations/invoiceOperation/InvoiceData elembe kell beágyazni
BASE64 kódolt formában, mely elem leírása „ **A /manageInvoice operáció”** fejezetben található.

Az InvoiceData elem vagy egy számláról/módosításról történő adatszolgáltatásra (invoice elem), vagy
egy számlasorszám alatt több módosító okiratra vonatkozóan tartalmaz közlést (batchInvoice elem).


## 38. ábra Az InvoiceDataType

Ha az adatszolgáltatás számláról (invoiceOperation = CREATE), vagy csak 1 darab módosító okiratról
(invoiceOperation = MODIFY, STORNO) tartalmaz információkat, úgy az invoiceMain csomóponton
belül az invoice elemet kell képezni. Ha az adatszolgáltatás ún. kötegelt módosítást (egy számlászámon
legalább 2 másik számla módosítását végzik el) tartalmaz, úgy kizárólag ebben az esetben lehetőség
van az invoiceMain csomóponton belül a batchInvoice elemet képezni.

Ez a fejezet a számláról/módosításról történő adatszolgáltatás részletes leírásával foglalkozik. A
kötegelt módosítás szabályait az „ **Adatszolgáltatás több számlát módosító okiratról”** szóló fejezet,
míg a korábbi adatszolgáltatás technikai érvénytelenítésével kapcsolatos tudnivalókat a „ **Korábbi
adatszolgáltatás technikai érvénytelenítése”** fejezet tartalmazza.

### 2.1 A SZÁMLA/MÓDOSÍTÁS SÉMA ÁLTALÁNOS JELLEMZŐI

Ebben a fejezetben a számlát vagy módosító okiratot leíró séma általános jellemzői szerepelnek. A
séma részletes tartalmával „ **A számla/módosítás séma részletes tartalma”** fejezet foglalkozik.

#### 2.1.1 Az InvoiceDataType komplex típus szerkezete

Az invoiceData elem tartalmazza a számla vagy számlával egy tekintet alá eső okirat felső szintű adatait,
a számla vagy módosító okirat sorszámát, illetve a számla vagy módosító okirat kiállításának napját. A
fenti adatok kiemelése azért szükséges, mert kötegelt módosítás esetén a számla belső tartalma
módosításonként eltérhet, azonban a számla száma és a számla kiállításának napja az egyes
módosításokra vonatkozóan minden esetben azonos lesz.


```
Tag Típus Kötelező Tartalma
invoiceNumber xs:string Igen Számla vagy módosító okirat
sorszáma - Áfa tv. 169. § b) vagy
```
170. § (1) bek. b) pont
invoiceIssueDate xs:date Igen Számla vagy módosító okirat
kelte - Áfa tv. 169. § a), Áfa tv.
170. § (1) bek. a)
completenessIndicator xs:boolean Igen Jelöli, ha az adatszolgáltatás
maga a számla

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
invoiceNumber SimpleText50NotBlankType .*[^\s].* - -
invoiceIssueDate InvoiceDateType \d{4}-\d{2}-\d{2}
minInclusive = 2010- 01 - 01
```
##### - -

```
completenessIndicator - - - false
```
A csomópont minden eleme saját típussal rendelkezik, amely összetett típus (complexType), vagy
egyszerű típus (simpleType) lehet. A konkrét számlaadatokat az egyszerű típusú elemek (simpleType)
tartalmazzák.

#### 2.1.2 Adatok kötelezősége

Az online adatszolgáltatásról szóló jogszabály (23/2014. (VI.30.) NGM rendelet) a számlákon általában
megjelenő adatoknak csak egy részéről, meghatározóan az Áfa tv. által megkövetelt adattartalomról
teszi kötelezővé az adatszolgáltatást. Lehetőség van azonban a kötelezőn túli adattartalom közlésére
is. A sémadefiníció kialakítása úgy történt meg, hogy az alkalmas legyen a számla teljes
adattartalmának leírására. Az adatszolgáltatásban főszabály szerint azokat az adatokat kötelező

szerepeltetni, amelyeket az Áfa tv. a számla/módosító okirat kötelező adattartalmaként határoz meg.
Egyes kötelező adattartalomként definiált adatokat azonban csak meghatározott esetekben kell a
számlán feltüntetni. Ilyen például a fordított adózás jelölése, amely akkor kötelező, ha az adott számlán
szereplő tétel fordítottan adózik (például gabona). Az ilyen adatokat értelemszerűen csak akkor kell az
adatszolgáltatásban szerepeltetni, ha relevánsak az adott számla/módosító okirat szempontjából.

A számlákon különböző adatok feltüntetéséről rendelkező jogszabályok általában csak azt határozzák
meg, hogy az adott elemet szerepeltetni kell a számlán. Egy konkrét adat – tartalmától függően –
vonatkozhat az egész számlára, például a számla pénzneme, vagy a számla egy tételére, például
fordítottan adózó termék. Az ilyen elemek nevesítése mindig az értelmüknek megfelelő számla- vagy
számlatételszinten történt.

Az adózó saját döntése alapján határozhat úgy, hogy az adatszolgáltatásban a kötelezőnél bővebb

adatkört szerepeltet, például azért, mert az adatszolgáltatásban megképzett és a NAV-nak beküldött
állományt a saját döntése alapján egyéb célra is használja (például elektronikus számlaként, a vevő
külön értesítésére, saját feldolgozórendszerében átmeneti fájlként stb).

A számla adatait leíró sémaállomány (invoiceData.xsd) lehetőséget biztosít a számlán szereplő további
adatok (például adótörvények^2 által megkövetelt adattartalom, vagy a számlán az adózó saját

(^2) Például a jövedéki törvény, termékdíj törvénystb.


elhatározásából szereplő adatok) szerepeltetésére is. Így a sémaállomány több olyan elemet is

tartalmaz, amelyet semelyik számlaadat-szolgáltatás esetén nem kötelező használni. A jogszabály
biztosítja azt a lehetőséget, hogy a számlázó programok az adatexportra vonatkozó kötelezettséget is
a jelen séma szerinti állomány létrehozásával teljesítsék. Így az online adatszolgáltatás opcionális
adatai az adatexportban kötelezőek lehetnek. Figyelemmel kell lenni arra, hogy a séma csak olyan
esetben jelöl (technikai értelemben) kötelezőként egy elemet, ha az Áfa tv. alapján az a számla vagy az
adatszolgáltatás kötelező adatát képezi, továbbá minden számla és módosítás esetén releváns, az
adatszolgáltatásban megkövetelt is. Ilyen adat például a számla egyedi azonosítója (sorszáma). Ha az
Áfa tv. által kötelezőként definiált számlaadat (például pénzügyi képviselő adatai) nem feltétlenül
szerepel minden egyes szabályos adattartalmú számlán és módosító okiraton, akkor ezen adat
feltüntetésére szolgáló elemet a séma nem jelöli kötelezőnek.

Több helyen előfordul, hogy egy szülőelemet a sémadefiníció nem jelöl kötelezőnek, de valamely
gyerekelemét igen. Ilyen például a pénzügyi képviselő adatai szülőelem (FiscalRepresentativeInfo) és
annak egyes gyermekelemei. Ebben az esetben a szülőelem szerepeltetése nem kötelező (hiszen nem
feltétlenül értelmezett egy adott számla vonatkozásában), de ha a szülőelem feltüntetésre kerül, akkor
a kötelezőként jelölt gyermekelemeinek szerepelni kell.

**Az egyes adatokat a számlát leíró XML azon elemében kell szerepeltetni, amelyikben annak a helyét
a vonatkozó XSD annotációi és jelen tájékoztató kijelöli.**

A fejlesztői munka megkönnyítése érdekében, ezen dokumentum 2. mellékletében szereplő táblázat
összefoglalva tartalmazza, hogy az Áfa törvény, mely adatok szerepeltetését követeli meg.

#### 2.1.3 Címadatok a sémában

Az adatszolgáltatásban több helyen is kell vagy lehet címadatokat szerepeltetni. Így a szállító (eladó)
adatai között, a vevő adatai között, a pénzügyi képviselő (ha releváns) adatai között, illetve speciális
esetben egyéb helyen is.

A címadatok leírására az invoiceBase.xsd-ben található AddressType komplex típus szolgál, ami vagy
egy egyszerű címet (simpleAddress elem, típusa: SimpleAddressType), vagy egy részletes címet

(detailedAddress, típusa: DetailedAddressType) tartalmazhat.

## 39. ábra Az AddressType felépítése

Tekintettel arra, hogy a sémában címadatok többször is szerepelnek, a típus itt kerül ismertetésre.

Az adatszolgáltatásban a számlán szereplő címadatot szükséges a megfelelő címtípus szerinti
bontásban szerepeltetni.


**2.1.3.1 Egyszerű címadat**

## 40. ábra A SimpleAddressType felépítése

```
Tag Típus Kötelező Tartalma
countryCode xs:string Igen Az országkód az ISO 3166 alpha-
2 szabvány szerint
region xs:string Nem Tartomány kódja (ha
értelmezhető az adott
országban) az ISO 3166-2 alpha
2 szabvány szerint
postalCode xs:string Igen Irányítószám (ha nem
értelmezhető, 0000 értékkel kell
kitölteni)
city xs:string Igen Település
additionalAddressDetail xs:string Igen További címadatok (például
közterület neve és jellege,
házszám, emelet, ajtó, helyrajzi
szám, stb.)
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
countryCode CountryCodeType [A-Z]{ 2 } - HU
region SimpleText50NotBlankType .*[^\s].* - -
postalCode PostalCodeType [A-Z0-9][A-Z0-
9 \s\-]{1,8}[A-Z0-9]
```
##### - -

```
city SimpleText255NotBlankType .*[^\s].* - -
additionalAddressDetail SimpleText255NotBlankType .*[^\s].* - -
```
Egyes esetekben előfordulhat, hogy az adatszolgáltatásban szerepeltetendő címadat részletes típus
szerinti bontása nem valósítható meg. Tipikus példa az olyan áfaregisztrált adóalany, akinek a
székhelye szerinti országban nem létezik utcanév és házszám szerinti bontás a postacímekben (például


Costa Rica), vagy a közterület neve és jellege nem bontható szét az adott nyelv sajátosságai miatt

(például Beispielstrasse, Hillakatu).

Ugyancsak előfordulhat, hogy az adatszolgáltatásra kötelezett meglévő rendszerében tárolt vevő
címadatok csak aránytalanul nagy erőforrás ráfordításával volnának a részletes típus szerinti
bontásban előállíthatók. Ilyen esetekben a címadat az egyszerű címadat szerinti tagolásban is
szerepelhet az adatszolgáltatásban.

Egyes speciális esetekben az irányítószám sem értelmezhető az adott országban (például Írország),
ilyenkor az irányítószám (PostalCode) elemet „0000” karaktersorozattal kell feltölteni. Az irányítószám
formátuma támogatja példálul a csak 3 karakter hosszú, illetve a szóközt és kötőjelet tartalmazó
irányítószám formátumokat. Más speciális esetekben, ha az adott ország irányítószáma pontosan
feltüntetve a séma szerint érvénytelen, az irányítószámot a séma szerint érvényesre célszerű

konvertálni.

Megjegyzendő, hogy magyar adószámoknál a NAV nyilvántartása szerinti székhelycím gép-gép
kapcsolaton keresztül bármikor lekérdezhető. Erről „ **A /queryTaxpayer operáció”** című fejezet ad
tájékoztatást.


**2.1.3.2 Részletes címadat**

## 41. ábra A DetailedAddressType felépítése

```
Tag Típus Kötelező Tartalma
countryCode xs:string Igen Az országkód ISO 3166 alpha- 2
szabvány szerint
region xs:string Nem Tartomány kódja (ha
értelmezhető az adott
országban) az ISO 3166-2 alpha
2 szabvány szerint
postalCode xs:string Igen Irányítószám (ha nem
értelmezhető, 0000 értékkel kell
kitölteni)
city xs:string Igen Település
streetName xs:string Igen Közterület neve
publicPlaceCategory xs:string Igen Közterület jellege
number xs:string Nem Házszám
building xs:string Nem Épület
```

```
staircase xs:string Nem Lépcsőház
floor xs:string Nem Emelet
door xs:string Nem Ajtó
lotNumber xs:string Nem Helyrajzi szám
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
countryCode CountryCodeType [A-Z]{2} - HU
region SimpleText50NotBlankType .*[^\s].* - -
postalCode PostalCodeType [A-Z0-9][A-Z0- 9 \s\-]{1,8}[A-
Z0-9]
```
##### - -

```
city SimpleText255NotBlankType .*[^\s].* - -
streetName SimpleText255NotBlankType .*[^\s].* - -
publicPlaceCategory SimpleText50NotBlankType .*[^\s].* - -
number SimpleText50NotBlankType .*[^\s].* - -
building SimpleText50NotBlankType .*[^\s].* - -
staircase SimpleText50NotBlankType .*[^\s].* - -
floor SimpleText50NotBlankType .*[^\s].* - -
door SimpleText50NotBlankType .*[^\s].* - -
lotNumber SimpleText50NotBlankType .*[^\s].* - -
```
Egyes esetekben (például áfaregisztrált adóalanyoknál) szükséges lehet a címadatban az országon
belüli régió szerepeltetése is, mivel számos országban fordul elő pontosan ugyanaz a településnév
országon belül többször úgy, hogy különböző nagyobb közigazgatási egységben (tartomány, megye
stb.) vannak. Ilyen esetekben a cím csak a régió megadásával egyértelmű.

#### 2.1.4 Adószámok a sémában

A gazdasági eseményt leíró számla, illetve módosítás adatai között kiemelt jelentősége van a gazdasági
eseményben részt vevő két fél, a szállító (eladó) és a vevő egyértelmű azonosításának.

A számlát vagy módosítást leíró adatszerkezetben az alábbi helyeken kell vagy lehet adószámot, vagy
adószámokat feltüntetni:

- a szállító (eladó) adatai között,
- a vevő adatai között,
- pénzügyi képviselő^3 megbízása esetén a pénzügyi képviselő adatai között,
- illetve a termékdíj fizetésére kötelezett adatai között speciális esetben.

A szállító (eladó) adatai között a számlán kötelező feltüntetni azt az adószámot, ami alatt a gazdasági
esemény történt (supplierTaxNumber elem, típusa: TaxNumberType). Ha az eladó csoportos áfaalany
tagja, akkor – az Áfa tv. előírásainak megfelelően – az eladó adóalany a csoport. A csoporttag
adószámát pedig a groupMemberTaxNumber elemben (típusa: TaxNumberType) kell feltüntetni, ha ez
szerepel a számlán. A szállító közösségi (uniós) adószáma pedig a communityVatNumber elemben
(típusa: CommunityVatNumberType) szerepeltethető, ha az szerepel a számlán.

(^3) Áfa törvény 148-149. §


A 3.0-ás számla verzió és a 2021. január 4 - től hatályos jogszabályok értelmében a **vevői** adatok, többek

között az adószám megadási módja, eltér a korábbi verziókhoz képest, így az a következő, különálló
alfejezetben lesz kifejtve.

Megjegyzendő, hogy a közösségi, illetve harmadik országbeli adószámoknak elsősorban adatexport
esetén van jelentősége 2021. január 4 - ig. 2021. január 4 - től az Áfa tv. változása miatt, ezek a számlák
is adatszolgáltatásra kötelezettek. A közösségi adómentes értékesítés esetén a közösségi adószám
szerepeltetése kötelező mind a számlán, mind pedig az adatszolgáltatásban vevői és eladói oldalon is.
A harmadik országbeli vevőnek történő értékesítés esetén a vevői adószám szerepeltetésére nincs
jogszabályi kötelezettség, ugyanakkor a sémában dedikált tagje van ezen adószámnak.

A pénzügyi képviselő adatai között egy magyar adószám feltüntetése kötelező a
fiscalRepresentativeTaxNumber elemben (típusa: TaxNumberType).

## 42. ábra A TaxNumberType felépítése

```
Tag Típus Kötelez
ő
```
```
Tartalma
```
```
taxpayerId xs:string Igen Az adóalany adó törzsszáma.
Csoportos adóalany esetén
csoportazonosító szám
vatCode xs:string Nem Áfakód az adóalanyiság
típusanak jelzésére. Egy
számjegy
countyCode xs:string Nem Megyekód, két számjegy
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
taxpayerId TaxpayerIdType [0-9]{8}
vatCode VatCodeType [1-5]{1}
countyCode CountyCodeType [0-9]{2}
```
Az adatszolgáltatási kötelezettséggel érintett számlák mindegyikében a szállító (eladó) rendelkezik
magyarországi adószámmal. Minden esetben ezt a magyar adószámot kell feltüntetni a
supplierInfo/supplierTaxNumber elemben. Ha a szállító (eladó) csoportos áfaalany, akkor a
csoportazonosító számát (áfa-kódja: „5”) kell a supplierInfo/supplierTaxNumber elemben
szerepeltetni, míg a csoporttag „saját” adószámát (áfakódja: „4”) a

supplierInfo/groupMemberTaxNumber elemben kell megadni.


2.1.4.1 Vevői adószám

A termékbeszerző, szolgáltatás igénybevevő belföldi adószámának, közösségi adószámának számlán
való kötelező feltüntetésére vonatkozó előírásokat az Áfa tv. 169. § d) pontja tartalmazza. A d) pont
alapján a belföldi értékesítésnél az adóalany vevő adószámának első nyolc számjegyét, a csoportos
általános forgalmi adóalanyiság esetén a csoportazonosító számának első nyolc számjegyét kötelező a
számlán, és így az adatszolgáltatásban is szerepeltetni. Ezen szabály alól kivételt képeznek azok a
számlakibocsátók, amelyek gazdasági céllal belföldön nem letelepedett, gazdasági célú letelepedés
hiányában a lakóhelye, szokásos tartózkodási helye nem belföldön van (kizárólag áfaregisztrációval
rendelkeznek). Számukra a belföldi vevő adószámának feltüntetési kötelezettsége nincsen (de
lehetősége van rá), így adatszolgáltatásban sem jelenik meg feltétlenül ezen adóalanyi körnél a belföldi

vevő adószáma.

A fentiekhez képest a belföldi fordított adózású számláknál a szabályt annyival kell kiegészíteni, hogy
a vevő adószámának nem csupán az első nyolc számjegyét, hanem a teljes adószámot fel kell tüntetni
a számlán és ezt az adatszolgáltatásnak is tartalmaznia kell. Ha az ügylet nem a belföldi fordított adózás
szabályai (Áfa tv. 142. §), hanem másik tagállamban, vagy harmadik országban teljesítettként tartozik
fordított adózás alá (az Áfa tv. 139-140. §-aiban foglaltakhoz hasonló szabályok alapján), akkor a
termékbeszerző, szolgáltatást igénybevevő harmadik országbeli adószámát (ha van ilyen), illetve másik
tagállami közösségi adószámát kötelező feltüntetni a számlán.

A közösségen belüli adómentes termékértékesítés esetén az Áfa tv. a közösségi adószám

szerepeltetését főszabály szerint elvárja a számlán, így az adatszolgáltatásnak is kötelező elemét
képezi.

2021. január 4 - től a nem adóalany magánszemélyeknek kiállított számlák adatszolgáltatása is kötelező.
Ilyen számlák esetén csak a magánszemély vevőtípus jelölése (customerVatStatus = PRIVATE_PERSON)
kötelező, semmilyen egyéb vevői adat nem szerepeltethető azadatszolgáltatásban. Ettől a számlának
kötelező adattartalma a magánszemély vevő neve, címe, ugyanakkor a számlaadattól ebben az
esetben eltér az adatszolgáltatás tartalma. Ha a vevő magánszemély (customerVatStatus =
PRIVATE_PERSON), akkor az adóhivatali rendszer nem fogad be olyan adatszolgáltatást, mely tartalmaz
vevői név és/vagy címadatot, bármi is szerepel ezekben a mezőkben.

A belföldi adószám helye a customerTaxNumber elem (típusa: CustomerTaxNumberType).

Amennyiben a vevő státusza belföldi adóalany (customerVatStatus = DOMESTIC), akkor az áfa
regisztrált számlakibocsátónak az egyenes adózású ügylete kivételével kötelező a belföldi adóalany
adószámának feltüntetése. Amennyiben a vevő belföldi adóalany (customerVatStatus = DOMESTIC) és
a belföldi adószám (customerTaxNumber) nincs kitöltve, akkor az adatszolgáltatást az adóhivatali
rendszer nem fogja befogadni (áfa regisztrált értékesítő kivételével).

Ha a vevő belföldi csoportos áfaalany, akkor – az Áfa tv. szerint – a vevő adószámaként a csoport
azonosító számát kell megadni, a csoporttag adószámát pedig a groupMemberTaxNumber elemben
(típusa: TaxNumberType) lehet feltüntetni, ha ez szerepel a számlán. A vevő közösségi (uniós)
adószáma a communityVatNumber elemben (típusa: CommunityVatNumberType) szerepeltethető, ha
szerepel a számlán. Harmadik országbeli fél harmadik országbeli adószáma a thirdStateTaxId elemben

(típusa: SimpleText50NotBlankType) szerepeltethető, ha szerepel a számlán.


A három adószám közül az adatszolgáltatásban csak egy adható meg. Ha a számlán esetlegesen több

vevői adószám szerepel (például belföldi adószám, közösségi adószám), akkor az adatszolgáltatásnál
azt az adószámot kell kiválasztani, amit Áfa tv. szerint a számlán - az ügylet sajátosságait is figyelembe
véve - fel kell tüntetni.

## 43. ábra A CustomerVatDataType felépítése

```
Tag Típus Kötelez
ő
```
```
Tartalma
```
```
customerTaxNumber/taxpayerId xs:string Igen Az adóalany adószámának
törzsszáma. Csoportos
adóalany esetén
csoportazonosító szám
customerTaxNumber/vatCode xs:string Nem Áfakód az adóalanyiság
típusanak jelzésére. Egy
számjegy
customerTaxNumber/countyCode xs:string Nem Megyekód, két számjegy
customerTaxNumber/
groupMemberTaxNumber/
taxpayerId
```
```
xs:string Igen Az adóalany adószámának
törzsszáma. Csoportos
adóalany esetén
csoportazonosító szám
```

```
customerTaxNumber/
groupMemberTaxNumber/vatCode
```
```
xs:string Nem Áfakód az adóalanyiság
típusanak jelzésére. Egy
számjegy
customerTaxNumber/
groupMemberTaxNumber/
countyCode
```
```
xs:string Nem Megyekód, két számjegy
```
```
communityVatNumber xs:string Igen Közösségi adószám
thirdStateTaxId xs:string Igen Harmadik országbeli
adóazonosító
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
customerTaxNumber/taxpayerId TaxpayerIdType [0-9]{8} - -
customerTaxNumber/vatCode VatCodeType [1-5]{1} - -
customerTaxNumber/countyCode CountyCodeType [0-9]{2} - -
customerTaxNumber/
groupMemberTaxNumber/ taxpayerId
```
```
TaxpayerIdType [0-9]{8} - -
```
```
customerTaxNumber/
groupMemberTaxNumber/vatCode
```
```
VatCodeType [1-5]{1} - -
```
```
customerTaxNumber/
groupMemberTaxNumber/ countyCode
```
```
CountyCodeType [0-9]{2} - -
```
```
communityVatNumber CommunityVatNumberType [A-Z]{2}[0-
9A-Z]{2,13}
```
##### - -

```
thirdStateTaxId SimpleText50NotBlankType .*[^\s].* - -
```
A vevő adószámának szerepeltetésére vonatkozóan egyes jellemző eseteket az alábbi táblázat mutatja
be.

```
Sorszá
m
```
```
Eset Adószám szerepeltetése és customerVatStatus töltése
```
1. Vevő
    Magyarországo
    n
    nyilvántartásba
    vett csoportos
    áfaalany és a
    számlán
    kötelező
    szerepeltetni az
    adószámát.

```
customerVatStatus = DOMESTIC
A csoportazonosító számát (áfakódja: „5”) kell a
customerInfo/customerVatData/customerTaxNumber/taxpayerId elemben
szerepeltetni, míg a csoport tag „saját” adószámát (áfakódja: „4”) a
customerInfo/customerVatData/customerTaxNumber/groupMemberTaxNumbe
r/taxpayerId elemben kell megadni.
```
2. Vevő
    Magyarországo
    n
    nyilvántartásba
    vett (nem
    csoportos)
    áfaalany és a
    számlán

```
customerVatStatus = DOMESTIC
Az adószám legalább első nyolc számjegyét (törzsszám) kell a
customerInfo/customerVatData/customerTaxNumber elemben szerepeltetni.
```

```
kötelező
szerepeltetni az
adószámát.
```
3. Vevő
    magánszemély

```
customerVatStatus = PRIVATE_PERSON
A customerVatData csomópontot ilyenkor nem szabad tölteni.
```
4. Vevő a
    Közösség másik
    tagállamában
    nyilvántartásba
    vett adóalany
    és közösségi
    adómentes
    termékértékesí
    tés az ügylet

```
customerVatStatus = OTHER
customerInfo/customerVatData/communityVatNumber töltése kötelező.
```
5. Vevő a
    Közösség másik
    tagállamában
    nyilvántartásba
    vett adóalany,
    és az ügyletet
    belföldi 27, 18
    vagy 5%-os áfa
    terheli.

```
customerVatStatus = OTHER
customerInfo/customerVatData/communityVatNumber töltése nem kötelező,
de lehetséges megadni.
```
6. A vevő
    harmadik
    országban
    letelepedett és
    az ügyletben
    nem másik
    tagállami
    adóalanyi
    minőségében
    vesz részt.

```
customerVatStatus = OTHER
customerInfo/customerVatData/thirdStateTaxId töltése nem kötelező, de
lehetséges megadni.
```
7. A vevő nem
    adóalany,
    ugyanakkor
    nem is
    magánszemély

```
customerVatStatus = OTHER
customerInfo/customerVatData egyik eleme sem adható meg, mivel a vevő nem
rendelkezik adószámmal.
```
#### 2.1.5 Előre nem nevesített adatok szerepeltetése

A típusdefiníció lehetőséget biztosít olyan adatok szerepeltetésére is, amelyek nem kerültek
nevesítésre a sémában (továbbiakban: extra adatok). Természetesen ilyen adatok szerepeltetése nem
kötelező az adatszolgáltatásban.

Szükségessé teheti extra adatok szerepeltetését, ha az adatszolgáltatásra kötelezett úgy dönt, hogy az
adatszolgáltatás érdekében előállított XML állományt saját folyamataiban is használja és az adatok


teljeskörűségének vagy könnyebb feldolgozhatóságának szempontja ezt megkívánja. Hasznos lehet a

felek számára például a vevőnek tájékoztatásul megküldött XML állományban struktúráltan feltüntetni
a számlát vagy az egyes tételeket jellemző egyezményes adatokat. Ugyancsak hasznos lehet a
számlával bizonylatolt szállítmány tömegét, térfogatát szerepeltetni az adatállományban, ha ez a vevő
vagy az eladó belső folyamataiban hatékonyság növekedést eredményezhet. A számlaadat-
szolgáltatásban csak olyan extra adatokat szabad szerepeltetni, amelyek a számlán is szerepelnek.

A séma mind a számlára, mind az egyes számlatételekre vonatkozóan biztosít lehetőséget a további
adatok feltüntetésére. Az erre szolgáló elemek:

```
Logikai egység Elem neve Elem típusa
Számla egésze additionalInvoiceData AdditionalDataType
Számla tétele additionalLineData AdditionalDataType
```
Az AdditionalDataType az alábbi elemekből épül fel:

## 44. ábra Az AdditionalDataType felépítése

```
Tag Típus Kötelező Tartalma
dataName xs:string Igen Az adatmező egyedi azonosítója
Például:
A00001_RENDELES_SZAM
X00002_SHIPMENT_ID
X0099 9 _SHIPMENT_VOLUME_
M3
dataDescription xs:string Igen Az adatmező tartalmának
szöveges leírása
dataValue xs:string Igen Az adat értéke
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
```
```
dataName DataNameType [A9]{1,249}-Z][0-9]{5}[_][_A - Z0- - -
dataDescription SimpleText255NotBlankType .*[^\s].* - -
dataValue SimpleText 512 NotBlankType .*[^\s].* - -
```

#### 2.1.6 Egyezményes, nevesített adatok szerepeltetése

Az előző fejezetben szereplő indokok miatt a 3.0 xsd verzióban megtörtént az egyezményes, nevesített
adatok feltüntetésére szolgáló mezők bevezetése.

A séma mind a számlára, mind az egyes számlatételekre vonatkozóan lehetőséget biztosít a nevesített
egyezményes adatok feltüntetésére. Az erre szolgáló elemek:

```
Logikai egység Elem neve Elem típusa
Számla egésze conventionalInvoiceInfo ConventionalInvoiceInfoType
Számla tétele conventionalLineInfo ConventionalInvoiceInfoType
```

## 45. ábra A ConventionalInvoiceInfoType felépítése

Mindenegyik csomópont opcionális, és a csomóponton belül nincs korlátozás az ismétlődésekre.

```
Tag Típus Kötelező Tartalma
```

```
orderNumbers/orderNumber xs:string Igen Megrendelésszám
deliveryNotes/deliveryNote xs:string Igen Szállítólevél szám
shippingDates/shippingDate xs:string Igen Szállítási dátum
contractNumbers/contractNumber xs:string Igen Szerződésszám
supplierCompanyCodes/supplierCo
mpanyCode
```
```
xs:string Igen Az eladó vállalati kódja
```
```
customerCompanyCodes/customer
CompanyCode
```
```
xs:string Igen A vevő vállalati kódja
```
```
dealerCodes/dealerCode xs:string Igen Beszállító kód
costCenters/costCenter xs:string Igen Költséghely
projectNumbers/projectNumber xs:string Igen Projektszám
generalLedgerAccountNumbers/ge
neralLedgerAccountNumber
```
```
xs:string Igen Főkönyvi számlaszám
```
```
glnNumbersSupplier/glnNumber xs:string Igen Kiállítói globális helyazonosító
szám
glnNumbersCustomer/glnNumber xs:string Igen Vevői globális helyazonosító
szám
materialNumbers/materialNumber xs:string Igen Anyagszám
itemNumbers/itemNumber xs:string Igen Cikkszám
ekaerIds/ekaerId xs:string Igen EKÁER azonosító
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
```
orderNumber SimpleText100NotBlankType (^) .*[^\s].* - -
deliveryNote SimpleText100NotBlankType (^) .*[^\s].* - -
shippingDate SimpleText100NotBlankType .*[^\s].* - -
contractNumber SimpleText100NotBlankType .*[^\s].* - -
supplierCompanyCode SimpleText100NotBlankType (^) .*[^\s].* - -
customerCompanyCode SimpleText100NotBlankType (^) .*[^\s].* - -
dealerCode SimpleText100NotBlankType (^) .*[^\s].* - -
costCenter SimpleText100NotBlankType (^) .*[^\s].* - -
projectNumber SimpleText100NotBlankType (^) .*[^\s].* - -
generalLedgerAccountNumber SimpleText100NotBlankType (^) .*[^\s].* - -
glnNumber SimpleText100NotBlankType (^) .*[^\s].* - -
materialNumber SimpleText100NotBlankType (^) .*[^\s].* - -
itemNumber SimpleText100NotBlankType (^) .*[^\s].* - -
ekaerId EkaerIdType [E]{1}[0-9]{6}[0-
9A-F]{8}

##### - -

Fontos megjegyezni, hogy a 3.0 verzió előtti sémában az ekaerIds csomópont még szerepelt a
tételeknél. Mivel ez belekerült a conventionalInvoiceInfo csomópontba, a line-ból ki lett vezetve a
különálló csomópont.

#### 2.1.7 Tizedes elválasztó........................................................................................................................

A tizedestörtek szerepeltetése esetén az XML 1.0 szabvány szerinti tizedespont használandó,

függetlenül attól, hogy a számlán a tizedes elválasztó karakter pont vagy vessző.


### 2.2 A SZÁMLA/MÓDOSÍTÁS SÉMA RÉSZLETES TARTALMA

Az invoice elem alapvetően 5 elemből épül fel, amely biztosítja az egységes működést valamennyi - az
elemtípussal érintett - operációban.

```
46. ábra Az InvoiceType felépítése
```
#### 2.2.1 invoiceReference

Ha az adatszolgáltatás nem eredeti számláról, hanem egy korábban kiállított számla módosításról
történik, akkor a módosító okirat (például „módosító számla”, „érvénytelenítő számla” stb.) adatait az
invoiceReference elem (típusa: invoiceReferenceType) tartalmazza.

Az elemet kizárólag a módosításról (érvénytelenítésről) történő adatszolgáltatásban kell és lehet
szerepeltetni.

## 47. ábra Az InvoiceReferenceType felépítése


```
Tag Típus Kötelez
ő
```
```
Tartalma
```
```
originalInvoiceNumber xs:string Igen Az eredeti számla sorszáma,
melyre a módosítás
vonatkozik - Áfa tv. 170. § (1)
c)
modifyWithoutMaster xs:boolean Igen Annak jelzése, hogy a
módosítás olyan
alapszámlára hivatkozik,
amelyről nem történt és nem
is fog történni
adatszolgáltatás
modificationIndex xs:int Igen A számlára vonatkozó
módosító okirat egyedi
sorszáma
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
originalInvoiceNumber SimpleText50NotBlankType .*[^\s].* - -
modifyWithoutMaster - - - false
modificationIndex InvoiceUnboundedIndexType minInclusive = 1 - -
```
Az originalInvoiceNumber elem tartalmazza annak az eredeti számlának (ahol invoiceOperation =
CREATE) a sorszámát (az eredeti számláról adott adatszolgáltatás invoiceNumber eleme), amire a
módosítás vonatkozik.

A módosító okirat „saját” sorszámát NEM az invoiceReference elem tartalmazza, azt az invoiceNumber
elemben kell szerepeltetni.

Speciális esetekben előfordulhat, hogy olyan módosító okiratról történik adatszolgáltatás, amelynek
az eredeti számlájáról még nem történt, és nem is fog történni. Ezt a tényt a modifyWithoutMaster
elem „true” értékével kell jelezni. Ilyen helyzet az alábbi esetekben állhat elő:

- az eredeti számla még 2018. július 1-jét megelőzően került kiállításra, a módosító okirat
    jelentésköteles
- az eredeti számla bár 2018. július 1-jét követően került kiállításra, de még nem volt
    jelentésköteles, és nem is történt róla adatszolgáltatás, ugyanakkor a módosító okirat
    kiállításakor már jelentéskötelessé válik
- közműszolgáltatók esetén, ha az adott elszámolószámla tartalmazza az utolsó időszak
    teljesítéséről szóló adatszolgáltatást is (lásd utilitySettlementIndicator működése)

A modificationIndex egyedi módon a módosítás sorrendiségét írja le a kiállító oldalán. Logikailag a
számla első alkalommal történő módosításáról modificationIndex = 1 értékkel kell adatot szolgáltatni.
Minden további módosítás esetén az elemben meg kell jelölni, hogy a módosító okiratról szóló
adatszolgáltatás a számla hanyadik módosítása. A modificationIndex értékét a rendszer a módosító


okiratok egyediség vizsgálatára használja fel, kétszer azonos modificationIndex értékkel nem lehet

adatot szolgáltatni. Sorrendiség ellenőrzést a rendszer a modificationIndex alapján nem végez.

Az egyediség vizsgálat azt is jelenti, hogy a korábbi verziójú (1.0, 1.1) és módosító vagy sztornó
adatszolgáltatások (ahol a modificationIndex még nem szerepelt) kiesnek az egyediség vizsgálatból. A
2.0-ás verziójú számlák viszont már beleszámítanak az egyediségvizsgálatba, mert abban a verzióban
lett bevezetve a modificationIndex mező. A rendszer nem vélelmez a korábbi verziójú (1.0, 1.1)
módosító vagy sztornó számlák között és az újabb verziójú (2.0, 3.0) módosító és sztornó számlák
között sorrendiséget, azonban a logikailag inkonszisztens módosítások (pl: a számlának már van 3
korábbi 1.x-es módosítása a rendszerben, és érkezik egy 3 .0-ás módosítás, ahol a modificationIndex
értéke 1) a kockázatkezelő rendszer bemeneti adataként szolgálhatnak.

#### 2.2.2 invoiceHead

## 48. ábra Az InvoiceHeadType felépítése

Az invoiceHead elem (típusa: InvoiceHeadType) a számla egészére (és nem az egyes számlatételek)
jellemző adatokat tartalmazza az itt szereplő sorrendben.

```
Tag Típus Kötelező Tartalma
supplierInfo SupplierInfoType Igen Számlakibocsátó (eladó) adatai
customerInfo CustomerInfoType Nem Vevő adatai
fiscalRepresentativeInfo FiscalRepresentativeT
ype
```
```
Nem Pénzügyi képviselő adatai
```
```
invoiceDetail InvoiceDetailType Igen Számla részletező adatok
```

**2.2.2.1 supplierInfo**

## 49. ábra A SupplierInfoType felépítése

```
Tag Típus Kötele
ző
```
```
Tartalma
```
```
supplierTaxNumber xs:complexType Igen Belföldi adószám, amely alatt a
számlán szereplő
termékértékesítés vagy
szolgáltatásnyújtás történt. Lehet
csoportazonosító szám is.
groupMemberTaxNumber xs:complexType Nem Csoporttag adószáma, ha a
termékértékesítés vagy
szolgáltatásnyújtás
csoportazonosító szám alatt
történt
communityVatNumber xs:string Nem Közösségi adószám
supplierName xs:string Igen Az eladó (szállító) neve
supplierAddress xs:complexType Igen Az eladó (szállító) címe
supplierBankAccountNumber xs:string Nem Az eladó (szállító)
bankszámlaszáma
individualExemption xs:boolean Nem Értéke true, ha a számlakibocsátó
(eladó) alanyi áfamentes
```

```
exciseLicenceNum xs:string Nem Az eladó adóraktári engedélyének
vagy jövedéki engedélyének
száma (2016. évi LXVIII. tv.)
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
supplierTaxNumber TaxNumberType - - -
groupMemberTaxNumber TaxNumberType - - -
communityVatNumber CommunityVatNumberType [A-Z]{2}[0-9A-Z]{2,13} - -
supplierName SimpleText512NotBlankType .*[^\s].* - -
supplierAddress AddressType - - -
supplierBankAccountNumber BankAccountNumberType [0-9]{8}[-][0-9]{8}[-][0-
9]{8}|[0-9]{8}[-][0-
9]{8}|[A-Z]{2}[0-9]{2}[0-
9A-Za-z]{11,30}
```
##### - -

```
individualExemption - - - false
exciseLicenceNum SimpleText50NotBlankType .*[^\s].* - -
```
A BankAccountNumberType típus leírása „ **Az üzleti tartalomban szereplő típusok leírása”** fejezetben
található.

Az AddressType típus a „ **Címadatok a sémában”** fejezetben került részletesen bemutatásra.

A TaxNumberType típus az „ **Adószámok a sémában”** fejezetben szerepelt.


**2.2.2.2 customerInfo**

## 50. ábra A CustomerInfoType felépítése

```
Tag Típus Kötelező Tartalma
customerVatStatus xs:complexType Igen Vevő áfa szerinti státusza
customerVatData xs:complexType Nem A vevő áfaalanyisági adatai
customerName xs:string Nem A vevő neve
customerAddress xs:complexType Nem A vevő címe
customerBankAccountNumber xs:string Nem Vevő bankszámlaszáma
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
customerVatStatus CustomerVatStatusType - DOMESTIC
OTHER
PRIVATE_PERSON
```
##### -

```
customerVatData CustomerVatDataType - - -
customerName SimpleText512NotBlankType .*[^\s].* - -
customerAddress AddressType - - -
```
customerBankAccountNumber BankAccountNumberType (^) [0-
9]{8}[-][0-
9]{8}[-][0-

##### - -


```
9]{8}|[0-
9]{8}[-][0-
9]{8}|[A-
Z]{2}[0-
9]{2}[0-9A-
Za-
z]{11,30}
```
A BankAccountNumberType típus leírása „ **Az üzleti tartalomban szereplő típusok leírása”** fejezetben

található.

Az AddressType típus a „ **Címadatok a sémában”** fejezetben került részletesen bemutatásra.

A CustomerVatDataType típus az „ **Adószámok a sémában”** fejezetben szerepelt.

A customerVatStatus lehetséges értékei:

- DOMESTIC: Belföldi áfaalany
- OTHER: Egyéb (belföldi nem áfaalany, nem természetes személy, külföldi áfaalany és külföldi nem
    áfaalany, nem természetes személy)
- PRIVATE_PERSON: Nem áfaalany (belföldi vagy külföldi) természetes személy

**2.2.2.3 fiscalRepresentativeInfo**

## 51. ábra A FiscalRepresentativeType felépítése

```
Tag Típus Kötelező Tartalma
fiscalRepresentativeTaxNumber xs:complexType Igen A pénzügyi képviselő adószáma
fiscalRepresentativeName xs:string Igen A pénzügyi képviselő neve
fiscalRepresentativeAddress xs:complexType Igen Pénzügyi képviselő címe
fiscalRepresentativeBankAccountN
umber
```
```
xs:string Nem Pénzügyi képviselő által a
számlakibocsátó (eladó)
számára megnyitott bankszámla
bankszámlaszáma
```
**Facetek és leírók**


```
Tag SimpleType Pattern Enum Default
fiscalRepresentativeTaxNumber TaxNumberType - - -
fiscalRepresentativeName SimpleText512NotBlankType .*[^\s].* - -
fiscalRepresentativeAddress AddressType - - -
fiscalRepresentativeBankAccountNumber BankAccountNumberType [0-9]{8}[-][0-
9]{8}[-][0-
9]{8}|[0-
9]{8}[-][0-
9]{8}|[A-
Z]{2}[0-
9]{2}[0-9A-
Za-z]{11,30}
```
##### - -

A BankAccountNumberType típus leírása „ **Az üzleti tartalomban szereplő típusok leírása”** fejezetben
található.

Az AddressType típus a „ **Címadatok a sémában”** fejezetben került részletesen bemutatásra.

A TaxNumberType típus az „ **Adószámok a sémában”** fejezetben szerepelt.

**2.2.2.4 invoiceDetail**



## 52. ábra Az InvoiceDetailType felépítése

```
Tag Típus Kötelező Tartalma
invoiceCategory xs:string Igen A számla típusa, módosító okirat
esetén az eredeti számla típusa
invoiceDeliveryDate xs:date Igen Teljesítés dátuma (ha nem
szerepel a számlán, akkor
azonos a számla keltével) - Áfa
tv. 169. § g)
invoiceDeliveryPeriodStart xs:date Nem Ha a számla egy időszakra
vonatkozik, akkor az időszak
első napja
invoiceDeliveryPeriodEnd xs:date Nem Ha a számla egy időszakra
vonatkozik, akkor az időszak
utolsó napja
invoiceAccountingDeliveryDate xs:date Nem Számviteli teljesítés dátuma.
Időszak esetén az időszak utolsó
napja
periodicalSettlement xs:boolean Nem Időszakos elszámolás jelzése
smallBusinessIndicator xs:boolean Nem Kisadózó jelzése
currencyCode xs:string Igen A számla pénzneme az ISO 4217
szabvány szerint
exchangeRate xs:decimal Igen HUF-tól különböző pénznem
esetén az alkalmazott árfolyam:
egy egység értéke HUF-ban
utilitySettlementIndicator xs:boolean Nem Közmű elszámolószámla jelölése
selfBillingIndicator xs:boolean Nem Önszámlázás jelölése
(önszámlázás esetén true)
paymentMethod xs:string Nem Fizetés módja
paymentDate xs:date Nem Fizetési határidő
cashAccountingIndicator xs:boolean Nem Pénzforgalmi elszámolás
jelölése, ha az szerepel a
számlán - Áfa tv. 169. § h).
Értéke true pénzforgalmi
elszámolás esetén
invoiceAppearance xs:string Igen A számla vagy módosító okirat
megjelenési formája
conventionalInvoiceInfo xs:complexType Nem A számlafeldolgozást segítő,
egyezményesen nevesített
egyéb adatok
additionalInvoiceData xs:complexType Nem A számlára vonatkozó egyéb
adat
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
invoiceCategory InvoiceCategoryType
NORMAL
SIMPLIFIED
AGGREGATE
```
##### -

```
invoiceDeliveryDate InvoiceDateType \d{4}-\d{2}-\d{2}
minInclusive =
2010 - 01 - 01
```
##### - -

```
invoiceDeliveryPeriodStart InvoiceDateType \d{4}-\d{2}-\d{2} - -
```

```
minInclusive =
2010 - 01 - 01
invoiceDeliveryPeriodEnd InvoiceDateType \d{4}-\d{2}-\d{2}
minInclusive =
2010 - 01 - 01
```
##### - -

```
invoiceAccountingDeliveryDate InvoiceDateType \d{4}-\d{2}-\d{2}
minInclusive =
2010 - 01 - 01
```
##### - -

```
periodicalSettlement - - - false
smallBusinessIndicator - - - false
currencyCode CurrencyType [A-Z]{3} -
exchangeRate ExchangeRateType minExclusive
value="0"
totalDigits
value="14"
fractionDigits
value="6"
```
##### - -

```
utilitySettlementIndicator - - - false
selfBillingIndicator - - - false
paymentMethod PaymentMethodType - TRANSFER
CASH
CARD
VOUCHER
OTHER
```
##### -

```
paymentDate InvoiceDateType \d{4}-\d{2}-\d{2}
minInclusive =
2010 - 01 - 01
```
##### - -

```
cashAccountingIndicator - - -- false
invoiceAppearance InvoiceAppearanceType - PAPER
ELECTRONIC
EDI
UNKNOWN
```
##### -

```
conventionalInvoiceInfo ConventionalInvoiceInfoType - - -
additionalInvoiceData AdditionalDataType - - -
```
Az AdditionalDataType és a ConventionalInvoiceInfoType leírása az **Előre nem nevesített adatok
szerepeltetése** , illetve az **„Egyezményes, nevesített adatok szerepeltetése”** fejezetben került leírásra.

Az InvoiceCategoryType, CurrencyType, ExchangeRateType, PaymentMethodType,
InvoiceAppearanceType leírása „ **Az üzleti tartalomban szereplő típusok leírása”** fejezetben szerepel.

Számlaadat-szolgáltatás esetén minden esetben meg kell adni a teljesítési dátumot
(invoiceDeliveryDate). Ha nem szerepel a számlán a teljesítési dátumra vonatkozó explicit adat, akkor
az Áfa törvény alapján a teljesítés dátuma a számla kelte (invoiceIssueDate), tehát az
invoiceDeliveryDate elemben ugyanazt a dátumot kell szerepeltetni, ami az invoiceIssueDate elemben
szerepel.

Gyűjtőszámla (invoiceCategory=AGGREGATE) esetén az egyes tételekhez tartozó teljesítési dátumok a
tételeknél szerepelnek. Technikailag gyűjtőszámla esetén is meg kell adni a számla teljesítési dátumát
(invoiceDeliveryDate), ami gyűjtőszámla esetén az egyes tételekhez tartozó teljesítési dátumok
(lineDeliveryDate) közül a legnagyobb (legkésőbbi).


A számláról vagy módosító okiratról történő adatszolgáltatáskor minden esetben meg kell adni a

használt pénznemet (currencyCode) és az átváltási árfolyamot (exchangeRate). Forint alapú számla
esetén 1-et kell közölni. Ha a módosító számla nem tartalmaz számlasort, de a számlafejben lévő
változás miatt az átváltási árfolyamot ismét közölni kell, akkor az exchangeRate tagban a módosítást
megelőző, utolsó érvényes értéket kell feltüntetni. Az árfolyam, nem a számla kötelező adattartalma,
azonban az Áfa tv. 10. melléklete 2021. január 4-étől hatályos 2. és 4. pontja alapján az adatszolgáltatás
kötelező eleme. Az adatszolgáltatásnál az Áfa tv. 80. § és 80/A. § szerinti árfolyamról kell az
adatszolgáltatást elvégezni 2021. január 4-től. A jogszabály változásával tehát nem csupán az áthárított
adót tartalmazó adatszolgáltatásoknál, hanem az áthárított adót nem tartalmazó
adatszolgáltatásoknál is kötelezően meg kell adni a valós, a számla nettó értékének átszámításához
használt árfolyamot.

Forinttól különböző fizetőeszközben kiállított gyűjtőszámla esetén az árfolyam adatok az egyes
tételeknél szerepeltetendők (aggregateInvoiceLineData/lineExchangeRate elem), nem a számla
egészére vonatkozóan, az exchangeRate elemben. Külföldi pénznemben kiállított gyűjtőszámla esetén
is fel kell tüntetni a számlafejben az átváltási árfolyamot, amely ebben az esetben a számla
összesítőben szereplő nettó összeg forintban kifejezett összegének, valamint a nettó összeg számla
pénznemében kifejezett összegének hányadosa
(invoiceSummary/summaryNormal/invoiceNetAmountHUF értéke elosztva az
invoiceSummary/summaryNormal/invoiceNetAmount értékével). Ha a külföldi pénznemben kiállított
gyűjtőszámla módosításakor nem szerepel számlasor az adatszolgáltatásban, és ez miatt a számla
összege nem változik, akkor az átváltási árfolyamban az utolsó, előzőekben ismertetett módon

kiszámított hányadost kell szerepeltetni.

Az utilitySettlementIndicator használatáról a „ **Közmű elszámoló számlájának adatszolgáltatása”**
alfejezet tartalmaz további információt. A mező értéke közműszolgáltatók elszámolószámlájának
időszaki teljesítésről (például alapdíj) szóló beküldéseknél kell, hogy true értékű legyen.

#### 2.2.3 invoiceLines

## 53. ábra A LinesType felépítése

Az invoiceLines elem (típusa: LinesType) szolgál a számlán vagy módosításon szereplő tétel adatok
feltüntetésére az adatszolgáltatásban. Ez az elem annyi line elemet (típusa: LineType) tartalmaz, ahány
termék/szolgáltatás tétel szerepel a számlán vagy módosításon.


A projekt indulása óta érdemben megoldatlan az úgynevezett nagyméretű adatszolgáltatások

problémája, amikor a POST body size meghaladja a 10 MB-t. Az ilyen jellegű számlák beküldési
módjáról részletes leírás a „ **Nagyméretű számlákról történő adatszolgáltatás”** fejezetben található.

```
Tag Típus Kötelező Tartalma
mergedItemIndicator xs:boolean Igen Jelöli, ha az adatszolgáltatás
méretcsökkentés miatt
összevont soradatokat tartalmaz
line xs:complexType Igen Termék/szolgáltatás tétel
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
mergedItemIndicator - - - -
line LineType - - -
```

**2.2.3.1 line**



## 54. ábra A LineType felépítése

A line elem (típusa: LineType) a számlán vagy módosításon szereplő egy tétel adatait tartalmazza. A

line elem az adott tétel értékadatait tartalmazza. Az értékadatok köre attól függ, hogy az adott számla
(vagy az az eredeti számla, amire vonatkozó módosításról készül adatszolgáltatás) egyszerűsített
számla-e vagy sem.

```
Tag Típus Kötelező Tartalma
lineNumber xs:nonNegativeInteger Igen A tétel sorszáma
lineModificationReference xs:complexType Nem Módosító számla esetén a
tételsorszintű módosítások
jelölése
referencesToOtherLines xs:complexType Nem Hivatkozások kapcsolódó
tételekre, ha ez az Áfa törvény
alapján szükséges
advanceData xs: complexType Nem Előleghez kapcsolódó adatok
productCodes xs:complexType Nem Termékkódok
lineExpressionIndicator xs:boolean Igen Értéke true, ha a tétel
mennyiségi egysége
természetes mértékegységben
kifejezhető
lineNatureIndicator xs:string Nem Termékértékesítés vagy
szolgáltatásnyújtás jelölése
lineDescription xs:string Nem A termék vagy szolgáltatás
megnevezése
quantity xs:decimal Nem Mennyiség
unitOfMeasure xs:string Nem Mennyiségi egység
unitOfMeasureOwn xs:string Nem Saját mennyiségi egység
unitPrice xs:decimal Nem Egységár a számla
pénznemében. Egyszerűsített
számla esetén bruttó, egyéb
esetben nettó egységár
unitPriceHUF xs:decimal Nem Egységár forintban.
Egyszerűsített számla esetén
bruttó, egyéb esetben nettó
egységár.
lineDiscountData xs:complexType Nem A tételhez tartozó árengedmény
adatok
lineAmountsNormal xs:complexType Nem Normál (nem egyszerűsített)
számla esetén (beleértve a
gyűjtőszámlát) kitöltendő tétel
érték adatok.
lineAmountsSimplified xs:complexType Nem Egyszerűsített számla esetén
kitöltendő tétel érték adatok
intermediatedService xs:boolean Nem Értéke true ha a tétel közvetített
szolgáltatás - Számviteli tv. 3.§
(4) 1
aggregateInvoiceLineData xs:complexType Nem Gyűjtőszámla adatok
```

```
newTransportMean xs:complexType Nem Új közlekedési eszköz
értékesítés Áfa tv. 89 § ill. 169 §
o)
depositIndicator xs:boolean Nem Értéke true, ha a tétel betétdíj
jellegű
obligatedForProductFee xs:boolean Nem Értéke true ha a tételt termékdíj
fizetési kötelezettség terheli
GPCExcise xs:decimal Nem Földgáz, villamos energia, szén
jövedéki adója forintban - Jöt.
```
118. § (2)
dieselOilPurchase xs:complexType Nem Gázolaj adózottan történő
beszerzésének adatai – 45/2016
(XI. 29.) NGM rendelet 75. § (1)
a)
netaDeclaration xs:boolean Nem Értéke true, ha a Neta tv-ben
meghatározott adókötelezettség
az adó alanyát terheli. 2011. évi
CIII. tv. 3.§(2)
productFeeClause xs:complexType Nem A környezetvédelmi
termékdíjról szóló 2011. évi
LXXXV. tv. szerinti tételekre
vonatkozó záradékok
lineProductFeeContent xs:complexType Nem A tétel termékdíj tartalmára
vonatkozó adatok
conventionalLineInfo xs:complexType Nem A számlafeldolgozást segítő,
egyezményesen nevesített,
egyéb adatok
additionalLineData xs:complexType Nem A termék/szolgáltatás tételhez
kapcsolódó, további adat
_* a kék háttérrel jelölt, séma szerint opcionális tagek kitöltése bizonyos feltételek alapján kötelező. A kötelezőség nem
teljesülésekor a rendszer validációs hibát ad az adatszolgáltatásra, lásd: „Hibakezelés” fejezet_

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
lineNumber LineNumberType - - -
lineModificationReference LineModificationReferenceType - - -
referencesToOtherLines ReferencesToOtherLinesType - - -
advanceData AdvanceDataType - - -
productCodes ProductCodesType - - -
lineExpressionIndicator - - - false
lineNatureIndicator LineNatureIndicatorType - PRODUCT
SERVICE
OTHER
```
##### -

```
lineDescription SimpleText5 12 NotBlankType .*[^\s].* - -
quantity QuantityType - - -
unitOfMeasure UnitOfMeasureType - PIECE
KILOGRAM
TON
KWH
DAY
HOUR
MINUTE
MONTH
```
##### -


##### LITER

##### KILOMETER

##### CUBIC_METER

##### METER

##### LINEAR_METER

##### CARTON

##### PACK

##### OWN

```
unitOfMeasureOwn SimpleText50NotBlankType .*[^\s].* - -
unitPrice QuantityType - - -
unitPriceHUF QuantityType - - -
lineDiscountData DiscountDataType - - -
lineAmountsNormal LineAmountsNormalType - - -
lineAmountsSimplified LineAmountsSimplifiedType - - -
intermediatedService - - - false
aggregateInvoiceLineData AggregateInvoiceLineDataType - - -
newTransportMean NewTransportMeanType - - -
depositIndicator - -
false
marginSchemeIndicator MarginSchemeType - TRAVEL_AGENCY
SECOND_HAND
ARTWORK
ANTIQUES
```
##### -

```
obligatedForProductFee - - - false
GPCExcise MonetaryType total
digits:18,
fraction
digits:2
```
##### - -

```
dieselOilPurchase DieselOilPurchaseType - - -
netaDeclaration - - - false
productFeeClause ProductFeeClauseType - - -
lineProductFeeContent ProductFeeDataType - - -
conventionalLineInfo ConventionalInvoiceInfoType - - -
additionalLineData AdditionalDataType - - -
```
A lineNumber elem minden számláról vagy módosításról történő adatszolgáltatás esetén 1-től induló,
ismétlés és kihagyás nélküli sorszám.

A módosításról történő adatszolgáltatásnál használatos lineModificationReference elem pontos
használatáról az „ **Adatszolgáltatás számlával egy tekintet alá eső okiratokról”** fejezet tartalmaz
leírást.

A unitPrice elem ugyan pénzértéket tartalmaz, de a használni szükséges tizedesjegyek száma miatt a

típusa QuantityType. Ha a számlán szereplő mennyiség vagy egységár kifejezésére a QuantityType által
lehetővé tett hat tizedesjegy sem elegendő, akkor javasolt a mennyiségi egység alkalmas
megválasztásával (például „darab” helyett „1000 darab”) kezelni a problémát.

Ha a termék vagy szolgáltatás számlán szereplő leírása hosszabb, mint ami a lineDescription elemben
szerepeltethető, akkor az adatszolgáltatásban a leírást a lehetséges maximális karakterhossznál
csonkolni kell.


**2.2.3.1.1 lineModificationReference**

## 55. ábra A LineModificationReferenceType felépítése

```
Tag Típus Kötelező Tartalma
lineNumberReference xs:nonNegativeInteger Igen Az eredeti számla módosítással
érintett tételének sorszáma,
(lineNumber). Új tétel
létrehozása esetén az új tétel
sorszáma, az eredeti számla
folytatásaként
lineOperation xs:string Igen A számlatétel módosításának
jellege
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
lineNumberReference LineNumberType - - -
lineOperation LineOperationType - CREATE
(MODIFY*)
```
##### -

A lineModificationReference elemet kizárólag módosításról történő adatszolgáltatás esetén lehet és
kell szerepeltetni. Ha a lineOperation elem értéke „CREATE”, akkor a lineNumberReference elem az
eredeti számla és az összes korábbi módosítás eredményeként előálló sorszámozás folytatása. Ha a

lineOperation elem értéke „MODIFY”, akkor a lineNumberReference elem azon eredeti számlán
szereplő tétel sorszámát (lineNumber), vagy korábbi módosító okiraton létrehozott új tétel sorszámát
(a korábbi módosító okiraton lineNumberReference) tartalmazza, amire a módosítás vonatkozik.

Módosító okiratról történő adatszolgáltatás esetén, ha annak eredeti számlájáról nem történt és nem
is fog történni adatszolgáltatás (modifyWithoutMaster = ”true”), akkor nem kifogásolható a
lineNumberReference elemekben egy adott értéktől (akár 1-től) kezdődő sorszámozást szerepeltetni
annak ellenére, hogy ezek az adatszolgáltatással nem érintett eredeti számla nem megfelelő
tételsoraira hivatkoznak.

*Az INVALID_LINE_OPERATION validáció bevezetése után a lineOperation elem értékének kizárólag a
„CREATE” érték fogadható el, amennyiben a „MODIFY” érték kerül megadásra valamely tételsorban,


akkor az adatszolgáltatás elutasításra kerül. A validációról részletesen a 3.3.2 Blokkoló validációs

hibakódok fejezetben tájékozódhat.

**2.2.3.1.2 referencesToOtherLines**

## 56. ábra A ReferencesToOtherLinesType felépítése

```
Tag Típus Kötelező Tartalma
referenceToOtherLine xs:nonNegativeInteger Igen Hivatkozások kapcsolódó
tételekre, ha ez az Áfa törvény
alapján szükséges
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
referenceToOtherLine LineNumberType - - -
```
A referenceToOtherLines elem szerepe: valamely tétel/tételek adóalapját az Áfa törvény 70. § (1)
bekezdése alapján adóalapot növelő költségek esetén indokolt megjelölni azon tételt/tételeket,
amelyeknek az adott költség az adójogi sorsát osztja, hogy például az alkalmazott adómérték
jogszerűsége egyértelműen megállapítható legyen. Ilyen lehet például a számlán szerepeltetett,

járulékos költséget (például szállítási költséget) terhelő áfa mértékének megállapítása különböző
adómérték alá tartozó termékek értékesítése esetén. Ilyenkor lehetőség van arra, hogy az adóalany a
szállítási költséget az általa teljesített ügyletekben értékesített termékek között megossza (például a
termékek súlya, mérete vagy értéke alapján), de az sem kifogásolható, ha a társaság az egyes termékek
értékesítésére jutó költség meghatározása, illetve megosztása helyett a költséget összesíti és a
legmagasabb – 27 százalékos– adómértékkel számolva minősíti azokat a kérdéses ügyleteknél
adóalapot képező tételnek.

2.2.3.1.3 advanceData


## 57. ábraAz AdvanceDataType felépítése

```
Tag Típus Kötelező Tartalma
advanceIndicator xs:boolean Igen Annak jelölése, hogy a tétel
előleg jellegű
advancePaymentData/advanceOrigi
nalInvoice
```
```
xs:string Igen Az előlegszámla sorszáma,
amelyben az előlegfizetés
történt
advancePaymentData/advancePay
mentDate
```
```
xs:string Igen Az előleg fizetésének dátuma
```
```
advancePaymentData/advanceExch
angeRate
```
```
xs:string Igen Az előlegfizetéskor alkalmazott
árfolyam
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enu
m
```
```
Defaul
t
advanceIndicator - - - false
advancePaymentData/advanceOriginalInvoic
e
```
```
SimpleText50NotBlankTyp
e
```
```
.*[^\s].* - -
```
```
advancePaymentData/advancePaymentDate InvoiceDateType minInclusive
= 2010- 01 -
01
\d{4}-\d{2}-
\d{2}
```
##### - -

```
advancePaymentData/advanceExchangeRat
e
```
```
ExchangeRateType minExclusive
value="0"
totalDigits
value=" 14 "
fractionDigit
s value=" 6 "
```
##### - -


A számla tételeinél lehetőség van jelölni, hogy az adott tétel előleg jellegű. Ha az advanceIndicator
jelölő értéke true, azaz a tétel előleg jellegű, akkor végszámla esetén lehetőség van megadni az
advancePaymentData csomópontot. Az előleggel kapcsolatos adatok közül ilyen esetben minden érték
kitöltése kötelező. Az előlegszámla adatszolgáltatása esetén csak az advanceIndicator = true értékkel
az előleg jellegének jelzése lehetséges. A csomópont használatáról a részletes leírás az „ **Előlegszámla,
végszámla adatszolgáltatása”** fejezetben található.

**2.2.3.1.4 productCodes**

## 58. ábra A ProductCodesType felépítése

## 59. ábra A ProductCodeType felépítése

```
Tag Típus Kötelező Tartalma
productCode xs:complexType
Termékkód
productCodeCategory xs:string Igen A termékkód értéke nem saját
termékkód esetén
productCodeValue xs:string Igen A termékkód értéke
productCodeOwnValue xs:string^ Igen^ Saját termékkód értéke^
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
ProductCodeCategory ProductCodeCategoryType - VTSZ
SZJ
KN
AHK
CSK
KT
EJ
TESZOR
OWN
OTHER
```
##### -

```
productCodeValue ProductCodeValueType [A-Z0-9]{2,30} - -
productCodeOwnValue SimpleText 25 5NotBlankType .*[^\s].* - -
```

A számla egy adott tétele esetén több, különböző típusú kód is szerepeltethető úgy, hogy a

ProductCodes elemen belül a ProductCode elem többször fordul elő. Nincs megkötés arra
vonatkozóan, hogy egy fajta termékkód (például VTSZ kód, CsK kód) egy tételnél csak egyszer
szerepelhet, mert bizonyos esetekben szükséges lehet ugyanazon kódfajtából több érték
szerepeltetése.

A saját termékkódokról való adatközélésre a típus külön elemet tartalmaz. Ha a productCodeCategory
értéke OWN, úgy a termékkód adatot a productCodeOwnValue elemben kell közölni.

Az egyes kódokat (a saját termékkód kivételével) – a sémának megfelelően – kizárólag nagybetűk és
számok használatával kell feltüntetni akkor is, ha a kód egyéb karaktereket (például pont, kötőjel,
szóköz stb.) is tartalmaz.

**2.2.3.1.5 lineDiscountData**

## 60. ábra A DiscountDataType felépítése

```
Tag Típus Kötelező Tartalma
discountDescription xs:string Nem Az árengedmény leírása
discountValue xs:decimal Nem Tételhez tartozó árengedmény
összege a számla pénznemében,
ha az egységár nem tartalmazza
discountRate xs:decimal Nem Tételhez tartozó árengedmény
aránya százalékban, ha az
egységár nem tartalmazza
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
discountDescription SimpleText255NotBlankType .*[^\s].* - -
discountValue MonetaryType total digits:18, fraction
digits:2
```
##### - -

```
discountRate RateType minInclusive value="0"
maxInclusive value="1"
totalDigits value="5"
fractionDigits value="4"
```
##### - -


A lineDiscountData elem pozitív számként tartalmazza az engedmény összegét. Ebben a tekintetben
az alábbi összefüggésnek kell teljesülnie, ha a kifejezésben szereplő összes elem kitöltött az adott
tételsorban:

Normál és gyűjtőszámla esetén,

```
𝑞𝑢𝑎𝑛𝑡𝑖𝑡𝑦∙𝑢𝑛𝑖𝑡𝑃𝑟𝑖𝑐𝑒−𝑑𝑖𝑠𝑐𝑜𝑢𝑛𝑡𝑉𝑎𝑙𝑢𝑒=𝑙𝑖𝑛𝑒𝑁𝑒𝑡𝐴𝑚𝑜𝑢𝑛𝑡
```
Egyszerűsített számla esetén a következő egyenlőségnek kell teljesülnie,

```
𝑞𝑢𝑎𝑛𝑡𝑖𝑡𝑦∙𝑢𝑛𝑖𝑡𝑃𝑟𝑖𝑐𝑒−𝑑𝑖𝑠𝑐𝑜𝑢𝑛𝑡𝑉𝑎𝑙𝑢𝑒=𝑙𝑖𝑛𝑒𝐺𝑟𝑜𝑠𝑠𝐴𝑚𝑜𝑢𝑛𝑡𝑆𝑖𝑚𝑝𝑙𝑖𝑓𝑖𝑒𝑑
```
(Ha a kedvezményt is tartalmazó tételsor érvénytelenítésre kerül, ott a discountValue negatív értéket
vesz fel és az egyenlőség továbbra is teljesül.)

Ha egy-egy tételhez több, különböző szempontból is engedményt ad az eladó (például 3% mennyiségi
kedvezmény, további 2 százalék törzsvevői kedvezmény), akkor az adott árengedményt összevontan

kell szerepeltetni az adatszolgáltatásban. Tételsoronként legfeljebb egy lineDiscountData elem
szerepeltethető.

Ha az árengedményt nem a tételsorhoz közvetlenül kapcsolódóan, hanem a számla végösszegéből,
százalékosan vagy fix összegben adja az eladó, az árengedményt az adatszolgáltatásban külön tételként
szükséges szerepeltetni, nem pedig a lineDiscountData elemben. Ha a számla több, különböző
áfamérték alá tartozó tételt tartalmaz, akkor szükséges a végösszegből adott kedvezmény megbontása
a különböző adómértékek között, így az ilyen árengedményt több tételként szükséges szerepeltetni.

A lineDiscountData elem nem szolgál felár jelzésére. A felárat az adózó választása szerint vagy az adott
számlatétel (egység)árába építetten, vagy külön tételként célszerű szerepeltetni a számlán és az

adatszolgáltatásban.


**2.2.3.2 lineAmountsNormal**

## 61. ábra A LineAmountsNormalType felépítése

A line elem „normál” (azaz nem egyszerűsített) számla esetén pontosan egy lineAmountsNormal
elemet (típusa: LineAmountsNormalType), egyszerűsített számla esetén pontosan egy

lineAmountSimplified elemet (típusa: LineAmountsSimplifiedType) tartalmaz. Módosításról történő
adatszolgáltatás esetén nem feltétlenül szerepel egyik vagy másik elem az adatszolgáltatásban.

A forint összegeket az Áfa tv. 10. számú melléklet 4. pontja alapján a 80. § és a 80/A. § szerinti
árfolyammal kell kiszámolni és szerepeltetni az adatszolgáltatásban.

```
Tag Típus Kötelező Tartalma
lineNetAmountData/lineNetAmoun
t
```
```
xs:decimal Igen Tétel nettó összege a számla
pénznemében, különbözeti
adózás esetén az ellenérték
lineNetAmountData/
lineNetAmountHUF
```
```
xs:decimal Igen Tétel nettó összege forintban
```

```
lineVatRate xs:complexType Igen Adómérték vagy adómentesség
jelölése
lineVatData/lineVatAmount xs:decimal Nem Tétel áfa összege a számla
pénznemében
lineVatData/lineVatAmountHUF xs:decimal Nem Tétel áfa összege forintban
lineGrossAmountData/lineGrossAm
ountNormal
```
```
xs:decimal Nem Tétel bruttó értéke a számla
pénznemében
lineGrossAmountData/lineGrossAm
ountNormalHUF
```
```
xs:decimal Nem Tétel bruttó értéke forintban
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
lineNetAmountData/lineNetAmount MonetaryType total digits:18,
fraction digits:2
```
##### - -

```
lineNetAmountData/ lineNetAmountHUF MonetaryType total digits:18,
fraction digits:2
```
##### - -

```
lineVatRate VatRateType - - -
lineVatData/lineVatAmount MonetaryType total digits:18,
fraction digits:2
```
##### - -

```
lineVatData/lineVatAmountHUF MonetaryType total digits:18,
fraction digits:2
```
##### - -

```
lineGrossAmountData/lineGrossAmountNormal MonetaryType total digits:18,
fraction digits:2
```
##### - -

```
lineGrossAmountData/lineGrossAmountNormalHUF MonetaryType total digits:18,
fraction digits:2
```
##### - -


**2.2.3.2.1 vatRate**

## 62. ábra A VatRateType felépítése

Ez a típus szolgál egy számlatétel, vagy a számla összesítés (invoiceSummary) esetén az áfa mértékének
feltüntetésére, vagy annak jelölésére, hogy az adott tétel – különböző okokból – nem tartalmaz áfát.
**A VatRateType típusú elemek az alábbi nyolc elem közül pontosan az egyiket tartalmazhatják,**

**sorrendben jelölve.**


- áfa mértéke
- áfatartalom (egyszerűsített számla esetén)
- áfamentesség jelölése
- Áfa törvény hatályon kívüliség
- beföldi fordított adózás
- különbözet szerinti adózás
- speciális esetek, ahol az áfaalap és a felszámított adó nem következik egymásból
- nincs felszámított áfa a 17. § alapján

```
Tag Típus Kötelező Tartalma
vatPercentage xs:decimal Igen Az alkalmazott adó mértéke -
Áfa tv. 169. § j)
vatContent xs:decimal Igen Áfatartalom egyszerűsített
számla esetén
vatExemption/case xs:string Igen Az adómentesség jelölés kódja
vatExemption/reason xs:string Igen Az adómentesség jelölés leírása
vatOutOfScope/case xs:string Igen Az Áfa tv.y hatályán kívüliség
kódja
vatOutOfScope/reason xs:string Igen Az Áfa tv.hatályán kívüliség
leírása
vatDomesticReverseCharge xs:boolean Igen A belföldi fordított adózás
jelölése - Áfa tv. 142. §
marginSchemeIndicator xs:complexType Igen Különbözet szerinti szabályozás
jelölése - Áfa tv. 169. § p) q)
vatAmountMismatch/vatRate xs:complexType Igen Adómérték, adótartalom
vatAmountMismatch/case xs:string Igen Adóalap és felszámított adó
eltérésének kódja
noVatCharge xs:boolean Igen Nincs felszámított áfa a 17. §
alapján
```
_* a kék háttérrel jelölt tagek értékkészletét validáció vizsgálja. Nem megengedett érték megadásakor a rendszer validációs
hibát ad az adatszolgáltatásra, lásd: „Hibakezelés” fejezet_

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Defa
ult
vatPercentage RateType minInclusive
value="0"
maxInclusive
value="1"
totalDigits
value="5"
fractionDigits
value="4"
```
##### - -

```
vatContent RateType minInclusive
value="0"
maxInclusive
value="1"
totalDigits
value="5"
```
##### - -


```
fractionDigits
value="4"
vatExemption/case SimpleText50NotBlankType .*[^\s].* - -
vatExemption/reason SimpleText 2 00NotBlankType - - -
vatOutOfScope/case SimpleText50NotBlankType - - -
vatOutOfScope/reason SimpleText 2 00NotBlankType - - -
vatDomesticReverseCharge - - - false
marginSchemeIndicator MarginSchemeType - TRAVEL_AGEN
CY
SECOND_HAND
ARTWORK
ANTIQUES
```
##### -

```
vatAmountMismatch/vatRat
e
```
```
RateType minInclusive
value="0"
maxInclusive
value="1"
totalDigits
value="5"
fractionDigits
value="4"
```
##### - -

```
vatAmountMismatch/case SimpleText 50 NotBlankType - - -
noVatCharge - - - false
```
A vatAmountMismatch/vatRate értékét külön üzleti valdiáció vizsgálja. Jelenleg elfogadott
értékkészlete: 0.27, 0.18, 0.05, 0.2126, 0.1525, 0.0426, illetve 0 (csak 2024.01.01. vagy utáni teljesítési
időpontú számlák esetén).

A boolean típusú jelölőknél (vatDomesticReverseCharge és noVatCharge) séma szinten ki van
kényszerítve a fixed:true attribútum, hiszen üzletileg csak ekkor van értelme az adott elem jelölésének.

A vatExemption és vatOutOfScope és vatAmountMismatch (az adóalap és a felszámított adó
eltérésének valamelyik esete) esetek alábontásban szerepelnek, ahol egy case mezőben definiálható
az eset a pontosabb beazonosíthatóság miatt. A vatExemption/case, vatOutOfScope/case és
vatAmountMismatch/case mezők értékeit külön üzleti validáció vizsgálja. Lehetséges értékek:

```
Típus Értékkészlet Jelentése
vatExemption/case AAM Alanyi adómentes
TAM „tárgyi adómentes” ill.
a tevékenység
közérdekű vagy
speciális jellegére
tekintettel adómentes
KBAET adómentes Közösségen
belüli
termékértékesítés, új
közlekedési eszköz
nélkül
KBAUK adómentes Közösségen
belüli új közlekedési
eszköz értékesítés
```

EAM adómentes
termékértékesítés a
Közösség területén
kívülre (termékexport
harmadik országba)
NAM egyéb nemzetközi
ügyletekhez
kapcsolódó jogcímen
megállapított
adómentesség
UNKNOWN 3.0 előtti számlára
hivatkozó, illetve
előzmény nélküli
módosító és sztornó
számlák esetén
használható, ha nem
megállapítható az
érték.
vatOutOfScope/case ATK
Áfa tárgyi hatályán
kívül
EUFAD37 Áfa tv. 37. §-a alapján
másik tagállamban
teljesített, fordítottan
adózó ügylet
EUFADE Másik tagállamban
teljesített, nem az Áfa
tv. 37. §-a alá tartozó,
fordítottan adózó
ügylet
EUE Másik tagállamban
teljesített, nem
fordítottan adózó
ügylet
HO Harmadik országban
teljesített ügylet
UNKNOWN 3.0 előtti számlára
hivatkozó, illetve
előzmény nélküli
módosító és sztornó
számlák esetén
használható, ha nem
megállapítható az
érték.
vatAmountMismatch/case REFUNDABLE_VAT az áfa felszámítása a

11. vagy 14. § alapján
történt és az áfát a
számla címzettjének
meg kell térítenie
NONREFUNDABLE_VAT az áfa felszámítása a
11. vagy 14. § alapján
történt és az áfát a


```
számla címzettjének
nem kell megtérítenie
UNKNOWN 3.0 előtti számlára
hivatkozó, illetve
előzmény nélküli
módosító és sztornó
számlák esetén
használható, ha nem
megállapítható az
érték.
```
Mivel a normál és egyszerűsített adómértékek egy komplex típusban szerepelnek, így üzleti validáció
ellenőrzi, hogy normál számla esetén ne lehessen a vatContent mezőt, míg egyszerűsített számla
esetén ne lehessen a vatPercentage mezőt kitölteni.

A case mezőknél szereplő UNKNOWN értékre külön üzleti validáció van, hogy csak előzmény nélküli,
illetve 3.0 verziónál kisebb hivatkozott számlák esetén megadható. A case mezőket érdemes a
számlázó program értékkészletével összerendelni. Az összerendeléshez a következő táblázat nyújt
segítséget:

```
Case érték Áfa tv. hivatkozás Magyarázat, használati példa
AAM XIII. fejezet A számla kibocsátója alanyi mentességet
választott és a mentesség használatára jogosult
(nem érte el a jogszabályi értékhatárt)
TAM 85. §, 86. § Az értékesítés a tevékenység közérdekű jellegére
vagy egyéb sajátos jellegére tekintettel mentes az
adó alól. (Például adómentes oktatás,
egészségügyi szolgáltatás).
KBAET 89. § A Közösség másik tagállamában regisztrált
adóalany számára történt termékértékesítés,
amennyiben a termék az adott tagállamba került
elszállításra. Az új közlekedési eszköz értékesítése
a KBAUK esethez tartozik.
A vevő közösségi adószámát a számlán kötelező
feltüntetni.
KBAUK 89. § (2) Új közlekedési eszköz másik tagállamba történő
értékesítése. A vevő nem feltétlenül adóalany,
lehet például magánszemély is, ezért közösségi
adószám nem feltétlenül jelenik meg a számlán.
Az Áfa törvény 259. § 25. pontjában felsorolt
adatok a számla kötelező adattartalmát képezik.
EAM 98 - 109. § Belföldön teljesített termékértékesítés, aminek a
következményeként a terméket kiléptetik
harmadik országba (termékexport). A jogszabály
alapján olyan speciális esetek is idetartoznak,
mint például a nemzetközi szerződés alapján
érvényesülő adómentesség.
NAM 93 - 95. §, 110 - 118. § A jogszabály felsorolja az ide tartozó eseteket.
Ilyen lehet például az adómentes közvetítői
tevékenység, termék nemzetközi forgalmához
```

kapcsolódó egyes tevékenységek
adómentessége.
ATK 2 - 3. § Kizárólag tárgyi hatályon kívüli ügyletről nem kell
számlát kiállítani, de egy számla tartalmazhat
tárgyi hatályon kívüli tételt is. Ide tartozik például
a kártérítés, a közhatalmi tevékenység, ,a közcélú
adomány stb.
EUFAD37 37. § (1) Adóalany számára nyújtott szolgáltatás, aminek a
teljesítési helyét a vevő gazdasági célú
letelepedése (vagy lakóhelye, szokásos
tartózkodási helye) határozza meg az Áfa tv. 37. §
(1) bekezdése alapján és az másik tagállamban
található. A számlán kötelező szerepeltetni a vevő
közösségi adószámát. Ezen szolgáltatásokat az
összesítő nyilatkozaton is szerepeltetni kell.
EUFADE Másik tagállamban teljesített fordítottan adózó
ügylet, amelynek teljesítési helyének
megállapítása nem az EUFAD37 esete alapján
történik. Ehhez az esethez tartozó ügyleteknél a
magyar adózónak nincs bejelentkezési
kötelezettsége a teljesítés helye szerinti
tagállamban. Ilyen eset például a fel- vagy
összeszerelés tárgyául szolgáló termék másik
tagállami értékesítése.
EUE Az EU másik tagállamában teljesített olyan ügylet,
ami után nem a másik tagállami terméket
beszerzőt, szolgáltatás igénybevevőt terheli az
adófizetési kötelezettség (nem tartozik az
EUFAD37 és EUFADE esetei közé).
HO Olyan ügylet, aminek az Áfa tv. szerinti teljesítési
helye EU-n kívül van. Például harmadik országban
teljesített szolgáltatás, harmadik országban fekvő
ingatlanhoz kapcsolódó szolgáltatás.
REFUNDABLE_VAT 11. §, 14. § Olyan, az adóalanytól eltérő személy részére
végzett szolgáltatás vagy termék átadás, amit az
Áfa tv. ellenérték fejében végzettnek minősít, és
ezért ahhoz kapcsolódóan az adóalanynak
adófizetési kötelezettsége van. Ilyen például az,
ha az adóalany az ellenérték fejében
igénybevehető szállodai szolgáltatását ingyenes
biztosítja az ügyvezető és családja számára addig,
amíg ők a saját lakásukban felújítást végeztetnek.
NONREFUNDABLE_VAT 11. §, 14. § Az ide tartozó eset annyiban tér el az előzőtől,
hogy a termékben, szolgáltatásban ingyenesen
részesülő az adóalannyal kötött szerződésében,
megállapodásában (ami lehet szóbeli is), vállalja,
hogy megtéríti az adóalanynak azt az adót, amit az
adóalanynak a neki nyújtott ingyenes termék,
szolgáltatás miatt kell fizetendő áfaként
megállapítania.


A marginSchemeIndicator felvehető értékei:

```
Jogcím
```
```
MarginSchemeType
típusú elem értéke
Utazási irodák TRAVEL_AGENCY
Használt cikkek SECOND_HAND
Műalkotások ARTWORK
Gyűjteménydarabok és régiségek ANTIQUES
```
**2.2.3.3 LineAmountsSimplified**

## 63. ábra A LineAmountsSimplifiedType felépítése

**Tag Típus Kötelező Tartalma**
lineVatRate xs:complexType Igen Áfatartalom vagy az áfával
kapcsolatos egyéb eset jelölése
lineGrossAmountSimplified xs:decimal Igen Tétel bruttó értéke a számla
pénznemében
lineGrossAmountSimplifiedHUF xs:decimal Igen Tétel bruttó értéke forintban
_* a kék háttérrel jelölt tagek értékkészletét validáció vizsgálja. Nem megengedett érték megadásakor a rendszer validációs
hibát ad az adatszolgáltatásra, lásd: „Hibakezelés” fejezet_

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
lineVatRate VatRateType - - -
lineGrossAmountSimplified MonetaryType total digits:18, fraction
digits:2
```
##### - -

```
lineGrossAmountSimplifiedHUF MonetaryType total digits:18, fraction
digits:2
```
##### - -

Egyszerűsített számla esetén megadható lineVatRate értékeket lásd az előző fejezetben.


**2.2.3.4 aggregateInvoiceLineData**

## 64. ábra Az AggregateInvoiceLineDataType felépítése

```
Tag Típus Kötelező Tartalma
lineExchangeRate xs:decimal Nem A tételhez tartozó árfolyam, 1
(egy) egységre vonatkoztatva.
Csak külföldi pénznemben
kiállított gyűjtőszámla esetén
kitöltendő
lineDeliveryDate xs:date Igen Gyűjtőszámla esetén az adott
tétel teljesítési dátuma
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
lineExchangeRate ExchangeRateType minExclusive value="0"
totalDigits value=" 14 "
fractionDigits value=" 6 "
```
##### - -

```
lineDeliveryDate InvoiceDateType \d{4}-\d{2}-\d{2}
minInclusive = 2010- 01 - 01
```
##### - -

Gyűjtőszámláról, vagy ennek módosításáról történő adatszolgáltatás esetén szükséges megadni a
tételhez tartozó teljesítési dátumot, illetve – ha a számla pénzneme nem forint – akkor az adott

tételhez tartozó árfolyamot.


**2.2.3.5 newTransportMean**

## 65. ábra A NewTransportMeanType felépítése

Az új közlekedési eszközökkel kapcsolatos adatokat, a line elem NewTransportMeans eleme
tartalmazza.

```
Tag Típus Kötelező Tartalma
brand xs:string Nem Gyártmány/típus
serialNum xs:string Nem Alvázszám/gyári szám/Gyártási
szám
engineNum xs:string Nem Motorszám
firstEntryIntoService xs:date Nem Első forgalomba helyezés
időpontja
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
brand SimpleText50NotBlankType .*[^\s].* - -
serialNum SimpleText255NotBlankType .*[^\s].* - -
engineNum SimpleText255NotBlankType .*[^\s].* - -
firstEntryIntoService InvocieDateType \d{4}-\d{2}-\d{2}
minInclusive = 2010- 01 - 01
```
##### - -

Ha a számla adott tétele új közlekedési eszköz értékesítése másik tagállamba, az Áfa tv. a számlán
további adatok feltüntetését írja elő. Megjegyzendő, hogy az ilyen értékesítések nem belföldi


adóalanyoknak történnek és áfamentesek, emiatt ezekről a számlákról 2021. január 4 - ét követően

szükséges adatot szolgáltatni.

A NewTransportMeans elem tartalma attól függ, hogy az adott számlatétel szárazföldi (vehicle), vízi
(vessel) vagy légi (aircraft) közlekedési eszköz. Ezen három lehetőség közül pontosan az egyik lehet
érvényes.

**2.2.3.5.1 vehicle**

## 66. ábra A VehicleType felépítése

```
Tag Típus Kötelező Tartalma
engineCapacity xs:decimal Igen Hengerűrtartalom
köbcentiméterben
enginePower xs:decimal Igen Teljesítmény kW-ban
kms xs:decimal Igen Futott kilométerek száma
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
engineCapacity QuantityType totalDigits value="22"
fractionDigits value="6"
```
##### - -

```
enginePower QuantityType totalDigits value="22"
fractionDigits value="6"
```
##### - -

```
kms QuantityType totalDigits value="22"
fractionDigits value="6"
```
##### - -


**2.2.3.5.2 vessel**

## 67. ábra A VesselType felépítése

```
Tag Típus Kötelező Tartalma
length xs:decimal Igen Hajó hossza méterben
activityReferred xs:boolean Igen Értéke true, ha a jármű az Áfa
tv. 259.§ 25 .pont b) alpontja
szerinti kivétel alá tartozik
sailedHours xs:decimal Igen Hajózott órák száma
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
length QuantityType totalDigits value="22"
fractionDigits value="6"
```
##### - -

```
activityReferred - - - false
sailedHours QuantityType totalDigits value="22"
fractionDigits value="6"
```
##### - -

**2.2.3.5.3 aircraft**

## 68. ábra Az AircraftType felépítése

```
Tag Típus Kötelező Tartalma
takeOffWeight xs:decimal Igen Felszállási tömeg kilogrammban
```

```
airCargo xs:boolean Igen Értéke true ha a jármű az Áfa tv.
```
259. § 25. pont c) alpontja
szerinti kivétel alá tartozik
operationHours xs:decimal Igen Repült órák száma

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
takeOffWeight QuantityType totalDigits value="22"
fractionDigits value="6"
```
##### - -

```
airCargo - - - false
operationHours QuantityType totalDigits value="22"
fractionDigits value="6"
```
##### - -

**2.2.3.6 dieselOilPurchase**

## 69. ábra A DieselOilPurchaseType felépítése

A line elemben lehetőség van a számlán szereplő, gázolaj adózottan történő beszerzésének adatainak
feltüntetésére is a 45/2016. (XI. 29.) NGM rendelet 75. § (1) a) szerint.

```
Tag Típus Kötelező Tartalma
purchaseLocation xs:complexType Igen Gázolaj beszerzés helye
purchaseDate xs:date Igen Gázolaj beszerzés dátuma
vehicleRegistrationNumber xs:string Igen Kereskedelmi jármű forgalmi
rendszáma (csak betűk és
számok
dieselOilQuantity xs:decimal Nem Gépi bérmunka-szolgáltatás
közben felhasznált gázolaj
mennyisége literben – Jöt. 117.
§ (2)
```
**Facetek és leírók**


```
Tag SimpleType Pattern Enum Default
purchaseLocation SimpleAddressType - - -
purchaseDate InvoiceDateType \d{4}-\d{2}-\d{2}
minInclusive = 2010- 01 - 01
```
##### - -

```
vehicleRegistrationNumber PlateNumberType [A-Z0-9]{2,30} - -
dieselOilQuantity QuantityType totalDigits value="22"
fractionDigits value="6"
```
##### - -

**2.2.3.6.1 purchaseLocation**
A purchaselocation típusa a simpleAddressType. Részletesen lásd a „ **Címadatok a sémában”**
fejezetben.

**2.2.3.7 productFeeClause**

## 70. ábra A ProductFeeClauseType felépítése

A séma lehetőséget biztosít a termékdíj törvényben előírt záradékok feltüntetésére is. A termékdíj

törvény az alábbi, adott tétel vonatkozásában egymást kizáró eseteket különbözteti meg:

```
A. A környezetvédelmi termékdíj-kötelezettség átvállalása
B. Az eladó a vevő nyilatkozata alapján mentesül a termékdíj megfizetése alól
```
Ennek megfelelően a ProductFeeClause elem productTakeoverData és a customerDeclaration elemek
közül pontosan az egyiket tartalmazza

```
Tag Típus Kötelező Tartalma
productFeeTakeoverData xs:complexType Igen A környezetvédelmi termékdíj-
kötelezettség átvállalásával
kapcsolatos adatok
customerDeclaration xs:complexType Igen Ha az eladó a vevő nyilatkozata
alapján mentesül a termékdíj
megfizetése alól, akkor az
érintett termékáram
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
productFeeTakeoverData ProductFeeTakeoverDataType - - -
```

```
customerDeclaration CustomerDeclarationType - - -
```
**2.2.3.7.1 productFeeTakeoverData**

## 71. ábra A ProductFeeTakeoverDataType felépítése

```
Tag Típus Kötelező Tartalma
takeoverReason xs:string Igen Az átvállalás iránya és
jogszabályi alapja
takeoverAmount xs:decimal Nem Az átvállalt termékdíj összege
forintban, ha a vevő vállalja át
az eladó termékdíj-
kötelezettségét
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
takeoverReason TakeoverType - 01
02_aa
02_ab
02_b
02_c
02_d
02_ea
02_eb
02_fa
02_fb
02_ga
02_gb
```
##### -

```
takeoverAmount MonetaryType total digits:18, fraction
digits:2
```
##### - -

A TakeOverType leírását „ **Az üzleti tartalomban szereplő típusok leírása”** fejezet tartalmazza.


**2.2.3.7.2 customerDeclaration**

## 72. ábra A CustomerDeclarationType felépítése

```
Tag Típus Kötelező Tartalma
productStream xs:string Igen Termékáram
productWeight xs:decimal Nem Termékdíj köteles termék
tömege kilogrammban
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
productStream ProductStreamType - BATTERY
PACKAGING
OTHER_PETROL
ELECTRONIC
TIRE
COMMERCIAL
PLASTIC
OTHER_CHEMICAL
PAPER
```
##### -

```
productWeight QuantityType totalDigits value="22"
fractionDigits
value="6"
```
##### - -

A ProductStreamType típusról „ **Az üzleti tartalomban szereplő típusok”** fejezet tartalmaz leírást.


**2.2.3.8 lineProductFeeContent**

## 73. ábra A ProductFeeDataType felépítése

Ha a számlán szerepel, a séma lehetőséget biztosít az adott számlatételhez kapcsolódó termékdíj
tartalom feltüntetésére is a lineProductFeeContent elemben.

```
Tag Típus Kötelező Tartalma
productFeeCode xs:complexType Igen Termékdíj kód (Kt vagy Csk)
productFeeQuantity xs:decimal Igen A termékdíjjal érintett termék
mennyisége
productFeeMeasuringUnit xs:string Igen A díjtétel egysége (kg vagy
darab)
productFeeRate xs:decimal Igen A termékdíj díjtétele
(HUF/egység)
productFeeAmount xs:decimal Igen Termékdíj összege forintban
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Def
ault
productFeeCode ProductCodeType - - -
productFeeQuantity QuantityType - - -
productFeeMeasuring
Unit
```
```
ProductFeeMeasuringUnitType - DARAB,
KG
```
##### -

```
productFeeRate MonetaryType total digits:18,
fraction digits:2
```
##### - -

```
productFeeAmount MonetaryType total digits:18,
fraction digits:2
```
Amikor a termékkód adatot a ProductFeeDataType-on belül szerepeltetik, ott csak Csk vagy Kt kód

adható meg.


**2.2.3.8.1 productFeeCode**

Az elem ProductCodeType típusú. Leírása a „ **productCodes”** fejezetben található. Ha a típust
productFeeCode-ként alkalmazzuk, akkor productCodeOwnValue ág nem használható.

**2.2.3.9 conventionalLineInfo**
A számla tételsorára jellemző további adatok szerepeltetéséhez. Részleteket lásd az **Egyezményes,
nevesített adatok szerepeltetése** cím alatt.

**2.2.3.10 additionalLineData**
A számla tételsorára jellemző további adatok szerepeltetéséhez. Részleteket lásd az **Előre nem
nevesített adatok szerepeltetése** cím alatt.

#### 2.2.4 productFeeSummary

## 74. ábra A ProductFeeSummaryType felépítése

A séma lehetőséget biztosít a környezetvédelmi termékdíj törvény szerinti azon záradékok

feltüntetésére is, amelyeket a termékdíj visszaigénylésekor, illetve az áru termékdíj raktárba történő
beszállításakor kell a számlán szerepeltetni.

A productFeeSummary elem (típusa: ProductFeeSummaryType) a termékdíj visszaigénylése esetén
pontosan egy refundData (típusa: RefundDataType) elemet tartalmaz.

```
Tag Típus Kötelező Tartalma
productFeeOperation xs:string Igen Annak jelzése, hogy a termékdíj
összesítés visszaigénylésre
(REFUND) vagy raktárba történő
beszállításra (DEPOSIT)
vonatkozik
productFeeData xs:complexType Igen Termékdíjadatok
ProductChargeSum xs:decimal Igen Termékdíj összesen
PaymentEvidenceDocumentData xs:complexType Nem A termékdíj bevallását igazoló
dokumentum adatai a 2011. évi
```

```
LXXXV. tv. 13. § (3) szerint és a
```
25. § (3) szerint

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
productFeeOperation ProductFeeOperationType - REFUND
DEPOSIT
```
##### -

```
productFeeData ProductFeeDataType -
ProductChargeSum MonetaryType total
digits:18,
fraction
digits:2
PaymentEvidenceDocumentData PaymentEvidenceDocumentDataType - - -
```
**2.2.4.1.1 productFeedata**

A típus megegyezik a „ **lineProductFeeContent”** fejezetben leírt típussal

**2.2.4.1.2 paymentEvidenceDocumentData**

## 75. ábra A PaymentEvidenceDocumentDataType felépítése

A paymentEvidenceDocumentData elemben hivatkozott dokumentumra (számla vagy egyéb
dokumentum) nem feltétlenül vonatkozik adatszolgáltatási kötelezettség, illetve tipikusan nem az az
adózó szolgáltat róla adatot, aki a visszaigényléssel kapcsolatos záradékokat a számlán szerepelteti.

```
Tag Típus Kötelező Tartalma
evidenceDocumentNo xs:string Igen Számla sorszáma vagy egyéb
okirat azonosító száma
evidenceDocumentDate xs:date Igen Számla kelte
obligatedName xs:string Igen Kötelezett neve
obligatedAddress xs:complexType Igen Kötelezett címe
obligatedTaxNumber xs:complexType Igen A kötelezett adószáma
```

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
evidenceDocumentNo SimpleText50NotBlankType .*[^\s].* - -
evidenceDocumentDate InvoiceDateType \d{4}-\d{2}-\d{2}
minInclusive = 2010- 01 - 01
```
##### - -

```
obligatedName SimpleText255NotBlankType .*[^\s].* - -
obligatedAddress AddressType - - -
obligatedTaxNumber TaxNumberType - - -
```
2.2.4.1.2.1 **obligatedAddress**
Az Addresstype leírást lásd a „ **Címadatok a sémában”** című fejezetben.

#### 2.2.5 invoiceSummary

## 76. ábra A SummaryType felépítése

A számla összegző adatait az invoiceSummary elem (típusa: SummaryType) tartalmazza. Az
invoiceSummary elem adattartalma attól függ, hogy az adott számla (illetve a módosítással érintett
eredeti számla) nem egyszerűsített (normál vagy gyűjtő) számla vagy egyszerűsített számla.

Az invoiceSummary elem nem egyszerűsített számla esetén summaryNormal elemet, egyszerűsített
számla esetén a summarySimplified elemet tartalmazza.

Az invoiceSummary elem módosításról történő adatszolgáltatás esetén az adott módosító okirat
hatását mutatja be az eredeti számla összesítő adataira.

```
Tag Típus Kötelező Tartalma
summaryGrossData/invoiceGrossA
mount
```
```
xs:decimal Nem A számla bruttó összege a
számla pénznemében
summaryGrossData/invoiceGrossA
mountHUF
```
```
xs:decimal Nem A számla bruttó összege
forintban
```

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
summaryGrossData/invoiceGrossAmount MonetaryType total digits:18,
fraction digits:2
```
##### - -

```
summaryGrossData/invoiceGrossAmountHUF MonetaryType total digits:18,
fraction digits:2
```
##### - -

**2.2.5.1 summaryNormal**

## 77. ábra A SummaryNormalType felépítése

```
Tag Típus Kötelező Tartalma
summaryByVatRate xs:complexType Igen Összesítés áfa-mérték szerint
invoiceNetAmount xs:decimal Igen A számla nettó összege a számla
pénznemében
invoiceNetAmountHUF xs:decimal Igen A számla nettó összege
forintban
invoiceVatAmount xs:decimal Igen A számla áfa összege a számla
pénznemében
invoiceVatAmountHUF xs:decimal Igen A számla áfa összege forintban
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
summaryByVatRate SummaryByVatRateType - - -
invoiceNetAmount MonetaryType total digits:18, fraction
digits:2
```
##### - -

```
invoiceNetAmountHUF MonetaryType total digits:18, fraction
digits:2
```
##### - -


```
invoiceVatAmount MonetaryType total digits:18, fraction
digits:2
```
##### - -

```
invoiceVatAmountHUF MonetaryType total digits:18, fraction
digits:2
```
##### - -

**2.2.5.1.1 summaryByVatRate**

## 78. ábra A SummaryByVatRate felépítése

```
Tag Típus Kötelező Tartalma
vatRate xs:complexType Igen Adómérték vagy adómentesség
jelölése
```

```
vatRateNetData/vatRateNetAmoun
t
```
```
xs:decimal Igen Az adott adómértékhez tartozó
értékesítés vagy
szolgáltatásnyújtás nettó
összege a számla pénznemében
vatRateNetData/vatRateNetAmoun
tHUF
```
```
xs:decimal Igen Az adott adómértékhez tartozó
értékesítés vagy
szolgáltatásnyújtás nettó
összege forintban
vatRateVatData/vatRateVatAmount xs:decimal Igen Az adott adómértékhez tartozó
értékesítés vagy
szolgáltatásnyújtás áfa összege
a számla pénznemében
vatRateVatData/vatRateVatAmount
HUF
```
```
xs:decimal Igen Az adott adómértékhez tartozó
értékesítés vagy
szolgáltatásnyújtás áfa összege
forintban
vatRateGrossData/vatRateGrossAm
ount
```
```
xs:decimal Nem Az adott adómértékhez tartozó
értékesítés vagy
szolgáltatásnyújtás bruttó
összege a számla pénznemében
vatRateGrossData/vatRateGrossAm
ountHUF
```
```
xs:decimal Nem Az adott adómértékhez tartozó
értékesítés vagy
szolgáltatásnyújtás bruttó
összege forintban
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
vatRate VatRateType - - -
vatRateNetData/vatRateNetAmount MonetaryType total digits:18, fraction
digits:2
```
##### - -

```
vatRateNetData/vatRateNetAmountHUF MonetaryType total digits:18, fraction
digits:2
```
##### - -

```
vatRateVatData/vatRateVatAmount MonetaryType total digits:18, fraction
digits:2
```
##### - -

```
vatRateVatData/vatRateVatAmountHUF MonetaryType total digits:18, fraction
digits:2
```
##### - -

```
vatRateGrossData/vatRateGrossAmount MonetaryType total digits:18, fraction
digits:2
```
##### - -

```
vatRateGrossData/vatRateGrossAmountHUF MonetaryType total digits:18, fraction
digits:2
```
##### - -

**2.2.5.1.2 vatRate**
A vatRateType komplex típus részletes leírása a „tételek (invoiceLines)” fejezeten belül olvasható.

Összesítőkben ugyanaz a komplex típus van használatban, ugyanolyan megadható értékekekkel és
szabályokkal a számla típusára vonatkozóan.

Azoknál az adómértékeknél, ahol case-reason alábontásos szerkeszet van (vatExemption,
vatOutOfScope), azonos case (de eltérő reason) esetekhez elegendő egy darab összesítőt közölni az


adatszolgáltatásban. A specifikációban szereplő magyarázatok az egyes case értékekhez megadhatóak

az összesítőben reason-ként.

A vatAmountMismatch csomópont esetén minden disztinkt case-vatRate párosra kell összesítőt
képezni, amely szerepel a tételek között.

**2.2.5.2 summarySimplified**

## 79. ábra A SummarySimplifiedType felépítése

**Tag Típus Kötelező Tartalma**
vatRate xs:complexType Igen Egyszerűsített számla esetén az
adótartalom vagy
adómentesség jelölése
vatContentGrossAmount xs:decimal Igen Az adott adótartalomhoz
tartozó értékesítés vagy
szolgáltatásnyújtás bruttó
összege a számla pénznemében
vatContentGrossAmountHUF xs:decimal Igen Az adott adótartalomhoz
tartozó értékesítés vagy
szolgáltatásnyújtás bruttó
összege forintban
_* a kék háttérrel jelölt tagek értékkészletét validáció vizsgálja. Nem megengedett érték megadásakor a rendszer validációs
hibát ad az adatszolgáltatásra, lásd: 3.3.2 fejezet_

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
vatRate VatRateType - - -
vatContentGrossAmount MonetaryType total digits:18, fraction
digits:2
```
##### - -

```
vatContentGrossAmountHUF MonetaryType total digits:18, fraction
digits:2
```
##### - -


A vatRateType komplex típus részletes leírása a „tételek (invoiceLines)” fejezeten belül olvasható.

Összesítőkben ugyanaz a komplex típus van használatban, ugyanolyan megadható értékekekkel és
szabályokkal a számla típusára vonatkozóan.

### 2.3 AZ ÜZLETI TARTALOMBAN SZEREPLŐ TÍPUSOK LEÍRÁSA

A jelen tájékoztató anyag „ **A számla/módosítás séma részletes tartalma”** fejezetében szereplő,
korábban nem részletezett típusok leírását ez a fejezet tartalmazza. Az egyes típusok betűrendben, a

típusok neve alapján szerepelnek.

#### 2.3.1 BankAccountNumberType (Bankszámlaszám típus)

Az ezen típusba tartozó elemek a következő bankszámlaszám formátumokat tartalmazhatják:

```
a) Kétszer nyolc számjegy, kötőjellel elválasztva (12345678-12345678)
b) Háromszor nyolc számjegy, kötőjellel elválasztva (12345678- 12345678 - 12345678)
c) Kétbetűs országkód + kétjegyű ellenőrzőszám + 11 - 30 számjegyű belföldi pénzforgalmi
jelzőszám (IBAN, International Bank Account Number)
```
#### 2.3.2 Boolean (Logikai érték)

Az XML 1.0 szabvány szerinti logikai érték. Értéke true (igaz) vagy false (hamis) lehet.

#### 2.3.3 InvoiceDateType (Dátum típus).................................................................................................

Az XML 1.0 szabvány szerinti dátum típus. Értéke „ÉÉÉÉ-HH-NN” alakú, ahol ÉÉÉÉ az év száma, HH a
hónap sorszáma két karakteren, NN a nap sorszáma két karakteren. 2010.01.01-nél korábbi érték nem
adható meg.

#### 2.3.4 ExchangeRateType (Árfolyam típus)

Az árfolyam típus a különböző árfolyamok leírására szolgál. Legfeljebb 14 számjegyet tartalmazhat,
ebből legfeljebb 6 lehet a tizedesponttól jobbra. Értéke csak nemnegatív lehet.

#### 2.3.5 InvoiceAppearanceType (Megjelenési forma típus)

Az ezen típusba tartozó elem lehetséges értékei a következők:

```
Számla megjelenési formája
```
```
InvoiceAppearanceType
típusú elem értéke
Papíralapú számla PAPER
Elektronikus, nem EDI számla ELECTRONIC
Elektronikus, EDI számla EDI
A szoftver nem képes azonosítani vagy a számla
kiállításakor nem ismert.
```
```
UNKNOWN
```
Elektronikus számlán az Áfa törvény 259. § 5. pontja szerinti számla értendő. Az EDI számlán az
elektronikus adatcsererendszerben elektronikus adatként létrehozott és továbbított elektronikus
számla értendő.

Az „UNKNOWN” érték például abban az esetben lehet használatos az adatszolgáltatásban, ha a
számlázó szoftver a számla kiállításakor még nem ismeri vagy nem képes azonosítani a számla
megjelenési formáját.

#### 2.3.6 InvoiceCategoryType (Számla típusa)

A számla típusának megjelölésére szolgáló típus az alábbi értékekkel.


```
Számla típusa
```
```
InvoiceCategoryType
típusú elem értéke
Normál (azaz nem egyszerűsített és
nem gyűjtő-) számla
```
```
NORMAL
```
```
Egyszerűsített számla SIMPLIFIED
Gyűjtőszámla AGGREGATE
```
#### 2.3.7 MarginSchemeType (Különbözet szerinti adózás típus)

A különbözet szerinti adózás jogcímének jelölésére szolgál.

```
Jogcím
```
```
MarginSchemeType
típusú elem értéke
Utazási irodák TRAVEL_AGENCY
Használt cikkek SECOND_HAND
Műalkotások ARTWORK
Gyűjteménydarabok és régiségek ANTIQUES
```
#### 2.3.8 MonetaryType (Pénzösszeg típus)

A pénzérték típusú elem legfeljebb 18 számjegyet tartalmazhat, amiből legfeljebb 2 lehet a
tizedesponttól jobbra. Értéke lehet negatív is.

#### 2.3.9 PaymentMethodType (Fizetés módja típus)

Az ezen típusba tartozó elem lehetséges értékei a következők:

```
Fizetés módja
```
```
PaymentMethodType
típusú elem értéke
Átutalás TRANSFER
Készpénz CASH
Bankkártya, hitelkártya, egyéb
készpénz helyettesítő eszköz
```
```
CARD
```
```
Utalvány, váltó, egyéb
pénzhelyettesítő eszköz
```
```
VOUCHER
```
```
Egyéb OTHER
```
#### 2.3.10 ProductCodeCategoryType (Termékkódfajta típus)

Az ezen típusba tartozó elem legfeljebb egyszer szerepelhet egy tételnél. A típusban számos
különböző, az adott tételre vonatkozó kód tüntethető fel, egy-egy termék - vagy szolgáltatáskód
típusból akár több is.

```
Termékkód típusa
```
```
ProductCodeCategoryType
típusú elem értéke
Vámtarifa szám VTSZ VTSZ
Szolgáltatás jegyzék szám SZJ SZJ
KN kód (Kombinált Nómenklatúra, 2658/87/EGK
rendelet I. melléklete)
```
```
KN
```

```
A Jövedéki törvény (2016. évi LXVIII. tv) szerinti e-
TKO adminisztratív hivatkozási kódja AHK
```
```
AHK
```
```
A termék 343/2011. (XII. 29) Korm. rendelet 1. sz.
melléklet A) cím szerinti csomagolószer-katalógus
kódja (CsK kód)
```
```
CSK
```
```
A termék 343/2011. (XII. 29) Korm. rendelet 1. sz.
melléklet B) cím szerinti környezetvédelmi
termékkódja (Kt kód)
```
```
KT
```
```
Építményjegyzék szám EJ
Termékek és szolgáltatások osztályozási rendszere TESZOR
A vállalkozás által képzett termékkód OWN
Egyéb OTHER
```
#### 2.3.11 ProductStreamType (Termékáram típus)

A környezetvédelmi termékdíj szempontjából sorolja be a tételt a termékdíj törvény szerinti
termékáramba. Lehetséges értékei az alábbiak:

```
Termékáram
```
```
ProductStreamType
típusú elem értéke
akkumulátor BATTERY
csomagolószer PACKAGING
egyéb kőolajtermék OTHER_PETROL
az elektromos, elektronikai berendezés ELECTRONIC
gumiabroncs TIRE
reklámhordozó papír COMMERCIAL
egyéb műanyag termék PLASTIC
egyéb vegyipari termék OTHER_CHEMICAL
irodai papír PAPER
```
#### 2.3.12 QuantityType (Mennyiség típus)

A mennyiség típus legfeljebb 22 számjegyet tartalmazhat, ebből legfeljebb 6 számjegy lehet a
tizedesponttól jobbra. Értéke lehet negatív is.

Ez a típus jelenik meg a tételhez tartozó mennyiség mellett az egységárra vonatkozó elemben is, mert
ugyan az egységár egy pénzérték, de a gyakorlatban szükséges lehet a pénzérték típusban
(MonetaryType) megengedettnél több tizedesjegyre.

#### 2.3.13 RateType (Arány típus)

Az arány típusú elem egy 0 és 1 közötti számot tartalmaz, a tizedesponttól jobbra legfeljebb 4
tizedesjegy állhat.

#### 2.3.14 TakeoverType (Termékdíj átvállalás típus)

A típusba tartozó elemek jelzik a termékdíj átvállalás irányát és jogszabályi alapját. A lehetséges
értékek listája az alábbi:


```
Termékdíj átvállalás iránya és alapja
```
```
TakeoverType típusú
elem értéke
A 2011. évi LXXXV. tv. 14. § (4) bekezdés szerint
az eladó (első belföldi forgalomba hozó) vállalja
át a vevő termékdíj-kötelezettségét.
```
```
01
```
```
A 2011. évi LXXXV. tv. 14. § (5) aa) alpontja
szerint a vevő szerződés alapján átvállalja az
eladó termékdíj-kötelezettségét.
```
```
02_aa
```
```
A 2011. évi LXXXV. tv. 14. § (5) ab) alpontja
szerint a vevő szerződés alapján átvállalja az
eladó termékdíj-kötelezettségét.
```
```
02_ab
```
```
A 2011. évi LXXXV. tv. 14. § (5) b) alpontja szerint
a vevő szerződés alapján átvállalja az eladó
termékdíj-kötelezettségét.
```
```
02_b
```
```
A 2011. évi LXXXV. tv. 14. § (5) c) alpontja szerint
a vevő szerződés alapján átvállalja az eladó
termékdíj-kötelezettségét.
```
```
02_c
```
```
A 2011. évi LXXXV. tv. 14. § (5) d) alpontja szerint
a vevő szerződés alapján átvállalja az eladó
termékdíj-kötelezettségét.
```
```
02_d
```
```
A 2011. évi LXXXV. tv. 14. § (5) ea) alpontja
szerint a vevő szerződés alapján átvállalja az
eladó termékdíj-kötelezettségét.
```
```
02_ea
```
```
A 2011. évi LXXXV. tv. 14. § (5) eb) alpontja
szerint a vevő szerződés alapján átvállalja az
eladó termékdíj-kötelezettségét.
```
```
02_eb
```
```
A 2011. évi LXXXV. tv. 14. § (5) fa) alpontja szerint
a vevő szerződés alapján átvállalja az eladó
termékdíj-kötelezettségét.
```
```
02_fa
```
```
A 2011. évi LXXXV. tv. 14. § (5) fb) alpontja szerint
a vevő szerződés alapján átvállalja az eladó
termékdíj-kötelezettségét.
```
```
02_fb
```
```
A 2011. évi LXXXV. tv. 14. § (5) ga) alpontja
szerint a vevő szerződés alapján átvállalja az
eladó termékdíj-kötelezettségét.
```
```
02_ga
```
```
A 2011. évi LXXXV. tv. 14. § (5) gb) alpontja
szerint a vevő szerződés alapján átvállalja az
eladó termékdíj-kötelezettségét.
```
```
02_gb
```
#### 2.3.15 InvoiceTimestampType (időbélyeg típus)

Az XML 1.0 szabvány szerinti időbélyeg típus. Értéke „ÉÉÉÉ-HH-NNTHH24:MM:SS.sssZ” alakú, ahol

ÉÉÉÉ az év száma, HH a hónap sorszáma két karakteren, NN a nap sorszáma két karakteren, T az
elválasztó, HH24 az óra két karakteren, MM a perc két karakteren, SS.sss a másodperc 5 karakteren
ezred másodperc értékig, és Z az UTC idő jelölő. 2010.01.01T00:00:00.000Z-nél korábbi érték nem
adható meg.


#### 2.3.16 UnitOfMeasureType (mennyiségi egység típus)

Számlasor megadásakor a számlán szereplő mennyiségi egység alábbi értékkészlet szerinti megadása
kötelező, ha a válaszott mennyiségi egység alkalmazható. Lehetőség van saját mennyiségi egység
megadására is, mely a számlán szereplő mennyiségi egységet jelenti.

```
Mennyiségi egység
```
```
UnitOfMeasureType
típusú elem értéke
Darab PIECE
Kilogramm KILOGRAM
Tonna TON
Kilowatt óra KWH
Nap DAY
Óra HOUR
Perc MINUTE
Hónap MONTH
Liter LITER
Kilométer KILOMETER
Köbméter CUBIC_METER
Méter METER
Folyóméter LINEAR_METER
Karton CARTON
Csomag PACK
Saját OWN
```
#### 2.3.17 LineNatureIndicatorType (termék/szolgáltatás jelölő típus)

A típus enumerációként tartalmazza, hogy az adott számlasorban található tétel jellege termék,
szolgáltatás vagy egyéb. Az enum helyes megállapításának az alapját képezi az, hogy számla

tételsorszinten elérhető legyen az az információ, hogy az adott tételsor terméket, szolgáltatást vagy
egyéb értékesítés jelleget takar. Kizárólag a tételsor leírásából ezt a helyes enumot az esetek túlnyomó
többségében nem lehetséges megképezni.

Az alábbiakban útmutatás jelleggel bemutatunk olyan lehetőségeket, melyek alapján a helyes
adatszolgáltatás összeállítható, ha a számlázóprogram implementálja a lineNatureIndicator tag
töltését. Az útmutató természetétől adódóan nem lehet teljes körű, kizárólag ötleteket ad a
lineNatureIndicator meghatározásához.

**Termék/szolgáltatás elkülönítése**

- Ha van terméktörzs, akkor mellé ki lehet alakítani szolgáltatás törzset is, mely által
    egyértelműen meghatározható, hogy az adott számlasor termék vagy szolgáltatás.
- A terméktörzset ki lehet bővíteni egy olyan jelölővel, mely a termék/szolgáltatás jellegre utal.
- Ha egy társaság jellemzően csak terméket vagy jellemzően csak szolgáltatást értékesít, akkor
    lehet azzal a megoldással élni, hogy a számlakiállításnál a jellemző értékesítés jelleget adja
    alapértelmezetten a program. Az alapértelmezett jelölést a számla kiállítója meg tudja
    változtatni, ugyanakkor erre csupán akkor van szükség, ha nem a szokásos értékesítése
    történik.


- A vállalatirányítási rendszereknél jellemzően használt elem az adókód. Az adókód
    meghatározása vállalatonként eltérő, nincs erre kialakított egységes standard. Ha az adókód
    felépítése egyben meghatározza a termék/szolgáltatás jelleget, akkor az adókód is megfelelő
    inputja lehet a lineNatureIndicator megképzésének.
- Előfordulhat, hogy a számlázó program nem használ törzset, vagy a törzsön kívüli adatokkal is
    lehetséges tételsor bevitele. Ezekben az esetekben a beviteli képernyőn célszerű kialakítani
    egy mezőt, melyben lehet jelölni a tételsor termék/szolgáltatás jellegét.

**Egyéb**

A terméken és szolgáltatáson kívül előfordulnak olyan tételsorok egy számlán, melyet ezekbe a
kategóriákba nem lehet besorolni. Ezek például olyan összegek, melyeket az adózó más nevében és
más javára szed be. Ilyen lehet például az idegenforgalmi adó.

Az elem meghatározása nagyon szoftverfüggő. Ha például egy szállodáknál alkalmazott számlázó
szoftverrel az idegenforgalmi adó meghatározásra kerül, akkor a szoftver jellemzően ezt külön is kezeli.
Ennek lehet akár egy külön termékkódja, melyhez hozzá lehet párosítani a lineNatureIndicator elemet.
Lehet akár egy belső logika is, mely alapján automatikusan számításra kerül. Ebben az esetben a belső

logika futásánál kerülhet kitöltésre a lineNatureIndicator.

Ha az ilyen típusú tételsorok meghatározása nem a fenti módszerekkel történik meg, akkor a
termék/szolgáltatás elkülönítése részben leírtakat lehet alkalmazni ennek az adatelemnek a
meghatározására.

### 2.4 KORÁBBI ADATSZOLGÁLTATÁS TECHNIKAI ÉRVÉNYTELENÍTÉSE

Az online számlaadat-szolgáltatáshoz kapcsolódóan lehetőség van korábban elvégzett adatszolgáltatás
technikai érvénytelenítésére abban az esetben, ha a korábbi adatszolgáltatás technikai hibából
kifolyólag hibás adatokkal valósult meg.

Kiemelendő, hogy **az adatszolgáltatás technikai érvénytelenítése NEM azonos a számla
érvénytelenítéséről („érvénytelenítő számláról”) történő adatszolgáltatással** : a technikai
érvénytelenítés azt az esetet kezeli, amikor a számla, vagy számlával egy tekintet alá eső okirat
helyesen írja le az adott gazdasági eseményt, de az adatszolgáltatás technikai hiba folytán hibás
adatokkal valósult meg.

Nem lehetséges az adatszolgáltatás érvénytelenítése, ha az adatszolgáltatás egyben a számla is, így a
<completnessIndicator> elem értéke „true”. Ugyancsak nem lehetséges az adatszolgáltatás
érvénytelenítését végrehajtani, ha az alapszámla bár nem számít egyben elektronikus számlának,
azonban a számlázási láncban szerepel olyan adatszolgáltatás, ahol a <completnessIndicator>=true.

Téves adatszolgáltatás esetén a technikai érvénytelenítésre nem kizárólag gép-gép kapcsolaton
keresztül van lehetőség. Az adatszolgáltatás „kézzel”, felhasználó által történő javításának módjára
jelen dokumentum nem tér ki. Fontos ugyanakkor kiemelni, hogy az adatszolgáltatás technikai
érvénytelenítését a megfelelő jogosultsággal rendelkező felhasználónak az Online Számla rendszer
felületén jóvá kell hagynia.

A technikai érvénytelenítés képességét, mint funkciót nem kötelező implementálni a számlázó

programokban, tekintettel a kézi javítás lehetőségére. Elsősorban olyan számlázó rendszerek esetén


ajánlott a funkciót kifejleszteni, ahol jellemző a számlák nagy tömegben történő kiállítása rövid idő

alatt, így ezen lehetőség nélkül, egy esetleges technikai hiba esetén a nagy tömegű, téves
adatszolgáltatás javítása megoldhatatlan feladat elé állítaná az adott rendszer üzemeltetőit.

## 80. ábra Az InvoiceAnnulmentType felépítése

```
Tag Típus Kötelező Tartalma
annulmentReference xs:string Igen A technikai érvénytelenítéssel érintett
számla vagy módosító okirat sorszáma
annulmentTimestamp dateTime Igen A technikai érvénytelenítés időbélyege a
forrásrendszerben UTC idő szerint
annulmentCode xs:string Igen A technikai érvénytelenítés kódja
annulmentReason xs:string Igen A technikai érvénytelenítés oka
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Defa
ult
annulmentRefer
ence
```
```
SimpleText50NotBlan
kType
```
```
.*[^\s].* - -
```
```
annulmentTime
stamp
```
```
InvoiceTimestampTyp
e
```
```
\d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.\
d{1,3})?Z minInclusive =
2010 - 01 - 01T00:00:00Z
```
##### - -

```
annulmentCode AnnulmentCodeType - ERRATIC_DATA
ERRATIC_INVOICE_NUMBE
R
ERRATIC_INVOICE_ISSUE_D
ATE
ERRATIC_ELECTRONIC_HAS
H_VALUE
```
##### -

```
annulmentReas
on
```
```
SimpleText1024NotBl
ankType
```
```
.*[^\s].* - -
```

#### 2.4.1 Adatszolgáltatás technikai érvénytelenítésére vonatkozó szabályok

1. Technikai érvénytelenítés kizárólag olyan korábbi adatszolgáltatásra vonatkozóan teljesíthető,
amelyre már sikeres visszaigazoló nyugta („DONE”) érkezett, és kizárólag figyelmeztetéseket („WARN”)
vagy azt sem tartalmaz a válaszüzenet.
2. Technikai érvénytelenítés a /manageAnnulment operáción keresztül történik úgy, hogy a legfeljebb
100 darab annulmentOperation elem mindegyike technikai érvénytelenítést tartalmaz. A belső base64
tartalomnak az invoiceAnnulment sémaleíróban definált elemeket kell tartalmaznia. A séma nem

enged meg egy műveleten belül technikai érvénytelenítést és „eredeti” (CREATE/MODIFY/STORNO)
adatszolgáltatást vegyesen benyújtani.

3. Technikai érvénytelenítés számlán és számlával egy tekintet alá eső okiraton egyaránt elvégezhető.
A technikai érvénytelenítések száma nem korlátozott. Ugyanakkor a technikai érvénytelenítésekre
vonatkozó adatok a kockázatelemző rendszer bemenő adataként használhatók.
4. A feldolgozó rendszer a technikai érvénytelenítést a számla vagy számlával egy tekintet alá eső okirat
sorszáma (invoiceNumber elem) alapján illeszti, amit a technikai érvénytelenítésről történő
adatszolgáltatásban az annulmentReference elemben kell közölni.
5. Ha a technikai érvénytelenítés olyan számlára érkezik, amelyhez kapcsolódóan már történt
módosításról történő adatszolgáltatás is, akkor a technikai érvénytelenítés automatikusan, külön kérés

nélkül vonatkozik mindegyik módosításról történő adatszolgáltatásra is.

6. Ha a technikai érvénytelenítés módosító okiratra vonatkozik, akkor a technikai érvénytelenítés
kizárólag erre az okiratra értendő, az eredeti számlára, illetve esetleges más módosításokra nem.
7. Technikai érvénytelenítéskor az annulmentOperation tag értékét mindig ANNUL értékkel kell
közölni.
8. A technikai érvénytelenítés sikeres teljesítését követően a technikai érvénytelenítések mindegyikére
vonatkozóan web felhasználói jóváhagyás szükséges. Ennek részleteit a felhasználói felület
dokumentációja tartalmazza.
9. A technikai érvénytelenítéssel érintett okiratok sorszáma (a technikai érvénytelenítés jóváhagyását

követően) újra felhasználható.

10. A completenessIndicator = true jelzésű adatszolgáltatásokat, ahol az adatszolgáltatás maga az
elektronikus számla, nem lehetséges technikai érvényteleníteni. Ezt külön üzleti validáció figyeli,
részletek a „Hibakezelés” fejezetben.

### 2.5 ADATSZOLGÁLTATÁS SZÁMLÁVAL EGY TEKINTET ALÁ ESŐ OKIRATOKRÓL

A Bevezetőben említett törvényi szabályozás kifejezetten rendelkezik arról, hogy a számlázó
programmal kiállított számlák módosításáról, érvénytelenítéséről (Áfa törvény terminológiája szerint
„számlával egy tekintet alá eső okiratokról”) is adatot kell szolgáltatnia a számlázó programnak, a
vonatkozó feltételek teljesülése esetén.

A számlát leíró séma úgy került kidolgozásra, hogy alkalmas legyen az adott számlát érintő módosítások
adatainak közlésére is, figyelemmel a következő tényekre:


- Az Áfa törvény a gazdasági eseményt leíró eredeti számlát tekinti számlának, ennek minden
    módosítása, adott esetben érvénytelenítése is az eredeti számlával egy tekintet alá eső
    okiratnak számít. Egy számla érvénytelenítése és újabb (immár helyes) számla kiállítása esetén,
    mind az érvénytelenítő okirat, mind az új számla az eredeti számla módosító okiratának
    tekintendő.
- Jogszabály nem tiltja, hogy egy számlára vonatkozóan több módosító okirat is kiállításra
    kerüljön.
- A módosító okirat kötelező adattartalma az Áfa törvény 170. § (1) bekezdés szerint:

```
„a) az okirat kibocsátásának kelte;
b) az okirat sorszáma, amely az okiratot kétséget kizáróan azonosítja;
c) hivatkozás arra a számlára, amelynek adattartalmát az okirat módosítja;
e) a számla adatának megnevezése, amelyet a módosítás érint, valamint a módosítás
természete, illetőleg annak számszerű hatása, ha ilyen van.”
```
- Jogszabály nem tiltja, hogy egy módosító okirattal több, korábban kiállított számla kerüljön
    módosításra.
- A módosító okiratot a módosításra okot adó tény, körülmény bekövetkeztétől számított
    ésszerű időn belül kell kibocsátani. A gyakorlatban az eredeti számla kiállításától
    (kibocsátásától) a módosító okirat kiállításáig (kibocsátásáig) hosszabb idő is eltelhet.
- Az online számlaadat-szolgáltatás alapvető céljából következően a módosításról történő
    adatszolgáltatást úgy kell megtenni, hogy a NAV feldolgozó rendszer oldalán minden
    időpontban egyértelműen megállapítható legyen az eredeti számla és az arra vonatkozó összes
    módosító (érvénytelenítő) okirat által együttesen leírt gazdasági esemény minden olyan adata,
    amire az adatszolgáltatási kötelezettség kiterjed.

Az online számlaadat-szolgáltatáskor az alábbiakra van lehetőség:

1. Adatszolgáltatás számláról (eredeti számláról)
2. Adatszolgáltatás számla módosításáról (számlával egy tekintet alá eső okirat)
3. Adatszolgáltatás számla érvénytelenítéséről (számlával egy tekintet alá eső okirat)

Nincs lehetőség módosító okirat módosítására. Az Áfa törvény alapján, ha a módosító okirat téves
adatokkal került kiadásra, akkor ennek esetleges módosítása az eredeti számla újabb módosításának
tekintendő és ennek megfelelően is kell róla adatot szolgáltatni.

Módosításról és érvénytelenítésről szóló adatszolgáltatás esetén, ha a hivatkozott számláról már van
létezik adatszolgáltatás, akkor érdemes annak DONE státuszát megvárni a módosítás beküldése előtt.
Mivel a számlafeldolgozás aszinkron módon történik, így a számla, és annak módosítása egyidejű
adatszolgáltatása esetén a sorrendiség nem garantált.

#### 2.5.1 Adatszolgáltatás számla érvénytelenítéséről

Számlát érvénytelenítő okirat kiállításáról történő adatszolgáltatás esetén az adatszolgáltatás API XML-
jében az invoiceOperation elem értéke „STORNO”, ettől eltekintve az érvénytelenítő okirat kiállításáról
történő adatszolgáltatás technikailag a számlaadat-szolgáltatással azonos módon történik.


Az érvénytelenítő okirat adatait leíró XML-ben az alábbi elemek szerepeltetése kötelező:

1. InvoiceData/invoiceMain/invoice/invoiceReference/originalInvoiceNumber: az eredeti,
    érvénytelenítésre kerülő számla sorszáma. (Az eredeti számlaadat-szolgáltatásban 1.x számla
    verzió esetén ez az invoiceHead/invoiceData/invoiceNumber elem értéke, míg 2.0 verziótól
    kezdődően az InvoiceData/invoiceNumber elem értéke).
2. InvoiceData/invoiceMain/invoice/invoiceReference/modificationIndex: a módosítás logikai
    sorrendjét jelölő adat (az első módosításnál mindig 1)
3. InvoiceData/invoiceIssueDate: a módosító okirat (jelen esetben az érvénytelenítő okirat) kelte.
4. InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/supplierTaxNumber/taxpayerId
5. InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/supplierAddress megfelelő
    ágának kötelező adatai
6. InvoiceData/invoiceNumber: az érvénytelenítő okirat saját sorszáma.
7. InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/invoiceCategory: az eredeti
    számla típusa
8. InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/invoiceDeliveryDate
9. InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/currencyCode
10. InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
11. InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/invoiceAppearance: a számla
    megjelenési formája.
12. InvoiceData/invoiceMain/invoice/invoiceSummary

Ezen túlmenően az érvénytelenítésről történő adatszolgáltatásban kötelező szerepeltetni azokat az
adatokat, amelyek az eredeti számlán (azt az esetleges korábbi módosító okiratokkal együtt tekintve)
módosulnak. Érvénytelenítő okiratról történő adatszolgáltatás esetén (ha a számla korábban nem lett
módosítva) az érvénytelenítésről történő adatszolgáltatás az alábbiak szerint valósul meg:

- Az eredeti számlán szereplő tételsorok adatait tartalmazza, a mennyiségek ellentétes előjellel
    szerepeltetve (ebből eredően tipikusan negatív tételsor összesen adatokkal).
- Az ellentétes előjelű számlatételek hivatkozása (lineNumberReference) folytatólagos
    sorszámot kap az eredeti számla tételeinek és az esetleges korábbi módosító számlák
    tételeinek sorszámozását folytatva.
- A lineModificationReference/lineNumberReference a lineNumberReference (a számla és
    összes módosításaiban) sorfolytonosan új tételsorszámra mutat és lineOperation értéke
    „CREATE”.
- Az eredeti számla összegző adataiban (invoiceSummary) szereplő összegek, az eredeti számla
    és az összes korábbi módosítás eredményeként előálló állapothoz képest ellentétes előjellel
    szerepelnek.

#### 2.5.2 Adatszolgáltatás számla módosításáról

Számlát módosító okirat kiállításáról történő adatszolgáltatás esetén az adatszolgáltatás API XML-
jében az invoiceOperation elem értéke „MODIFY”, ettől eltekintve a módosító okirat kiállításáról
történő adatszolgáltatás technikailag a számlaadat-szolgáltatással azonos módon történik.

A módosító okirat adatait leíró XML-ben az alábbi elemek szerepeltetése kötelező:


1. InvoiceDate/invoiceMain/invoice/invoiceReference/originalInvoiceNumber: az eredeti,
    módosításra kerülő számla sorszáma. (Az eredeti számlaadat-szolgáltatásban 1.x számla verzió
    esetén ez az invoiceHead/invoiceData/invoiceNumber elem értéke, míg 2.0 verziótól
    kezdődően az InvoiceData/invoiceNumber elem értéke).
2. InvoiceData/invoiceMain/invoice/invoiceReference/modificationIndex: a módosítás logikai
    sorrendjét jelölő adat (az első módosításnál mindig 1)
3. InvoiceData/invoiceIssueDate: a módosító okirat kelte.
4. InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/supplierTaxNumber/taxpayerId
5. InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/supplierAddress megfelelő
    ágának kötelező adatai
6. invoiceData/invoiceNumber: a módosító okirat saját sorszáma.
7. InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/invoiceCategory: az eredeti
    számla típusa
8. InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/invoiceDeliveryDate: az eredeti
    számla teljesítési dátuma, kivéve, ha ezt módosítja a bizonylat
9. InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/currencyCode
10. InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
11. InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/invoiceAppearance: a számla
    megjelenési formája.
12. InvoiceData/invoiceMain/invoice/invoiceSummary

Ezen túlmenően a módosító okiratról történő adatszolgáltatásban kötelező szerepeltetni azokat az
adatokat, amelyek az eredeti számlán (azt az esetleges korábbi módosító okiratokkal együtt tekintve)
módosulnak, az alábbiak szerint.

#### 2.5.3 Módosuló adatok a tételsorokban

Módosításról (érvénytelenítésről) történő adatszolgáltatáskor, ha a módosító okirat az eredeti számla
bármelyik tételsorában levő adatot (is) módosítja, a módosítással érintett tételsor teljes újraközlésére
van szükség annak érdekében, hogy a gazdasági eseményt leíró számla és módosító okirat(ok)
adatainak értelmezése egyértelmű legyen.

A tételsor újraközlésekor a számszerű adatokat (árak, mennyiségek) **KÜLÖNBSÉGKÉNT** kell jelölni a

módosítandó tételsor aktuális értékéhez képest. (Az aktuális értéket az eredeti számla és az összes
korábbi módosítás együttese állítja elő.) Kivételt képeznek ez alól a közlekedési eszközök
tulajdonságait leíró, számadatokkal megadható jellemzői. Ennek értelmében szárazföldi jármű esetén
a hengerűrtartalom, teljesítmény, futott kilométer, vízi járműnél a hajó hossza, hajózott órák száma és
légi járműnél a felszállási tömeg és repült órák számának módosításakor a helyes érték újraközlése
szükséges. (Az aktuális érték az utolsó módosításban közölt érték lesz.)

A lineNumber elem minden számláról vagy módosításról történő adatszolgáltatás esetén 1-től indulva,
ismétlés és kihagyás nélküli sorszám.

A módosításról történő adatszolgáltatásban a lines/line/lineModificationReference elem tartalmazza
a módosítással érintett tételének sorszámára (lineNumberReference) történő hivatkozást, a

lineOperation elem pedig a tétel módosításának jellegét.

A lineOperation elem értéke az alábbiak egyike lehet:


- CREATE: a módosítás újabb tételsorral egészíti ki az eredeti számla és az esetleges korábbi
    módosítás(ok) által leírt állapotot. Ilyenkor a lineModificationReference elem az eredeti
    számla (lineNumber) és a korábbi módosítások (lineNumberReference) által létrehozott
    sorszámozást folytatja.
- MODIFY: **Az INVALID_LINE_OPERATION validáció bevezetése után a „MODIFY” érték**
    **megadása nem támogatott.** (a módosítás az adott tételsorban változó adatokat tartalmaz.
    Ilyenkor a lineNumberReference elem azon eredeti számlán szereplő tétel sorszámát
    (lineNumber), vagy korábbi módosító okiraton létrehozott új tétel sorszámát (a korábbi
    módosító okiraton lineNumberReference) tartalmazza, amire a módosítás vonatkozik.)

Ugyanazon módosító okiratban az eredeti számla adott tételsorára legfeljebb egy tételnél lehet
hivatkozni (lineNumberReference).

#### 2.5.4 Módosításkor szolgáltatandó adatok

Módosításról (érvénytelenítésről) történő adatszolgáltatáskor annak érdekében, hogy a módosító
okiratról teljesített gép-gép adatszolgáltatás alapján az eredeti számla és a módosító okirat együttes
tartalma megképezhető legyen, egyes adatok módosítása esetén szükséges az adatot tartalmazó elem

szülőelemének vagy a szülőelem szülőelemének teljes adattartalommal történő újraközlésére, az
alábbi táblázat szerint:

```
Módosuló adat Adatszolgáltatásban teljes adattartalommal
szerepeltetendő elem
Eladó bármelyik adata supplierInfo
Vevő bármelyik adata customerInfo
Pénzügyi képviselő bármelyik adata fiscalRepresentativeInfo
invoiceDetail elemben vagy annak
gyermekelemében szereplő bármelyik adat
```
```
invoiceDetail
```
```
Egy adott tételsorban szereplő bármelyik adat line (az adott tételsor adatait tartalmazó)
Termékdíj összegzés adatai közül bármelyik productFeeSummary
Összesítő adatok invoiceSummary (figyelemmel a 2.5.5-re)
```
#### 2.5.5 Számla összegzés adatok módosításkor

Módosításról (érvénytelenítésről) történő adatszolgáltatáskor minden esetben kötelező szerepeltetni
az invoiceSummary elemet. Módosításról történő adatszolgáltatás esetén ebben a módosító okirat
hatását kell szerepeltetni megfelelő módon a számla összegző adataira: tehát azt, hogy a módosítás
következtében az eredeti számla összegző adatai mennyivel növekedtek vagy csökkentek.

Módosításról történő adatszolgáltatás esetén tehát kifejezetten tilos az invoiceSummary elemben a
változással „egybeszerkesztett”, azaz módosult (új) állapotot közölni.

#### 2.5.6 Adatszolgáltatás több számlát módosító okiratról

Egy számla vagy módosító okirat adatait a sémában az InvoiceData/invoiceMain/invoice csomópont
írja le. Ha egy módosító okirattal több korábbi számla kerül módosításra, úgy kizárólag ebben az
esetben az adatszolgáltatási XML-ben képezhető a batchInvoice csomópont.

A batchInvoice csomópont a számlaadat-szolgáltatások leírására használt invoice csomópontot ismétli.
Az egyes módosításokat külön batchIndex értékkel kell ellátni. Az adatszolgáltatás szempontjából nincs


relevanciája, hogy az egyes módosítások melyik batchIndex alá kerülnek, azonban a batchIndex

értékének 1-től monoton növekvőnek kell lennie.

## 81 ábra A BatchInvoiceType felépítése

A kötegelt (csoportos) módosítások feldolgozása közben a rendszer az alábbi plusz ellenőrzéseket végzi
el, melyeket az adatszolgáltatáskor be kell tartani:

- A rendszernek egy adatszolgáltatási kérés közben csak egyetlen batchInvoice csomópontot
    tartalmazó kérés adható át. Másként fogalmazva, a /manageInvoice hívásban ilyen esetben az
    API XML-ben csak az 1-es index szerepelhet. Azon kéréseknél, ahol a belső base64 tartalom
    kibontásánál a rendszer batchInvoice tartalmat talál és az nem az első és kizárólagos indexen
    szerepelt az adatszolgáltatásban, automatikusan a kérés minden indexét elutasítja és
    ABORTED státuszba teszi.
- A belső base64 tartalomban batchInvoice csak akkor állhat, ha az API XML-ben az
    invoiceOperation vagy MODIFY vagy STORNO, a CREATE érték nem elfogadott. A fenti
    szabálynak nem megfelelő kérések feldolgozását a rendszer elutasítja és ABORTED státuszba
    teszi.
- A base64-es tartalomban a batchInvoice csomópontok felső korlátja nincs meghatározva,
    azonban - a séma számosságától eltérően – legalább 2 batchInvoice csomópontnak kell
    szerepelnie. Azon kérések, amelyek csak 1 batchInvoice csomópontot tartalmaznak, nem
    számítanak kötegelt módosításnak, ezért ezeknek a feldolgozását a rendszer elutasítja és
    ABORTED státuszba teszi.


- A rendszer az egyes batchInvoice csomópontok alatt szereplő adatokat külön dolgozza fel, a
    feldolgozás eredmény a batchIndex értéke alapján illeszthető. Ha a kötegelt módosítás
    feldolgozásakor bármelyik batchIndex alatt szereplő módosító okirat feldolgozása ABORTED
    státuszt kap, úgy a rendszer a kérésben szereplő összes többi kötegelt módosítás feldolgozását
    is automatikusan ABORTED státuszba teszi.
- Kötegelt módosítás csak olyan számlákra állítható ki, amelyek azonos vevőhöz tartoznak. A
    rendszer a fenti szabályt az adatszolgáltatáskor csak úgy ellenőrzi, hogy ha a kötegelt
    módosításról szóló adatszolgáltatásban szerepelnek vevői adószámok, azoknak homogénnek
    kell lennie. A fenti szabálynak nem megfelelő kérések feldolgozását a rendszer elutasítja és
    ABORTED státuszba teszi.
- Kötegelt módosításról történő adatszolgáltatáskor nem lehet ugyanannak a számlának
    ugyanazon módosítását többször szerepeltetni a kérésben. Másként fogalmazva, a teljes XML-
    ben a módosítások által hivatkozott számla számának (invoiceReference) és a módosítás
    sorrendiségét leíró elemnek (modificationIndex) egyedinek kell lennie. A fenti szabálynak nem
    megfelelő kérések feldolgozását a rendszer elutasítja és ABORTED státuszba teszi.
- A sikeresen befogadott kötegelt módosítást egyedi módon a számlaszám azonosítja. A számla
    teljes adattartalmú lekérdezése vevői oldalról ennek a birtokában végezhető el. A lekérdezés
    válaszában a vevő csak azokat a batchInvoice tételeket látja, amelyekben a vevői adószám fel
    volt tüntetve és az megegyezik a lekérdezést végző adószámával.

#### 2.5.7 Adatszolgáltatás többszöri módosításokról

A gyakorlatban előfordulhat, hogy egy kiállított eredeti számlát az adózó módosít, majd a módosító
okirat kiállítását követően újabb körülmény válik ismertté, ami miatt az adózó újabb módosító okiratot
állít ki az eredeti számla vonatkozásában.

Ugyanazon számla többszöri módosítása alkalmával az egyes módosító okiratokról adott
adatszolgáltatást mindig azon adatkörre vonatkozóan kell megtenni, ami az előző állapothoz képest
módosul az adott okirattal.

Előfordul olyan gyakorlat, hogy téves adattartalmú számlák esetén először egy ellentételező (kvázi

érvénytelenítő) számlát bocsátanak ki, majd újabb számla kerül kiállításra, immár helyes
adattartalommal. (Ezt a gyakorlatot a 2007. december 31-ig hatályban levő Áfa törvény kifejezetten
előírta a számlázó programmal kiállított számlák módosítása esetére.) Megjegyzendő, hogy ebben az
esetben a helyesen kibocsátott számla is az eredetileg kibocsátott számla módosító okiratának
tekintendő, mivel az azon bizonylatolt gazdasági esemény(ek)re vonatkozik. Így a helyes
adattartalommal rendelkező második módosító okiratnak az eredeti számlára kell hivatkoznia.

#### 2.5.8 Értelmezést segítő példák

**Példa-1.** Hibásan szerepeltetett tétel módosításának lehetőségei

Egy adózó észreveszi, hogy egy korábban kiállított, öt tételből álló számlán, annak negyedik tételeként
téves terméket tüntetett fel. A számlán a ténylegesen eladott 1 darab „F termék” helyett 4 darab „D
termék” szerepel.

**Az adózó a tévedést az alábbi módokon korrigálhatja:**

**Első lehetőség:** a számla módosítása egy lépésben, egy módosító okirattal


Az adózó módosító számlát bocsát ki, amin módosító tételként -4 darab „D termék”, illetve 1 darab „F

termék” szerepel. Ezen módosításról történő adatszolgáltatásban az adózó újabb tételként szerepelteti
a -4 db „D terméket”, illetve az 1 db „F terméket”.

Ezen módosító okiratról történő adatszolgáltatásban:

a) A módosító okiratot leíró XML első tételsorában (lineNumber=1) a LineModificationReference
elemben a lineNumberReference elem értéke „6”, lineOperation elem értéke „CREATE”, ez
tartalmazza a -4 darab „D termék” adatait.

b) A módosító okiratot leíró XML második tételsorában (lineNumber=2) a LineModificationReference
elemben a lineNumberReference elem értéke „7”, lineOperation elem értéke „CREATE”, ez
tartalmazza az 1 darab „F termék” adatait.

c) A módosító okiratot leíró XML invoiceSummary eleme teljes egészében szerepel, abban az egyes

értékek módosulásának előjeles összege szerepel.

**Második lehetőség:** a számla módosítása több lépésben, több módosító okirattal

Az adózó olyan módosító számlát bocsát ki, amelyben az eredeti számla minden tételét ellenkező
előjellel szerepelteti (kvázi érvényteleníti), ezt követően a valóságnak megfelelő adattartalommal új
okiratot bocsát ki. Fontos azonban, hogy ilyenkor mindkét okirat az eredeti számla módosításaként
kerül kiadásra, így az adatszolgáltatást mindkét okiratról az „Adatszolgáltatás számla módosításáról”
fejezetben foglaltak szerint kell teljesíteni.

**Példa-2.** Több eredeti számla módosítása egy módosító okirattal

Egy adózó észreveszi, hogy négy, korábban kibocsátott számláján tévesen tüntette fel a számla keltét.
Mivel mind a négy számlát ugyanannak a vevőnek állította ki, a hibát egy módosító okirat

kibocsátásával javítja.

Ezen módosító okiratról történő adatszolgáltatás a batchInvoice elem használatával négy különböző
módosításként fog történni úgy, hogy az egyes számlák módosuló adatait külön-külön batchInvoice
elem tartalmazza.

**Példa-3.** Eredeti számla többszöri módosítása

Egy adózó észreveszi, hogy az eredeti számlán nem szerepel a szállítmány egyik áruja, továbbá tévesen
szerepel rajta a teljesítés időpontja. Ezért módosító okiratot bocsát ki, amin egyrészt tételsorként
szerepelteti a lemaradt árut, másrészt helyesbíti a teljesítés időpontját.

Néhány nappal később kiderül, hogy a teljesítés időpontja mégsem szerepelt tévesen az eredeti
számlán. Ezért az adózó újabb módosító okiratot bocsát ki, amin jelzi, hogy mégis az eredeti számlán

feltüntetett teljesítési időpont a helyes.

Az első módosító okiratot leíró adatszolgáltatás első tételsorában (lineNumber=1) a lineOperation
elem értéke „CREATE”, ez tartalmazza az eredeti számlán nem szereplő áru adatait. Ehhez
kapcsolódóan az adatszolgáltatásban szerepel az invoiceSummary elem, ami az adott áruösszesítő
adatokra gyakorolt hatását tartalmazza. Az adatszolgáltatásban szerepel továbbá a teljesítési időpont
újabb értéke. A második módosító okiratot leíró adatszolgáltatásban csak a teljesítési időpont valódi
értéke szerepel a megfelelő elemben.

**Példa-4.** Módosított számla érvénytelenítése


Egy adózó a leszállított árukról számlát állít ki. A vevő minőségi kifogásokat támaszt, erre tekintettel a

felek 40 százalékos engedményben egyeznek meg, ezt az adózó az eredeti számla módosításával követi
le úgy, hogy a módosító okiraton tételsorként szerepelteti a minőségi kedvezményt (negatív egységár,
pozitív mennyiség).

A módosításról történő adatszolgáltatásban, az első tételsorában (lineNumber=1) a lineOperation
elem értéke „CREATE”, ez tartalmazza a minőségi kedvezmény adatait. Ehhez kapcsolódóan az
adatszolgáltatásban szerepel az invoiceSummary elem, ami a 40 százalékos kedvezmény
számlaösszesítő adatokra gyakorolt hatását (40 százalékos csökkenés) tartalmazza.

Később a vevő újabb minőségi kifogások miatt eláll az ügylettől, ezért az adózó a számlát érvényteleníti.

Az érvénytelenítő számla első tételsorában a termék eredeti egységára szerepel, negatív
mennyiséggel. A második tételsorban negatív mennyiséggel szerepel a negatív egységárú kedvezmény.

Az érvénytelenítésről nyújtott adatszolgáltatásban mindkét tételsor esetén a lineOperation elem
értéke „CREATE”. Az adatszolgáltatásban szerepel az invoiceSummary elem, ami a negatív eredeti ár
és a negatív kedvezmény eredményeként a számlaösszesítő adatokra gyakorolt hatásaként az eredeti
számlaérték 60 százalékát tartalmazza, negatív előjellel.

### 2.6 ELEKTRONIKUS SZÁMLÁZÁS TÁMOGATÁSA

Az XSD 3.0 verziója két lényeges ponton támogatja a gazdasági szereplők ügyvitelének hatékonyságát
növelő elektronikus számlázás elterjesztését:

#### 2.6.1 Archiválás

Az elektonikus számlázás terjedésének lényeges akadályaként voltak azonosíthatóak az elektronikus

számla digitális archiválásával kapcsolatos szabályozás értelmezésével, a gyakorlatban előforduló
megoldások megfelelőségével kapcsolatos bizonytalanságok.

Az 1/2018. (VI. 29.) ITM rendelet bevezette annak lehetőségét, hogy az elektronikus számlák
archiválását az adatszolgáltatásba épített és az elektronikus számla adattartalmát védő hash-kóddal is
lehet teljesíteni, más, e jogszabályban felsorolt módszerek mellett. Erre az Online Számla rendszer az
alábbi megoldást nyújtja:

A számlázási folyamatban az eladó oldalán létrejön egy elektronikus számla dokumentum (például: egy
elektronikus aláírással és időpecséttel nem ellátott PDF fájl), melyre a jelen specifikációban megjelölt
lenyomatképző algoritmusok egyikével az eladó rendszere hash-kódot képez. Ezt a hexadecimális
számot a számláról adott adatszolgáltatás részeként közli a NAV-val (electronicInvoiceHash elem az

invoiceApi.xsd-ben).

Eladó oldalon a kibocsátott, vevő oldalon az eladótól kapott elektronikus számlát megfelelő
adathordozón őrizni kell. Ha egy adóhatósági ellenőrzés közben az elektronikus számla (ami egy fájl,
ebben a példában egy PDF fájl) hitelességét és sértetlenségét igazolni szükséges, akkor erre megfelelő
módszer az őrzött állományon az eladó által az adatszolgáltatásban megjelölt algoritmussal képzett
hash-érték, valamint az eladó/vevő által őrzött állomány adott algoritmussal képzett hash-értékének
egyezősége. Ha tehát az ellenőrzés közben az adott algoritmussal megképzett hash-érték azonos azzal,
amit az eladó a számla kiállításakor megadott, akkor bizonyítottnak tekinthető az elektronikus számla


Áfa tv-ben megkövetelt hitelessége (ténylegesen az eladó adta ki) és sértetlensége (keletkezése óta az

adattartalmán nem módosítottak).

Elektronikus számlaadat-szolgáltatás esetén nem kötelező a hash-érték megképzése és szerepeltetése
az adatszolgáltatásban. Ez egy lehetőség az elektronikus számlához kapcsolódó digitális archiválási
kötelezettség hatékony teljesítésére.

#### 2.6.2 Adatszolgáltatás elektronikus számla beküldésével

Az Online Számla adatszolgáltatás 2018-as bevezetése óta lényegében minden magyarországi áfaalany
számlázó programja képes a számla adattartalmát vagy annak egy részét az adatszolgáltatásban

megkövetelt séma szerinti struktúrába foglalni. A számlaadatok leírásának ezen egységessége kiváló
lehetőséget nyújt az adózók ügyviteli folyamatainak számítógépes támogatására, így hatékonyabbá
tételére.

Az XSD 3.0 verziója lehetőséget biztosít arra, hogy az adatszolgáltatást az eladó a teljes adattartalmú
elektronikus számla beküldésével valósítsa meg, ha ez az elektronikus számla éppen az ezen
dokumentáció szerinti invoiceData.xsd -séma szerinti XML állomány.

A teljes adattartalmú, minden számlázó program által használt séma szerinti elektronikus számla
használata jelentős hatékonyság növekedést tesz lehetővé az adózók ügyviteli folyamataiban, ami
egyrészt az elektronikus számla alkalmazásából, másrészt a NAV által nyújtott szolgáltatások (például
/queryInvoiceData operáció használata vevő oldalon) használatából, harmadrészt az egységes

formátum által lehetővé tett gépi feldolgozási lehetőségek megnyílásából adódik. Jelen specifikációnak
nem feladata a lehetőségek ennél részletesebb ismertetése.

Ha az eladó (saját elhatározásából) adatszolgáltatásként magát az elektronikus számlát küldi be, ezt a
tényt az invoiceApi.xsd <completenessIndicator> elem ’true’ értékkel történő szerepeltetésével
szükséges jelezni. Amennyiben az eladó ezt a számlázási módot választja, akkor érdemes kiemelt
figyelmet fordítania a belföldi adóalany vevő adószámának helyes feltüntetésére. Amennyiben a vevő
adószáma nem megfelelő, akkor a vevő nem fogja tudni letölteni a rendszerből az elektronikus számlát.

Az adatszolgáltatás elektronikus számlával történő teljesítése esetén az alábbi korlátozásokat
figyelembe kell venni:

a) A vevő (termékbeszerző, szolgáltatást igénybevevő) nem lehet természetes személy
(<customerVatStatus> nem lehet PRIVATE_PERSON) és nem lehet nem belföldi adóalany vagy
adószámmal nem rendelkező nem természetes személy nem adóalany (<customerVatStatus> nem
lehet OTHER, vagy ha igen, akkor customerTaxNumber kitöltött),

b) Nem tartalmazhat a számla, számlával egy tekintet alá eső okirat összevont tételsorokat (tehát
a <mergedItemIndicator> nem lehet ’true’). Ez azon esetekben fordulhat elő, ha az XML állomány
mérete a kiállítást követően a10 Mb-nál nagyobb. Lásd: 2.7 fejezet).

c) Nem küldhető be <completenessIndicator>=’true’ értékkel olyan számlával egy tekintet alá eső
okirat (módosító vagy érvénytelenítő számla), ami olyan számla adattartalmát módosítja vagy
érvényteleníti, amiről az adatszolgáltatás nem az elektronikus számla beküldésével,

<completenessIndicator>=’true’ jelöléssel történt.

d) Az elektronikus számla adatszolgáltatásként történő beküldését
(<completenessIndicator>=’true’), használatát legkorábban 2021. január 4 - én szabad alkalmazni.


e) Bár az elektronikus számla, mint az adatszolgáltatás eszköze ugyan megtalálható az adóhivatal

rendszerében, azonban ebben az esetben sem vállalja az adóhivatal az archiválási rendelet szerinti
megőrzést. Az elektronikus számlák megőrzéséről minden esetben az adózónak kell gondoskodnia.

f) Az Áfa törvény alapján az elektronikus számlázáshoz a vevőnek hozzá kell járulnia. Ebben a két
partnernek kell megállapodnia, az adóhivatal nem vállalja át a megállapodás létrejöttéhez kapcsolódó
ügyvitelt még részben sem. A vevő elektronikus számlázáshoz történő hozzájárulása – az általános
szabályok szerint – megtörténhet írásban, szóban, ráutaló magatartással is, azonban ez az Online
Számla rendszeren kívüli hozzájárulást jelent.

g) Az adatszolgáltatás elektronikus számla beküldésével történő teljesítése esetén a
számlakibocsátási kötelezettség teljesítése az értékesítő felelőssége. Az adóhivatal nem vállalja át az
Áfa törvényben foglalt értékesítői és vevői kötelezettségeket, felelősségeket. Az Online Számla

rendszerben az elektronikus számlának számító adatszolgáltatás egy lehetőséget jelent az
adminisztráció csökkentésére, azonban a két félnek kell mérlegelnie az ebben rejlő lehetőségeket,
kockázatokat.

Ha az eladó adatszolgáltatási kötelezettségét az elektronikus számla beküldésével valósítja meg,
kötelező használnia a 2.6.1 fejezetben leírt lehetőséget. Tehát kötelező hash-értéket képeznie az
adatszolgáltatásként szolgáló elektronikus számlára, a hash képzése kizárólag az SHA3- 512
algoritmussal történhet és ezt a hash-értéket az invoiceApi.xsd <electronicInvoiceHash> elemben
szerepeltetnie kell. A hash-érték megfelelő képzése az elektronikus számla, mint adatszolgáltatás
feldolgozási folyamatában ellenőrzésre kerül, nem megfelelő hash-képzés esetén az adatszolgáltatás

meghiúsul. (Lásd: 3.3.2 fejezet)

### 2.7 NAGYMÉRETŰ SZÁMLÁKRÓL TÖRTÉNŐ ADATSZOLGÁLTATÁS

Az Online Számla rendszer nem képes fogadni 10 Mb-nál nagyobb adatszolgáltatásokat. Az ekkora
méretű adatszolgáltatások esetén ugyanazon termék/szolgáltatás több tételsoron jelenik meg. Ennek

a problémának a kiküszöbölése érdekében az adatszolgáltatásnál összevonást kell elvégezni, melynek
alkalmazásával a számla tényleges adattartalmához képest összevontabb adatszolgáltatás fog előállni.
Az összevonást az adatszolgáltatásban úgy kell jelölni, hogy a <mergedItemIndicator> elemet ’true’-ra
állítjuk.

Az összevonást az adózó rendszerének a következő elvek betartásával kell elvégeznie:

```
a) Az összevonáskor az azonos termékeket, szolgáltatásokat egy tételsorban kell megjeleníteni a
mennyiségi egység összeadásával (ha természetes mértékegységben kifejezhető).
b) Ha az azonos termékeknél, szolgáltatásoknál az egységár eltérő, akkor egységáranként külön
tételsorban kell szerepeltetni az adatszolgáltatásban az értékesítést.
c) Ha az azonos terméknek, szolgáltatásnak eltérő a mennyiségi egysége, akkor mennyiségi
egységenként külön tételsorban kell szerepeltetni az adatszolgáltatásban az értékesítést.
d) A termékenkénti, szolgáltatásonkénti összevonást nem feltétlenül megnevezés egyezőség
alapján kell elvégeznie az adózó programjának, hanem az adózó rendszere által nyilvántartott
azonosító kódonként (például cikkszám, VTSZ, TESZOR stb.) is elvégezheti.
e) Az összevont adatszolgáltatás összesítő adatai nem térhetnek el a számla összesítő adataitól.
```
### 2.8 KÖZMŰ ELSZÁMOLÓ SZÁMLÁJÁNAK ADATSZOLGÁLTATÁSA


A közüzemi szolgáltatóknak a rájuk vonatkozó iparági szabályozás alapján a közüzemi szolgáltatásukról

olyan elszámolószámlát kell kibocsátaniuk, mely adott időszaki teljesítést és korábbi időszaki számlák
(részszámlák) módosításait is tartalmazhatja. Az ide tartozó szolgáltatások teljesítési időpontjának
megállapítására az Áfa tv. 58. §-a alkalmazandó. Ezt figyelembe véve, abban az esetben, ha az
elszámolószámlán

- elszámolt időszakban nyújtott szolgáltatás értéke meghaladja az ezen időszak részszámlái
    összesített értékét, vagyis az elszámolás eredménye pozitív (a szolgáltatás igénybevevőjének
    további ellenérték fizetési kötelezettsége van), akkor az elszámoló számla normál számlának
    minősül, melynek új, Áfa tv. 58. § szerint meghatározott teljesítési időpontja lesz. Ebben az
    esetben tehát nem a korábban kiállított részszámlák módosítása, hanem egy új teljesítési
    időponttal új számlakiállítás valósul meg és arról és CREATE operációval szükséges az
    adatszolgáltatást elvégezni.
- elszámolt időszakban nyújtott szolgáltatás értéke kevesebb az ezen időszak részszámlái
    összesített értékénél, vagyis az elszámolás eredménye negatív (a szolgáltatás igénybevevője
    vevője részére visszatérítendő, illetve a későbbi fizetési kötelezettségével szemben
    elszámolandó összeg van), akkor a korábban kiállított számlákat (részszámlákat) szükséges
    módosítani. Erről az adatszolgáltatásoknak MODIFY operációval szükséges beérkezniük.

A közüzemi elszámolószámla esetében az utóbbinak speciális az adatszolgáltatása, mivel az
elszámolószámlának nem csupán a korábbi időszaki módosításokat kell tartalmaznia, hanem – az

iparág szabályozás szerinti – adott időszaki teljesítést is.Az adatszolgáltatáskor ezeket a számlákat
MODIFY operációval, batchInvoice számlaként kell beküldeni a következő módon:

- adott időszaki teljesítésről (például alapdíj) az adatszolgáltatást a következők szerint kell
    teljesíteni:
       o az <originalInvoiceNumber> az aktuális számla sorszáma,
       o a <modifyWithoutMaster> értéke true,
       o a <utilitySettlementIndicator> értéke true
       o a <modificationIndex> értéke’1’.
- korábbi időszaki számlák módosításait pedig értelemszerűen kell megadni:
    o az <originalInvoiceNumber> a részszámla sorszáma,
    o a <modifyWithoutMaster> értéke attól függően, hogy a részszámláról történt-e
       adatszolgáltatás,
    o a <utilitySettlementIndicator> értéke false vagy nem megadott
    o a <modificationIndex> értéke az adott részszámla soron következő módosításának
       indexe.

A technikai megoldást az alábbi példa szemlélteti:

Elszámoló számla adatai:

- Utolsó havi alapdíj: 100
- 11. havi részszámla 200
- 10. havi részszámla 200
- Elszámolt összeg leolvasást követően -500 (mely az utolsó időszaki alapdíjnak, és a 10. és 11.
    havi részszámlának a korrekcióját jelenti).

Ennek az adatszolgáltatása a következően néz ki:


- Utolsó havi alapdíj ( 100 ) adatszolgáltatása: számlasorszám hivatkozás (originalInvoiceNumber)
    az elszámoló számla sorszáma, közmű elszámoló számla jelölése true
    (utilitySettlementIndicator=true).
- Utolsó havi alapdíj csökkentésének adatszolgáltatása az elszámolás miatt (-100):
    számlasorszám hivatkozás (originalInvoiceNumber) az elszámoló számla sorszáma, közmű
    elszámoló számla jelölése true (utilitySettlementIndicator=true)
- 11. havi részszámla módosítása (-200): számlasorszám hivatkozás (originalInvoiceNumber) a
    11. havi részszámla sorszáma, közmű elszámoló számla jelölése false
    (utilitySettlementIndicator=false)
- 10. havi részszámla módosítása (-200): számlasorszám hivatkozás (originalInvoiceNumber) a
    10. havi részszámla sorszáma, közmű elszámoló számla jelölése false
    (utilitySettlementIndicator=false)

Amennyiben az elszámoló számla adatai valami miatt nem helytállóak és módosításra van szükség,
akkor a fenti elveket kell figyelembe venni. Amennyiben az elszámoló számla CREATE-el állt elő, akkor
az elszámoló számlát szükséges módosítani. Amennyiben az elszámoló számla MODIFY-al állt elő, akkor
vissza kell lépni a részszámlákra és azokat szükséges módosítani, amennyiben negatív irányú a
módosítás (pozitív módosítás esetén új számlát szükséges kiállítani és nem a korábbi számlát
módosítani).

### 2.9 ELŐLEGSZÁMLA, VÉGSZÁMLA ADATSZOLGÁLTATÁSA

Az előleget tartalmazó tételsor esetén az <advanceIndicator> értékét „true”-ra kell állítani és az
<advancePaymentData> csomópontot nem szabad kitölteni. Ezzel lehet jelölni, hogy a számlán az
adott tételsort előlegként kell figyelembe venni.

A végszámláról az adatszolgáltatást úgy kell összeállítani, hogy tartalmazza a gazdasági esemény teljes
összegét, ebből az összegből levonásra kerülő előleg számlát/számlákat, és összegzésben pedig a kettő
különbözetét. Ha nagyobb összegben került sor az előleg befizetésére a vevő részéről, mint a gazdasági
esemény teljes összege, akkor ezt a különbözetet az előleg számlában kell rendeznie a számla
kiállítójának, nem pedig a végszámlában (vagyis abban az esetben, ha az ügylet adóval növelt
ellenértéke meghaladja a kapott előleget, akkor a különbözettel az előlegszámla módosítandó). Ha a
végszámla végösszege negatív végösszeget tartalmaz, akkor warning-al jelöli a rendszer a nem
megfelelő értéket. Fontos kiemelni, hogy ekkor a számla adattartalma nem megfelelő, tehát a számlát
és nem az adatszolgáltatást szükséges javítani.

A végszámla adatszolgáltatásánál az <advanceIndicator> értékét „true”-ra kell állítani és ha a számla
tartalmazza (vagy a számlázó program ki tudja tölteni), akkor az <advancePaymentData> csomópontot
is ki lehet tölteni. Az előleg fizetéshez kapcsolódó adatok kitöltésénél figyelembe kell venni azt is, hogy
a csomópont alatt szereplő mindhárom mezőt (advanceOriginalInvoice, advancePaymentData,
advanceExchangeRate) kötelező kitölteni.

Ha a végszámla külföldi pénznemben kerül kiállításra, akkor a számla árfolyamát az adatszolgáltatás
invoiceHead csomópontja alatt lévő <exchangeRate> mezőben szükséges megadni. A végszámlának
kizárólag egy árfolyama van. Tehát a korábban megfizetett előleg beszámításakor is ezzel az
árfolyammal szükséges számolni. A séma ugyanakkor az advancePaymentData csomópontban
lehetőséget ad arra, hogy az előleg fizetésekori árfolyam is megadható legyen. Fontos felhívni


ugyanakkor arra a figyelmet, hogy az Áfa törvény szempontjából a végszámlánál ennek az árfolyamnak

nincs jelentőssége, ugyanakkor számviteli elszámolásnál lehetséges. Tehát az advanceExchangeRate
megadása nem az Áfa törvény szempontjából, hanem számviteli elszámolások miatt lehet fontos.


## 3 HIBAKEZELÉS

A szolgáltatás egy közös, a szolgáltatás oldalán enumerált értékkészletből vett eredmény és hibakód
listával működik. Az eredménykódoktól eltérően a hibakódok szándékosan nem jelennek meg a
sémaleíró enumerációiban, hogy azok esetleges változása vagy bővülése ne keletkeztessen
implementációs függőséget a kliensek oldalán. Az eredménykódok a BasicResultType node funcCode
tagjában, míg a hibakódok az errorCode tagban kerülhetnek visszaadásra a válaszüzenetben. A

visszakapott funcCode értékeket a hívott üzleti folyamatnak megfelelően kell értelmezni.

### 3.1 Általános hibakódok

#### 3.1.1 GeneralExceptionResponseType

A szolgáltatás minden operációjában a technikailag feldolgozhatatlan üzenetre (rosszul formázott XML,
helytelen namespace, vagy helytelen context root) a GeneralTechnicalException hibatípus kerül
visszaadásra.

## 82. ábra A GeneralExceptionResponseType felépítése

A típus a BasicResultType-ot terjeszti ki, azonban azon kívül más elemet nem tartalmaz.

#### 3.1.2 GeneralErrorResponseType

A szolgáltatás minden operációjának általános hibatípus üzenetét a GeneralErrorResponseType
implementálja.


## 83 ábra A GeneralErrorResponseType felépítése

A típus a BasicOnlineInvoiceResponseType-ot terjeszti ki, így az abban foglalt elemeken kívül egy
technikai validációs listatípust tartalmaz. A listatípus az invoiceApi sémaleíróhoz (tehát az interfész
szinkron feldolgozási részéhez) tartozó minden sémasértést tételesen tartalmaz, ha a kérésben volt

legalább 1 nem séma valid tag.

```
Tag Típus Kötelező Tartalma
validationResultCode xs:string Igen A technikai validáció eredménye
validationErrorCode xs:string Nem A technikai validáció hibakódja
message xs:string Nem A technikai validáció eredményéhez
tartozó szöveges üzenet
```
**Facetek és leírók**

```
Tag SimpleType Pattern Enum Default
validationResultCode TechnicalResultCodeType - CRITICAL
ERROR
```
##### -

```
validationErrorCode SimpleText 10 0NotBlankType .*[^\s].* - -
message SimpleText1024NotBlankType .*[^\s].* - -
```
**Leírás és kapcsolódó követelmények**


```
1) Ha a technicalValidationMessages tag képződik, akkor a validationResultCode jelenleg csak
ERROR értéket vehet fel (a CRITICAL ebben a típusban fenntartott érték az esetleges jövőbeni
validációk számára)
2) A validationErrorCode tag a hibatípus kódját tartalmazza.
3) A message tag a technikai validáción fennakadt hibás tag nevét, értékét, illetve az elvárt
értéket tartalmazza séma sértés esetén, egyéb esetben pedig a validationErrorCode taghoz
tartozó szöveges hibaüzenetet
```
A következő fejezetben leírt technikai hibakódokat a rendszer minden esetben vagy a
GeneralTechnicalException, vagy a GeneralErrorResponse válaszelemben adja vissza, a „ **Hibakezelés”**
fejezetben leírt response elemek csak és kizárólag akkor képződnek, ha a szinkron feldolgozás üzletileg
és technikailag is sikeres volt! Így a HTTP response body-ban visszakapott valamely error tag mindig
valamilyen hibát fog jelezni.


### 3.2 TECHNIKAI HIBAKÓDOK

A szinkronhívások errorCode értékkészletét a következő táblázat tartalmazza.

**Technikai és authentikációs hibák**

```
# HTTP válasz Response body funcCode errorCode requestVersion
1 HTTP 404 NOT_FOUND - - - 1.0
2 HTTP 500 INTERNAL_SERVER_ERROR Undertow üzenet, Generic exception occured! - - 1.0
3 HTTP 400 BAD_REQUEST GeneralExceptionResponse XML tag ERROR INVALID_REQUEST 1.0
```
**4** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR INVALID_REQUEST 1.0
**5** HTTP 401 UNAUTHORIZED GeneralErrorResponse XML tag (^) ERROR INVALID_SECURITY_USER 1.0
**6** HTTP 500 INTERNAL_SERVER_ERROR GeneralErrorResponse XML tag (^) ERROR NOT_REGISTERED_CUSTOMER 1.0
**7** HTTP 500 INTERNAL_SERVER_ERROR GeneralErrorResponse XML tag (^) ERROR INVALID_CUSTOMER 1.0
**8** HTTP 500 INTERNAL_SERVER_ERROR GeneralErrorResponse XML tag ERROR INVALID_USER_RELATION 1.0
**9** HTTP 500 INTERNAL_SERVER_ERROR GeneralErrorResponse XML tag ERROR FORBIDDEN 1.0
**10** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag ERROR REQUEST_ID_NOT_UNIQUE 1.0
**11** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR INVALID_REQUEST_SIGNATURE 1.0
**12** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR INDEX_NOT_SEQUENTIAL 1.0
**13** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR INVALID_EXCHANGE_TOKEN 1.0
**14** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR REQUEST_VERSION_NOT_ALLOWED 1.0
**15** HTTP 5 27 SERVICE_UNAVAILABLE GeneralErrorResponse XML tag ERROR MAINTENANCE_MODE 1.0
**16** HTTP 500 INTERNAL_SERVER_ERROR GeneralErrorResponse XML tag (^) ERROR STATUS_QUERY_NOT_ALLOWED 1.1
**17** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR MULTIPLE_QUERY_RESULT_FOUND 2.0
**18** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR BAD_QUERY_PARAM_OVERLAP 2.0
**19** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR BAD_QUERY_PARAM_RANGE_EXCEEDED 2.0
**20** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag ERROR BAD_QUERY_PARAM_EQ_NOT_STANDALONE 2.0
**21** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR BAD_QUERY_PARAM_OPERATOR_COLLISION 2.0
**22** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR BAD_QUERY_PARAM_SUPPLIER_NOT_EXPECTED 2.0
**23** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR BAD_QUERY_PARAM_SUPPLIER_EXPECTED 2.0


**24** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR INVALID_TIMESTAMP 2.0
**25** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR INVALID_PASSWORD_HASH_CRYPTO 3.0
**26** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR INVALID_REQUEST_SIGNATURE_HASH_CRYPTO 3.0
**27** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag ERROR INVALID_REQUEST_VERSION 3.0
**28** HTTP 400 BAD_REQUEST GeneralErrorResponse XML tag (^) ERROR INVALID_HEADER_VERSION 3.0
**29** HTTP 500 INTERNAL_SERVER_ERROR GeneralErrorResponse XML tag ERROR INVALID_PREDECESSOR_TAX_NUMBER 3.0
_* a kékkel jelölt hibakódot a rendszer publikus végpontja mögött lévő hálózati eszköz HTTP 503 SERVICE_UNAVAILABLE üzenetre átforgatja._
**Hibaeset, teendők
# Hiba oka Teendő
1** hibás a szolgáltatás endpoint a kérésben Az egyes környezetekben megcímzendő endpointokról a „ **Környezetek elérhetőségei”** című fejezet tartalmaz
információkat, ellenőrizni kell az URL-t.
**2** hibás a HTTP metódus a kérésben Az URL helyes, de a HTTP metódus nem POST. Az interfész minden operációját POST metódussal kell küldeni!
**3** rosszul formázott az XML a request body-ban A szintaktikailag helytelen XML -üzenetet az XML szabvány szerint tilos XML-nek tekinteni és feldolgozni, javítani kell.
**4** nem séma-valid XML a request body-ban A beküldött XML - válaszban felsorolt - elemei sértik az invoiceApi.xsd megkötéseit, javítani kell.
**5** a kérésben hibás login + passwordHash pár Számos esetben jelentkezhet a hibaüzenet. Lehetséges okok: a megadott login névvel nem létezik felhasználó, vagy nem
helyes a jelszava, vagy a login + passwordHash pár szemantikailag helyes, de a jelszóhash rosszul kerül kiszámításra a kliens
oldalán. Meg kell győződni az adatok és a hashelés helyességéről, szükség esetén fel kell venni a kapcsolatot a technikai
felhasználót birtokló adózóval.
**6** a kérésben megadott adózó nincs regisztrálva A user tagban megadott adószám nem regisztrált adózóhoz tartozik.
**7** a kérésben hibás a taxNumber A user tagban megadott adószám vagy nem létezik, vagy a státusza nem engedi a számlaműveletek végzését. Meg kell
győződni az adatok helyességéről, szükség esetén fel kell venni a kapcsolatot az érintett adózóval.
**8** a kérésben szereplő entitások között nincs
kapcsolat
A megadott adószámhoz nem tartozik a megadott login névvel technikai felhasználó, vagy a felhasználó státusza már nem
engedélyezi a művelet elvégzését. Meg kell győződni az adatok helyességéről, szükség esetén fel kell venni a kapcsolatot
az érintett adózóval.
**9** a kérésben szereplő technikai felhasználó
nem jogosult az endpoint szolgáltatását hívni
A technikai felhasználók jogosultságait az adózó elsődleges felhasználói osztják ki. Szükség esetén fel kell venni a
kapcsolatot az érintett adózóval.
**10** a kérésben szereplő requestId nem egyedi A kérésben szereplő adószámra a megadott requestId-t már felhasználták. Az egyediség miatt új id megadása szükséges.
**11** a kérésben szereplő requestSignature hibás A szerver oldalon elvégzett requestSignature számítás nem egyezik meg a kliens oldalon kiszámított értékkel. A számítás
módjáról ld. a „ **requestSignature számítása”** című fejezetet.


**12** a kérésben szereplő index nem sorfolytonos Az invoiceOperations listaelem alatt lévő indexeknek sorfolytonosan emelkedőnek kell lenniük. Ellenőrizni kell, hogy a
kérésben nincs helytelen sorrendű, hézagos, vagy 1-nél többször előforduló index.
**13** a kérésben szereplő adatszolgáltatási token
érvénytelen

Számos esetben jelentkezhet a hibaüzenet. Lehetséges okok: a megadott token nem található a rendszerben, a token már
lejárt, a token nem a megadott adózóra lett kiállítva, vagy a kliensoldali AES dekódolás hiányzik, esetleg hibás. Meg kell
győződni az adatok és a dekódolás helyességéről.
**14** a kérésben szereplő requestVersion tag
értéke már nem megengedett

A kérés requestVersion értéke már nem támogatott verzió. Ez akkor fordulhat elő, amikor valamilyen szabály változása
miatt át kell állni az interfész egy újabb verziójára úgy, hogy adott időponttól kezdve a korábbi verzió már nem
használható. Javítani kell!
**15** karbantartás van folyamatban A hívott operáció karbantartás miatt átmenetileg nem szolgál ki. Kísérje figyelemmel a felületen elhelyezett tájékoztatót és
ismételje meg a kérést egy későbbi időpontban!
**16** túl alacsony a státusz lekérdezés verziószáma A feldolgozási státusz lekérdezésének requestVersion értéke nem lehet a lekérdezett tranzakció beküldéskori
requestVersion értékétől kisebb. Javítani kell!
**17** a keresett számlaszám többször szerepel
érvényesként a rendszerben

A hibaüzenet a /queryInvoiceData és /queryInvoiceCheck operációkban adható vissza akkor, ha a lekérdezett számlaszám
többször érvényesként szerepel a rendszerben. Ebben az esetben a számlaszámot technikailag érvényteleníteni kell, majd
a jóváhagyást követően az adatszolgáltatást meg kell ismételni a helyes adatokkal.
**18** dátumátfedés a lekérdező paraméterekben A hibaüzenet a /queryInvoiceDigest és /queryTransactionList operációkban adható vissza akkor, ha a kötelező
keresőparaméterek (invoiceIssueDate vagy insDate) dátumai átfedik egymást. A paraméterek között legfeljebb egyenlőség
engedélyezett. Javítani kell!
**19** túl nagy lekérdezési intervallum A hibaüzenet a /queryInvoiceDigest és /queryTransactionList operációkban adható vissza akkor, ha a kötelező
keresőparaméterek (invoiceIssueDate vagy insDate) dátumai közötti távolság nagyobb, mint 35 nap. Szűkíteni kell a
keresett intervallumot.
**20** egyenlőségre történő keresés nem
önmagában áll

A hibaüzenet a /queryInvoiceDigest operációban adható vissza akkor, ha a relációs keresőparaméterek között valamelyik
csomópont kétszer van megképezve, és a kettő közül az egyikben az EQ keresőfeltétel szerepel. Az EQ kereső operator
adott csomóponton csak önmagában állhat, javítani kell!
**21** hibás intervallum meghatározás a
lekérdezésben

A hibaüzenet a /queryInvoiceDigest operációban adható vissza akkor, ha a relációs keresőparaméterek között valamelyik
csomópont kétszer van megképezve, és a keresőfeltételek nyitott intervallumot határoznak meg (pl: GT és GT, vagy LT és
LTE kereső operátorok állnak párban) Az intervallumos keresésnél a keresőoperátorok közül az egyiknek GT vagy GTE, míg
a másiknak LT vagy LTE értéket kell adni.
**22** kiállítóként kereséskor nem szabad a kiállító
adószámára szűrni

```
A hibaüzenet mindkét számla lekérdező operációban (queryInvoiceCheck és queryInvoiceData) visszaadható akkor, ha a
keresést számlaszám megadásával végezzük, a keresés kiállítóként történik és a kiállítói adószámra szűrés ki van töltve. A
kérésből törölni kell a supplierTaxNumber taget!
```

```
23 vevői kereséskor többértelmű
eredményhalmaz, szűrni kell a kiállító
adószámára
```
```
A hibaüzenet mindkét számla lekérdező operációban (queryInvoiceCheck és queryInvoiceData) visszaadható akkor, ha a
keresést számlaszám megadásával végezzük, a keresés vevőként történik és a keresett számlaszámot több kiállító is
kiállította ugyan azon vevőnek. A kérésben meg kell adni a supplierTaxNumber taget. A szűrésre használható adószámok
listáját a /queryInvoiceDigest operációból lehet megállapítani.
24 kérésben megadott időbélyeg 1 napon kívül
esik
```
```
A hibaüzenet az összes autentikációt tartalmazó operációban adható vissza akkor, ha a header csomópontban megadott
timestamp értéke a szerveridő +- 1 napos intervallumán kívül esik.
25 technikai felhasználó jelszavának hash-képző
algoritmusa helytelen
```
```
A hibaüzenet akkor adható vissza, ha a user/passwordHash/cryptoType értéke nem SHA- 512.
```
```
26 kérés aláírásának hash-képző algoritmusa
helytelen
```
```
A hibaüzenet akkor adható vissza, ha a user/requestSignature/cryptoType értéke nem SHA3- 512.
```
```
27 kérés verziója érvénytelen A hibaüzenet akkor adható vissza, ha a header/requestVersion értéke nem 3.0
28 header verziója érvénytelen A hibaüzenet akkor adható vissza, ha a /header/headerVersion értéke meg van adva és nem 1.0
29 a kérésben megadott jogelőd adószám
érvénytelen
```
```
A hibaüzenet akkor adható vissza, ha a user/predecessorTaxNumber és a user/taxNumber mezőkben megadott adózók
között nem áll fenn jogelőd-jogutód viszony.
```
A javításokhoz az „ **Önellenőrzés”** című fejezetet ad további támpontokat.

**Feldolgozási hibák**

```
# HTTP válasz Response body funcCode errorCode requestVersion
```
**1** HTTP 500 INTERNAL_SERVER_ERROR GeneralErrorResponse (^) ERROR OPERATION_FAILED 1.0
**2** HTTP 500 INTERNAL_SERVER_ERROR GeneralErrorResponse (^) ERROR NOT_ALLOWED_EXCEPTION 3.0
**Hibaeset, teendők
# Hiba oka**^ **Teendő**^
**1** váratlan feldolgozási hiba Az aszinkron műveletek hibatűrése szerver oldalon biztosított. A szóban forgó hiba csak szinkronhívásoknál jelentkezhet,
ilyenkor a műveletet kis idő elteltével meg kell ismételni. Ha az éles rendszerben többszöri próbálkozásra sem sikerül a
művelet, fel kell venni a kapcsolatot a NAV helpdeskkel, azonban célszerű előtte tájékozódni, hogy a portál oldalon nincs-e
üzemszünettel, üzemzavarral kapcsolatos tájékoztatás. Felhívjuk a figyelmet, hogy a felhasználói teszt rendszerben nincs
garantált rendelkezésre állás, ezért kérjük, hogy a tesztrendszer hibáit ne jelentsék be!


```
(A hibakód továbbá akkor is jelentkezhet, ha egy request nem a megfelelő operáció végpontjára van beküldve, például egy
sémavalid számla beküldése a /manageInvoice helyett a /queryTaxpayer végpontra történik.)
2 nem létező művelet A hibaüzenet akkor fordulhat elő, ha egy végpont hívása nem a megfelelő HTTP metódussal történik. (Pl. a POST metódust
váró manageInvoice-ra érkezik egy GET hívás)
```
### 3.3 VALIDÁCIÓS HIBAKÓDOK

A validációs hibakódok csak a /queryTransactionStatus operáció válaszüzenetében érkezhetnek. Ezen hibakódok közös jellemzője, hogy a processingResult
elemen belül jelennek meg, a /queryTransactionStatus operáció válasza sikeres lekérdezés esetén mindig funcCode = OK értékkel fog visszatérni. Ez nem
összetévesztendő a számlaadatokra vonatkozó feldolgozási eredményekkel! Értékük lehet ERROR, mely blokkoló üzleti vagy technikai hibát jelez, illetve WARN,
amely figyelmeztet a számlaadatok valamely üzleti helytelenségére, vagy INFO, ami csak tájékoztatási célokat szolgál. Mindhárom esetben a visszaadott
hibakód az adott indexen lévő számlaadat-szolgáltatásra vonatkozik, sosem az adatszolgáltatás egészére!

#### 3.3.1 Technikai validációs hibakódok

Figyelemmel arra, hogy a számlaadat-szolgáltatás adatainak BASE64 dekódolása aszinkron módon történik, nem lehet kizárni azok esetleges érvénytelenségét
vagy egyéb hibáját. Ha a kérésben szereplő adott adatszolgáltatás nem séma-valid vagy egyéb módon hibás, annak a ténye ezen az ágon kerül visszaadásra.

```
# HTTP válasz Response body validationResultCode validationErrorCode requestVersion
1 HTTP 200 OK technicalValidationMessages XML tag ERROR SCHEMA_VIOLATION 1.0
2 HTTP 200 OK technicalValidationMessages XML tag ERROR DUPLICATE_IN_REQUEST 1.0
3 HTTP 200 OK technicalValidationMessages XML tag ERROR COMPRESSION_TOLERANCE_EXCEEDED 1.0
4 HTTP 200 OK technicalValidationMessages XML tag ERROR DECOMPRESSION_ERROR 1.0
5 HTTP 200 OK technicalValidationMessages XML tag ERROR CREATE_WITH_BATCH_INVOICE_FOUND 2.0
6 HTTP 200 OK technicalValidationMessages XML tag ERROR MULTIPLE_INDICES_WITH_BATCH_INVOICE_FOUND 2.0
7 HTTP 200 OK technicalValidationMessages XML tag ERROR DUPLICATE_IN_INVOICE_REFERENCE 2.0
8 HTTP 200 OK technicalValidationMessages XML tag ERROR BATCH_INDEX_NOT_SEQUENTIAL 2.0
9 HTTP 200 OK technicalValidationMessages XML tag ERROR BATCH_INVOICE_CARDINALITY_ERROR 2.0
10 HTTP 200 OK technicalValidationMessages XML tag ERROR DUPLICATE_INVOICE_LINE_CREATION 2.0
```
**Hibaeset, teendők**

```
# Hiba oka Teendő
```

```
1 nem séma-valid XML A dekódolt - válaszban felsorolt - elemei sértik az invoiceData.xsd megkötéseit, javítani kell.
2 az adatszolgáltatásban többször szerepel
ugyan az a számlaszám
```
```
Minden számlaműveletnél használt hibakód (CREATE, MODIFY, STORNO és ANNUL), akkor kerül visszaadásra, ha az
adatszolgáltatásban többször szerepel ugyan az a számlaszám. A szerver az adatszolgáltatásban egynél többször
feltüntetett számlák feldolgozását mérlegelés nélkül, egységesen elutasítja, javítani kell.
3 a tömörített számla eredeti mérete túl nagy Az adatszolgáltatásban szereplő tömörített számla eredeti mérete meghaladja az engedélyezett méretkorlátot.
4 hiba a kitömörítés közben A számla nem kitömöríthető. Vagy a tömörítési metódus hibás, vagy a compressedContent tag értéke és a számla
tömörítése nincs egymással szinkronban. (nem tömörített számla, miközben compressedContent = true) Ha a számla
tömörített, de eközben compressedContent = false, úgy séma validációs hiba kerül visszaadásra az aszinkron feldolgozás
eredményeként.
5 kötegelt módosítás CREATE operációval került
beküldésre
```
```
A rendszernek kötegelt módosítás (batchInvoice) csak MODIFY vagy STORNO invoiceOperation értékkel küldhető be
CREATE értékkel nem, javítani kell.
6 kötegelt módosítás (is) található a kérésben,
azonban a kérés egynél több indexet
tartalmaz
```
```
A rendszernek kötegelt módosítás (batchInvoice) csak 1 indexes /manageInvoice kérésben küldhető be, javítani kell.
```
```
7 az adatszolgáltatásban többször szerepel
ugyan az a számlaszám hivatkozás és a
módosítás sorrendjét leíró pár
```
```
Az adatszolgáltatáson belül az invoiceReference és a modificationIndex értékeknek együtt egyedinek kell lennie, javítani
kell.
```
```
8 kötegelt módosítás belső indexe nem
sorfolytonos
```
```
Kötegelt módosítás (batchInvoice) esetén a batchIndex értéknek 1-től kezdődően monoton növekvőnek kell lennie,
ahogyan az API XML indexnél is, javítani kell.
9 kötegelt módosításnak legalább 2 módosító
okiratot kell tartalmaznia
```
```
Kötegelt módosítás (batchInvoice) esetén legalább 2 batchIndex szükséges a belső tartalomban, javítani kell.
```
```
10 ugyanazzal a sorszámmal egy sor többször
van hozzáadva a számlához
```
```
Tételsort ugyanolyan sorszámmal nem lehet többször hozzáadni egy számlához, javítani kell.
```
#### 3.3.2 Blokkoló validációs hibakódok

A blokkoló validációs hibák olyan tartalmi hibát jeleznek, melyek az adatszolgáltatás sikerességét megakadályozzák. Ilyen hiba megjelenésekor a számlaadat-
szolgáltatást nem lehet sikeresnek tekinteni, a beküldött adatokat minden esetben javítani kell!

```
# operation Számla típus Response body validationResultCode validationErrorCode requestVersion
```

##### 1 CREATE,

##### MODIFY,

```
STORNO
```
```
minden típus businessValidationMessages
XML tag
```
```
ERROR SUPPLIER_TAX_NUMBER_MISMATCH 1.0
```
##### 2 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVOICE_NUMBER_NOT_UNIQUE 1.0

##### 3 CREATE,

##### MODIFY,

```
STORNO
```
```
minden típus businessValidationMessages
XML tag
```
```
ERROR LINE_NUMBER_NOT_SEQUENTIAL 1.0
```
##### 4 CREATE,

```
STORNO
```
```
minden típus businessValidationMessages
XML tag
```
```
ERROR INVOICE_LINE_MISSING 1.0
```
**5** MODIFY,
STORNO

```
minden típus businessValidationMessages
XML tag
```
```
ERROR INVALID_INVOICE_REFERENCE 1.0
```
**6** MODIFY,
STORNO

```
minden típus businessValidationMessages
XML tag
```
```
ERROR INVOICE_TYPE_MISMATCH 1.0
```
**7** MODIFY,
STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVOICE_LINE_ALREADY_EXISTS 1.0

**8** ANNUL minden típus businessValidationMessages
XML tag

##### ERROR INVALID_ANNULMENT_REFERENCE 1.0

**9** ANNUL minden típus businessValidationMessages
XML tag

##### ERROR ANNULMENT_IN_PROGRESS 1.0

##### 10 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR CUSTOMER_NOT_ASSIGNED 1.0

##### 11 MODIFY,

##### STORNO,

##### ANNUL

```
minden típus businessValidationMessages
XML tag
```
##### ERROR REQUEST_VERSION_REFERENCE_ERROR 1.1

##### 12 MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR LINE_NUMBER_REFERENCE_NOT_UNIQUE 1.1


##### 13 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR MANDATORY_LINE_CONTENT_MISSING 1.1

##### 14 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_VAT_DATA 1.1

##### 15 MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR MULTIPLE_INVOICES_FOUND 1.1

##### 16 MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR MODIFICATION_INDEX_NOT_UNIQUE 2.0

**17** CREATE minden típus businessValidationMessages
XML tag

##### ERROR CUSTOMER_INFO_MISSING 2.0

##### 18 MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVOICE_REFERENCE_EXPECTED 2.0

**19** CREATE minden típus businessValidationMessages
XML tag

##### ERROR INVOICE_REFERENCE_NOT_EXPECTED 2.0

##### 20 MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR MODIFY_WITHOUT_MASTER_MISMATCH 2.0

##### 21 MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR LINE_MODIFICATION_EXPECTED 2.0

**22** CREATE minden típus businessValidationMessages
XML tag

##### ERROR LINE_MODIFICATION_NOT_EXPECTED 2.0

##### 23 MODIFY,

##### STORNO

```
batchInvoice businessValidationMessages
XML tag
```
##### ERROR CUSTOMER_NOT_IDENTICAL 2.0

##### 24 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR CUSTOMER_DATA_NOT_EXPECTED 3.0

##### 25 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR CUSTOMER_DATA_EXPECTED 3.0


##### 26 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR ELECTRONIC_INVOICE_HASH_EXPECTED 3.0

##### 27 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_INVOICE_HASH_CRYPTO 3.0

##### 28 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_INVOICE_HASH 3.0

##### 29 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVOICE_APPEARANCE_MISMATCH 3.0

**30** ANNUL minden típus businessValidationMessages
XML tag

##### ERROR ELECTRONIC_INVOICE_ANNULMENT_NOT_ALLOWED 3.0

##### 31 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_LINE_VAT_EXEMPTION_CODE 3.0

##### 32 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_SUMMARY_VAT_EXEMPTION_CODE 3.0

##### 33 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_LINE_VAT_OUT_OF_SCOPE_CODE 3.0

##### 34 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_SUMMARY_VAT_OUT_OF_SCOPE_CODE 3.0

##### 35 MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INCOMPLETE_ELECTRONIC_INVOICE_REFERENCE 3.0

##### 36 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_LINE_VAT_AMOUNT_MISMATCH_CODE 3.0


##### 37 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_SUMMARY_VAT_AMOUNT_MISMATCH_CODE 3.0

##### 38 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVOICE_COMPLETENESS_MERGED_ITEM_INDICATOR_MISMATCH 3.0

##### 39 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVOICE_COMPLETENESS_PRIVATE_PERSON_INDICATOR_MISMATCH 3.0

##### 40 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVOICE_COMPLETENESS_NOT_ALLOWED 3.0

##### 41 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_LINE_VAT_RATE_NORMAL 3.0

##### 42 CREATE,

##### MODIFY,

##### STORNO

```
normál,
gyűjtő
```
```
businessValidationMessages
XML tag
```
##### ERROR INVALID_LINE_VAT_RATE_SIMPLIFIED 3.0

##### 43 CREATE,

##### MODIFY,

##### STORNO

```
egyszerűsített businessValidationMessages
XML tag
```
##### ERROR INVALID_SUMMARY_VAT_RATE_NORMAL 3.0

##### 44 CREATE,

##### MODIFY,

##### STORNO

```
normál,
gyűjtő
```
```
businessValidationMessages
XML tag
```
##### ERROR INVALID_SUMMARY_VAT_RATE_SIMPLIFIED 3.0

##### 45 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR MISSING_CUSTOMER_DOMESTIC_TAXNUMBER 3.0

##### 46 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR CUSTOMER_COMMUNITY_TAXNUMBER_NOT_EXPECTED 3.0


##### 47 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR CUSTOMER_THIRD_STATE_TAXNUMBER_NOT_EXPECTED 3.0

##### 48 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_LINE_VAT_AMOUNT_MISMATCH_VAT_RATE

##### 3.0

##### 49 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_SUMMARY_VAT_AMOUNT_MISMATCH_VAT_RATE 3.0

##### 50 CREATE,

##### MODIFY

```
minden típus businessValidationMessages
XML tag
```
##### ERROR DOMESTIC_TAXNUMBER_EXPECTED_REVERSE_CHARGE 3.0

##### 51 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_INVOICE_NUMBER 3.0

##### 52 MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR MODIFICATION_SOURCE_MISMATCH 3.0

##### 53 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_INVOICE_CATEGORY 3.0

##### 54 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVOICE_DELIVERY_DATE_LATE 3.0

##### 55 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVOICE_ISSUE_DATE_LATE 3.0

##### 56 CREATE,

##### MODIFY,

##### STORNO

```
normál,
gyűjtő
```
```
businessValidationMessages
XML tag
```
##### ERROR LINE_SUMMARY_TYPE_MISMATCH_LINE_SIMPLIFIED 3.0

##### 57 CREATE,

##### MODIFY,

##### STORNO

```
normál,
gyűjtő
```
```
businessValidationMessages
XML tag
```
##### ERROR LINE_SUMMARY_TYPE_MISMATCH_SUMMARY_SIMPLIFIED 3.0


##### 58 CREATE,

##### MODIFY,

##### STORNO

```
egyszerűsített businessValidationMessages
XML tag
```
##### ERROR LINE_SUMMARY_TYPE_MISMATCH_LINE_NORMAL 3.0

##### 59 CREATE,

##### MODIFY,

##### STORNO

```
egyszerűsített businessValidationMessages
XML tag
```
##### ERROR LINE_SUMMARY_TYPE_MISMATCH_SUMMARY_NORMAL 3.0

##### 60 MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_LINE_OPERATION 3.0

##### 61 CREATE,

##### MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR INVALID_PREDECESSOR_OPERATION 3.0

##### 62 MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR SUPPLIER_NOT_IDENTICAL 3.0

##### 63 MODIFY,

##### STORNO

```
minden típus businessValidationMessages
XML tag
```
##### ERROR PREDECESSOR_REFERENCE_NOT_IDENTICAL 3.0

**Hibaeset, teendők**

```
# Hiba oka Teendő
```

**1** az eladó adószáma eltér a kérésben szereplő
adószámtól

A számla eladójának adószáma eltér az API XML-ben szereplő authentikált adószámtól, javítani kell.
A validáció engedélyezi a kiállító adószámának eltérését, amennyiben a jogelőd nevében történő pótlás jelzésre került.
(A10000_JOGELOD_POTLAS)
**2** nem egyedi számlasorszám Az invoiceNumber mezőben szereplő számlasorszámon az adózó már teljesített adatszolgáltatást. A számlasorszámnak
adózónként egyedinek kell lennie! Ebbe nem számítanak bele a technikailag érvénytelenített számlák, de csak akkor, ha a
technikai érvénytelenítést az adózó már jóváhagyta!
**3** nem sorfolytonos számozás az invoiceLines
listaelemen belül

Az invoiceLines listaelem alatt lévő lineNumber elemeknek sorfolytonosan emelkedőnek kell lenniük. Ellenőrizni kell, hogy
a kérésben nincs helytelen sorrendű, hézagos, vagy 1-nél többször előforduló lineNumber.
**4** a számla nem tartalmaz tételt Alapszámláról nem szolgáltatható adat számlatétel nélkül, javítani kell.
**5** hibás a számlahivatkozás módosítás vagy
érvénytelenítés esetén

```
A módosítás vagy érvénytelenítés által hivatkozott számla nem található meg az adózó alapszámlái (ahol
invoiceOperation = CREATE) között a rendszerben, és a kérésben nem jelölték, hogy a módosításhoz nem tartozik korábbi
adatszolgáltatás (invoiceReference-ben a modifyWithoutMaster tag értéke false).
Javítani kell a hivatkozott számlasorszámot, vagy a modifyWithoutMaster taget true értékkel kell beküldeni.
```
```
Amennyiben a módosítás/érvénytelenítés jogelődre hivatkozik, akkor a referencia validálása a megjelölt jogelődnél
történik.
```
**6** a módosításban/érvénytelenítésben jelölt
számla típusa eltér az alapszámla típusától

A modifyWithoutMaster false értéke esetén a módosítás vagy érvénytelenítés által hivatkozott számla típusa
(invoiceCategory) nem egyezik meg a módosító okiratban közölt számla típussal (invoiceCategory), javítani kell.
**7** a megadott sorszámmal már létezik tétel a
számlaláncban

Az adatszolgáltatásban lévő lineModificationReference elemben olyan sorszám (lineNumberReference) van megadva,
mint létrehozandó új sor (lineOperation = CREATE), ami már létezik a számlalánc egy korábbi számlaadat-
szolgáltatásában. Vagy a lineNumberReference vagy a lineOperation hibás, javítani kell.
Jogelőd számlájára való hivatkozásnál a jogelőd és a jogutód számlalánc elemeit is figyelembe veszi.
**8** hibás a számla hivatkozás technikai
érvénytelenítés esetén

```
A technikai érvénytelenítés olyan számlasorszámra hivatkozik az annulmentReference-ben, mely az adózó számlái között
nem található meg a rendszerben, vagy megtalálható, de az Online Pénztárgépes vagy az Online Számlázó rendszerben
kiállított számla. Ellenőrizni kell a hivatkozott számlasorszámot.
Amennyiben a technikai érvénytelenítési kérésben jelölve volt a jogelőd adószáma, akkor a hivatkozás helyessége a
jogelődnél kerül megvizsgálásra.
```

**9** technikai érvénytelenítés van folyamatban A hibakód két esetben jelentkezhet. Az első, ha olyan számlára érkezik ismételten technikai érvénytelenítés, amire már
van jóváhagyásra váró technikai érvénytelenítés folyamatban. A másik, ha olyan alapszámlához érkezik új módosító vagy
sztornó számla, amire már van jóváhagyásra váró technikai érvénytelenítés folyamatban. A technikai érvénytelenítés
jóváhagyása / elutasítása az Online Számla felületén végezhető el, mindkét esetben meg kell várni az érvénytelenítési
kérés elbírálását.
Az adott számlára a számla kiállítója és a jogutódja(i) által beküldött érvénytelenítési kéréseket is figyelembe veszi a
validáció.
**10** a vevő adószáma nincs a technikai
felhasználóhoz rendelve

Ha az adatszolgáltatást teljesítő technikai felhasználót a bejelentő elsődleges technikai felhasználója egy bizonyos vevői
körre korlátozta, akkor a technikai felhasználó csak a korlátozásban szereplő vevők nevére (adószámára) állíthat ki
számlaadat-szolgáltatást. A hibakód akkor kerül visszaadásra, ha az adatszolgáltatásban nem engedélyezett vevői
adószám szerepel, vagy a vevő adószáma üres.
**11** a számla vagy számlalánc magasabb
verziószámú, mint a kérés requestVersion
értéke

A számlalánchoz módosító vagy sztornó számlát fűzni csak az alapszámla requestVersion értékével megegyező vagy attól
nagyobb verzióval lehet. Hasonlóképp, számlát vagy számlaláncot technikailag érvényteleníteni szintén csak az
alapszámla requestVersion értékével megegyező vagy attól nagyobb verzióval lehet. Ha a számlalánc kevert, akkor az
abban szereplő legalacsonyabb verzió értéke számít. Javítani kell a kérésben a requestVersion értékét.
**12** a lineNumberReference számlaszinten nem
egyedi

Módosító vagy sztornó számlában számlasor megadásakor a lineNumberReference elemnek számlaszinten egyedinek kell
lennie. Ha adott számlasor többször változik, a változást egy soron belül, egyesítve kell közölni. Javítani kell az
adatszolgáltatást.
**13** számlasor kötelező tartalmi eleme hiányzik Ha a lineExpressionIndicator tag értéke true, akkor a számlasorban az alábbi tagek mindegyikének megadása kötelező:

- termék vagy szolgáltatás megnevezése
- mennyiség
- mennyiségi egység
- egységár
Ha a lineExpressionIndicator tag értéke false, akkor a számlasorban csak a termék vagy szolgáltatás megnevezésének
megadása kötelező. Javítani kell az adatszolgáltatást.


**14** érvénytelen áfakulcs vagy áfatartalom A rendszer validációval kényszeríti az elévülési időn belül lévő áfakulcsok vagy tartalmak helyes megadását. Normál és
gyűjtőszámla esetén csak:

- 0. 05
- 0. 07
- 0. 12
- 0. 18
- 0. 2 (csak MODIFY/STORNO számla vagy 2013.01.01 előtti teljesítési időpontú CREATE számla esetén)
- 0. 25 (csak MODIFY/STORNO számla vagy 2013.01.01 előtti teljesítési időpontú CREATE számla esetén)
- 0. 27
- 0 (csak 2024.01.01. vagy utáni teljesítési időpontú számlák esetén)
egyszerűsített számla esetén pedig csak:
- 0. 0476
- 0.1525
- 0. 1667 (csak MODIFY/STORNO számla vagy 2013.01.01 előtti teljesítési időpontú CREATE számla esetén)
- 0.2 (csak MODIFY/STORNO számla vagy 2013.01.01 előtti teljesítési időpontú CREATE számla esetén)
- 0.2126
- 0 (csak 2024.01.01. vagy utáni teljesítési időpontú számlák esetén)
értékek adhatók meg mind a számlasorban, mind a számlaösszesítőkben. Javítani kell az adatszolgáltatást.
**15** a hivatkozott alapszámla egynél többször
szerepel érvényesként a rendszerben

A hivatkozott alapszámlára technikai érvénytelenítést kell jóváhagyni, majd az adatszolgáltatást megismételni a helyes
adatokkal. Az alapszámla feldolgozását követően a módosító vagy sztornó adatszolgáltatás újból beküldhető.
**16** a módosítás sorszáma nem egyedi A hivatkozott számla módosításáról megadott modificationIndex értékkel már szolgáltattak adatot. Ellenőrizni kell az
adatszolgáltatás tartalmát.
Amennyiben az adott számla jogelődre hivatkozik, akkor a jogelőd és a beküldő jogutód számlalánc elemeit is figyelembe
veszi a validáció.
**17** hiányoznak a vevő adatai Számláról (CREATE) szóló adatszolgáltatás esetén a customerInfo csomópont képzése kötelező, javítani kell.
**18** a módosító okirat adatai hiányoznak Módosításról (MODIFY) vagy érvénytelenítésről (STORNO) szóló adatszolgáltatás esetén a módosítás adatait leíró
invoiceReference csomópont képzése kötelező, javítani kell.
**19** a módosító okirat adatait nem szabad
feltüntetni

```
Számláról (CREATE) szóló adatszolgáltatás esetén a belső tartalomban az invoiceReference csomópont nem szerepelhet,
javítani kell.
```

**20** előzmény nélkülinek jelölt módosítás
előzményes

```
Módosító okiratról szóló adatszolgálatásban a módosítás előzmény nélkülinek volt jelölve (modifyWithoutMaster = true)
de a hivatkozott számla ennek ellenére érvényesként szerepel a rendszerben.
Ellenőrizni kell az adatszolgáltatás tartalmát (a fordított esetet az INVALID_INVOICE_REFERENCE foglalja magában).
```
Amennyiben a módosítás/érvénytelenítés jogelődre hivatkozik, akkor a referencia validálása a megjelölt jogelődnél
történik.
**21** számlasor módosítási adatai hiányoznak Módosításról (MODIFY) vagy érvénytelenítésről (STORNO) szóló adatszolgáltatás esetén a számlasorokban kötelező a
lineModificationReference csomópont szerepeltetése, javítani kell.
**22** számlasor módosítási adatait nem szabad
feltüntetni

Számláról (CREATE) szóló adatszolgáltatás esetén a belső tartalom számlasoraiban a lineModificationReference
csomópont nem szerepelhet, javítani kell.
**23** kötegelt módosításról szóló
adatszolgáltatásban a vevő adatai nem
azonosak

```
Kötegelt módosítás (batchInvoice) esetén, ahol a vevő adószáma meg van adva, akkor annak minden batchIndex alatt
azonos értékűnek kell lennie, javítani kell.
```
**24** magánszemély vevő adatait nem szabad
feltüntetni

```
Ha a vevő magánszemély (customerVatStatus = PRIVATE_PERSON), akkor a vevői adatok közül az alábbi csomópontok
nem lehetnek kitöltve:
```
- customerVatData
- customerName
- customerAddress
**25** nem magánszemély vevő adatainak
megadása kötelező

```
Ha a vevő nem magánszemély (customerVatStatus != PRIVATE_PERSON), akkor a vevői adatok közül az alábbi
csomópontok kitöltése kötelező:
```
- customerName
- customerAddress
**26** elektronikus számla hash-értékének
megadása kötelező

Ha a completenessIndicator (az adatszolgáltatás maga az elektronikus számla) jelölő értéke true, akkor az
electronicInvoiceHash megadása kötelező.
**27** érvénytelen hash-képző algoritmus Ha a completenessIndicator (az adatszolgáltatás maga az elektronikus számla) jelölő értéke **true** , akkor az
electronicInvoiceHash cryptoType hash képző algoritmus attribútum értéke csak SHA3-512 lehet.

Ha a completenessIndicator jelölő értéke **false** , akkor az electronicInvoiceHash cryptoType hash-képző algoritmus
attribútum lehetséges értékei: SHA-256, SHA3- 512
**28** érvénytelen hash-érték Ha a completenessIndicator (az adatszolgáltatás maga az elektronikus számla) jelölő értéke true, akkor az
electronicInvoiceHash értéke meg kell, hogy egyezzen az invoiceData csomópont **BASE64 enkódolt értékének** (a
megadott algoritmussal számolt) **nagybetűs** hash értékével.


**29** nem elektronikus megjelenésű számla
adatszolgáltatása nem lehet elektronikus
számlaként elfogadott

```
Ha a completenessIndicator (az adatszolgáltatás maga az elektronikus számla) jelölő értéke true, akkor a számla
megjelenési formája (invoiceAppearance) csak ELECTRONIC lehet.
```
**30** elektronikus számlaként elfogadott
adatszolgáltatás nem technikai
érvényteleníthető

```
Ha technikai érvénytelenítés beküldésnél a hivatkozott számlánál a completenessIndicator (az adatszolgáltatás maga az
elektronikus számla) jelölő értéke true, akkor a számla nem technikai érvényteleníthető.
```
**31** érvénytelen adómentességi kód (tétel) Az összes számlatípusnál tétel szinten (lineAmountsNormal, lineAmountsSimplified) is megadható adómentesség jelölése,
vatExemption néven. Ez a 3.0 verziótól kezdve alábontásra került egy kód (case) és leírás (reason) mezőkre.
A case értékre jelenleg az alábbi értékek elfogadottak (csak nagybetűvel megadva):

- AAM (Jelentése: alanyi adómentes)
- TAM (Jelentése: „tárgyi adómentes” ill. a tevékenység közérdekű vagy speciális jellegére tekintettel adómentes)
- KBAET (Jelentése: adómentes Közösségen belüli termékértékesítés, új közlekedési eszköz nélkül)
- KBAUK (Jelentés: adómentes Közösségen belüli új közlekedési eszköz értékesítés)
- EAM (Jelentése: adómentes termékértékesítés a Közösség területén kívülre (termékexport harmadik országba)
- NAM (Jelentése: egyéb nemzetközi ügyletekhez kapcsolódó jogcímen megállapított adómentesség)
- UNKNOWN (Csak MODIFY és STORNO számlánál elfogadott, ha az előzmény nélküli (modifyWithoutMaster =
    true VAGY a hivatkozott számla verziója 3.0-nál kisebb)
**32** érvénytelen adómentességi kód (összesítő) Az összes számlatípusnál összesítő szinten (summaryNormal, summarySimplified) is megadható adómentesség jelölése,
vatExemption néven. Ez a 3.0 verziótól kezdve alábontásra került egy kód (case) és leírás (reason) mezőkre.
A case értékre jelenleg az alábbi értékek elfogadottak (csak nagybetűvel megadva):
- AAM (Jelentése: alanyi adómentes)
- TAM (Jelentése: „tárgyi adómentes” ill. a tevékenység közérdekű vagy speciális jellegére figyelemmel
adómentes)
- KBAET (Jelentése: adómentes Közösségen belüli termékértékesítés, új közlekedési eszköz nélkül)
- KBAUK (Jelentés: adómentes Közösségen belüli új közlekedési eszköz értékesítés)
- EAM (Jelentése: adómentes termékértékesítés a Közösség területén kívülre (termékexport harmadik országba)
- NAM (Jelentése: egyéb nemzetközi ügyletekhez kapcsolódó jogcímen megállapított adómentesség)
- UNKNOWN (Csak MODIFY és STORNO számlánál elfogadott, ha az előzmény nélküli (modifyWithoutMaster =
true VAGY a hivatkozott számla verziója 3.0-nál kisebb)


**33** érvénytelen Áfa törvény hatályán kívüliséget
jelölő kód (tétel)

```
Az összes számlatípusnál tétel szinten (lineAmountsNormal, lineAmountsSimplified) is megadható Áfa törvény hatályán
kívüliség jelölése, vatOutOfScope néven. Ez a 3.0 verziótól kezdve alábontásra került egy kód (case) és leírás (reason)
mezőkre.
A case értékre jelenleg az alábbi értékek elfogadottak (csak nagybetűvel megadva):
```
- ATK (Jelentése: áfa tárgyi hatályán kívül)
- EUFAD37 (Jelentése: Áfa tv. 37. §-a alapján másik tagállamban teljesített, fordítottan adózó ügylet)
- EUFADE (Jelentése: másik tagállamban teljesített, nem az Áfa tv. 37. §-a alá tartozó, fordítottan adózó ügylet)
- EUE (Jelentése: másik tagállamban teljesített, nem fordítottan adózó ügylet)
- HO (Jelentése: harmadik országban teljesített ügylet)
- UNKNOWN (Csak MODIFY és STORNO számlánál elfogadott, ha az előzmény nélküli (modifyWithoutMaster =
    true VAGY a hivatkozott számla verziója 3.0-nál kisebb)

**34** érvénytelen Áfa törvény hatályán kívüliséget
jelölő kód (összesítő)

```
Az összes számlatípusnál összesítő szinten (summaryNormal, summarySimplified) is megadható Áfa törvény hatályán
kívüliség jelölése, vatOutOfScope néven. Ez a 3.0 verziótól kezdve alábontásra került egy kód (case) és leírás (reason)
mezőkre.
A case értékre jelenleg az alábbi értékek elfogadottak (csak nagybetűvel megadva):
```
- ATK (Jelentése: áfa tárgyi hatályán kívül)
- EUFAD37 (Jelentése: Áfa tv. 37. §-a alapján másik tagállamban teljesített, fordítottan adózó ügylet)
- EUFADE (Jelentése: másik tagállamban teljesített, nem az Áfa tv. 37. §-a alá tartozó, fordítottan adózó ügylet)
- EUE (Jelentése: másik tagállamban teljesített, nem fordítottan adózó ügylet)
- HO (Jelentése: harmadik országban teljesített ügylet)
- UNKNOWN (Csak MODIFY és STORNO számlánál elfogadott, ha az előzmény nélküli (modifyWithoutMaster =
    true VAGY a hivatkozott számla verziója 3.0-nál kisebb)

**35** hivatkozott számla nem elektronikus
számlaként elfogadott adatszolgáltatás

```
Módosításról (MODIFY) vagy érvénytelenítésről (STORNO) szóló adatszolgáltatás esetén a hivatkozott számlánál a
completenessIndicator (az adatszolgáltatás maga az elektronikus számla) jelölő értéke false, és a beküldött
MODIFY/STORNO számlánál completenessIndicator értéke true.
```

**36** érvénytelen adóalap és felszámított adó
eltérés kód (tétel)

```
Az összes számlatípusnál tétel szinten (lineAmountsNormal, lineAmountsSimplified) is megadható adóalap és felszámított
adó eltérést jelölő kód, vatAmountMismatch néven. Ez alábontásra került egy kód (case) és adómérték (vatRate)
mezőkre.
A case értékre jelenleg az alábbi értékek elfogadottak (csak nagybetűvel megadva):
```
- REFUNDABLE_VAT (Jelentése: az áfa felszámítása a 11. vagy 14. § alapján történt és az áfát a számla
    címzettjének meg kell térítenie)
- NONREFUNDABLE_VAT (Jelentése: az áfa felszámítása a 11. vagy 14. § alapján történt és az áfát a számla
    címzettjének nem kell megtérítenie)
- UNKNOWN (Csak MODIFY és STORNO számlánál elfogadott, ha az előzmény nélküli (modifyWithoutMaster =
    true VAGY a hivatkozott számla verziója 3.0-nál kisebb)
**37** érvénytelen adóalap és felszámított adó
eltérés kód (összesítő)

```
Az összes számlatípusnál összesítő szinten (summaryNormal, summarySimplified) is megadható adóalap és felszámított
adó eltérést jelölő csomópont, vatAmountMismatch néven. Ez szintén alábontásra került egy kód (case) és adómérték
(vatRate) mezőkre.
A case értékre jelenleg az alábbi értékek elfogadottak (csak nagybetűvel megadva):
```
- REFUNDABLE_VAT (Jelentése: az áfa felszámítása a 11. vagy 14. § alapján történt és az áfát a számla
    címzettjének meg kell térítenie)
- NONREFUNDABLE_VAT (Jelentése: az áfa felszámítása a 11. vagy 14. § alapján történt és az áfát a számla
    címzettjének nem kell megtérítenie)
- UNKNOWN (Csak MODIFY és STORNO számlánál elfogadott, ha az előzmény nélküli (modifyWithoutMaster =
    true VAGY a hivatkozott számla verziója 3.0-nál kisebb)
**38** összevont tételeket tartalmazó számla
adatszolgáltatása nem lehet elektronikus
számlaként elfogadott

```
Összevont adattartalmú tételeket tartalmazó számla (mergedItemIndicator = true) adatszolgáltatása nem lehet
elektronikus számla, tehát a completenessIndicator jelölő értéke nem lehet true.
```
**39** magánszemélynek kiállított számla
adatszolgáltatása nem lehet elektronikus
számlaként elfogadott

```
Magánszemélynek kiállított számla (customerVatStatus = PRIVATE_PERSON) adatszolgáltatása nem lehet elektronikus
számla, tehát a completenessIndicator jelölő értéke nem lehet true.
```
**40** adatszolgáltatás elektronikus számlaként
történő elfogadása nem engedélyezett

Adatszolgáltatás elektronikus számlaként történő elfogadtatása jelenleg nem támogatott, tehát completenessIndicator
jelölő értéke nem lehet true.
Ez egy átmeneti hibakód, ami a jogszabályok érvényre jutásának időpontjáig adhat a rendszer.
**41** áfatartalom nem adható meg nem
egyszerűsített tétel érték adatként

```
Tétel szinten, ha a normal típusú értékadatokat tartalmazó csomópont van képezve (lineAmountsNormal), akkor a
lineVatRate csomóponton belül a vatContent érték nem tölthető ki, hiszen az csak egyszerűsített számlák esetén
értelmezhető.
```

**42** adómérték nem adható meg egyszerűsített
tétel értékadatként

Tétel szinten, ha az egyszerűsített típusú értékadatokat tartalmazó csomópont van képezve (lineAmountsSimplified),
akkor a lineVatRate csomóponton belül a vatPercentage érték nem tölthető ki, hiszen az csak nem egyszerűsített számlák
esetén értelmezhető.
**43** áfatartalom nem adható meg nem
egyszerűsített összesítő érték adatként

Összesítő szinten, ha a normal típusú értékadatokat tartalmazó csomópont van képezve (summaryNormal), akkor a
vatRate csomóponton belül a vatContent érték nem tölthető ki, hiszen az csak egyszerűsített számlák esetén
értelmezhető.
**44** adómérték nem adható meg egyszerűsített
összesítő értékadatként

Összesítő szinten, ha az egyszerűsített típusú értékadatokat tartalmazó csomópont van képezve (summarySimplified),
akkor a vatRate csomóponton belül a vatPercentage érték nem tölthető ki, hiszen az csak nem egyszerűsített számlák
esetén értelmezhető.
**45** belföldi áfaalany vevő esetén a magyar
adószám kötelező

Ha a vevő belföldi áfaalany (CustomerVatStatusType = DOMESTIC), akkor a magyar adószám (customerVatData)
megadása kötelező (kivéve, ha az eladó áfaregisztrált).
**46** belföldi áfaalany vevő esetén a közösségi
adószám nem adható meg

Ha a vevő belföldi áfaalany (CustomerVatStatusType = DOMESTIC), akkor a közösségi adószám (communityVatNumber)
nem adható meg.
**47** belföldi áfaalany vevő esetén a harmadik
országbeli adószám nem adható meg

Ha a vevő belföldi áfaalany (CustomerVatStatusType = DOMESTIC), akkor a harmadik országbeli adószám
(thirdStateTaxId) nem adható meg.
**48** érvénytelen adóalap és felszámított adó
eltérés áfamérték (tétel)

```
Tétel szinten az adóalap és felszámított adó eltérést jelölő adómérték csak a következ értékek valamelyike lehet:
```
- 0.27, 0.18, 0.05, 0.2126, 0.1525, 0.04 76 ,
- 0 (csak 2024.01.01. vagy utáni teljesítési időpontú számlák esetén)
**49** érvénytelen adóalap és felszámított adó
eltérés áfamérték (összesítő)

```
Összesítő szinten az adóalap és felszámított adó eltérést jelölő adómérték csak a következ értékek valamelyike lehet:
```
- 0.27, 0.18, 0.05, 0.2126, 0.1525, 0.04 76
- 0 (csak 2024.01.01. vagy utáni teljesítési időpontú számlák esetén)
**50** belföldi fordított adózású ügyletnél a magyar
adószám kötelező

Ha a számla tételei között szerepel olyan, ami belföldi fordított adózású (vatDomesticReverseCharge), akkor a magyar
adószám (customerVatData) megadása kötelező.
**51** érvénytelen számla sorszám A számla sorszáma (invoiceNumber) elején és végén nem lehet whitespace karakter (LF (line feed), CR (carriage return),
HT (horizontal tab), space).
**52** módosító vagy sztornó számla beküldése nem
lehetséges létező egyéb forrású módosító
számla miatt

```
Ha az alapszámlára létezik már nem OPG-s módosítás/sztornózás (akár előzményes, akár előzmény nélküli), akkor OPG-s
módosító/sztornó számla nem küldhető be.
```
**53** Online Pénztárgépes számla csak
egyszerűsített számla lehet.

```
OPG forrású számla típusa csak egyszerűsített (SIMPLIFIED) lehet.
```

**54** teljesítés időpontja nem lehet későbbi, mint a
kiállítás időpontja + 5 év.

Ha a teljesítés időpontja (invoiceDeliveryDate) későbbi, mint a kiállítás időpontja (issueDate) + 5 év, akkor az hiba, javítani
kell.
**55** kiállítás időpontja nem lehet későbbi, mint a
beküldés időpontja + 1 év.

```
Ha a kiállítás időpontja (issueDate) későbbi, mint a beküldés időpontja +1 év, akkor az hiba, javítani kell.
```
**56** normál vagy gyűjtőszámla egyszerűsített
számlatétel(eke)t tartalmaz.

```
Ha normál-, vagy gyűjtőszámlában egyszerűsített számlatételadatok kerülnek kitöltésre, akkor az hiba, javítani kell.
```
**57** normál vagy gyűjtőszámla egyszerűsített
számlaösszesítőt tartalmaz.

```
Ha normál-, vagy gyűjtőszámlában egyszerűsített számla összesítő adatok kerülnek kitöltésre, akkor az hiba, javítani kell.
```
**58** egyszerűsített számla normál
számlatétel(eke)t tartalmaz.

```
Ha egyszerűsített számlában normál számla számlatételadatok kerülnek kitöltésre, akkor az hiba, javítani kell.
```
**59** egyszerűsített számla normál
számlaösszesítőt tartalmaz.

```
Ha egyszerűsített számlában normál számla összesítő adatok kerülnek kitöltésre, akkor az hiba, javítani kell.
```
**60** módosító vagy érvénytelenítő számla
valamely tétele meglévő tételsort módosít.

Ha módosító vagy érvénytelenítő számláról beküldött adatszolgáltatásban valamely tételben a lineOperation elem
értékében “MODIFY” kerül megadásra, akkor az hiba, javítani kell az adatszolgáltatást. A lineOperation értékének minden
esetben „CREATE”-nek kell lennie.
**61** A művelet az adott jogelődre vonatkozóan
tiltott vagy helytelenül van jelölve.

```
A hiba több esetben érkezhet.
```
- Ha a beküldött adatszolgáltatásban az invoiceHead/invoiceDetail/additionalInvoiceData listában a dataName =
    “A10000_JOGELOD_ADOSZAM” vagy “A10000_JOGELOD_POTLAS” kód többször szerepel, az hiba. Legfeljebb
    egyszer szerepelhet.
- A jogelőd számlájára való hivatkozás jelzése csak MODIFY/STORNO számlán engedélyezett, CREATE számla
    esetén tiltott (dataName = “A10000_JOGELOD_ADOSZAM” kód jelzése).
- Jogelőd számlájára való hivatkozás jelzése esetén validálásra kerül a beküldő és a megjelölt adózó közötti
    kapcsolat (dataName = “A10000_JOGELOD_ADOSZAM” kód jelzés esetén a beküldő és a dataValue-ban
    megadott adószám vizsgálata).
- Jogelőd nevében beküldött számlaadat-szolgáltatás esetén validálásra kerül a beküldő és a megjelölt kiállító
    közötti kapcsolat (dataName = “A10000_JOGELOD_POTLAS” kód jelzés során a beküldő és az eladói oldalon
    megadott adózó kapcsolatának vizsgálata). Pótlás esetén további megkötés, hogy a beküldő és a megjelölt
    kiállító között tiltott a leválás és kiválás típus jogutódlási forma. Továbbá áfacsoportok számára tiltott a jogelődre
    vonatkozó pótlás művelete.
**62** több eladóhoz tartozó számlák kötegelt
módosítása nem lehetséges

```
Kötegelt módosítás (batchInvoice) esetén az összes invoice csomópontban csak ugyanaz a supplierTaxNumber
szerepelhet. Jogelődre és jogutódra ugyanazon számlaadat-szolgáltatáson belül nem küldhető be számla, ezeket külön
kell beküldeni.
```

```
63 jogelődre való hivatkozás nem egységes Kötegelt módosítás (batchInvoice) esetén nem keveredhet a saját és a jogelőd számlákra való hivatkozás.
Az összes invoice csomópontban kell szerepelnie invoiceHead/invoiceDetail/additionalInvoiceData/dataName =
“A10000_JOGELOD_ADOSZAM” kódnak vagy sehol sem.
Amennyiben minden invoice csomópontban szerepel, akkor elvárt továbbá, hogy a dataValue-ban megadott jogelőd
ugyanaz legyen mindenhol.
```
#### 3.3.3 Figyelmeztetések

A figyelmeztetések nem akadályozzák az adatszolgáltatás teljesítését, azonban a számla tartalmát felül kell vizsgálni, és szükség szerint javítani. Az egyes
figyelmeztetések típusosak, a figyelmeztetéssel érintett tagek a message-ben kerülnek megjelölésre, olyan számossággal, ahányszor az adatszolgáltatás
megsérti az összefüggésben meghatározott feltételt.

A figyelmeztetéseket a feldolgozó rendszer szolgáltató jelleggel, az adatszolgáltatásra kötelezett adózó tájékoztatása céljából képezi meg és szerepelteti a
válaszüzenetben. Az adatszolgáltatásban észlelt, de magát az adatszolgáltatást nem ellehetetlenítő problémákról nyújtott tájékoztatás célja, hogy segítséget
nyújtson az adatszolgáltatásra kötelezett adózó oldalán jelentkező esetleges szoftverhibák, adatbeviteli hibák, hibás gyakorlatok észlelésében és javításában.
Figyelmeztetés csak a probléma egyértelmű létezése esetén keletkezik, kétes esetben nem.

Ha egy adatszolgáltatásban a számlaadatok befogadásakor nem generálódik figyelmeztetés, ezen tény nem bizonyítja a küldött adattartalom helyességét sem
jogi, sem technikai értelemben. Gépi vizsgálattal nem feltétlenül mutatható ki az adatszolgáltatásban szereplő adathiba, különösen nem mutatható ki az
eredeti okirat és az adatszolgáltatás adattartalmának eltérése.

Az adatszolgáltatás feldolgozásakor ellenőrzött adatok és összefüggések listája nem lezárt, a rendszer működtetési tapasztalatai alapján ezen ellenőrzések
köre folyamatosan bővülhet.

A beküldött számlaadatok számszaki összefüggéseinek vizsgálatakor a rendszer nem küld figyelmeztetést az olyan esetekben, amikor a számszaki eltérés ugyan
létezik, de minden bizonnyal a kerekítésből adódik. Az így „tolerált” legnagyobb eltérés a nettó ár 1 százaléka, legalább 1 egység.

A jogszabály nem ír elő kötelezően követendő eljárást, így általános szabály nem adható arra vonatkozóan, hogy pontosan mi a teendő a figyelmeztetések
esetén. Alapvetően a figyelmeztetésre okot adó körülmény jellege – szoftverhiba, adatbeviteli hiba, hibás gyakorlat – határozza meg a követendő eljárást. A
figyelmeztetést kiváltó körülmények sokrétűsége miatt az adott szervezet jellegéből, tevékenységéből, létszámából következően a figyelmeztetést célszerű


lehet a felhasználónak, a számvitelért felelős egységnek, a technikai támogató egységnek, a szoftver fejlesztőjének vagy ezek közül többnek is hozzáférhetővé
tenni.

A figyelmeztetések kapcsán követendő eljárást nem az adatszolgáltatás szabályai határozzák meg, hanem a bizonylatolásra és a számlázásra vonatkozó
általános szabályok. Például egy számszaki hibás (például hibás összeadás) számlát az általános szabályok szerint módosító okirattal ki kell javítani. Nem azért,

mert figyelmeztetés érkezett rá, hanem azért, mert számszaki hibás.

A figyelmeztetések részletes leírása az I. számú mellékletben található.


## 4 TÖRZSEK

### 4.1 AZ ILLETÉKES ÁLLAMI ADÓHATÓSÁGOT JELZŐ ILLETÉKESSÉGI KÓDOK (COUNTYCODE)

```
Társas vállalkozás megye kódja Egyéni vállalkozás megye kódja
Baranya megye 02 22
Bács-Kiskun megye 03 23
Békés megye 04 24
Borsod-Abaúj-Zemplén megye 05 25
Csongrád megye 06 26
Fejér megye 07 27
Győr-Moson-Sopron megye 08 28
Hajdú-Bihar megye 09 29
Heves megye 10 30
Komárom-Esztergom megye 11 31
Nógrád megye 12 32
Pest megye 13 33
Somogy megye 14 34
Szabolcs-Szatmár-Bereg
megye
```
```
15 35
```
```
Jász-Nagykun-Szolnok megye 16 36
Tolna megye 17 37
Vas megye 18 38
Veszprém megye 19 39
Zala megye 20 40
Észak-Budapest 41 41
Kelet-Budapest 42 42
Dél-Budapest 43 43
Pest Megyei és Fővárosi
Kiemelt Adózók Igazgatósága
```
```
44 44
```
```
Kizárólagos illetékességű
adóalanyok
```
```
51 51
```
### 4.2 ORSZÁGKÓD TÍPUS ISO 3166 ALPHA- 2 SZABVÁNY SZERINT

Az alábbi linken megtalálható a hivatalos nemzetközi ISO szabvány szerinti országkód lista, ahol az
Alpha-2 code oszlopot kell figyelembe venni.

https://www.iso.org/obp/ui/#search

### 4.3 IRÁNYÍTÓSZÁM TÖRZS ELÉRHETŐSÉGE

https://www.posta.hu/szolgaltatasok/iranyitoszam-kereso

https://www.posta.hu/static/internet/download/Iranyitoszam-Internet_uj.xlsx

### 4.4 VTSZ TÖRZS ELÉRHETŐSÉGE

https://nav.gov.hu/pfile/file?path=/szabalyzok/tajekoztatasok/4002_2019._1.melleklet


### 4.5 SZJ TÖRZS ELÉRHETŐSÉGE

https://www.ksh.hu/osztalyozasok_teszor2- 1

### 4.6 KN TÖRZS ELÉRHETŐSÉGE

https://www.ksh.hu/kombinalt_nomenklatura

### 4.7 CSK TÖRZS ELÉRHETŐSÉGE

[http://njt.hu/cgi_bin/njt_doc.cgi?docid=142904.348985](http://njt.hu/cgi_bin/njt_doc.cgi?docid=142904.348985) 1. melléklet A) cím

### 4.8 KT TÖRZS ELÉRHETŐSÉGE

[http://njt.hu/cgi_bin/njt_doc.cgi?docid=142904.348985](http://njt.hu/cgi_bin/njt_doc.cgi?docid=142904.348985) 1. melléklet B) cím

### 4.9 EJ TÖRZS ELÉRHETŐSÉGE

https://www.ksh.hu/epitmenyjegyzek_menu

### 4.10 TESZOR TÖRZS ELÉRHETŐSÉGE

https://www.ksh.hu/osztalyozasok_teszor2- 1

## 5 VERZIÓKÖVETÉS

A szolgáltatás módosításának könnyebb nyomon követhetősége miatt, jelen pont tartalmazza a
lényegesebb változásokat és a különböző bevezetett interfészverziókat.

### 5.1 1.0-ÁS XSD-VERZIÓ

A dokumentum publikálásának idején a header/requestVersion elemében 1.0-át kell szerepeltetni.

### 5.2 1.1-ES XSD-VERZIÓ

Az 1.1-es interfészverzió adatminőség javítási célokat szolgál. Mivel a verzió biztosítja szerver oldalon
az új XSD visszafelé kompatibilitását az 1.0-ás verzióval, a séma névtér sem változik a jövőben addig,
amíg fenti állítás igaz.

**A bevezetett módosítások az 1.0-ás verzióval történő adatszolgáltatást nem befolyásolják, az összes
módosítás csak requestVersion > 1.0 esetben lép életbe.**

A módosítások tételesen a következők.

API XSD módosítás

A felsorolt módosítások csak requestVersion > 1.0 esetén lépnek életbe.

1) A BasicHeaderType típusban 1.1 értékkel bűvült a requestVersion tag értékkészlete.
2 ) a /queryInvoiceStatus lekérdező operáció válaszában visszaadásra kerül a lekérdezett tranzakció
requestVersion értéke (amivel az adatszolgáltatás történt) az originalRequestVersion tagban
3 ) a /queryInvoiceData lekérdező operáció válaszában, nem paraméteres keresés esetén visszaadásra
kerül a lekérdezett számla requestVersion értéke (amivel az adatszolgáltatás történt) az
auditData/originalRequestVersion tagban

Data XSD módosítás

A felsorolt módosítások csak requestVersion > 1.0 esetén lépnek életbe.


1) A DateType típus legkisebb megadható értéke 2010 - 01 - 01 értékre változott. Ez azt is jelenti,

hogy az API szerinti számlaadat keresésben sem lehet ennél kisebbet megadni.
2) A TimestampType típus legkisebb megadható értéke 2010- 01 - 01T00:00:00.000Z értékre
változott.
3) A számlafejben az átváltási árfolyam megadása (exchangeRate) tag kötelezővé vált. Forint
számla esetén 1-et, devizaszámla esetén a tényleges átváltási árfolyamot kell közölni. Ha a
módosító számla nem tartalmaz számlasort, de a számlafejben lévő változás miatt az átváltási
árfolyamot ismét közölni kell, akkor az exchangeRate tagban a módosítást megelőző, utolsó
érvényes értéket kell feltüntetni.
4) Nem gyűjtőszámla esetén az áfamérték szerinti összesítést (summaryByVatRate) legalább
egyszer kötelező közölni a számlaösszesítőben. Ha módosító számla nem tartalmaz számlasort
(és ez miatt nem lehet az áfaösszesítőt tényszerűen megadni) akkor normál és gyűjtőszámla
esetén 27 százalékos áfát és 0 forintot, egyszerűsített számla esetén 0% adómértéket és 0
forint adómértéket kell megadni.
5) A számlasorba bevezetésre került egy logikai jelölő tag (lineExpressionIndicator), amelynek
megadása minden számlasorban kötelező. Ha a tag értéke true, akkor adott számlasorban
kötelező megadni:
a. a termék vagy szolgáltatás nevét
b. mennyiségét
c. mennyiségi egységét
d. egységárát
Ha a tag értéke false, akkor adott számlasorban csak a termék vagy szolgáltatás nevét kötelező
megadni.
6) A számlasorban megadható mennyiségi egység (unitOfMeasure) saját típust kapott az alábbi
enumerációkkal, melyeket kötelező használni:

```
Mennyiségi egység
```
```
UnitOfMeasureType
típusú elem értéke
Darab PIECE
Kilogramm KILOGRAM
Tonna TON
Kilowatt óra KWH
Nap DAY
Óra HOUR
Perc MINUTE
Hónap MONTH
Liter LITER
Kilométer KILOMETER
Köbméter CUBIC_METER
Méter METER
Folyóméter LINEAR_METER
Karton CARTON
Csomag PACK
Saját OWN
```
```
Ha a számlán szereplő mennyiségi egység nem sorolható be egyik típusba sem, akkor az OWN
értéket kell választani.
```

```
7) A számlasorban bevezetésre került egy saját mennyiségi egység típus. Ezt akkor szükséges
használni, ha a számlán szereplő mennyiségi egység nem sorolható be a unitOfMeasure elem
értéklistájában szereplő mennyiségi egységek egyikébe sem, így a unitOfMeasure elemben
"OWN" érték szerepel. Ha a kanonikus mennyiségi egység értéke OWN, és a saját mennyiségi
egység nincs megadva, akkor a rendszer egy WARN-üzenetet ad vissza. Nem tilos a saját
mennyiségi egység feltüntetése akkor sem, ha a unitOfMeasure elemben "OWN"-tól
különböző érték szerepel.
```
Új technikai hibák

```
1) Számla feldolgozási eredményt lekérdezni a /queryInvoiceStatus operációban csak az
adatszolgáltatással azonos vagy magasabb requestVersion értékkel lehet. Ha a szabály nem
teljesül, a szinkron művelet STATUS_QUERY_NOT_ALLOWED hibakóddal elutasításra kerül és
az adatszolgáltatás nem számít lekérdezettnek.
```
Új blokkoló validációk

A felsorolt validációk csak abban az esetben futnak, ha requestVersion > 1.0. A sorszintű validációk
pointert is visszaadnak.

```
1) MODIFY, STORNO és ANNUL operációk esetén, ha a hivatkozott számla verziója nagyobb, mint
1.0, akkor azon, műveletet végezni csak legalább ugyanazon verziójú kéréssel lehet. Így az 1.1-
es verzióval készült számlát módosítani, sztornózni vagy technikailag érvényteleníteni nem
lehet 1.0-ás kéréssel. Ha a szabály nem teljesül, a művelet
REQUEST_VERSION_REFERENCE_ERROR hibakóddal elutasításra kerül.
2) Módosító vagy sztornó számlában, ha számlasor meg van adva, akkor a számla egészében a
lineNumberReference tagnak egyedinek kell lennie. Ha a hivatkozott sort több módosítás is
érinti, akkor azokat egyben, összegezve kell közölni. Ha a fenti szabály nem teljesül, a művelet
LINE_NUMBER_REFERENCE_NOT_UNIQUE hibakóddal elutasításra kerül.
3) Alapszámlában, vagy módosító és sztornó számlában (ha ezek tartalmaznak számlasort)
minden számlasorban kötelező megadni a lineExpressionIndicator tag értékét. Ha a fenti
szabály nem teljesül, a művelet LINE_EXPRESSION_INDICATOR_MISSING hibakóddal
elutasításra kerül.
4) A lineExpressionIndicator tag értékének megfelelően adott számlasorban a kitöltési
szabályoknak teljesülni kell (lásd Data XSD módosítás, 5-ös pont). Ha a kitöltési szabály nem
teljesül, a művelet MANDATORY_LINE_CONTENT_MISSING hibakóddal elutasításra kerül.
5) A rendszer validáció szintjén vizsgálja a számlasorokban és számla összesítőkben megadott
áfakulcs és áfamérték értékeket. Normál és gyűjtőszámla esetén csak:
o 0. 05
o 0. 07
o 0. 12
o 0. 18
o 0. 2 (csak MODIFY/STORNO számla vagy 2013.01.01 előtti teljesítési időpontú CREATE
számla esetén)
o 0. 25 (csak MODIFY/STORNO számla vagy 2013.01.01 előtti teljesítési időpontú
CREATE számla esetén)
o 0. 27
```
```
egyszerűsített számla esetén pedig csak:
```

```
o 0
o 0. 0476
o 0.1525
o 0. 1667 (csak MODIFY/STORNO számla vagy 2013.01.01 előtti teljesítési időpontú
CREATE számla esetén)
o 0.2 (csak MODIFY/STORNO számla vagy 2013.01.01 előtti teljesítési időpontú CREATE
számla esetén)
o 0.2126
```
```
értékek adhatók meg mind a számlasorban, mind a számlaösszesítőkben. Ha a fenti szabály
nem teljesül, a művelet INVALID_VAT_DATA hibakóddal elutasításra kerül.
```
WARN módosítások

A felsorolt módosítások csak akkor lépnek életbe, ha requestVersion > 1.0, kivéve a kivezetett WARN -
üzenetek, melyek módosítása visszamenőleges az 1.0-ra.

```
1) Kivezetésre kerültek az alábbi WARN -üzenetek:
a. INCORRECT_SUMMARY_CALCULATION_VAT_RATE_GROSS_AMOUNT_LINE
b. INCORRECT_SUMMARY_CALCULATION_INVOICE_VAT_RATE_GROSS_AMOUNT_SUM
MARY
c. INCORRECT_SUMMARY_CALCULATION_INVOICE_GROSS_AMOUNT
d. INCORRECT_LINE_DATA_LINE_VAT_RATE
e. MISSING_SUMMARY_DATA_INVOICE_VAT_AMOUNT_HUF
f. INCORRECT_PRODUCT_CODE_EXCISE_LICENSE_NUM
g. INCORRECT_PRODUCT_FEE_DATA_OBLIGATED_SUMMARY
h. INCORRECT_PRODUCT_FEE_CALCULATION_PRODUCT_CODE_VALUE
i. MISSING_LINE_DATA_QUANTITY
j. MISSING_LINE_DATA_DESCRIPTION
k. MISSING_HEAD_DATA_EXCHANGE_RATE
l. INVALID_UNIT_OF_MEASURE_OWN
m. MISSING_HEAD_DATA_INVOICE_ISSUE_DATE
n. MISSING_LINE_DATA_LINE_EXCHANGE_RATE
2) Bevezetésre kerültek az alábbi WARN -üzenetek:
a. SUPPLIER_CUSTOMER_MATCH_NAME
b. MISSING_LINE_PRODUCT_FEE_CONTENT
c. MISSING_LINE_DATA_LINE_EXCHANGE_RATE
d. MISSING_HEAD_DATA_CUSTOMER_TAXNUMBER
e. INCORRECT_SUMMARY_DATA_INVOICE_VAT_AMOUNT_HUF
f. INCORRECT_SUMMARY_DATA_AGGREGATE_INVOICE_VAT_AMOUNT_HUF
g. INCORRECT_SUMMARY_CALCULATION_VAT_RATE_VAT_AMOUNT_SUMMARY
h. INCORRECT_SUMMARY_CALCULATION_INVOICE_VAT_AMOUNT_SUMMARY
i. INCORRECT_PRODUCT_CODE_VALUE_OWN
j. INCORRECT_DATE_INVOICE_MODIFICATION_ISSUE_DATE_ORIGINAL
k. INCORRECT_DATE_INVOICE_MODIFICATION_ISSUE_DATE_LATE
l. INCORRECT_DATE_INVOICE_MODIFICATION_ISSUE_DATE_EARLY
m. INCORRECT_DATE_INVOICE_ISSUE_DATE_LATE
n. INCORRECT_DATE_INVOICE_ISSUE_DATE_EARLY
o. INCORRECT_DATE_INVOICE_DELIVERY_DATE_LATE
p. INCORRECT_DATE_INVOICE_DELIVERY_DATE_EARLY
```

q. INCORRECT_DATE_AGGREGATE_INVOICE_DELIVERY_DATE
r. INCORRECT_SUMMARY_CALCULATION_INVOICE_GROSS_AMOUNT_LINE
s. INCORRECT_SUMMARY_CALCULATION_VAT_CONTENT_SUMMARY_SIMPLIFIED
t. INCORRECT_SUMMARY_CALCULATION_VAT_CONTENT_GROSS_AMOUNT_SUMMAR
Y_SIMPLIFIED
u. INCORRECT_SUMMARY_CALCULATION_INVOICE_VAT_AMOUNT
v. INCORRECT_LINE_REFERENCE
w. INCORRECT_LINE_DATA_UOM_INCOMPLETE
3) Módosításra kerültek az alábbi WARN -üzenetek:
a. INCORRECT_VAT_CODE_SUPPLIER
b. INCORRECT_VAT_CODE_SUPPLIER_GROUPMEMBER
c. INCORRECT_VAT_CODE_CUSTOMER
d. INCORRECT_VAT_CODE_CUSTOMER_GROUPMEMBER
e. INCORRECT_VAT_CODE_FISCALREPRESENTATIVE
f. INCORRECT_VAT_CODE_TAXNUMBEROFOBLIGATOR
g. INCORRECT_COUNTY_CODE_SUPPLIER_GROUPMEMBER
h. INCORRECT_COUNTY_CODE_CUSTOMER_GROUPMEMBER
i. INCORRECT_COUNTY_CODE_FISCAL_REPRESENTATIVE
j. INCORRECT_COUNTRY_CODE_FISCALREPRESENTATIVEADDRESS
k. INCORRECT_DATE_INVOICE_MODIFICATION_TIMESTAMP
l. MISSING_HEAD_DATA_CUSTOMER
m. INCORRECT_HEAD_DATA_FISCAL_REPRESENTATIVE_TAX_NUMBER
n. INCORRECT_LINE_DATA_LINE_AMOUNTS_NORMAL_MANDATORY
o. INCORRECT_LINE_DATA_AGGREGATE_INV_LINE_DATA_MANDATORY
p. INCORRECT_VAT_CODE_SUPPLIER_GROUPMEMBER_MISSING
q. INCORRECT_HEAD_DATA_LAST_MOD_INVOICE_NUMBER
r. INCORRECT_HEAD_DATA_MOD_REF_INVOICE_NUMBER
s. INCORRECT_HEAD_DATA_INVOICE_NUMBER_LAST_MOD_DOC_NUMBER
t. INCORRECT_HEAD_DATA_LAST_MOD_LAST_MOD_DOC_NUMBER átnevezésre került
INCORRECT_HEAD_DATA_ORIGINAL_LAST_MOD_DOC_NUMBER-re
u. INCORRECT_LINE_DATA_LINE_AMOUNTS_SIMPLIFIED_NOT_ALLOWED
v. INCORRECT_PRODUCT_FEE_CALCULATION_PRODUCT_FEE_AMOUNT
w. INCORRECT_PRODUCT_FEE_CALCULATION_AGGREGATE_PRODUCT_CHARGE_SUM
x. INCORRECT_LINE_CALCULATION_GROSS_AMOUNT
y. INCORRECT_LINE_CALCULATION_NETTO_AMOUNT átnevezésre került
INCORRECT_LINE_CALCULATION_NET_AMOUNT
z. INCORRECT_SUMMARY_CALCULATION_VAT_RATE_NET_AMOUNT_LINE
aa. INCORRECT_SUMMARY_DATA_VAT_PERCENTAGE
bb. INCORRECT_SUMMARY_DATA_VAT_EXEMPTION
cc. INCORRECT_SUMMARY_DATA_VAT_OUT_OF_SCOPE
dd. INCORRECT_SUMMARY_DATA_VAT_DOMESTIC_REVERSE_CHARGE
ee. INCORRECT_SUMMARY_DATA_MARGIN_SCHEME_VAT
ff. INCORRECT_SUMMARY_DATA_MARGIN_SCHEME_NO_VAT
gg. INCORRECT_HEAD_DATA_FISCALREPRESENTATIVE
hh. INCORRECT_SUMMARY_CALCULATION_INVOICE_NET_AMOUNT
ii. INCORRECT_SUMMARY_CALCULATION_VAT_RATE_VAT_AMOUNT_HUF_SUMMARY
átnevezésre került
INCORRECT_SUMMARY_CALCULATION_INVOICE_VAT_AMOUNT_HUF_SUMMARY
jj. INCORRECT_SUMMARY_CALCULATION_INVOICE_GROSS_AMOUNT_SUMMARY


```
kk. ISSUE_DATE_TIMESTAMP_MISMATCH
```
A meglévő, illetve az új és módosított WARN -üzenetek pontos vizsgálatait az I. sz. melléklet
tartalmazza.

### 5.3 2.0-ÁS XSD-VERZIÓ

A 2.0-ás interfészverzió célja refaktorlálni a meglévő rendszert, bővíteni a nyújtott szolgáltatások körét,
valamint lecserélni az SHA-512 hash algoritmust az SHA3-512 algoritmusra a requestSignature
számításakor. A változtatás breaking change, ezért a 2.0-ás főverzió új szolgáltatás végpontokat és új
XML namespace-t kap.

**A bevezetett módosítások az 1. 1 - es verzióval történő adatszolgáltatást nem befolyásolják, az összes
módosítás csak akkor lép életbe, ha requestVersion > 1.1 és a kérést a kliens az új, v2-es végpontra
küldi. Az új teszt és éles végpontok leírása a 6. fejezetben található.**

A módosítások tételesen a következők.

Általános módosítások

1) A korábbi két darab XSD (invoiceApi és invoiceData) szétválasztásra került, a 2.0-ás verzióban a
technikai érvénytelenítés adatait az invoiceAnnulment XSD tartalmazza, ezáltal a korábbi belső choice
az invoiceData XSD-ben eltűnik. Ezen felül bevezetésre kerül egy új serviceMetrics XSD, amely a
szolgáltatás működési metrikáit tartalmazza.
2) Minden sémában új namespace kerül bevezetésre „http://schemas.nav.gov.hu/OSA/2.0/...”
értékkel.
3) A dokumentáció kiegészítésre került az eltérő verziók közötti általános összefüggésekkel. A
részletekről lásd: „Verziókezelés”.

API XSD általános módosítások

1) Minden request és response saját komplex típust kapott.
2) Minden requestben kötelező a software adatok megadása a sémában defininált mezőkkel.
3) Minden requestben változik a requestSignature számításának módja. A részletekről lásd: 1.5 fejezet.

API XSD operációk módosításai

1) Bevezetésre került a /manageAnnulment operáció. Ebben a kérésben van lehetőség technikai
érvénytelenítést beküldeni, tehát a 2.0-ban a technikai érvénytelenítést már nem a /manageInvoice
operáció alatt kell küldeni. A részletekről lásd: „A /manageAnnulment operáció” fejezet.
2) A /manageInvoice operáció típusából törlésre került a korábbi technicalAnnulment boolean,
valamint külön típust kapott az operáció, melynek a megadható értékei csak CREATE, MODIFY,
STORNO.
3) A korábbi heterogén /queryInvoiceData lekérdező operáció szétválasztásra került három részre:

- - /queryInvoiceCheck, amely számlaszám alapján csak a számla létezését ellenőrzi, a számla
    adatainak visszaadása nélkül
- /queryInvoiceDigest, amely paraméteres számla lekédezési lehetőséget biztosít, és lapozható
    válaszban csak a számlák meghatározott üzleti adatait (kivonatát) adja vissza
- a szétválasztás után a /queryInvoiceData operációnak egyetlen felelősségi köre marad, hogy
    számlaszám alapján a számla teljes adattartalmát lekérdezhetővé tegye


- mind a három lekérdezés használható kiállítói és vevői oldalról is, a részletekről lásd a
    megfelelő operációk leírásait az „A /queryInvoiceCheck operáció”, „A /queryInvoiceDigest
    operáció” és „A /queryInvoiceData operáció” fejezetekben
4) Az interfész szolgáltatásai között megjelent a /queryServiceMetrics operáció, amely a rendszer és a
számla fogadó szolgáltatás üzleti metrikáit teszi lekérdezhetővé. A szolgáltatás jelenleg nem aktív, a
későbbiekben kerül megnyitásra és dokumentálásra.
5) A számlák feldolgozási státuszát visszaadó /queryInvoiceStatus operáció átnevezésre került
/queryTransactionStatus névre. A szolgáltatás tranzakcióazonosító alapján képes technikai
érvénytelenítéseket tartalmazó tranzakció esetén visszaadni a jóváhagyás státuszát és egyéb üzleti
adatait. Ezen felül a válaszban visszaadott pointer tag kiegészítésre került az originaInvoiceNumber
taggal, ami MODIFY és STORNO adatszolgáltatás esetén lesz töltve.
6) Az adószám lekérdezésre használt /queryTaxpayer operáció válasza létező adószám lekérdezésekor
tartalmazza az adózó rövid nevét és az adózó áfacsoport tagságát, ha volt ilyen. A belső címadatok nem
saját típusból, hanem a data sémaleíró DetailedAddressType típusából öröklődnek. Jelezzük, hogy a
rövid név jelenleg még nem kerül töltésre egy hiányzó adatkapcsolati fejlesztés miatt. Amint a
fejlesztés megvalósul, külön hírt teszünk közzé a rövid név elérhetőségéről.
7) Az adószám lekérdezésre használt /queryTaxpayer operáció válasza létező adószám lekérdezésekor
tartalmazza az adózó adatainak utolsó változását, valamint visszaadásra kerül az adózó teljes adószáma
(törzsszám – áfakör – megyekód). Az adózóhoz tartozó címadat már listaként szerepel a válaszban.
8) Bevezetésre került a /queryInvoiceChainDigest lekérdező operáció. A lekérdezés elsősorban a
számlaláncban szereplő sorok számát, illetve a módosításokra vonatkozó adatokat tartalmazza. Az
operáció kezeli a vegyes verziójú (1.x, 2.0) számaláncokat is.
9) Bevezetésre került a /queryTransactionList lekérdező operáció. A lekérdezés a megadott
időintervallumban történt adatszolgáltatások tranzakciónak kilistázására szolgál.
10) Bevezetésre került a /queryServiceMetrics lekérdező operáció. A lekérdezés az Online Számla
rendszer általános működési metrikáit szolgáltatja. A részletekről lásd. a „Rendszerdiagnosztika”
fejezetet.
11) A /queryInvoiceDigest operációban lehetőség van a kiállító és a vevő adószámára is szűrni a
visszaadott számlákat. Ezzel a korábbi supplierTaxNumber keresőparaméter törlésre került a
mandatoryQueryParams csomópont alatt, szűkítő adószám megadására az
additionalQueryParams/taxNumber tagban van lehetőség.

Új szinkron hibaüzenetek

1) A 2.0-ás verzióban az alábbi új szinkron hibaüzenetek adhatók vissza:

- MULTIPLE_QUERY_RESULT_FOUND
- BAD_QUERY_PARAM_OVERLAP
- BAD_QUERY_PARAM_RANGE_EXCEEDED
- BAD_QUERY_PARAM_EQ_NOT_STANDALONE
- BAD_QUERY_PARAM_OPERATOR_COLLISION
- BAD_QUERY_PARAM_SUPPLIER_NOT_EXPECTED
- BAD_QUERY_PARAM_SUPPLIER_EXPECTED
- INVALID_TIMESTAMP

A hibakódok működéséről lásd: 3.2 fejezet.

Törölt szinkron hibaüzenetek

1) A 2.0-ás verzióban a séma változásai az alábbi hibaüzenetek törlését eredményezik:


- INVALID_OPERATION
- BAD_QUERY_PARAM

Számla (CREATE) adattartalom általános változásai

1) A 2.0-ás invoiceData séma a következő módosításokat tartalmazza:

- a számla legfelső szintjére kiemelésre került a számla sorszáma és a kiállításának dátuma
- a lineExpressionIndicator tag kötelezővé vált, default értéke false a többi boolean mezővel
    összhangban
- a PostalCodeType új patternt kapott, a bevitt érték kötelező hossza 4-ről 3-ra csökkent és
    elfogadott a szóköz és a kötőjel is, ha a stringben nem kezdő vagy záró pozíción áll
- a lineDescription tag 512 hosszú lett
- ProductCodeCategoryType új enummal bővült (TESZOR), a maximális hossza 6-ra változott
- a productCodeOwnValue tag 255 hosszú lett
- a számlafejben a számla további üzleti adatait leíró korábbi invoiceData csomópont
    átnevezésre került invoiceDetail névre
- az invoiceDeliveryDate tag kötelezővé vált
- új tartalomként bekerült a számla üzleti adatai közé a kisadózó jelzése (smallBusinessIndicator)
    és az időszakos elszámolás (periodicalSettlement) jelzése
- új tartalomként opcionális elemként bekerült a számlasorok adatai közé a termék/szolgáltatás
    minősítésére használható lineNatureIndicator, a kitöltési útmutatóról szóló segédlethez lásd:
    2.3.17
- új tartalomként a normál és egyszerűsített számlasorok, valamint a normál és egyszerűsített
    számláknál használt számlaösszesítők is kiegészítésre kerültek azon monetáris kifejezések
    párjával, amelyek eddig vagy csak a számla pénznemében, vagy csak forintban voltak kifejezve,
    a módosítást követően minden monetáris kifejezésnek létezik a számla pénznemében és
    forintban is kifejezett összege a következők szerint:
       a. egységár forintban (line/unitPriceHUF)
       b. tétel nettó összege forintban
          (invoiceLines/line/lineAmountsNormal/lineNetAmountData/lineNetAmountHUF)
       c. tétel bruttó összege forintban
          (invoiceLines/line/lineAmountsNormal/lineGrossAmountData/lineGrossAmountNor
          malHUF)
       d. tétel bruttó összege forintban
          (invoiceLines/line/lineAmountsSimplified/lineGrossAmountSimplifiedHUF)
       e. számla bruttó összege forintban
          (invoiceSummary/summaryGrossData/invoiceGrossAmountHUF)
       f. számla nettó összege forintban
          (invoiceSummary/summaryNormal/invoiceNetAmountHUF)
       g. számla adótartalom bruttó összege forintban
          (invoiceSummary/summarySimplified/vatContentGrossAmountHUF)
       h. adómérték nettó összege forintban
          (invoiceSummary/summaryNormal/summaryByVatRate/vatRateNetData/vatRateNet
          AmountHUF)
       i. adómérték bruttó összege forintban
          (invoiceSummary/summaryNormal/summaryByVatRate/vatRateGrossData/vatRateG
          rossAmountHUF)


```
Az elemek kötelezősége öröklődik a sémában már korábban definiált párjukból.
```
Módosító, érvénytelenítő számlákról (MODIFY, STORNO) szóló adatszolgáltatás új szabályai

1) A 2.0-ás verzióban megszűnnek a korábbi modificationIssueDate, modificationTimestamp és
lastModificationReference elemek. A módosító okirat kiállítási dátumát a számla kiállítási dátumát
tartalmazó invoiceIssueDate elemben kell közölni ugyanúgy, ahogy a számlánál is. Plusz elemként
megjelenik a modificationIndex, amely a módosítás logikai sorrendjét írja le a számlának. A
részletszabályokról lásd: 2.2.1 fejezet.

Adatszolgáltatás több számlát módosító okiratról

1) A 2.0-ás verziótól más módszerrel történik meg az egy módosító okirattal több számla
módosításának adatszolgáltatása. A részletszabályokról lásd: 2.5.6 fejezet.

Technikai érvénytelenítés új indoka

1) A számla kiállítási dátumának kiemelésével logikailag módosíthatatlanná vált az invoiceIssueDate
tag értéke. A technikai jellegű helyesbítéshez a technikai érvénytelenítés okát leíró annulmentCode új
enummal, az ERRATIC_INVOICE_ISSUE_DATE értékkel bővült.

Új aszinkron hibaüzenetek

1) A 2.0-ás verzióban az alábbi új aszinkron hibaüzenetek adhatók vissza:

- MODIFICATION_INDEX_NOT_UNIQUE
- CUSTOMER_INFO_MISSING
- INVOICE_REFERENCE_EXPECTED
- INVOICE_REFERENCE_NOT_EXPECTED
- MODIFY_WITHOUT_MASTER_MISMATCH
- LINE_MODIFICATION_EXPECTED
- LINE_MODIFICATION_NOT_EXPECTED
- CUSTOMER_NOT_IDENTICAL
- DUPLICATE_INVOICE_LINE_CREATION

A hibakódok működéséről lásd: 3.3.2 fejezet.

Szétválaszott aszinkron (ERROR) hibaüzenetek

1) A 2.0-ás verzióban két korábban többértelmű hibaüzenet került szétválasztásra több külön esetre
annak érdekében, hogy a hibás XML-ek elkülöníthetők legyenek kliens oldalon az állapotfüggő
esetektől.

INVALID_INVOICE_REFERENCE

- az operáció nem CREATE és nincs a belső tartalomban invoiceReference csomópont:
    INVOICE_REFERENCE_EXPECTED
- az operáció CREATE és a belső tartalomban szerepel invoiceReference csomópont:
    INVOICE_REFERENCE_NOT_EXPECTED
- a modifyWithoutMaster értéke nem a valóságnak megfelelő (az értéke true és a hivatkozott
    számla érvényesként szerepel az adózó számlái között):
    MODIFY_WITHOUT_MASTER_MISMATCH


A szétválasztás után az INVALID_INVOICE_REFERENCE hibakód csak egy logikai esetben adható vissza:

ha a hivatkozott számla nincs meg az adózó számlái között érvényesként.

INVOICE_LINE_ALREADY_EXISTS

- az operáció nem CREATE és nincs a belső tartalom számlasoraiban lineModificationReference
    csomópont: LINE_MODIFICATION_EXPECTED
- az operáció CREATE és a belső tartalom számlasoraiban szerepel a lineModificationReference
    csomópont: LINE_MODIFICATION_NOT_EXPECTED

Törölt aszinkron (ERROR) hibaüzenetek

1) A 2.0-ás verzióban a séma változásai az alábbi hibaüzenetek törlését eredményezi:

- MANDATORY_CONTENT_MISSING
- LINE_EXPRESSION_INDICATOR_MISSING

WARN működési módosítások

1) A 2.0-ás verzióban az alábbi WARN módosítások történtek:

- az INCORRECT_DATE_AGGREGATE_INVOICE_DELIVERY_DATE nevű WARN nem fut MODIFY és
    STORNO operációkban
- a korábbi INCORRECT_DATE_INVOICE_MODIFICATION_ISSUE_DATE_ORIGINAL nevű WARN
    átnevezésre került INCORRECT_DATE_MODIFICATION_ISSUE_DATE_EARLY névre

WARN -leírások didaktikai módosításai

1) A WARN -üzenetek message tagban szereplő leírásai egyértelműbbek lettek, hogy a felhasználóknak
megjelenítve közérthetőbben tükrözzék a problémát és a megoldás módját. A módosított leírás a

dokumentáció I. mellékletében található.

Törölt WARN -üzenetek

1) A 2.0-ás verzióban a séma változásai az alábbi WARN -üzenetek törlését eredményezik:

- INCORRECT_DATE_INVOICE_MODIFICATION_TIMESTAMP
- INCORRECT_HEAD_DATA_LAST_MOD_INVOICE_NUMBER
- INCORRECT_HEAD_DATA_INVOICE_NUMBER_LAST_MOD_DOC_NUMBER
- INCORRECT_HEAD_DATA_ORIGINAL_LAST_MOD_DOC_NUMBER
- ISSUE_DATE_TIMESTAMP_MISMATCH

Új WARN -üzenetek

1) A 2.0-ás verzióban az alábbi új WARN -üzenetek adhatók vissza:

- INCORRECT_SUMMARY_DATA_INVOICE_NET_AMOUNT
- INCORRECT_SUMMARY_DATA_INVOICE_GROSS_AMOUNT
- INCORRECT_LINE_CALCULATION_LINE_NET_AMOUNT_HUF
- INCORRECT_LINE_CALCULATION_AGGREGATE_LINE_NET_AMOUNT_HUF
- INCORRECT_LINE_CALCULATION_LINE_VAT_AMOUNT_HUF
- INCORRECT_LINE_CALCULATION_AGGREGATE_LINE_VAT_AMOUNT_HUF
- INCORRECT_LINE_CALCULATION_LINE_UNIT_PRICE_HUF
- INCORRECT_LINE_CALCULATION_AGGREGATE_LINE_UNIT_PRICE_HUF


- INCORRECT_LINE_CALCULATION_LINE_GROSS_AMOUNT_NORMAL_HUF
- INCORRECT_LINE_CALCULATION_AGGREGATE_LINE_GROSS_AMOUNT_NORMAL_HUF
- INCORRECT_LINE_CALCULATION_LINE_GROSS_AMOUNT_SIMPLIFIED_HUF
- INCORRECT_LINE_CALCULATION_LINE_GROSS_AMOUNT_NORMAL_SUM
- INCORRECT_SUMMARY_DATA_INVOICE_NET_AMOUNT_HUF
- INCORRECT_SUMMARY_DATA_INVOICE_VAT_CONTENT_GROSS_AMOUNT_HUF
- INCORRECT_SUMMARY_DATA_INVOICE_GROSS_AMOUNT_HUF
- INCORRECT_SUMMARY_DATA_INVOICE_VAT_RATE_NET_AMOUNT_HUF
- INCORRECT_SUMMARY_DATA_INVOICE_VAT_RATE_VAT_AMOUNT_HUF
- INCORRECT_SUMMARY_CALCULATION_VAT_RATE_NET_AMOUNT_HUF_LINE
- INCORRECT_SUMMARY_CALCULATION_INVOICE_NET_AMOUNT_HUF
- INCORRECT_SUMMARY_CALCULATION_INVOICE_GROSS_AMOUNT_HUF_SUMMARY
- INCORRECT_SUMMARY_CALCULATION_VAT_RATE_VAT_AMOUNT_HUF_SUMMARY
- INCORRECT_SUMMARY_CALCULATION_INVOICE_GROSS_AMOUNT_HUF_LINE
- INCORRECT_SUMMARY_CALCULATION_VAT_CONTENT_GROSS_AMOUNT_HUF_SUMMARY_
    SIMPLIFIED
- INCORRECT_SUMMARY_CALCULATION_INVOICE_VAT_AMOUNT_HUF
- INCORRECT_SUMMARY_CALCULATION_INVOICE_NET_AMOUNT_LINE_HUF

Az új WARN-ok működéséről lásd. I. melléklet.

### 5.4 3.0-ÁS XSD-VERZIÓ

#### 3.0-ás alkalmazásverzió

A 3.0-ás interfészverzió célja elsősorban a 2021. január 4 - étől érvénybe lépő új üzleti funkcionalitások
biztosítása, illetve egy általános, hosszú távon fenntartható rugalmas séma kialakítása.

Új üzleti funkcionalitások

A 3.0-ás séma legfontosabb üzleti funkciói az alábbiak:

- elektronikus számlázás támogatása
- nagyméretű számlák adatszolgáltatása
- közszolgáltatói elszámolószámlák adatszolgáltatása

Ezen funkciók külön-külön fejezetekben (2.6 – 2.8) kerülnek kifejtésre.

Általános XSD módosítások

Figyelemmel arra, hogy a 2020.07.01 óta történt értékhatár eltörlés miatt az Online számla API egy
olyan közös nyelv és kommunikációs platform lett, amelyet országosan minden jogszabály szerint
működő számlázó szoftvernek ismernie kell, a NAV informatikailag továbbviszi ezt a koncepciót. Az
Online Számla saját sémáiból kiemelésre kerülnek azon generikus, üzleti katalógus jellegű, valamint a
kommunikációt leíró típusok, amelyek más projektben is felhasználhatóak és átkerülnek egy új
common XSD-be. A common XSD-nek saját névtere van és külön is verziózzuk, ami okán a GitHubon is
külön projektben található (https://github.com/nav-gov-hu/Common). A kiemelés rengeteg
namespace változással és átnevezéssel is jár az Online Számla sémáiban, azonban a kiemelés azt


eredményezi, hogy más, jövőben készülő NAV-os XML API-hoz nem kell új technikai felhasználókat

létrehozni az adózóknak. Az Online Számla alatt regisztrált technikai felhasználók ugyanazokkal az
authentikációs adatokkal és kulcsokkal, ugyanazon alap XML szerkezetben, ugyanazon (vagy hasonló)
kriptográfiai metódusokkal képesnek lesznek más projekt API-t is megszólítani. Példaként a
folyamatban lévő e-áfa projekt XML API-ját lehetne felhozni, amely képes lesz ennek a működésnek a
támogatására.

Tekintettel arra, hogy a common XSD esetében az Online Számla projekt sémái már olyan névteret is
importálnak, amely már nem a projekt része, bevezetésre kerül a catalog XSD, mint technológia
(https://www.oasis-open.org/committees/download.php/14809/xml-
catalogs.html#s.using.catalogs). Ez azt eredményezi, hogy minden <xs:import> tag elveszíti a

"schemaLocation" attribútumát, az importok helyét NAV által szerkesztett sémában a catalog
határozza meg. A legtöbb XML processzor az importált sémákat ugyanazon a filepath-on keresi, mint
ahol a feldolgozandó séma definíció is van, ezért minden fejlesztőnek el kell dönteni, hogy vagy
visszaírja a "schemaLocation" értékeket a NAV-tól letöltött sémába saját magánál, vagy catalogot
használ. Mindkét megoldás elfogadható. A common XSD esetében a catalog használatát azért
javasoljuk mindenkinek, mert ha már több saját projektben fogja a common-os sémát használni, akkor
elég lesz csak egy helyen frissíteni, ha a fenti séma változik. A catalogra biztosítunk template fájlt, amit
fel lehet majd használni. A template-ben lesz uri name és publicId támogatás is, valamint működni fog
lokálból és webes resource eléréssel is a GitHub repón keresztül.

Megtörténik az XSD hierarchia rendezése, így megszűnik az invoiceData elsődlegessége az
importokban. Ezt úgy lehet elérni, hogy az Online Számla rendszerre nézve több sémában felhasznált

azon típusok, amelyek túl speciálisak ahhoz, hogy betegyük a common XSD-be, egy új, invoiceBase
nevű sémában lesznek elérhetőek. Az Online Számla rendszer 3.0-ás sémái (Api, Data, Annulment,
Metrics) már csak a common-t és az invoiceBase sémát importálják, ez által a függési struktúra tisztul.

API XSD operációk módosításai

1) A /queryTaxpayer operáció válasza új elemmel bővül: incorporation, amely megmondja, hogy az
adószám gazdasági társaság vagy egyéni vállalkozó-e. Lehetséges értékei:

- ORGANIZATION: Gazdasági társaság
- SELF_EMPLOYED: Egyéni vállalkozó
- TAXABLE_PERSON: Adószámos magánszemély

2) A /queryTransactionList operáció válasza 2 új elemmel bővül:

- requestStatus: a tranzakció státusza
- technicalAnnulment: technikai érvénytelenítés ténye

3) A /queryInvoiceDigest operáció válasza visszaadja a completenessIndicator (adatszolgáltatás maga
az elektronikus számla) értékét

4) A /queryInvoiceDigest operáció válaszában pontosításra kerültek a csoportazonosító számokat
tartalmazó elemek nevei: supplierGroupTaxNumber -> supplierGroupMemberTaxNumber,
customerGroupTaxNumber -> customerGroupMemberTaxNumber


5) A /manageInvoice request részében az invoiceOperation csomópont kiegészült az

electronicInvoiceHash mezővel.

6) A /queryInvoiceData response részében az InvoiceDataResult szintén kiegészült az
electronicInvoiceHash mezővel.

7) A / queryTransactionList request része kiegészül a requestStatus mezővel, ami opcionális, és a
tranzakció státuszára lehet vele szűrni.

Új szinkron hibaüzenetek

1) A 3.0-ás verzióban az alábbi új aszinkron hibaüzenetek adhatók vissza:

- INVALID_PASSWORD_HASH_CRYPTO
- INVALID_REQUEST_SIGNATURE_HASH_CRYPTO
- INVALID_REQUEST_VERSION
- INVALID_HEADER_VERSION

A hibakódok működéséről lásd: „Hibakezelés” fejezet.

Számla adattartalom általános változásai

1) Az electronicInvoiceHash (opcionális) mező kikerült API szintre, mivel a hash-értékét a teljes
invoiceData csomópont BASE64 értékéből kell számolni.

2) Bevezetesre került a completenessIndicator (kötelező) mező, amely segítségével jelölhető, hogy az

adatszolgáltatás maga az elektronikus számla.

3) A customerInfo kiegészült a customerVatStatus (kötelező) mezővel, amely jelzi a vevő áfa szerinti
státuszát:

- DOMESTIC: Belföldi áfaalany,
- OTHER: Egyéb (belföldi nem áfaalany, nem természetes személy, külföldi áfaalany és külföldi nem
áfaalany, nem természetes személy),
- PRIVATE_PERSON: Nem áfaalany (belföldi vagy külföldi) természetes személy

4) A vevői adószám megadására bevezetésre került a customerVatData, amelyen belül a belföldi
adószám, közösségi adószám, harmadik országbeli adóazonosító közül pontosan egy adható meg.
Részletes leírás a „ **Vevői adószám”** fejezetben.

5) Az invoiceDetail kiegészítésre került a utilitySettlementIndicator (opcionális) mezővel, amellyel a
közmű elszámolószámla típus jelezhető.

6) Bevezetésre került tétel és számla szinten a conventionalInvoiceInfo/conventionalLineInfo
(opcionális) csomópont, amelyben egyezményes, nevesített egyéb adatok adhatóak meg, melyek a
könnyebb feldolgozást hivatottak segíteni.


7) Az invoiceLine csomópont kiegészült a mergedItemIndicator (kötelező) mezővel, amellyel jelezhető,

ha a számla összevont adattartalmú tétel(eke)t tartalmaz.

8) Tétel szinten az előleg jelleget jelző mező komplex típussá alakult. Az új advanceData (opcionális)
csomópont tartalmazza a tétel előlegre vonatkozó adatait.

9) Tétel és összesítő szinten is az adómérték/adómentesség értékeket tartalmazó csomópont került
bevezetésre egyszerűsített és normál csomópontok esetén is. Lásd „ **vatRate”** fejezet.

10) Egyszerűsített számlák esetén a megadott adómérték már nem veheti fel a 0 értéket 3.0 XSD
verziótól kezdve. Ilyenkor az INVALID_VAT_DATA hibaüzenet jön.

Technikai érvénytelenítés új indoka

1) A számla hash-értékének API szintre emelésével logikailag módosíthatatlanná vált az
electronicInvoiceHash tag értéke. A technikai jellegű helyesbítéshez a technikai érvénytelenítés okát
leíró annulmentCode új enummal, az ERRATIC_ELECTRONIC_HASH_VALUE értékkel bővült.

Új aszinkron hibaüzenetek

1) A 3.0-ás verzióban az alábbi új aszinkron hibaüzenetek adhatók vissza:

- CUSTOMER_DATA_NOT_EXPECTED
- CUSTOMER_DATA_EXPECTED
- ELECTRONIC_INVOICE_HASH_EXPECTED
- INVALID_INVOICE_HASH_CRYPTO
- INVALID_INVOICE_HASH
- INVOICE_APPEARANCE_MISMATCH
- ELECTRONIC_INVOICE_ANNULMENT_NOT_ALLOWED
- INVALID_LINE_VAT_EXEMPTION_CODE
- INVALID_SUMMARY_VAT_EXEMPTION_CODE
- INVALID_LINE_VAT_OUT_OF_SCOPE_CODE
- INVALID_SUMMARY_VAT_OUT_OF_SCOPE_CODE
- INCOMPLETE_ELECTRONIC_INVOICE_REFERENCE
- INVALID_LINE_VAT_AMOUNT_MISMATCH_CODE
- INVALID_SUMMARY_VAT_AMOUNT_MISMATCH_CODE
- INVOICE_COMPLETENESS_MERGED_ITEM_INDICATOR_MISMATCH
- INVOICE_COMPLETENESS_PRIVATE_PERSON_INDICATOR_MISMATCH
- INVOICE_COMPLETENESS_NOT_ALLOWED
- INVALID_LINE_VAT_RATE_NORMAL
- INVALID_LINE_VAT_RATE_SIMPLIFIED
- INVALID_SUMMARY_VAT_RATE_NORMAL
- INVALID_SUMMARY_VAT_RATE_SIMPLIFIED
- MISSING_CUSTOMER_DOMESTIC_TAXNUMBER
- CUSTOMER_COMMUNITY_TAXNUMBER_NOT_EXPECTED
- CUSTOMER_THIRD_STATE_TAXNUMBER_NOT_EXPECTED
- INVALID_LINE_VAT_AMOUNT_MISMATCH_VAT_RATE
- INVALID_SUMMARY_VAT_AMOUNT_MISMATCH_VAT_RATE


- DOMESTIC_TAXNUMBER_EXPECTED_REVERSE_CHARGE
- INVALID_INVOICE_NUMBER

A hibakódok működéséről lásd: „Hibakezelés” fejezet.

WARN működési módosítások

1) A 3.0-ás verzióban az alábbi meglévő WARN-ok működései változnak:

- SUPPLIER_CUSTOMER_MATCH_NAME
- SUPPLIER_CUSTOMER_MATCH_BANKACCOUNT
- INCORRECT_VAT_CODE_FISCALREPRESENTATIVE
- INCORRECT_HEAD_DATA_MOD_REF_INVOICE_NUMBER

2) A tolerált eltérést vizsgáló WARN-ok esetében változott a tolerált eltérés mértéke a következők
szerint:

„A tolerált eltérés a számított forintban kifejezett érték 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.”

Törölt WARN -üzenetek

1) A 3.0-ás verzióban a séma változásai az alábbi WARN -üzenetek törlését eredményezik:

- INCORRECT_VAT_CODE_SUPPLIER_GROUPMEMBER
- NCORRECT_VAT_CODE_CUSTOMER
- INCORRECT_VAT_CODE_CUSTOMER_GROUPMEMBER
- INCORRECT_HEAD_DATA_CUSTOMER_COMMUNITY_VAT_NUMBER
- MISSING_HEAD_DATA_CUSTOMER
- MISSING_HEAD_DATA_CUSTOMER_TAXNUMBER
- INCORRECT_SUMMARY_DATA_MARGIN_SCHEME_VAT

2) Az alábbi WARN üzenet átsorolásra kerül INFO-nak:

- INCORRECT_DATE_INVOICE_ISSUE_DATE_EARLY

Új WARN -üzenetek

1) A 3.0-ás verzióban az alábbi új WARN -üzenetek adhatók vissza:

- INCORRECT_HEAD_DATA_SUPPLIER_GROUPMEMBER_TAXPAYERID
- INCORRECT_HEAD_DATA_CUSTOMER_TAXPAYERID
- INCORRECT_HEAD_DATA_CUSTOMER_GROUPMEMBER_TAXPAYERID
- INCORRECT_HEAD_DATA_PERIODICAL_SETTLEMENT


- INCORRECT_LINE_DATA_VAT_EXEMPTION_NORMAL
- INCORRECT_LINE_DATA_VAT_OUT_OF_SCOPE_NORMAL
- INCORRECT_LINE_DATA_VAT_DOMESTIC_REVERSE_CHARGE_NORMAL
- INCORRECT_LINE_DATA_MARGIN_SCHEME_INDICATOR_NORMAL
- INCORRECT_LINE_DATA_AGGREGATE_INVOICE_LINE_DATA
- INCORRECT_SUMMARY_DATA_VAT_EXEMPTION_NORMAL
- INCORRECT_SUMMARY_DATA_VAT_OUT_OF_SCOPE_NORMAL
- INCORRECT_SUMMARY_DATA_VAT_DOMESTIC_REVERSE_CHARGE_NORMAL
- INCORRECT_SUMMARY_DATA_MARGIN_SCHEME_INDICATOR
- INCORRECT_SUMMARY_DATA_MARGIN_SCHEME_INDICATOR_NORMAL
- INCORRECT_SUMMARY_DATA_VAT_AMOUNT_MISMATCH_NORMAL
- INCORRECT_SUMMARY_CALCULATION_VAT_EXEMPTION_SUMMARY_SIMPLIFIED
- INCORRECT_SUMMARY_CALCULATION_VAT_OUT_OF_SCOPE_SUMMARY_SIMPLIFIED
- INCORRECT_SUMMARY_CALCULATION_VAT_DOMESTIC_REVERSE_CHARGE_SUMMARY_SIM
    PLIFIED
- INCORRECT_SUMMARY_CALCULATION_VAT_MARGIN_SCHEME_INDICATOR_SUMMARY_SI
    MPLIFIED
- INCORRECT_SUMMARY_CALCULATION_VAT_AMOUNT_MISMATCH_SUMMARY_SIMPLIFIED
- INCORRECT_LINE_DATA_VAT_DOMESTIC_REVERSE_CHARGE

#### 3.11-es alkalmazásverzió

Újonnan bevezetésre kerülő blokkoló ERROR üzenetek:

- INVOICE_ISSUE_DATE_LATE
- INVOICE_DELIVERY_DATE_LATE

Kivezetésre került WARN üzenet:

- INCORRECT_DATE_INVOICE_DELIVERY_DATE_LATE

Újonnan bevezetésre kerülő WARN üzenetek:

A vevő ÁFA státusza és a tételek ÁFA minősítése közötti ellentmondások vizsgálata:

- INCORRECT_LINE_DATA_VAT_STATUS_VAT_DATA_MISMATCH_KBAET
- INCORRECT_LINE_DATA_VAT_STATUS_VAT_DATA_MISMATCH_KBAET_SIMPLIFIED
- INCORRECT_LINE_DATA_VAT_STATUS_VAT_DATA_MISMATCH_KBAUK
- INCORRECT_LINE_DATA_VAT_STATUS_VAT_DATA_MISMATCH_KBAUK_SIMPLIFIED
- INCORRECT_LINE_DATA_VAT_STATUS_VAT_DATA_MISMATCH_EUFAD37
- INCORRECT_LINE_DATA_VAT_STATUS_VAT_DATA_MISMATCH_EUFADE
- INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_KBAET
- INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_KBAET_SIMPLIFIED
- INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_KBAUK
- INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_KBAUK_SIMPLIFIED
- INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_EAM
- INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_EAM_SIMPLIFIED
- INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_EUFAD37


- INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_EUFADE
- INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_EUE

Továbbá bevezetésre kerültek az alábbi adatszolgáltatás logikai és számszaki ellenőrzését vizsgáló
warnok:

- INCONSISTENT_MODIFICATION_DATA_STORNO_ALREADY_EXISTS
- INCONSISTENT_MODIFICATION_DATA_NETAMOUNT_NOT_ZERO_NORMAL
- INCONSISTENT_MODIFICATION_DATA_VATAMOUNT_NOT_ZERO
- INCONSISTENT_MODIFICATION_DATA_VATAMOUNT_NOT_ZERO_HUF

#### 3.17-es alkalmazásverzió

Az alábbi WARN üzenetek átsorolásra kerültek ERROR üzenetté:

- LINE_SUMMARY_TYPE_MISMATCH_LINE_SIMPLIFIED
- LINE_SUMMARY_TYPE_MISMATCH_LINE_NORMAL
- LINE_SUMMARY_TYPE_MISMATCH_SUMMARY_SIMPLIFIED
- LINE_SUMMARY_TYPE_MISMATCH_SUMMARY_NORMAL

Kivezetésre került WARN üzenet:

- SUPPLIER_CUSTOMER_MATCH_NAME

Az alábbi meglévő WARN-ok működései változnak:

- INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_EAM
- INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_EAM_SIMPLIFIED
- INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_EUFADE
- INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_EUE
- INCORRECT_HEAD_DATA_PERIODICAL_SETTLEMENT

Az alábbi meglévő ERROR-ok működései változnak:

- INVOICE_LINE_MISSING
- INVALID_VAT_DATA

Újonnan bevezetésre kerülő WARN üzenetek:

- INCORRECT_HEAD_DATA_CUSTOMER_GROUPMEMBER_TAXNUMBER
- INCONSISTENT_MODIFICATION_DATA_AMOUNT_NOT_ZERO_SIMPLIFIED
- INCONSISTENT_MODIFICATION_DATA_MODIFICATIONINDEX_UNREAL


- INCORRECT_HEAD_DATA_CURRENCY_CODE_HUF
- INCORRECT_HEAD_DATA_EXCHANGE_RATE_1
- INCORRECT_HEAD_DATA_EXCHANGERATE_EXTREME

Újonnan bevezetésre kerülő INFO üzenetek:

- UNINTENDED_MODIFICATION_DELIVERY_DATE
- INCORRECT_HEAD_DATA_CUSTOMER_TAXPAYERID_DIFFERS
- INCORRECT_HEAD_DATA_SUPPLIER_BANKACCOUNT_MISSING
- MODIFICATIONINDEX_SEQUENCE_INCOMPLETE

#### 3.21-es alkalmazás verzió

Újonnan bevezetésre kerülő blokkoló ERROR üzenetek:

- INVALID_LINE_OPERATION

#### 3.2 4 - es alkalmazás verzió

#### Módosultak az alábbi ERROR üzenetek:

- 14. INVALID_VAT_DATA
- 48. INVALID_LINE_VAT_AMOUNT_MISMATCH_VAT_RATE
- 49. INVALID_SUMMARY_VAT_AMOUNT_MISMATCH_VAT_RATE

Az alábbi RateType típusú elemekben elfogadottá vált a 0 érték megadása:

- vatPercentage
- vatContent
- vatAmountMismatch/vatRate

Módosult az alábbi WARN üzenet:

- 910. INCORRECT_SUMMARY_CALCULATION_VAT_CONTENT_SUMMARY_SIMPLIFIED

```
„Csak 0-nál nagyobb áfatartalomra fut le.” feltétel módosult az alábbira:
```
```
MODIFY és STORNO esetben csak akkor fut le, ha létezik a lineAmountsSimplified csomópont.
```
**3.25-ös alkalmazás verzió**

A requestID egyediségvizsgálatba az INVALID_REQUEST_SIGNATURE és FORBIDDEN hibakóddal
visszautasításra kerülő kérések azonosítói is beleszámítanak. Részletesen 1.3.1-es fejezet.

OPG számlák invoiceNumber képzésének pontosítása. Részletesen IV.4.2 fejezet.

**3.35-ös alkalmazás verzió**


```
A common.xsd-ben a UserHeaderType bővítésre került egy opcionális új elemmel:
```
- **predecessorTaxNumber**

A módosítás visszafelé kompatibilis, tehát azon kliensek, akik nem kívánják használni, azok számára
nem szükséges fejlesztést elvégezni. A common.xsd-hez tartozó namespace és verzió változatlan, az
invoiceData.xsd és invoiceApi.xsd-ben nem történt módosítás.

A headerben megadható új elem lehetővé teszi az adózó jogelődjeire vonatkozó műveletek
elvégzését.

A jogelődökre vonatkozó műveletek bevezetése miatt módosításra kerültek az alábbi validációk:

Újonnan bevezetésre kerülő blokkoló ERROR üzenetek:

- INVALID_PREDECESSOR_OPERATION
- SUPPLIER_NOT_IDENTICAL
- PREDECESSOR_REFERENCE_NOT_IDENTICAL

Újonnan bevezetésre kerülő WARN üzenet:

- INVALID_GROUP_MEMBER_TAX_NUMBER

Módosultak az alábbi ERROR üzenetek:

- INVALID_INVOICE_REFERENCE
- MODIFY_WITHOUT_MASTER_MISMATCH
- INVALID_ANNULMENT_REFERENCE
- SUPPLIER_TAX_NUMBER_MISMATCH
- ANNULMENT_IN_PROGRESS
- MODIFICATION_INDEX_NOT_UNIQUE
- INVOICE_LINE_ALREADY_EXIST

Módosultak az alábbi WARN üzenetek:

- INCONSISTENT_MODIFICATION_DATA_NETAMOUNT_NOT_ZERO_NORMAL
- INCONSISTENT_MODIFICATION_DATA_AMOUNT_NOT_ZERO_SIMPLIFIED
- INCONSISTENT_MODIFICATION_DATA_VATAMOUNT_NOT_ZERO
- INCONSISTENT_MODIFICATION_DATA_STORNO_ALREADY_EXISTS

Módosultak az alábbi INFO üzenetek:

- MODIFICATIONINDEX_SEQUENCE_INCOMPLETE

## 6 KÖRNYEZETEK ELÉRHETŐSÉGEI

Az Online Számla rendszer szolgáltatásai a következő környezetekben és címeken érhetők el.


### 6.1 FELHASZNÁLÓI TESZTKÖRNYEZET

Customer frontend: https://onlineszamla-test.nav.gov.hu
Számla bejelentő interfész: https://api-test.onlineszamla.nav.gov.hu

**URL-ek és erőforrások:**

https://api-test.onlineszamla.nav.gov.hu/invoiceService/v 3 /manageAnnulment
https://api-test.onlineszamla.nav.gov.hu/invoiceService/v 3 /manageInvoice
https://api-test.onlineszamla.nav.gov.hu/invoiceService/v 3 /queryInvoiceChainDigest
https://api-test.onlineszamla.nav.gov.hu/invoiceService/v 3 /queryInvoiceCheck
https://api-test.onlineszamla.nav.gov.hu/invoiceService/v 3 /queryInvoiceData
https://api-test.onlineszamla.nav.gov.hu/invoiceService/v 3 /queryInvoiceDigest
https://api-test.onlineszamla.nav.gov.hu/invoiceService/v 3 /queryTransactionList
https://api-test.onlineszamla.nav.gov.hu/invoiceService/v 3 /queryTransactionStatus
https://api-test.onlineszamla.nav.gov.hu/invoiceService/v 3 /queryTaxpayer
https://api-test.onlineszamla.nav.gov.hu/invoiceService/v 3 /tokenExchange

### 6.2 ÉLES KÖRNYEZET

Customer frontend: https://onlineszamla.nav.gov.hu
Számla bejelentő interfész: https://api.onlineszamla.nav.gov.hu

**URL-ek és erőforrások:**

https://api.onlineszamla.nav.gov.hu/invoiceService/v 3 /manageAnnulment
https://api.onlineszamla.nav.gov.hu/invoiceService/v 3 /manageInvoice
https://api.onlineszamla.nav.gov.hu/invoiceService/v 3 / queryInvoiceChainDigest
https://api.onlineszamla.nav.gov.hu/invoiceService/v 3 /queryInvoiceCheck
https://api.onlineszamla.nav.gov.hu/invoiceService/v 3 /queryInvoiceData
https://api.onlineszamla.nav.gov.hu/invoiceService/v 3 /queryInvoiceDigest
https://api.onlineszamla.nav.gov.hu/invoiceService/v 3 / queryTransactionList
https://api.onlineszamla.nav.gov.hu/invoiceService/v 3 /queryTransactionStatus
https://api.onlineszamla.nav.gov.hu/invoiceService/v 3 /queryTaxpayer
https://api.onlineszamla.nav.gov.hu/invoiceService/v 3 /tokenExchange

## 7 HELPDESK ÉS TECHNIKAI SEGÍTSÉGNYÚJTÁS

A fejezet a hibaelhárításhoz és további segítség igénybevételéhez nyújt támpontokat.

### 7.1 ÖNELLENŐRZÉS

Az egyes kódolások, hashelések helyességének ellenőrzéséhez, valamint az XML formátum általános
szintaxisának ellenőrzéséhez a következő weboldalakon található információ.

Aktuális UTC középidő: https://www.timeanddate.com/worldclock/timezone/utc


BASE64 online encode/decode: https://www.base64decode.org/

CRC számítás online: https://www.functions-online.com/crc32.html (az online konverterek jellemzően
hexadecimális értékben számolnak, ezek is használhatók, de ekkor az outputot felhasználás előtt át
kell váltani decimálisra)

SHA-512 online encode: [http://www.convertstring.com/Hash/SHA512](http://www.convertstring.com/Hash/SHA512)

SHA 3 - 512 online encode: https://emn178.github.io/online-tools/sha3_512.html

AES-128 ECB online decode: https://8gwifi.org/CipherFunctions.jsp (AES ECB PKCS5PADDING opciót
kell választani)

XML jól formázottság és séma konformitás ellenőrző online: https://www.xmlvalidation.com/

Regex ellenőrzés: https://regex101.com/

GZIP tömörítés előtti méret ellenőrzés: [http://www.txtwizard.net/compression](http://www.txtwizard.net/compression) vagy
https://www.multiutil.com/text-to-gzip-compress/

XML szintaxis információk: https://www.w3schools.com/xml/xml_syntax.asp

XML -séma információk: https://www.w3schools.com/xml/schema_intro.asp

### 7.2 HELPDESK ELÉRHETŐSÉG

Az Online Számla rendszerben felmerülő hibák megoldására és kérdések megválaszolására két
különálló helpdesk vehető igénybe. Minden éles rendszerrel kapcsolatos kérdéssel és problémával a
https://nav.gov.hu/ugyfeliranytu/keressen_minket/levelkuldes/e-ugyfsz funkción keresztül „Online
számlával kapcsolatos informatikai hibák bejelentése” tárggyal küldött megkereséssel lehet fordulni.
A levélküldő űrlap angol nyelven is elérhető.

Kizárólag a teszt rendszerre vonatkozó és ott is kizárólag a számlaadat-szolgáltatás interfész-
szolgáltatással kapcsolatos, fejlesztőknek szóló technikai segítségnyújtás az Online Számla rendszer
felületén e célra közzétett címre küldött e-mailen keresztül vehető igénybe.

Kérjük, hogy ha az interfész használatához kapcsolódóan technikai segítséget igényel, a
megkeresésben a teljes HTTP request (header és body) tartalmát és a beküldés pontos időpontját
tüntesse fel!

### 7.3 GITHUB ELÉRHETŐSÉG

Az Online Számla rendszerhez kötődően több publikus repository is elérhető GitHubon. Mindegyik
tárhelyre elmondható általánosan, hogy azok publikusan elérhetőek, a véleményezéshez és a
fejlesztéshez hozzájáruláshoz GitHub userre van szükség. A felhasználó ingyenesen, néhány perc alatt
létrehozható. Az Online Számla rendszerhez kapcsolódó repoitory-k az alábbiak.


#### 7.3.1 Common repository

A tárhely abból a célból jött létre, hogy az Online Számla rendszerben található atomi típusokat, üzleti
katalógus jellegű elemeket, valamint a generikus API kommunikációt megvalósító típusokat egy külön,
közös XSD-ben (common.xsd) lehessen verziókezelni. Ez lehetővé teszi azt, hogy ezeket a séma
elemeket több NAV-os projekt is felhasználhassa, ez által az API kommunikáció egységesíthető.

**A repository elérése:** https://github.com/nav-gov-hu/Common

#### 7.3.2 Online-Invoice repository

A tárhely az Online Számla rendszer számlabejelentő M2M interfészéhez kapcsolódó nyilvános, nem-
funkcionális kódokat (sémaleíró, példa XML-ek) és leírásokat tartalmazza jelenleg. A tárhely célja, hogy
a GitHub által nyújtott kollaborációs eszközök segítségével, a nemzetközi opensource fejlesztés
irányelveit követve a számlázóprogram fejlesztők és más érintettek a jövőben történő interfész verzió
változásokat véleményezhessék, követhessék, illetve észrevételeikkel, javaslataikkal
hozzájárulhassanak az interfész fejlesztéséhez. Ezen a platformon szintén lehetőség van a teszt
rendszerre vonatkozó, felhasználóknak és fejlesztőknek szóló technikai segítségnyújtás kérésére.

**A repository elérése:** https://github.com/nav-gov-hu/Online-Invoice

#### 7.3.3 Online-Invoice-Test-Tool repository

A tárhely az Online Számla rendszer számlaadat-szolgáltatás (beleértve többek között az összes API
végpontot) teszteléséhez használható grafikus ellenőrzőeszközt és a hozzá kapcsolódó
dokumentációkat tartalmazza.

**A repository elérése:** https://github.com/nav-gov-hu/Online-Invoice-Test-Tool

## 8 RENDSZERDIAGNOSZTIKA

Az Online Számla rendszer a 2.0-ás XML API verziójától kezdve szolgáltat olyan általános működési
metrikákat, amelyek publikusan bárki számára elérhetők. A metrikák a rendszer szolgáltatásainak
általános állapotát és működését reprezentálják. Jelen fejezetben található a metrikalekérdezéseket

kiszolgáló szolgáltatás technikai leírása, valamint a válaszban visszaadott üzenetstruktúra leírása.

### 8.1 A SZOLGÁLTATÁS TECHNIKAI LEÍRÁSA

Az /queryServiceMetrics egy RESTful típusú állapottalan (stateless) webszerviz. A szolgáltatás technikai
jellemzői a következők.

#### 8.1.1 Általános technikai adatok

A szolgáltatástól metrikát lekérdezni HTTP GET metódussal lehet a meghatározott végpontokon. A
metrika lekérdező végpont authentikáció nélküli, tehát sem adózói regisztráció, sem technikai
felhasználó, sem API szintű hitelesítés nem szükséges a szolgáltatás igénybevételhez.

A kérés helyességétől függően a szerver vagy üzleti XML választ, vagy csupán standard HTTP választ ad
vissza.

**Context root:**


/metricService/v 3

**XSD:**

serviceMetrics.xsd

Az XML -séma csak a válasz struktúráját tartalmazza, a kérésnek a GET metódus miatt nincs body része.

#### 8.1.2 Erőforrások................................................................................................................................

/queryServiceMetrics/metric
/queryServiceMetrics/list
/queryServiceMetrics/metric/{metricName}

#### 8.1.3 HTTP fejlécek

A kérésben a következő HTTP fejléc mezőket kötelező megadni:

content-type=application/xml
accept=application/xml

#### 8.1.4 HTTP válaszkódok

A szolgáltatás a hívónak helyes kérés esetén minden esetben HTTP 200-as választ ad vissza. Ettől eltérő
válaszkód csak a /queryServiceMetrics/metric/{metricName} kéréseknél fordulhat elő nem létező
{metricName} paraméter megadása esetén, mely esetben a rendszer HTTP 404 választ ad.

#### 8.1.5 Válaszidő, timeout

A szerver cacheből szolgálja ki a metrikalekérdezéseket, ezért a válaszidő jellemzően 200ms alatti lesz.
A kliens timeoutot csak abban az esetben tapasztalhat, ha a szolgáltatás leállt vagy a kérés nem jutott
el a szerverhez.

#### 8.1.6 Elérhetőségek

**8.1.6.1 Felhasználói tesztkörnyezet**
https://api-test.onlineszamla.nav.gov.hu/metricService/v 3 /queryServiceMetrics/metric
https://api-test.onlineszamla.nav.gov.hu/metricService/v 3 /queryServiceMetrics/list
https://api-test.onlineszamla.nav.gov.hu/metricService/v 3 /queryServiceMetric/metric/{metricName}

**8.1.6.2 Éles környezet**

https://api.onlineszamla.nav.gov.hu/metricService/v 3 /queryServiceMetrics/metric
https://api.onlineszamla.nav.gov.hu/metricService/v 3 /queryServiceMetrics/list
https://api.onlineszamla.nav.gov.hu/metricService/v 3 /queryServiceMetric/metric/{metricName}

### 8.2 A SZOLGÁLTATÁS ÉS AZ ÜZLETI METRIKÁK MŰKÖDÉSE

A szolgáltatás által biztosított működési metrikák névtér specifikusak. Ez azt jelenti, hogy a szolgáltatás
megnyitásának időpontjában az 1.x-es számlák feldolgozásáról nem lesz lekérdezhető metrika, csakis
a 2.0 verziótól kezdve.

A működési metrikák percenként automatikusan termelődnek szerver oldalon. A kliensek számára
javasolt lekérdezési intervallum fentiek miatt 1 perc. A metrikák lekérdezése az elmúlt 60 perces


```
intervallumra biztosított publikusan, melyeknek az értékeit a szolgáltatás szerver oldalon cacheli is. A
kiszolgálás szintén cacheből történik, ezért egy percnél sűrűbb tömeges lekérdezések esetén sem lesz
performancia vesztés.
```
```
Mivel a lekérdezésben nem vesz részt technikai felhasználó, ezért a kapcsolattartás nyelve sem ismert.
Így a válaszban a metrikák leírása minden támogatott nyelven lokalizálva, egyben kerül visszaadásra.
```
```
A metrikák adatai nem perzisztensek, bizonyos körülmények között előfordulhat, hogy a korábbi
metrika adatok törlődnek (például a teljes rendszer újraindításakor, egyes telepítések esetén), ez nem
hiba. Viszont ilyen esetben is a következő percben a metrika adatoknak újra kell termelődni.
```
#### 8.2.1 Metrikák típusai

```
A rendszer által szolgáltatott metrikák típusai a következők.
```
```
A representationType típusa Leírás
COUNTER Növekmény típusú metrika. Értéke az adott
időszeletre vetítve vagy konstansan 0 vagy növekvő.
GAUGE Pillanatkép típusú metrika. Értéke növekedhet és
csökkenhet is az előző időszelethez képest.
HISTOGRAM Kvantilis típusú, eloszlást mérő metrika. Az értéke
időben - az adott kvantilisre vonatkozóan –
növekedhet és csökkenhet is.
SUMMARY Összegző érték típusú metrika. Az értéke az adott
kvantilishez tartozó részösszeg és a summa érték.
Értéke időben növekedhet és csökkenthet is.
```
```
A publikus metrikák nem feltétlenül tartalmazzák az összes fent felsorolt típust.
```
#### 8.2.2 Metrikák leírása

```
A rendszer által szolgáltatott metrikák és azok üzleti tartalma a következő.
```
**metricName metricType Metrika leírása**
responseTimeAverageMsManageAnnulment GAUGE Az XML API azonos nevű végpontjának
responseTimeAverageMsManageInvoice válaszidejei milliszekundumban.^
responseTimeAverageMsQueryInvoiceChainDigest
responseTimeAverageMsQueryInvoiceCheck
responseTimeAverageMsQueryInvoiceData
responseTimeAverageMsQueryInvoiceDigest
responseTimeAverageMsQueryTransactionList
responseTimeAverageMsQueryTransationStatus
responseTimeAverageMsQueryTaxpayer
responseTimeAverageMsTokenExchange
processingTimeAverageMsInvoice Átlagos számla feldolgozási idő
milliszekundumban.

### 8.3 ÜZLETI OPERÁCIÓK

```
Jelen fejezetben a metrikalekérdező szolgáltatás interfész funkcionalitásait megvalósító /metricService
technikai leírása és az egyes operációkat és kérés-válasz struktúrákat leíró root elementek bemutatása
található.
```

#### 8.3.1 A /queryServiceMetrics operáció

A /queryServiceMetrics végpont egy publikusan, GET metódussal meghívható operáció. Célja a
rendszer általános, egy előre meghatározott időablakban (elmúlt 1 óra) lévő metrikáit visszaadni a
felhasználók számára.

**8.3.1.1 QueryServiceMetricsRequest**
A metrikalekérdező operációt három módon lehet GET metódussal meghívni, az alábbiak szerint:

- /metricService/v3/queryServiceMetrics/metric: visszaadásra kerül az összes elérhető metrika,
    értékekkel együtt

#### - /metricService/v 3 /queryServiceMetrics/list: visszaadásra kerül az összes elérhető metrika

#### neve és leírása, érték nélkül

- /metricService/v 3 /queryServiceMetrics/metric/{metricName}: visszaadásra kerül a
    metricName paraméterben megadott metrika neve, leírása és értékei.

**Leírás és kapcsolódó követelmények**

```
1) A /queryServiceMetrics/metric/{metricName} kéréseknél nem létező {metricName}
paraméter megadása esetén a rendszer standard HTTP 404 választ ad vissza. A szolgáltatáshoz
nem tartozik a „ Hibakezelés” fejezetben definiált külön üzleti hibakód.
```
**8.3.1.2 QueryServiceMetricsResponse**

A /queryServiceMetrics operáció válaszának struktúráját a QueryServiceMetricsResponse element
tartalmazza. Egy metrikához mindig az elmúlt egy óra adatai kerülnek visszaadásra, percenkénti
felbontásban.


## 84. ábra A QueryServiceMetricsResponse felépítése

A típus a BasicResultType-ot terjeszti ki, így az abban foglalt elemeken kívül a metrikák adatainak utolsó
frissítési időpontját, valamint az összes elérhető metrika adatait tartalmazza, értékekkel együtt.

```
Tag Típus Kötelező Tartalma
metricsLastUpdateTime xs:dateTime Nem A metrikák
adatainak
utolsó frissítési
időpontja
metric/metricDefinition/metricName xs:dateTime Igen A metrika neve
metric/metricDefinition/metricType xs:string Igen A metrika
típusa
metric/metricDefinition/metricDescription/language xs:string Igen A metrika
leírásának
nyelve
metric/metricDefinition/metricDescription/localizedDescription xs:string Igen A metrika
leírása
metric/metricValues/value xs:decimal Igen A metrika
értéke
metric/metricValues/timestamp xs:dateTime Igen A metrika
értékhez
tartozó
időbélyeg
```

**Facetek és leírók**

```
Tag SimpleType Pattern Enum Defa
ult
metricsLastUpdateTime InvoiceTimestampTy
pe
```
```
\d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.
\d{1,3})?Z minInclusive
= 2010 - 01 - 01T00:00:00Z
```
##### - -

```
metric/metricDefinition/metricName SimpleText200NotBl
ankType
```
```
.*[^\s].* - -
```
```
metric/metricDefinition/metricType MetricTypeType - COUNTE
R
GAUGE
HISTOGR
AM
SUMMA
RY
```
##### -

```
metric/metricDefinition/metricDescri
ption/language
```
```
LanguageType - HU
EN
DE
```
##### -

```
metric/metricDefinition
/metricDescription/localizedDescripti
on
```
```
SimpleText 512 NotBl
ankType
```
```
.*[^\s].* - -
```
```
metric/metricValues/value GenericDecimalType .*[^\s].* - -
metric/metricValues/timestamp InvoiceTimestampTy
pe
```
```
\d{4}-\d{2}-
\d{2}T\d{2}:\d{2}:\d{2}(.
\d{1,3})?Z minInclusive
= 2010 - 01 - 01T00:00:00Z
```
##### - -

A /queryServiceMetrics/list operáció válaszának struktúráját a QueryServiceMetricsListResponse
element tartalmazza.

## 85. ábra A QueryServiceMetricsListResponse felépítése


A típus az metrikák nevét és leírását tartalmazza listaként.

```
Tag Típus Kötelező Tartalma
metricDefinition/metricName xs:dateTime Igen A metrika neve
metricDefinition/metricType xs:string Igen A metrika típusa
metricDefinition/metricDescripiton/language xs:string Igen A metrika leírásának
nyelve
metricDefinition/metricDescripiton/localizedDescription xs:string Igen A metrika leírása
```
**Facetek és leírók**

```
Tag SimpleType Patter
n
```
```
Enum Defau
lt
metricDefinition/metricName SimpleText200NotBlank
Type
```
```
.*[^\s].
*
```
##### - -

```
metricDefinition/metricType MetricTypeType - COUNTER
GAUGE
HISTOGRA
M
SUMMAR
Y
```
##### -

```
metricDefinition/metricDescription/language LanguageType - HU
EN
DE
```
##### -

```
metricDefinition/metricDescription/localizedDes
cription
```
```
SimpleText 512 NotBlank
Type
```
```
.*[^\s].
*
```
##### - -

## 9 MELLÉKLETEK

```
I. Az Online Számla Rendszer által küldött figyelmeztető üzenetek
II. Az Online Számla Rendszer adatszótára
```

## I. AZ ONLINE SZÁMLA RENDSZER ÁLTAL KÜLDÖTT FIGYELMEZTETŐ ÜZENETEK

```
Az alábbi jegyzék az Online Számla rendszer 3. 11 - es verziójának figyelmeztetéseit tartalmazza.
Naprakész információk az Online Számla portál kezdőlapján jelennek meg.
```
### I.1 A SZÁMLA FEJLÉC ADATAIVAL KAPCSOLATOS FIGYELMEZTETÉSEK

```
Azonosító: 10.
Figyelmeztetés csoport: SUPPLIER_CUSTOMER_MATCH
az eladó és vevő adataiban azonosság található
Figyelmeztetés kód: SUPPLIER_CUSTOMER_MATCH_TAXPAYER
Figyelmeztetés szövege: Eladó és vevő adószáma nem lehet azonos.
Működés: Figyelmeztet, ha az eladó és a vevő adószám első nyolc számjegye azonos.
Csak akkor fut le, ha mindkét adat létezik.
```
```
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierTaxNumber/taxpayerId
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatData/customerTaxNumber/taxpayerId
Találat esetén hibásként
megjelölt elem:
```
```
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/supplierTaxNumber/
taxpayerId
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 11.
Figyelmeztetés csoport:** SUPPLIER_CUSTOMER_MATCH
az eladó és vevő adataiban azonosság található
**Figyelmeztetés kód: SUPPLIER_CUSTOMER_MATCH_NAME
Figyelmeztetés szövege: Eladó és vevő neve nem lehet azonos.
Működés:** Figyelmeztet, ha az eladó és a vevő neve azonos.
Csak akkor fut le, ha a vevő nem belföldi adóalany és nem magánszemély
(CustomerVatStatusType = OTHER)

InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/supplierName
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerName
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/supplierName
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -

**Megjegyzés:** 3.17 verzióban kivezetésre került.

**Azonosító: 20.
Figyelmeztetés csoport:** SUPPLIER_CUSTOMER_MATCH
az eladó és vevő adataiban azonosság található
**Figyelmeztetés kód: SUPPLIER_CUSTOMER_MATCH_BANKACCOUNT
Figyelmeztetés szövege: Eladó és vevő bankszámlaszáma nem lehet azonos.
Működés:** Figyelmeztet, ha a vevő és az eladó bankszámlaszáma azonos.
Csak akkor fut le, ha mindkét adat létezik.
Csak akkor fut le, ha a vevő nem belföldi adóalany és nem magánszemély
(CustomerVatStatusType = OTHER)

InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierBankAccountNumber
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerBankAccountNumber
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerBankAccountNumber
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE**^ +^ +^ +^ -^


**Azonosító: 30.
Figyelmeztetés csoport:** SUPPLIER_FISCAL_MATCH
az eladó és a pénzügyi képviselő adataiban azonosság található
**Figyelmeztetés kód: SUPPLIER_FISCAL_MATCH_TAXPAYER
Figyelmeztetés szövege: Eladó és pénzügyi képviselő adószáma nem lehet azonos.
Működés:** Figyelmeztet, ha az eladó és a pénzügyi képviselő adószámának első nyolc
számjegye azonos.

InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierTaxNumber/taxpayerId
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeTaxNumber/taxpayerId
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierTaxNumber/taxpayerId
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE^ +^ +^ +^ -^

**Azonosító: 40.
Figyelmeztetés csoport:** SUPPLIER_FISCAL_MATCH
az eladó és a pénzügyi képviselő adataiban azonosság található
**Figyelmeztetés kód: SUPPLIER_FISCAL_MATCH_NAME
Figyelmeztetés szövege: Eladó és a pénzügyi képviselő neve nem lehet azonos.
Működés:** Figyelmeztet, ha az eladó és a pénzügyi képviselő neve azonos.
Csak akkor fut le, ha mindkét elem kitöltött.

InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/supplierName
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeName
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeName
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE**^ +^ +^ +^ -^


**Azonosító: 530.
Figyelmeztetés csoport:** INCORRECT_HEAD_DATA
helytelen számlafejadat
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_FISCALREPRESENTATIVE
Figyelmeztetés szövege: Pénzügyi képviselő adat csak akkor lehet kitöltve, ha az eladó adószámának
megyekódja „51”.
Működés:** Figyelmeztet, ha a pénzügyi képviselő adatai ki vannak töltve, de az eladó
megyekódja szerepel és nem egyenlő „51”.
Csak akkor fut le, ha mindkét elem kitöltött.

InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierTaxNumber/countyCode
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeTaxNumber/taxpayerId
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierTaxNumber/countyCode
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -
**Azonosító: 50.
Figyelmeztetés csoport:** INCORRECT_VAT_CODE
helytelen áfakód
**Figyelmeztetés kód: INCORRECT_VAT_CODE_SUPPLIER
Figyelmeztetés szövege: Érvénytelen áfakód. Eladó áfakódja nem lehet 4-es.
Működés:** Figyelmeztet, ha az eladó áfakódja érvénytelen. (értékkészlet: 1, 2, 3, 5)
Csak akkor fut le, ha az elem kitöltött.
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierTaxNumber/vatCode
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierTaxNumber/vatCode
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 60.
Figyelmeztetés csoport:** INCORRECT_VAT_CODE
helytelen áfakód
**Figyelmeztetés kód: INCORRECT_VAT_CODE_SUPPLIER_GROUPMEMBER_MISSING
Figyelmeztetés szövege: Az áfacsoporttag eladó adószáma nincs kitöltve.
Működés:** Figyelmeztet, ha az eladó áfacsoport tagja és a csoporttag adószáma nincs
megadva.
Csak akkor fut le, ha az eladó áfakódja = 5.

InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierTaxNumber/vatCode
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
groupMemberTaxNumber
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
groupMemberTaxNumber/vatCode
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierTaxNumber/vatCode
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -

**Azonosító: 71.
Figyelmeztetés csoport:** INCORRECT_HEAD_DATA
helytelen számlafej adat
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_SUPPLIER_GROUPMEMBER_TAXPAYERID
Figyelmeztetés szövege: Hibás adószám. Eladóként áfa csoporttag adószáma lett megadva.
Működés:** Figyelmeztet, ha a számlán eladóként megadott adóalany törzsszáma áfa csoport
tagja. Ilyen esetben az áfa csoport adószámának megadása szükséges.
A megadott adat adószám listába kérdez be.

InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierTaxNumber/taxpayerId
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierTaxNumber/taxpayerId
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 81.
Figyelmeztetés csoport:** INCORRECT_HEAD_DATA
helytelen számlafej adat
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_CUSTOMER_TAXPAYERID
Figyelmeztetés szövege: Hibás adószám. A vevő adószáma nem élő.
Működés:** Figyelmeztet, ha a számlán vevőként megadott adóalany törzsszáma létezik, de
státusza nem „élő”.
Csak akkor fut, ha customerVatData kitöltött.

InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatData/customerTaxNumber/taxpayerId
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatData/customerTaxNumber/taxpayerId
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 82.
Figyelmeztetés csoport:** INCORRECT_HEAD_DATA
helytelen számlafej adat
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_CUSTOMER_GROUPMEMBER_TAXNUMBER
Figyelmeztetés szövege: Hibás adószám. A vevő ÁFA csoporttagként megadott adószáma csoporthoz
tartozik.
Működés:** Figyelmeztet, ha a számlán vevőként megadott adóalany ÁFA csoporttagi
adószáma valójában ÁFA csoportazonosító (177-tel kezdődik).

```
Csak akkor fut, ha customerVatData kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatData /groupMemberTaxNumber
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerVatData/
groupMemberTaxNumber
```
**Hatókör:** (^) **operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -

**Megjegyzés:** (^) **Ez a figyelmeztetés várhatóan ERROR esetté válik.**


**Azonosító: 85.
Figyelmeztetés csoport:** INCORRECT_HEAD_DATA
helytelen számlafejadat
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_CUSTOMER_COMMUNITY_VAT_NUMBER
Figyelmeztetés szövege: Vevő közösségi adószáma hibás.
Működés:** Figyelmeztet, ha az első két karakter nem szerepel a meglévő értékkészletben
(értékkészlet: AT, BE, BG, CY, CZ, DE, DK, EE, EL, ES, FI, FR, GB, HR, IE, IT, LT, LU, LV,
MT, NL, PL, PT, RO, SE, SI, SK), vagy az adószám CDV hibás.

```
Csak akkor fut le, ha a közösségi adószám kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerVatData/
communityVatNumber
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerVatData/
communityVatNumber
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -
**Megjegyzés:** (^) 3.5 verzióban kivezetésre került.
**Azonosító: 91.
Figyelmeztetés csoport:** INCORRECT_HEAD_DATA
helytelen számlafejadat
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_CUSTOMER_GROUPMEMBER_TAXPAYERID
Figyelmeztetés szövege: Hibás adószám. Vevőként áfacsoporttag adószáma lett megadva.
Működés:** Figyelmeztet, ha a számlán vevőként megadott adóalany törzsszáma áfacsoport
tagja. Ilyen esetben az áfacsoport adószámának megadása szükséges.
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerVatData/
customerTaxNumber/taxpayerId
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerVatData/
customerTaxNumber/taxpayerId
**Hatókör:
operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -


**Azonosító: 100.
Figyelmeztetés csoport:** INCORRECT_VAT_CODE
helytelen áfakód
**Figyelmeztetés kód: INCORRECT_VAT_CODE_FISCALREPRESENTATIVE
Figyelmeztetés szövege: Érvénytelen áfakód. Pénzügyi képviselő áfakódja 1, 2, vagy 4 lehet.
Működés:** Figyelmeztet, ha a pénzügyi képviselő áfakódja érvénytelen. (értékkészlet: 1, 2,
4)
Csak akkor fut le, ha az elem kitöltött.

InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeTaxNumber/vatCode
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeTaxNumber/vatCode
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -


**Azonosító: 112.**

**Figyelmeztetés csoport:** INCORRECT_HEAD_DATA

```
helytelen számlafej adat
```
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_CASH_ACCOUNTING_INDICATOR**

**Figyelmeztetés szövege: Hibás pénzforgalmi elszámolás jelölés**

**Működés:** Figyelmeztet, ha az adatszolgáltatásban pénzforgalmi elszámolás jelölése szerepel
(cashAccountingIndicator=true), de a NAV által nyilvántartott törzsadatokban
nem szerepel a pénzforgalmi elszámolás.

```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/
cashAccountingIndicator
```
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/
cashAccountingIndicator
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -
**Megjegyzés:** (^) Inaktív.


**Azonosító: 113.
Figyelmeztetés csoport:** INCORRECT_VAT_CODE
helytelen áfakód
**Figyelmeztetés kód: INVALID_GROUP_MEMBER_TAX_NUMBER
Figyelmeztetés szövege: Áfacsoportból kivált tag számlaadat-szolgáltatás pótlása esetén a csoporttagi
adószám csak a sajátja lehet.
Működés:** Figyelmeztet, ha egy áfacsoportból kivált adózó olyan számlaadat-szolgáltatás
pótlást küld be, amelyen az áfacsoport az eladó és nem a beküldő került
megadásra a tagi adószám(groupMemberTaxNumber) mezőben.

```
InvoiceData/invoiceMain/invoice/invoiceHead/
supplierInfo/groupMemberTaxNumber/base:taxpayerId
```
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/
supplierInfo/groupMemberTaxNumber/base:taxpayerId
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 120.
Figyelmeztetés csoport:** INCORRECT_COUNTY_CODE
helytelen megyekód
**Figyelmeztetés kód: INCORRECT_COUNTY_CODE_SUPPLIER
Figyelmeztetés szövege: Érvénytelen megyekód (eladó).
Működés:** Figyelmeztet, ha az eladó adószám utolsó két számjegye (megyekód)
érvénytelen. (értéklista: 02-20; 22-44; 51)
Csak akkor fut le, ha az elem kitöltött.

InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierTaxNumber/countyCode
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierTaxNumber/countyCode
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -

**Azonosító: 130.
Figyelmeztetés csoport:** INCORRECT_COUNTY_CODE
helytelen megyekód
**Figyelmeztetés kód: INCORRECT_COUNTY_CODE_SUPPLIER_GROUPMEMBER
Figyelmeztetés szövege: Érvénytelen csoporttag megyekód (eladó).
Működés:** Figyelmeztet, ha az eladó csoporttag adószámának utolsó két számjegye
(megyekód) érvénytelen. (értéklista: 02-20; 22-44; 51)
Csak akkor fut le, ha az elem kitöltött.

InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
groupMemberTaxNumber/countyCode
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
groupMemberTaxNumber/countyCode
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -


**Azonosító: 140.
Figyelmeztetés csoport:** INCORRECT_COUNTY_CODE
helytelen megyekód
**Figyelmeztetés kód: INCORRECT_COUNTY_CODE_CUSTOMER
Figyelmeztetés szövege: Érvénytelen megyekód (vevő).
Működés:** Figyelmeztet, ha az vevő adószám utolsó két számjegye (megyekód) érvénytelen.
(értéklista: 02-20; 22-44; 51)
Csak akkor fut le, ha az elem kitöltött.

InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatData/customerTaxNumber/countyCode
**Találat esetén
hibásként megjelölt
elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatData/customerTaxNumber/countyCode
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -

**Azonosító: 150.
Figyelmeztetés csoport:** INCORRECT_COUNTY_CODE
helytelen megyekód
**Figyelmeztetés kód: INCORRECT_COUNTY_CODE_CUSTOMER_GROUPMEMBER
Figyelmeztetés szövege: Érvénytelen csoporttag megyekód (vevő).
Működés:** Figyelmeztet, ha a vevő csoporttag adószámának utolsó két számjegye (megyekód)
érvénytelen. (értéklista: 02-20; 22-44; 51)
Csak akkor fut le, ha az elem kitöltött.

InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerVatData/
customerTaxNumber/groupMemberTaxNumber/countyCode
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/ customerVatData/
customerTaxNumber/groupMemberTaxNumber/countyCode
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -


**Azonosító: 160.
Figyelmeztetés csoport:** INCORRECT_COUNTY_CODE
helytelen megyekód
**Figyelmeztetés kód: INCORRECT_COUNTY_CODE_FISCALREPRESENTATIVE
Figyelmeztetés szövege: Érvénytelen megyekód (pénzügyi képviselő).
Működés:** Figyelmeztet, ha a pénzügyi képviselő adószám utolsó két számjegye
(megyekód) érvénytelen. (értéklista: 02-20; 22-44; 51)
Csak akkor fut le, ha az elem kitöltött.

InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeTaxNumber/countyCode
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeTaxNumber/countyCode
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -


**Azonosító: 161.
Figyelmeztetés csoport:** INCORRECT_CITY_ZIP_CODE
helytelen irányítószám és településnév pár
**Figyelmeztetés kód: INCORRECT_CITY_ZIP_CODE_FISCAL_REPRESENTATIVE
Figyelmeztetés szövege: Hibás címadat, irányítószám és helységnév nem kapcsolódik egymáshoz
(pénzügyi képviselő).
Működés:** Figyelmeztet, ha a pénzügyi képviselő címében az irányítószáma és a helységnév
nincs összhangban. Egyszerű és részletes cím esetén is.

```
Csak akkor fut, ha pénzügyi képviselő elemek kitöltöttek.
```
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeAddress/simpleAddress/postalCode
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeAddress/simpleAddress/city
vagy
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeAddress/detailedAddress/postalCode
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeAddress/detailedAddress/city
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeAddress/simpleAddress/postalCode
vagy
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeAddress/detailedAddress/postalCode
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -

**Megjegyzés:** (^) Inaktív.


**Azonosító: 180.
Figyelmeztetés csoport:** INCORRECT_COUNTRY_CODE
helytelen országkód
**Figyelmeztetés kód: INCORRECT_COUNTRY_CODE_SUPPLIERADDRESS
Figyelmeztetés szövege: Érvénytelen országkód (eladó).
Működés:** Figyelmeztet, ha az eladó országkódja hibás (a kód nem szerepel a vonatkozó
szabványban). Egyszerű és részletes cím megadása esetén is.

InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/supplierAddress
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/supplierAddress/
simpleAddress/countryCode
vagy
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/supplierAddress/
detailedAddress/countryCode
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE^ +^ +^ +^ -^

**Megjegyzés:** (^) Inaktív.
**Azonosító: 190.
Figyelmeztetés csoport:** INCORRECT_COUNTRY_CODE
helytelen országkód
**Figyelmeztetés kód: INCORRECT_COUNTRY_CODE_CUSTOMERADDRESS
Figyelmeztetés szövege: Érvénytelen országkód (vevő).
Működés:** Figyelmeztet, ha a vevő országkódja hibás (a kód nem szerepel a vonatkozó
szabványban). Egyszerű és részletes cím megadása esetén is.
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerAddress
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerAddress
/simpleAddress/countryCode
vagy
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerAddress/detailedAddress/countryCode
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -

**Megjegyzés:** (^) Inaktív.


**Azonosító: 200.
Figyelmeztetés csoport:** INCORRECT_COUNTRY_CODE
helytelen országkód
**Figyelmeztetés kód: INCORRECT_COUNTRY_CODE_FISCALREPRESENTATIVEADDRESS
Figyelmeztetés szövege: Érvénytelen országkód (pénzügyi képviselő).
Működés:** Figyelmeztet, ha a pénzügyi képviselő országkódja nem „HU”.

```
Csak akkor fut le, ha pénzügyi képviselő adatai kitöltöttek.
```
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeAddress
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeAddress/simpleAddress/countryCode
vagy
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeAddress/detailedAddress/countryCode
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 210.
Figyelmeztetés csoport:** INCORRECT_CITY_ZIP_CODE
helytelen irányítószám és településnév pár
**Figyelmeztetés kód: INCORRECT_CITY_ZIP_CODE_SUPPLIER
Figyelmeztetés szövege: Hibás címadat, irányítószám és helységnév nem kapcsolódik egymáshoz
(eladó).
Működés:** Figyelmeztet, ha az eladó címe magyarországi, továbbá irányítószáma és
helységneve nincs összhangban.

InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/supplierAddress
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/supplierAddress/
simpleAddress/city
vagy
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/supplierAddress/
detailedAddress/city
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -
**Megjegyzés:** (^) Inaktív.


**Azonosító: 220.
Figyelmeztetés csoport:** INCORRECT_CITY_ZIP_CODE
helytelen irányítószám és településnév pár
**Figyelmeztetés kód: INCORRECT_CITY_ZIP_CODE_CUSTOMER
Figyelmeztetés szövege: Hibás címadat, irányítószám és helységnév nem kapcsolódik egymáshoz
(vevő).
Működés:** Figyelmeztet, ha a vevő címe magyarországi, továbbá irányítószáma és
helységneve nincs összhangban.

InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerAddress
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerAddress
/simpleAddress/city
vagy
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerAddress/detailedAddress/city
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -
**Megjegyzés:** (^) Inaktív.


**Azonosító: 500.
Figyelmeztetés csoport:** INCORRECT_HEAD_DATA
helytelen számlafejadat
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_SUPPLIER_COMMUNITY_VAT_NUMBER
Figyelmeztetés szövege: Hibás közösségi adószám. Az eladó adószámának első nyolc karaktere nem
egyezik meg közösségi adószámának utolsó 8 karakterével.
Működés:** Figyelmeztet, ha az eladó adószámának első nyolc karaktere nem egyezik meg
közösségi adószámának utolsó 8 karakterével.

```
Csak akkor fut, ha a közösségi adószám kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierTaxNumber/taxpayerId
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
communityVatNumber
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
communityVatNumber
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE**^ +^ +^ +^ -^

**Azonosító: 310.
Figyelmeztetés csoport:** INCORRECT_DATE
helytelen dátumadat
**Figyelmeztetés kód: INCORRECT_DATE_INVOICE_ISSUE_DATE_LATE
Figyelmeztetés szövege: Számla kelte jövőbeli dátum.
Működés:** Figyelmeztet, ha a számla kelte olyan jövőbeli dátum, ami későbbi, mint az
adatszolgáltatás dátuma.

```
Tolerált eltérés: 5 naptári nap.
```
InvoiceData/invoiceIssueDate
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceIssueDate
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 312.
Figyelmeztetés csoport:** INCORRECT_DATE
helytelen dátumadat
**Figyelmeztetés kód: INCORRECT_DATE_INVOICE_DELIVERY_DATE_EARLY
Figyelmeztetés szövege: Teljesítési dátum elévült időszakra esik.
Működés:** Figyelmeztet, ha a számla teljesítés dátuma korábbi, mint az adatszolgáltatás
előtti hatodik év első napja.

InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/
invoiceDeliveryDate
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/
invoiceDeliveryDate
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -

**Azonosító: 313.
Figyelmeztetés csoport:** INCORRECT_DATE
helytelen dátumadat
**Figyelmeztetés kód: INCORRECT_DATE_INVOICE_DELIVERY_DATE_LATE
Figyelmeztetés szövege: Teljesítés dátuma túl távoli. Kiállítás és teljesítés között legalább 13 hónap az
eltérés.
Működés:** Figyelmeztet, ha a számla teljesítés dátuma legalább 397 nappal (egy év + egy
hónap) későbbi, mint a számla kelte.

InvoiceData/invoiceIssueDate
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/
invoiceDeliveryDate
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/
invoiceDeliveryDate
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -

**Megjegyzés:** (^) ERROR szintre emelve.


**Azonosító: 320.
Figyelmeztetés csoport:** INCORRECT_DATE
helytelen dátumadat
**Figyelmeztetés kód: INCORRECT_DATE_AGGREGATE_INVOICE_ISSUE_DATE
Figyelmeztetés szövege: Gyűjtőszámla kelte korábbi, mint az egyes tételsorok teljesítési dátuma közül
a legnagyobb.
Működés:** Figyelmeztet, ha a gyűjtőszámla kelte korábbi, mint az egyes teljesítések
dátuma közül a legnagyobb.

InvoiceData/invoiceIssueDate
InvoiceData/invoiceMain/invoice/invoiceLines/line/aggregateInvoiceLineData/
lineDeliveryDate
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceIssueDate
```
**Hatókör:** (^)
**operation/
invoiceCateg
ory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED - - - -

##### AGGREGATE^ +^ +^ -^ -^


**Azonosító: 321.
Figyelmeztetés csoport:** INCORRECT_DATE
helytelen dátumadat
**Figyelmeztetés kód: INCORRECT_DATE_AGGREGATE_INVOICE_DELIVERY_DATE
Figyelmeztetés szövege: Gyűjtőszámla teljesítési dátumaként szereplő dátum nem azonos a
tételsoroknál megjelölt teljesítési dátumok közül a legkésőbbivel.
Működés:** Figyelmeztet, ha a gyűjtőszámlán megjelölt technikai teljesítés dátum nem
azonos a tételsoroknál megjelölt teljesítés dátumok közül a legkésőbbivel.
(A gyűjtőszámla esetén a teljesítési dátum technikai jellegű, mert a teljesítések
tényleges dátuma a tételsorokban szerepel.)

InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/
invoiceDeliveryDate
InvoiceData/invoiceMain/invoice/invoiceLines/line/aggregateInvoiceLineData/
lineDeliveryDate
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/
invoiceDeliveryDate
**Hatókör:
operation/
invoiceCateg
ory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED - - - -

##### AGGREGATE + - - -


**Azonosító: 330.
Figyelmeztetés csoport:** INCORRECT_DATE
helytelen dátumadat
**Figyelmeztetés kód: INCORRECT_DATE_INVOICE_DELIVERY_TO_FROM
Figyelmeztetés szövege: A teljesítési időszak záró dátuma korábbi, mint a nyitó dátuma.
Működés:** Figyelmeztet, ha időszakra vonatkozó számla esetén annak utolsó napja
korábbi, mint a kezdő napja.

```
Csak akkor fut le, ha mindkét adat kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/
invoiceDeliveryPeriodStart
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/
invoiceDeliveryPeriodEnd
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/
invoiceDeliveryPeriodEnd
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE**^ +^ +^ +^ -^
**Azonosító: 340.
Figyelmeztetés csoport:** INCORRECT_DATE
helytelen dátumadat
**Figyelmeztetés kód: INCORRECT_DATE_INVOICE_MODIFICATION_ISSUE_DATE_LATE
Figyelmeztetés szövege: A módosító okirat kelte jövőbeli dátum.
Működés:** Figyelmeztet, ha a módosító okirat kelte jövőbeni dátum.
Tolerált eltérés: 5 nap.
InvoiceData/invoiceIssueDate
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceIssueDate
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - + + -

##### SIMPLIFIED - + + -

##### AGGREGATE^ -^ +^ +^ -^


**Azonosító: 341.
Figyelmeztetés csoport:** INCORRECT_DATE
helytelen dátumadat
**Figyelmeztetés kód: INCORRECT_DATE_INVOICE_MODIFICATION_ISSUE_DATE_EARLY
Figyelmeztetés szövege: A módosító okirat kelte túl korai.
Működés:** Figyelmeztet, ha a módosító okirat kelte legalább 15 nappal korábbi, mint az
adatszolgáltatás napja.

InvoiceData/invoiceIssueDate
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceIssueDate
```
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - + + -
**SIMPLIFIED** - + + -
**AGGREGATE**^ -^ +^ +^ -^

**Azonosító: 342.
Figyelmeztetés csoport:** INCORRECT_DATE
helytelen dátumadat
**Figyelmeztetés kód: INCORRECT_DATE_MODIFICATION_ISSUE_DATE_EARLY
Figyelmeztetés szövege: A módosító okirat kelte korábbi, mint az eredeti okirat kelte.
Működés:** Figyelmeztet, ha a módosító okirat az eredeti okirat dátumát megelőzi.
InvoiceData/invoiceIssueDate korábbi, mint az
InvoiceData/invoiceMain/invoice/invoiceReference/originalInvoiceNumber
alapján az adatbázisban szereplő ezen elem: InvoiceData/invoiceIssueDate
értéke
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceIssueDate
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - + + -

##### SIMPLIFIED - + + -

##### AGGREGATE^ -^ +^ +^ -^


**Azonosító: 510.
Figyelmeztetés csoport:** INCORRECT_HEAD_DATA
helytelen számlafejadat
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_CUSTOMER_TAX_NUMBER
Figyelmeztetés szövege: Vevő adószáma nem létezik.
Működés:** Figyelmeztet, ha a vevő adószámának első nyolc karaktere nem szerepel a
nyilvántartásban.

InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatData/customerTaxNumber/taxpayerId
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatData/customerTaxNumber/taxpayerId
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE^ +^ +^ +^ -^

**Azonosító: 540.
Figyelmeztetés csoport:** INCORRECT_HEAD_DATA
helytelen számlafejadat
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_FISCAL_REPRESENTATIVE_TAX_NUMBER
Figyelmeztetés szövege: Nem létező adószám (pénzügyi képviselő).
Működés:** Figyelmeztet, ha a pénzügyi képviselő adószámának első nyolc karaktere nem
szerepel a nyilvántartásban.

InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeTaxNumber/taxpayerId
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/fiscalRepresentativeInfo/
fiscalRepresentativeTaxNumber/taxpayerId
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE^ +^ +^ +^ -^


**Azonosító: 560.
Figyelmeztetés csoport:** INCORRECT_HEAD_DATA
helytelen számlafejadat
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_MOD_REF_INVOICE_NUMBER
Figyelmeztetés szövege: Módosító okirat sorszáma megegyezik az eredeti számláéval.
Működés:** Figyelmeztet, ha a módosító okirat sorszáma megegyezik az eredeti számla
sorszámával.
Csak akkor fut le, ha utilitySettlementIndicator<>true.

InvoiceData/invoiceMain/invoice/invoiceReference/originalInvoiceNumber
InvoiceData/invoiceNumber
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceNumber
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - + + -

##### SIMPLIFIED - + + -

##### AGGREGATE - + + -

**Azonosító: 561.
Figyelmeztetés csoport:** INCORRECT_HEAD_DATA
helytelen számlafejadat
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_PERIODICAL_SETTLEMENT
Figyelmeztetés szövege: A periodicalSettlement értéke nem lehet „false”, ha az időszakra vonatkozó
számla első és/vagy utolsó napja kitöltött.
Működés:** Figyelmeztet, ha időszakos elszámolás kezdő és/vagy záró dátumának
kitöltöttsége esetén a periodicalSettlement elem nem „true”.

```
Csak akkor fut le, ha legalább az egyik dátum kitöltött.
```
invoiceMain/invoice/invoiceHead/invoiceDetail/periodicalSettlement
invoiceMain/invoice/invoiceHead/invoiceDetail/invoiceDeliveryPeriodStart
invoiceMain/invoice/invoiceHead/invoiceDetail/invoiceDeliveryPeriodEnd
**Találat esetén hibásként
megjelölt elem:**

```
invoiceMain/invoice/invoiceHead/invoiceDetail/periodicalSettlement
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 1150.
Figyelmeztetés csoport:** INCONSISTENT_MODIFICATION_DATA
Inkonzisztens számlamódosítás adatok
**Figyelmeztetés kód: INCONSISTENT_MODIFICATION_DATA_MODIFICATIONINDEX_UNREAL
Figyelmeztetés szövege: Számla módosítás sorszáma irreális
Működés:** Figyelmeztet, ha módosító vagy sztornó számlaként beküldött számla (API
invoiceOperation=MODIFY vagy invoiceOperation=STORNO) esetén a
módosítás sorszáma irreálisan nagy (modificationIndex > 1000).

```
Csak akkor fut le, ha az adatszolgáltatás beküldésekor az API
invoiceOperation=MODIFY vagy invoiceOperation=STORNO.
```
InvoiceData/invoiceMain/invoice/invoiceReference/modificationIndex
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceReference/modificationIndex
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - + + -
**SIMPLIFIED** - + + -
**AGGREGATE** - + + -
**Azonosító: 1300.
Figyelmeztetés csoport:** INCORRECT_HEAD_DATA
helytelen számlafej adat
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_CURRENCY_CODE_HUF
Figyelmeztetés szövege: Eltérés a pénznem (HUF) és a megadott árfolyam között.
Működés:** Figyelmeztet, ha a pénznem HUF, de az árfolyam nem 1.
Csak akkor fut le, ha mindkét elem kitöltött.
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/currencyCode
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL + + + -
SIMPLIFIED + + + -
AGGREGATE + + + -**


**Azonosító: 1301.
Figyelmeztetés csoport:** INCORRECT_HEAD_DATA
helytelen számlafej adat
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_EXCHANGE_RATE_1
Figyelmeztetés szövege: Eltérés a megadott árfolyam és a pénznem (HUF) között.
Működés:** Figyelmeztet, ha az árfolyam 1, de a pénznem nem HUF.

```
Csak akkor fut le, ha mindkét elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/currencyCode
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/currencyCode
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

**NORMAL + + +** (^) **-
SIMPLIFIED + + + -
AGGREGATE + + +** (^) **-**


**Azonosító: 1310.
Figyelmeztetés csoport:** INCORRECT_HEAD_DATA
helytelen számlafej adat
**Figyelmeztetés kód: INCORRECT_HEAD_DATA_EXCHANGERATE_EXTREME
Figyelmeztetés szövege: A megjelölt pénznemhez tartozó árfolyam extrém.
Működés:** Figyelmeztet, ha a pénznemhez tartozó árfolyam kívül esik a megjelölt határokon.

```
Figyelt pénznemek és határok (szükség esetén a határokat külön értesítés nélkül
változnak):
```
```
currencyCode Minimum Maximum
EUR 250 500
USD 200 500
GBP 250 600
CHF 200 500
BGN 120 300
RON 50 150
PLN 50 150
UAH 2 30
SEK 20 60
NOK 20 60
MKD 2 20
CZK 5 40
ILS 40 200
DKK 20 100
RSD 1 9
BAM 100 300
HRK 30 90
```
```
Megjegyzés:
Ezen figyelmeztetés csak a nyilvánvaló tévedéseket jelzésére való (pl. nem egy
egységre vetített árfolyam szerepeltetése), nem vizsgálja pontosan a használt
árfolyam helyességét.
```
```
Csak akkor fut le, ha mindkét elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/currencyCode
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


### I.2 TÉTELSOROKBAN SZEREPLŐ ADATOKRA VONATKOZÓ FIGYELMEZTETÉSEK

```
Azonosító: 431.
Figyelmeztetés csoport: INCORRECT_LINE_DATA
helytelen számlatétel adat
Figyelmeztetés kód: INCORRECT_LINE_DATA_PRODUCTCODE_VTSZ
Figyelmeztetés szövege: Érvénytelen vámtarifaszám.
Működés: Figyelmeztet, ha a tételsorban megadott vámtarifaszám (productCodeValue,
ahol productCodeCategory=”VTSZ”) nem szerepel a vámtarifaszám
jegyzékben.
```
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/productCodes/
productCode
Találat esetén hibásként
megjelölt elem:
```
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/productCodes/
productCode
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -
**Megjegyzés:** (^) Inaktív.


**Azonosító: 432.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_PRODUCTCODE_SZJ
Figyelmeztetés szövege: Érvénytelen SZJ szám.
Működés:** Figyelmeztet, ha a tételsorban megadott szolgáltatásjegyzék szám
(productCodeValue, ahol productCodeCategory=”SZJ”) nem szerepel a
jegyzékben.

InvoiceData/invoiceMain/invoice/invoiceLines/line/productCodes/
productCode
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/productCodes/
productCode
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -

**Megjegyzés:** Inaktív.

**Azonosító: 433.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_PRODUCTCODE_TESZOR
Figyelmeztetés szövege: Érvénytelen TESZOR szám.
Működés:** Figyelmeztet, ha a tételsorban megadott TESZOR szám (productCodeValue,
ahol productCodeCategory=”TESZOR”) nem szerepel a jegyzékben.

InvoiceData/invoiceMain/invoice/invoiceLines/line/productCodes/
productCode
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceLines/line/productCodes/
productCode
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -

**Megjegyzés:** (^) Inaktív.


**Azonosító/eredeti sorszám 434.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_UOM_INCOMPLETE
Figyelmeztetés szövege: A számlatétel saját mértékegység használatát jelölte
(unitOfMeasure=”OWN”), de unitOfMeasureOwn elem nem szerepel az
adatszolgáltatásban.
Működés:** Figyelmeztet, ha a tételsorban megadott unitOfMeasure elem értéke „OWN”,
de nem szerepel a tételsorban unitOfMeasureOwn elem.

InvoiceData/invoiceMain/invoice/invoiceLines/line/unitOfMeasure
InvoiceData/invoiceMain/invoice/invoiceLines/line/unitOfMeasureOwn
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/unitOfMeasure
```
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE**^ +^ +^ +^ -^


**Azonosító: 740.
Figyelmeztetés csoport:** INCORRECT_LINE_CALCULATION
helytelen tételszámítás
**Figyelmeztetés kód: INCORRECT_LINE_CALCULATION_NET_AMOUNT
Figyelmeztetés szövege: A tétel mennyiség és egységár szorzata (figyelembe véve az adott kedvezményt) eltér a
nettó értékétől.
Működés:** Figyelmeztet, ha a tétel mennyiségének és egységárának szorzataként számított és az
esetleges kedvezményekkel csökkentett nettó érték eltér a tételsorhoz közölt nettó értéktől.

```
A számított nettó érték meghatározása:
Ha a kedvezmény összege (discountValue) kitöltött, akkor
Számított nettó érték=a mennyiség és egységár szorzata, csökkentve a kedvezmény
összegével.
Ha a kedvezmény százalékban van megadva, vagyis a distcountRate kitöltött, akkor
Számított nettó érték = a mennyiség és egységár szorzata, csökkentve a mennyiség, az
egységár és a százalékban kifejezett kedvezmény szorzatával.
```
```
A tolerált eltérés a számított forintban kifejezett érték 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.
```
Csak akkor fut le, ha .../quantity, .../unitPrice, .../lineNetAmount elemek kitöltöttek, illetve
módosító/sztornó számla esetén csak akkor, ha lineOperation = CREATE.
InvoiceData/invoiceMain/invoice/invoiceLines/line/quantity
InvoiceData/invoiceMain/invoice/invoiceLines/line/unitPrice
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineDiscountData/discountValue
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineDiscountData/discountRate
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineNetAmountData/lineNetAmount
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineNetAmountData/lineNetAmount
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 741.
Figyelmeztetés csoport:** INCORRECT_LINE_CALCULATION
helytelen tételszámítás
**Figyelmeztetés kód: INCORRECT_LINE_CALCULATION_LINE_NET_AMOUNT_HUF
Figyelmeztetés szövege: Eltérés a számla tétel eredeti pénznemben és forintban megadott nettó
értéke között.
Működés:** Figyelmeztet, ha a tétel nettó összege és a tétel forintban feltüntetett nettó
összege eltér egymástól, figyelembe véve az alkalmazott árfolyamot.
lineNetAmount * exchangeRate <> lineNetAmountHUF

```
A tolerált eltérés a számított forintban kifejezett érték 1%-a, de legalább 1 HUF
és a számla pénznemének 0,01 egysége közül a nagyobb.
```
```
Csak akkor fut le, ha mindhárom elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineNetAmountData/lineNetAmount
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineNetAmountData/lineNetAmountHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineNetAmountData/lineNetAmountHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - - -


**Azonosító: 742.
Figyelmeztetés csoport:** INCORRECT_LINE_CALCULATION
helytelen tételszámítás
**Figyelmeztetés kód: INCORRECT_LINE_CALCULATION_AGGREGATE_LINE_NET_AMOUNT_HUF
Figyelmeztetés szövege: Eltérés a gyűjtőszámla tétel eredeti pénznemben és forintban megadott
nettó értéke között.
Működés:** Figyelmeztet, ha a gyűjtőszámla tétel nettó összege és a tétel forintban
feltüntetett nettó összege eltér egymástól, figyelembe véve az alkalmazott
árfolyamot.
lineNetAmount * lineExchangeRate <> lineNetAmountHUF

```
A tolerált eltérés a számított forintban kifejezett érték 1%-a, de legalább 1 HUF
és a számla pénznemének 0,01 egysége közül a nagyobb.
```
```
Csak akkor fut le, ha mindhárom elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/aggregateInvoiceLineData/
lineExchangeRate
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineNetAmountData/lineNetAmount
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineNetAmountData/lineNetAmountHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineNetAmountData/lineNetAmountHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 743.
Figyelmeztetés csoport:** INCORRECT_LINE_CALCULATION
helytelen tételszámítás
**Figyelmeztetés kód: INCORRECT_LINE_CALCULATION_LINE_VAT_AMOUNT_HUF
Figyelmeztetés szövege: Eltérés a számla tétel eredeti pénznemben és forintban megadott áfa értéke
között.
Működés:** Figyelmeztet, ha a tétel áfaösszege és a tétel áfaösszege forintban eltér
egymástól, figyelembe véve az alkalmazott árfolyamot.
lineVatAmount * exchangeRate <> lineVatAmountHUF

```
A tolerált eltérés a számított forintban kifejezett érték 1%-a, de legalább 1 HUF
és a számla pénznemének 0,01 egysége közül a nagyobb.
```
```
Csak akkor fut le, ha mindhárom elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatData/lineVatAmount
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatData/lineVatAmountHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatData/lineVatAmountHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - - -


**Azonosító: 744.
Figyelmeztetés csoport:** INCORRECT_LINE_CALCULATION
helytelen tételszámítás
**Figyelmeztetés kód: INCORRECT_LINE_CALCULATION_AGGREGATE_LINE_VAT_AMOUNT_HUF
Figyelmeztetés szövege: Eltérés a gyűjtőszámla tétel eredeti pénznemben és forintban megadott áfa
értéke között.
Működés:** Figyelmeztet, ha a gyűjtőszámla tétel áfaösszege és áfaösszege forintban eltér
egymástól, figyelembe véve az alkalmazott árfolyamot.
lineVatAmount * lineExchangeRate <> lineVatAmountHUF

```
A tolerált eltérés a számított forintban kifejezett érték 1%-a, de legalább 1 HUF
és a számla pénznemének 0,01 egysége közül a nagyobb.
```
```
Csak akkor fut le, ha mindhárom elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/aggregateInvoiceLineData/
lineExchangeRate
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatData/lineVatAmount
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatData/lineVatAmountHUF
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatData/lineVatAmountHUF
**Hatókör:**

```
operation/
invoiceCategory CREATE^ MODIFY^ STORNO^ ANNUL^
NORMAL - - - -
SIMPLIFIED - - - -
AGGREGATE + + + -
```

**Azonosító: 745.
Figyelmeztetés csoport:** INCORRECT_LINE_CALCULATION
helytelen tételszámítás
**Figyelmeztetés kód: INCORRECT_LINE_CALCULATION_LINE_UNIT_PRICE_HUF
Figyelmeztetés szövege: Eltérés a számla tétel eredeti pénznemben és forintban megadott egységára
között.
Működés:** Figyelmeztet, ha a tétel egységára és a tétel egységára forintban eltér
egymástól, figyelembe véve az alkalmazott árfolyamot.
unitPrice* exchangeRate <> unitPriceHUF

```
A tolerált eltérés a számított forintban kifejezett érték 1%-a, de legalább 1 HUF
és a számla pénznemének 0,01 egysége közül a nagyobb.
```
```
Csak akkor fut le, ha mindhárom elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
InvoiceData/invoiceMain/invoice/invoiceLines/line/unitPrice
InvoiceData/invoiceMain/invoice/invoiceLines/line/unitPriceHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/unitPriceHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -


**Azonosító: 746.
Figyelmeztetés csoport:** INCORRECT_LINE_CALCULATION
helytelen tételszámítás
**Figyelmeztetés kód: INCORRECT_LINE_CALCULATION_AGGREGATE_LINE_UNIT_PRICE_HUF
Figyelmeztetés szövege: Eltérés a gyűjtőszámla tétel eredeti pénznemben és forintban megadott
egységára között.
Működés:** Figyelmeztet, ha a gyűjtőszámla tétel egységára és a tétel egységára forintban
eltér egymástól, figyelembe véve az alkalmazott árfolyamot.
unitPrice* lineExchangeRate <> unitPriceHUF

```
A tolerált eltérés a számított forintban kifejezett érték 1%-a, de legalább 1 HUF
és a számla pénznemének 0,01 egysége közül a nagyobb.
```
```
Csak akkor fut le, ha mindhárom elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/aggregateInvoiceLineData/
lineExchangeRate
InvoiceData/invoiceMain/invoice/invoiceLines/line/unitPrice
InvoiceData/invoiceMain/invoice/invoiceLines/line/unitPriceHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/unitPriceHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -


**Azonosító: 750.
Figyelmeztetés csoport:** INCORRECT_LINE_CALCULATION
helytelen tételszámítás
**Figyelmeztetés kód: INCORRECT_LINE_CALCULATION_GROSS_AMOUNT
Figyelmeztetés szövege: Egyszerűsített számla tételsor mennyiség és egységár szorzata a kedvezmény
adatait figyelembe véve (ha releváns) eltér a tételsor bruttó értékétől.
Működés:** Figyelmeztet, ha az egyszerűsített számla tételsorban a mennyiség és egységár
szorzata (figyelembe véve az adott kedvezményt) eltér a tételsor bruttó
értékétől.
Csak akkor fut le, ha .../quantity, .../unitPrice, .../lineGrossAmountSimplified
elemek kitöltöttek, illetve módosító/sztornó számla esetén csak akkor, ha
lineOperation = CREATE.

```
A tolerált eltérés a számított forintban kifejezett érték 1%-a, de legalább 1 HUF
és a számla pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/quantity
InvoiceData/invoiceMain/invoice/invoiceLines/line/unitPrice
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineDiscountData
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineGrossAmountSimplified
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineGrossAmountSimplified
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED + + + -

##### AGGREGATE - - - -


**Azonosító: 751.
Figyelmeztetés csoport:** INCORRECT_LINE_CALCULATION
helytelen tételszámítás
**Figyelmeztetés kód: INCORRECT_LINE_CALCULATION_LINE_GROSS_AMOUNT_NORMAL_HUF
Figyelmeztetés szövege: Eltérés a számla tétel eredeti pénznemben és forintban megadott bruttó
értéke között.
Működés:** Figyelmeztet, ha a tétel bruttó összege és a tétel bruttó összege forintban eltér
egymástól, figyelembe véve az alkalmazott árfolyamot.
lineGrossAmountNormal * exchangeRate <> lineGrossAmountNormalHUF

```
A tolerált eltérés a számított forintban kifejezett érték 1%-a, de legalább 1 HUF
és a számla pénznemének 0,01 egysége közül a nagyobb.
```
```
Csak akkor fut le, ha mindhárom elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineGrossAmountData/lineGrossAmountNormal
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineGrossAmountData/lineGrossAmountNormalHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineGrossAmountData/lineGrossAmountNormalHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - - -


**Azonosító: 752.
Figyelmeztetés csoport:** INCORRECT_LINE_CALCULATION
helytelen tételszámítás
**Figyelmeztetés kód: INCORRECT_LINE_CALCULATION_AGGREGATE_LINE_GROSS_AMOUNT_NOR
MAL_HUF
Figyelmeztetés szövege: Eltérés a gyűjtőszámla tétel eredeti pénznemben és forintban megadott
bruttó értéke között.
Működés:** Figyelmeztet, ha a gyűjtőszámla tétel bruttó összege és a tétel bruttó összege
forintban eltér egymástól, figyelembe véve az alkalmazott árfolyamot.
lineGrossAmountNormal * lineEexchangeRate <> lineGrossAmountNormalHUF

```
A tolerált eltérés a számított forintban kifejezett érték 1%-a, de legalább 1 HUF
és a számla pénznemének 0,01 egysége közül a nagyobb.
```
```
Csak akkor fut le, ha mindhárom elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/aggregateInvoiceLineData/
lineExchangeRate
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineGrossAmountData/lineGrossAmountNormal
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineGrossAmountData/lineGrossAmountNormalHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineGrossAmountData/lineGrossAmountNormalHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 753.
Figyelmeztetés csoport:** INCORRECT_LINE_CALCULATION
helytelen tételszámítás
**Figyelmeztetés kód: INCORRECT_LINE_CALCULATION_LINE_GROSS_AMOUNT_SIMPLIFIED_HUF
Figyelmeztetés szövege: Eltérés az egyszerűsített számla tétel eredeti pénznemben és forintban
megadott bruttó értéke között.
Működés:** Figyelmeztet, ha az egyszerűsített számla tétel bruttó összege és a tétel bruttó
összege forintban eltér egymástól, figyelembe véve az alkalmazott árfolyamot.
lineGrossAmountSimplified * exchangeRate <> lineGrossAmountSimplifiedHUF

```
A tolerált eltérés a számított forintban kifejezett érték 1%-a, de legalább 1 HUF
és a számla pénznemének 0,01 egysége közül a nagyobb.
```
```
Csak akkor fut le, ha mindhárom elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineGrossAmountSimplified
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineGrossAmountSimplifiedHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineGrossAmountSimplifiedHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -


**Azonosító: 754.
Figyelmeztetés csoport:** INCORRECT_LINE_CALCULATION
helytelen tételszámítás
**Figyelmeztetés kód: INCORRECT_LINE_CALCULATION_LINE_GROSS_AMOUNT_NORMAL_SUM
Figyelmeztetés szövege: A számla tétel forintban megadott bruttó értéke eltér a tétel forintban
megadott nettó és áfa értékeinek összegétől.
Működés:** Figyelmeztet, ha a számlatétel bruttó összege forintban eltér a tétel nettó és
áfa értékeinek összegétől.
lineNetAmountNormalHUF + lineVatAmountNormalHUF <>
lineGrossAmountNormalHUF

```
Tolerált eltérés: lineGrossAmountNormalHUF 1%-a, de legalább 1 HUF és a
számla pénznemének 0,01 egysége közül a nagyobb.
```
```
Csak akkor fut le, ha mindhárom elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineNetAmountData/lineAmountNormalHUF
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatData/lineVatAmountHUF
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineGrossAmountData/lineGrossAmountNormalHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineGrossAmountData/lineGrossAmountNormalHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 590.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_SELF_LINE_NUMBER
Figyelmeztetés szövege: Másik számlatételre közölt hivatkozás az adott tétel saját sorszámát
tartalmazza.
Működés:** Figyelmeztet, ha más tételre vonatkozó hivatkozásban saját sorszámát adja
meg.
Csak akkor fut, ha az elem kitöltött.

InvoiceData/invoiceMain/invoice/invoiceLines/line/referencesToOtherLines/
referenceToOtherLine
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineNumber
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/referencesToOtherLines/
referenceToOtherLine
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -
**Azonosító: 591.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számla tétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_EXEMPTION_NORMAL
Figyelmeztetés szövege: A normál/gyűjtőszámla tételben adómentesség jelölés ellenére ÁFA adat(ok)
szerepel(nek).
Működés:** Figyelmeztet, ha a normál vagy gyűjtőszámla tételében adómentesség jelölés
szerepel, mégis szerepelnek ÁFA adatok a tételsorban (lineVatAmount vagy
lineVatAmountHUF <> 0).
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/vatExemption
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatData
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/vatExemption
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

**SIMPLIFIED** - - (^) - -
**AGGREGATE** + + + -


**Azonosító: 593.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számla tétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_OUT_OF_SCOPE_NORMAL
Figyelmeztetés szövege: A normál/gyűjtőszámla tételben ÁFA törvény hatályán kívüli jelölés ellenére
ÁFA adat(ok) szerepel(nek).
Működés:** Figyelmeztet, ha a normál vagy gyűjtőszámla tétel ÁFA törvény hatályon kívüli
jelölés szerepel, mégis szerepelnek ÁFA adatok a tételsorban (lineVatAmount
vagy lineVatAmountHUF <> 0).

InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/vatOutOfScope
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatData
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/vatOutOfScope
```
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^

**NORMAL** + + (^) + -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -


**Azonosító: 595.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_DOMESTIC_REVERSE_CHARGE_NORMAL
Figyelmeztetés szövege: A normál/gyűjtőszámla tételben belföldi fordított adózás jelölés ellenére ÁFA
adat(ok) szerepel(nek).
Működés:** Figyelmeztet, ha a normál vagy gyűjtőszámla tétel belföldi fordított adózás
jelölése true érték esetén ÁFA adatok szerepelnek a tételsorban (lineVatAmount
vagy lineVatAmountHUF <> 0).

InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/vatDomesticReverseCharge
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatData
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/vatDomesticReverseCharge
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -
**Azonosító: 596.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_DOMESTIC_REVERSE_CHARGE
Figyelmeztetés szövege: Hibás jelölés: belföldi fordított adózás jelölése esetén a vevő csak belföldi
áfaalany lehet.
Működés:** Figyelmeztet, ha a tételek között belföldi fordított adózás jelölése szerepel, de a
vevő nem belföldi áfaalany.
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/vatDomesticReverseCharge
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatStatus
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/vatDomesticReverseCharge
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 597.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számla tétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_MARGIN_SCHEME_INDICATOR_NORMAL
Figyelmeztetés szövege: A normál/gyűjtőszámla tételben különbözet szerinti szabályozás jelölés
ellenére ÁFA adat(ok) szerepel(nek).
Működés:** Figyelmeztet, ha a normál vagy gyűjtőszámla tétel különbözet szerinti
szabályozás jelölése esetén ÁFA adatok szerepelnek a tételsorban
(lineVatAmount vagy lineVatAmountHUF <> 0).

```
Csak akkor fut le, ha marginSchemeIndicator értéke <> TRAVEL_AGENCY.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/marginSchemeIndicator
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatData
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/marginSchemeIndicator
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

**SIMPLIFIED** - - (^) - -
**AGGREGATE** + + + -


**Azonosító: 600.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_LINE_AMOUNTS_NORMAL_MANDATORY**

**Figyelmeztetés szövege: Hiányzó tételsor érték adatok.
Működés:** Figyelmeztet, ha normál vagy gyűjtőszámla tételsor összeg adat nincs kitöltve.

```
Módosító/sztornó számla esetén csak akkor fut le, ha lineOperation = CREATE.
```
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal
```
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE^ +^ +^ +^ -^

**Azonosító: 610.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_LINE_AMOUNTS_SIMPLIFIED_MANDATORY
Figyelmeztetés szövege: Hiányzó számla tételsor érték adatok.
Működés:** Figyelmeztet, ha egyszerűsített számla tételsorösszeg adat nincs kitöltve.

```
Módosító/sztornó számla esetén csak akkor fut le, ha lineOperation = CREATE.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED + + + -

##### AGGREGATE^ -^ -^ -^ -^


**Azonosító: 620.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_AGGREGATE_INV_LINE_DATA_MANDATORY
Figyelmeztetés szövege: A gyűjtőszámla tételében nem szerepel a tétel teljesítés dátuma.
Működés:** Figyelmeztet, ha gyűjtőszámla esetén (invoiceCategory=”AGGREGATE”) az
adott tételsorban nem szerepel gyűjtőszámlaadat (aggregateInvoiceLineData
elem).

```
Módosító/sztornó számla esetén csak akkor fut le, ha lineOperation = CREATE.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/aggregateInvoiceLineData
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/aggregateInvoiceLineData
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -

**Azonosító: 630.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_LINE_AMOUNTS_SIMPLIFIED_NOT_ALLOWED
Figyelmeztetés szövege: Normál vagy gyűjtőszámla tétele egyszerűsített számla tételsor összegzést
tartalmaz.
Működés:** Figyelmeztet, ha normál vagy gyűjtőszámla esetén egyszerűsített számlára
vonatkozó elem lett kitöltve.

InvoiceData/invoiceMain/invoice/invoiceLines/line/
lineAmountsSimplified/lineVatContent
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineGrossAmountSimplified
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineVatContent
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -


**Azonosító: 631.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_AGGREGATE_INVOICE_LINE_DATA
Figyelmeztetés szövege: Nem gyűjtőszámla gyűjtőszámlára jellemző tételadatot tartalmaz.
Működés:** Figyelmeztet, ha normál vagy egyszerűsített számla tételsorban gyűjtőszámla
adat(ok) szerepel(nek).

InvoiceData/invoiceMain/invoice/invoiceLines/line/aggregateInvoiceLineData
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/aggregateInvoiceLineData
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE - - - -

**Azonosító: 581.**

**Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_STATUS_VAT_DATA_MISMATCH_KBAET
Figyelmeztetés szövege: Helytelen áfa jelölés. KBAET választása esetén a vevő áfa jelölése csak egyéb
(OTHER) lehet.
Működés:** Normál vagy gyűjtőszámlánál figyelmeztet, ha adómentes Közösségen belüli
termékértékesítés,
új közlekedési eszköz nélkül (vatExemption/case=KBAET) választása esetén a
vevő áfa jelölése nem „egyéb” (customerVatStatus<>OTHER).

InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatStatus
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatExemption/case
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatExemption/case
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -


**Azonosító: 5810.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_STATUS_VAT_DATA_MISMATCH_KBAET_SIMPLIFIED
Figyelmeztetés szövege: Helytelen áfa jelölés. KBAET választása esetén a vevő áfa jelölése csak egyéb
(OTHER) lehet.
Működés:** Egyszerűsített számlánál figyelmeztet, ha adómentes Közösségen belüli
termékértékesítés, új közlekedési eszköz nélkül (vatExemption/case=KBAET)
választása esetén a vevő áfa jelölése nem „egyéb” (customerVatStatus<>OTHER).

InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatStatus
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsSimplified/
lineVatRate/vatExemption/case
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsSimplified/
lineVatRate/vatExemption/case
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -
**Azonosító: 582.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_STATUS_VAT_DATA_MISMATCH_KBAUK
Figyelmeztetés szövege: Helytelen áfa jelölés. KBAUK választása esetén a vevő áfa jelölése csak
magánszemély (PRIVATE_PERSON) vagy egyéb (OTHER) lehet.
Működés:** Normál számlánál figyelmeztet, ha adómentes Közösségen belüli új
közlekedési eszköz értékesítés (vatExemption/case=KBAUK) választása
esetén a vevő áfa jelölése
belföldi (customerVatStatus=DOMESTIC).
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatStatus
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatExemption/case
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatExemption/case
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - - -


**Azonosító: 5820.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_STATUS_VAT_DATA_MISMATCH_KBAUK_SIMP
LIFIED
Figyelmeztetés szövege: Helytelen áfa jelölés. KBAUK választása esetén a vevő áfa jelölése csak
magánszemély (PRIVATE_PERSON) vagy egyéb (OTHER) lehet.
Működés:** Egyszerűsített számlánál figyelmeztet, ha adómentes Közösségen belüli új
közlekedési eszköz értékesítés (vatExemption/case=KBAUK) választása esetén
a vevő áfa jelölése belföldi (customerVatStatus=DOMESTIC).

InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatStatus
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsSimplified/
lineVatRate/vatExemption/case
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsSimplified/
lineVatRate/vatExemption/case
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -
**Azonosító: 583.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_STATUS_VAT_DATA_MISMATCH_EUFAD37
Figyelmeztetés szövege: Helytelen áfa jelölés. EUFAD37 választása esetén a vevő áfa jelölése csak
egyéb (OTHER) lehet.
Működés:** Figyelmeztet, ha Áfa tv. 37. §-a alapján másik tagállamban teljesített, fordítottan
adózó ügylet (vatOutOfScope=EUFAD37) választása esetén a vevő áfa jelölése
nem „egyéb” (customerVatStatus<>OTHER).
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatStatus
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatOutOfScope/case
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatOutOfScope/case
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - - -


**Azonosító: 584.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_STATUS_VAT_DATA_MISMATCH_EUFADE
Figyelmeztetés szövege: Helytelen áfa jelölés. EUFADE választása esetén a vevő áfa jelölése csak
egyéb (OTHER) lehet.
Működés:** Figyelmeztet, ha másik tagállamban teljesített, nem az Áfa tv. 37. §-a alá
tartozó, fordítottan adózó ügylet (vatOutOfScope=EUFADE) választása esetén
a vevő áfa jelölése nem „egyéb” (customerVatStatus<>OTHER).

InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatStatus
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatOutOfScope/case
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatOutOfScope/case
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - - -
**Azonosító: 585.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_KBAET
Figyelmeztetés szövege: Helytelen vevő adószám. KBAET választása esetén csak a közösségi adószám
lehet kitöltött.
Működés:** Normál számlánál figyelmeztet, ha adómentes Közösségen belüli
termékértékesítés, új közlekedési eszköz nélkül (vatExemption/case=KBAET)
választása esetén közösségi adószámtól (communityVatNumber) különböző
adószám van kitöltve.
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerVatData
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatExemption/case
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatExemption/case
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - - -


**Azonosító: 5850.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_KBAET_SIMPLIFIED
Figyelmeztetés szövege: Helytelen vevő adószám. KBAET választása esetén csak a közösségi adószám
lehet kitöltött.
Működés:** Egyszerűsített számlánál figyelmeztet, ha adómentes Közösségen belüli
termékértékesítés, új közlekedési eszköz nélkül (vatExemption/case=KBAET)
választása esetén közösségi adószámtól (communityVatNumber) különböző
adószám van kitöltve.

InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatData
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsSimplified/
lineVatRate/vatExemption/case
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsSimplified/
lineVatRate/vatExemption/case
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -
**Azonosító: 586.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_KBAUK
Figyelmeztetés szövege: Helytelen vevő adószám. KBAUK választása esetén csak a közösségi adószám
lehet kitöltött.
Működés:** Normál számlánál figyelmeztet, ha adómentes Közösségen belüli új közlekedési
eszköz értékesítés (vatExemption/case=KBAUK) választása esetén a közösségi
adószámtól (communityVatNumber) különböző adószám van kitöltve.
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatData
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatExemption/case
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatExemption/case
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - - -


**Azonosító: 5860.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_KBAUK_SIMPLIFIED
Figyelmeztetés szövege: Helytelen vevő adószám. KBAUK választása esetén csak a közösségi adószám
lehet kitöltött.
Működés:** Egyszerűsített számlánál figyelmeztet, ha adómentes Közösségen belüli új
közlekedési eszköz értékesítés (vatExemption/case=KBAUK) választása esetén
közösségi adószámtól (communityVatNumber) különböző adószám van kitöltve.

InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatData
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsSimplified/
lineVatRate/vatExemption/case
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsSimplified/
lineVatRate/vatExemption/case
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -


**Azonosító: 587.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_EAM
Figyelmeztetés szövege: Helytelen vevő adószám. EAM választása esetén csak belföldi vagy harmadik
országbeli adószám lehet kitöltött.
Működés:** Normál számlánál figyelmeztet, ha adómentes termékértékesítés a közösség
területén kívülre (termékexport harmadik országba) (vatExemption/case=EAM)
választása esetén közösségi adószám (communityTaxNumber) különböző
adószám van kitöltve.

InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatData
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatExemption/case
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatExemption/case
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -
**Azonosító: 5870.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_EAM_SIMPLIFIED
Figyelmeztetés szövege: Helytelen vevő adószám. EAM választása esetén csak belföldi vagy harmadik
országbeli adószám lehet kitöltött.
Működés:** Egyszerűsített számlánál figyelmeztet, ha adómentes termékértékesítés a
közösség területén kívülre (termékexport harmadik országba)
(vatExemption/case=EAM) választása esetén közösségi adószám
(communityVatNumber) van kitöltve.
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerVatData
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsSimplified/
lineVatRate/vatExemption/case
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsSimplified/
lineVatRate/vatExemption/case
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -


**Azonosító: 588.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_EUFAD37
Figyelmeztetés szövege: Helytelen vevő adószám. EUFAD37 választása esetén csak a közösségi adószám
lehet kitöltött.
Működés:** Figyelmeztet, ha Áfa tv. 37. §-a alapján másik tagállamban teljesített, fordítottan
adózó ügylet (vatOutOfScope=EUFAD37) esetén a közösségi adószámtól
(communityVatNumber) különböző adószám van kitöltve.

InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerVatData
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatOutOfScope/case
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatOutOfScope/case
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - - -
**Azonosító: 589.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_EUFADE
Figyelmeztetés szövege: Helytelen vevő adószám. EUFADE választása esetén csak a közösségi vagy
belföldi adószám lehet kitöltött.
Működés:** Figyelmeztet, ha másik tagállamban teljesített, nem az Áfa tv. 37. §-a alá tartozó,
fordítottan adózó ügylet (vatOutOfScope=EUFADE) választása esetén harmadik
országbeli adószám (thirdStateTaxId) van kitöltve.
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerVatData
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatOutOfScope/case
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatOutOfScope/case
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - - -


**Azonosító: 592.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: INCORRECT_LINE_DATA_VAT_DATA_MISMATCH_EUE
Figyelmeztetés szövege: Helytelen vevő adószám. EUE választása esetén csak a belföldi vagy a
közösségi adószám lehet kitöltött.
Működés:** Figyelmeztet, ha másik tagállamban teljesített, nem fordítottan adózó ügylet
(vatOutOfScope=EUE) választása esetén a harmadik országbeli adószám
(thirdStateTaxId) van kitöltve.

InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/
customerVatData
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatOutOfScope/case
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLine/line/lineAmountsNormal/
lineVatRate/vatOutOfScope/case
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - - -


**Azonosító: 632.
Figyelmeztetés csoport:** INCORRECT_LINE_DATA
helytelen számlatétel adat
**Figyelmeztetés kód: ITEM_AGGREGATION_MISMATCH
Figyelmeztetés szövege: A mergedItemIndicator értéke nem lehet „false”, ha a számlaláncban korábban
„true” értéket vett fel.
Működés:** Figyelmeztet, ha a beküldött számlához tartozó számlaláncban van olyan korábbi
számla, ahol a mergedItemIndicator = true, de a számla mergedItemIndicator
értéke false.

invoiceMain/invoice/invoiceLines/mergedItemIndicator
invoiceMain/invoice/invoiceReference/modificationIndex
**Találat esetén hibásként
megjelölt elem:**

```
invoiceMain/invoice/invoiceLines/mergedItemIndicator
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - + + -

##### SIMPLIFIED - + + -

##### AGGREGATE - + + -

**Azonosító: 980.
Figyelmeztetés csoport:** LINE_SUMMARY_TYPE_MISMATCH
sor-összesítés típuseltérés
**Figyelmeztetés kód: LINE_SUMMARY_TYPE_MISMATCH_LINE_SIMPLIFIED
Figyelmeztetés szövege: Hibás számlaösszesítő. Normál vagy gyűjtőszámla egyszerűsített
számlatétel(eke)t tartalmaz.
Működés:** Figyelmeztet, ha normál-, vagy gyűjtőszámlában egyszerűsített számlatétel
adatok kerülnek kitöltésre.

InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/invoiceCategory
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -
**Megjegyzés:** (^) ERROR szintre emelve.


**Azonosító: 1000.
Figyelmeztetés csoport:** LINE_SUMMARY_TYPE_MISMATCH
sor-összesítés típuseltérés
**Figyelmeztetés kód: LINE_SUMMARY_TYPE_MISMATCH_LINE_NORMAL
Figyelmeztetés szövege: Hibás számlaösszesítő. Egyszerűsített számla normál számlatétel(eke)t
tartalmaz.
Működés:** Figyelmeztet, ha egyszerűsített számlában normál számla számlatétel adatok
kerülnek kitöltésre.

InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/invoiceCategory
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED + + + -

##### AGGREGATE - - - -

**Megjegyzés:** ERROR szintre emelve.

**Azonosító: 1030.
Figyelmeztetés csoport:** INCORRECT_LINE_REFERENCE
hibás sor hivatkozás módosítás vagy érvénytelenítés esetén
**Figyelmeztetés kód: INCORRECT_LINE_REFERENCE
Figyelmeztetés szövege: A módosító számla hivatkozott tételsora nem szerepel a tárolt számlában,
vagy annak utolsó módosításában.
Működés:** Módosító számla esetén (operation=MODIFY) figyelmeztet, ha a hivatkozott
tételsor nem szerepel a tárolt számlában és/vagy utolsó módosításában.

```
Csak abban az esetben fut le, ha az adott tételsorban lineOperation=”MODIFY”
és az adott módosításban modifyWithoutMaster=false.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineModificationReference/
lineNumberReference
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineModificationReference/
lineNumberReference
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - + + -
**SIMPLIFIED** - + + -
**AGGREGATE** - + + -


### I.3 TERMÉKDÍJADATOKHOZ KAPCSOLÓDÓ FIGYELMEZTETÉSEK

```
Azonosító: 110.
Figyelmeztetés csoport: INCORRECT_VAT_CODE
helytelen áfakód
Figyelmeztetés kód: INCORRECT_VAT_CODE_TAXNUMBEROFOBLIGATOR
Figyelmeztetés szövege: Érvénytelen áfakód a termékdíj fizetésre kötelezett adószámában.
Működés: Figyelmeztet, ha a termékdíj fizetésére kötelezett áfakódja érvénytelen.
(értékkészlet: 1, 2, 3, 5)
```
```
Csak akkor fut le, ha az elem kitöltött.
```
```
InvoiceData/invoiceMain/invoice/productFeeSummary/
paymentEvidenceDocumentData/obligatedTaxNumber/vatCode
Találat esetén hibásként
megjelölt elem:
```
```
InvoiceData/invoiceMain/invoice/productFeeSummary/
paymentEvidenceDocumentData/obligatedTaxNumber/vatCode
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 111.
Figyelmeztetés csoport:** INCORRECT_PRODUCT_FEE_DATA
helytelen termékdíjadat
**Figyelmeztetés kód: INCORRECT_PRODUCT_FEE_DATA_CUSTOMER_TAXPAYERID
Figyelmeztetés szövege: Nem létező vevő adószám a termékdíj összesítőben.
Működés:** Figyelmeztet, ha a termékdíj összesítőben szereplő kötelezett adószámának
első nyolc karaktere nem létezik a nyilvántartásban.

```
Csak akkor fut, ha az elem kitöltött.
```
InvoiceData/invoiceMain/invoice/productFeeSummary/
paymentEvidenceDocumentData/obligatedTaxNumber/taxpayerId
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/productFeeSummary/
paymentEvidenceDocumentData/obligatedTaxNumber/taxpayerId
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -

**Megjegyzés:** (^) Inaktív.
**Azonosító: 170.
Figyelmeztetés csoport:** INCORRECT_COUNTY_CODE
helytelen megyekód
**Figyelmeztetés kód: INCORRECT_COUNTY_CODE_TAXNUMBEROFOBLIGATOR
Figyelmeztetés szövege: Érvénytelen megyekód a termékdíj fizetésére kötelezett adószámában.
Működés:** Figyelmeztet, ha a termékdíj fizetésére kötelezett adószámának utolsó két
számjegye (megyekód) érvénytelen. (értéklista: 02-20; 22-44; 51)
Csak akkor fut le, ha az elem kitöltött.
InvoiceData/invoiceMain/invoice/productFeeSummary/
paymentEvidenceDocumentData/obligatedTaxNumber/countyCode
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/productFeeSummary/
paymentEvidenceDocumentData/obligatedTaxNumber/countyCode
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -


**Azonosító: 230.
Figyelmeztetés csoport:** INCORRECT_PRODUCT_CODE
helytelen termékkód
**Figyelmeztetés kód: INCORRECT_PRODUCT_CODE_CATEGORY_TAKEOVER_01
Figyelmeztetés szövege: A környezetvédelmi termékdíj átvállalás iránya és jogszabályi alapja „01”, de
a termékkód fajtájának jelölései között CSK vagy KT kód nem szerepel.
Működés:** Figyelmeztet, ha a környezetvédelmi termékdíj átvállalás iránya és jogszabályi
alapja „01”, de a termékkódok között nem szerepel „CSK”, vagy „KT”.

```
Csak akkor fut, ha mindkét elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/productFeeClause/
productFeeTakeoverData/takeoverReason
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeCategory
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeCategory
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 240.
Figyelmeztetés csoport:** INCORRECT_PRODUCT_CODE
helytelen termékkód
**Figyelmeztetés kód: INCORRECT_PRODUCT_CODE_VALUE_TAKEOVER_01
Figyelmeztetés szövege: Termékdíj kötelezett tétel VTSZ termékkód értéke hibás (kezdete 271019,
271020, 3403, 3819 lehet).
Működés:** Figyelmeztet, ha a környezetvédelmi termékdíj átvállalás iránya és jogszabályi
alapja „01”, és a termékkód kategóriája VTSZ, de a hozzá tartozó termékkód
értékének kezdete nem „271019”, vagy „271019”, vagy „3403”, vagy „3819”.
Vagyis nem egyéb kőolajterméket jelöl.

```
Csak akkor fut le, ha mindhárom elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/productFeeClause/
productFeeTakeoverData/takeoverReason
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeCategory
InvoiceData/invoiceMain/invoice/invoiceLines/line/productCodes/
productCode/productCodeValue
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeValue
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeValue
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -


**Azonosító: 241.
Figyelmeztetés csoport:** INCORRECT_PRODUCT_CODE
helytelen termékkód
**Figyelmeztetés kód: INCORRECT_PRODUCT_CODE_VALUE_OWN
Figyelmeztetés szövege: Saját termékkód érték nem megfelelő elemben szerepel.
Működés:** Figyelmeztet, ha saját termékkód értéke (productCodeCategory= „OWN”) nem
a saját termékkód megjelenítésére szolgáló elemben (productCodeOwnValue)
szerepel.

InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeCategory
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeValue
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeValue
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -


**Azonosító: 250.
Figyelmeztetés csoport:** INCORRECT_PRODUCT_CODE
helytelen termékkód
**Figyelmeztetés kód: INCORRECT_PRODUCT_CODE_CATEGORY_VALUE_TAKEOVER_01
Figyelmeztetés szövege: Ha a környezetvédelmi termékdíj átvállalás iránya és jogszabályi alapja „01”,
és a termékkód jelölése „KT”, a termékkód értéke csak „601” lehet.
Működés:** Figyelmeztet, ha a környezetvédelmi termékdíj átvállalás iránya és jogszabályi
alapja „01”, és a termékkód jelölése „KT”, de a termékkód értéke nem „601”.

```
Csak akkor fut le, ha mindhárom elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/productFeeClause/
productFeeTakeoverData/takeoverReason
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeCategory
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeValue
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeValue
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -


**Azonosító: 260.
Figyelmeztetés csoport:** INCORRECT_PRODUCT_CODE
helytelen termékkód
**Figyelmeztetés kód: INCORRECT_PRODUCT_CODE_FEE_WEIGHT
Figyelmeztetés szövege: Ha a termékdíj köteles termék tömege kilogrammban elem kitöltött, akkor a
termékkód fajtája csak „CSK”, vagy „KT” lehet.
Működés:** Figyelmeztet, ha a termékdíj köteles termék tömege kilogrammban elem
kitöltött, akkor a termékkód fajtája csak „CSK”, vagy „KT” lehet.

```
Csak akkor fut le, ha a termékdíj köteles termék kilogrammban elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/productFeeClause/
customerDeclaration/productFeeWeight
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeCategory
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeCategory
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 270.
Figyelmeztetés csoport:** INCORRECT_PRODUCT_CODE
helytelen termékkód
**Figyelmeztetés kód: INCORRECT_PRODUCT_CODE_FEE_CATEGORY
Figyelmeztetés szövege: Termékkód fajtája típus megjelölése hiba (CSK vagy KT lehet).
Működés:** Figyelmeztet, ha termékdíjat tartalmazó számlasor esetén a termékkód fajtája
mező nem „CSK”, vagy „KT”.

```
Csak akkor fut le, ha a legalább egy számlasoron a termékkód fajtája elem
kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeCategory
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeCategory
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -
**Azonosító: 280.
Figyelmeztetés csoport:** INCORRECT_PRODUCT_CODE
helytelen termékkód
**Figyelmeztetés kód: INCORRECT_PRODUCT_CODE_FEE_SUMMARY_CATEGORY
Figyelmeztetés szövege: Termékkód fajtája típus megjelölése hiba (CSK vagy KT lehet).
Működés:** Figyelmeztet, ha termékdíj összesítő adatok közt a termékkód fajtája mező
nem „CSK”, vagy „KT”.
Csak akkor fut le, ha a legalább a termékkóddal kapcsolatos összesítő adatok
kitöltöttek.
InvoiceData/invoiceMain/invoice/productFeeSummary/productFeeData/
productFeeCode/productCodeCategory
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/productFeeSummary/productFeeData/
productFeeCode/productCodeCategory
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 290.
Figyelmeztetés csoport:** MISSING_PRODUCT_CODE
helytelen termékkód
**Figyelmeztetés kód: INCORRECT_PRODUCT_CODE_FEE_CATEGORY_MISSING
Figyelmeztetés szövege: Tételsorban olyan termékkód típust közölt, amely az összesítőben nem
szerepel.
Működés:** Figyelmeztet, ha valamelyik tételsorban olyan termékkód típus van feltüntetve,
amely az összesítőben nem szerepel.

InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeCode/productCodeCategory
InvoiceData/invoiceMain/invoice/productFeeSummary/productFeeData/
productFeeCode/productCodeCategory
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/productFeeSummary/productFeeData/
productFeeCode/productCodeCategory
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -
**Azonosító: 450.
Figyelmeztetés csoport:** MISSING_PRODUCT_FEE_DATA
hiányzó termékdíjadat
**Figyelmeztetés kód: MISSING_PRODUCT_FEE_DATA_LINE_OBLIGATED_CONTENT_EMPTY
Figyelmeztetés szövege: A számlatételben termékdíj fizetési kötelezettséget jelzett, de nem közölt
adatot.
Működés:** Figyelmeztet a számlatétel termékdíjadatainak hiányára, ha
obligatedProductFee=true.
Csak akkor fut, ha az elem (obligatedProductFee) kitöltött.
InvoiceData/invoiceMain/invoice/invoiceLines/line/obligatedForProductFee
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 460.
Figyelmeztetés csoport:** MISSING_PRODUCT_FEE_DATA
hiányzó termékdíjadat
**Figyelmeztetés kód: MISSING_PRODUCT_FEE_DATA_LINE_OBLIGATED_SUMMARY_EMPTY
Figyelmeztetés szövege: Termékdíj fizetési kötelezettséget jelzett, de nem közölt termékdíj-összesítőt.
Működés:** Figyelmeztet a hiányzó termékdíj-összesítő adatokra, ha
obligatedProductFee=true.

```
Csak akkor fut, ha az elem (obligatedProductFee) kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/obligatedForProductFee
InvoiceData/invoiceMain/invoice/productFeeSummary
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/productFeeSummary
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -

**Azonosító: 470.
Figyelmeztetés csoport:** MISSING_PRODUCT_FEE_DATA
hiányzó termékdíjadat
**Figyelmeztetés kód: MISSING_PRODUCT_FEE_DATA_LINE_CONTENT_SUMMARY_EMPTY
Figyelmeztetés szövege: Számlatétel(ek)ben termékdíjadat szerepel, de termékdíj-összesítő nincs
kitöltve.
Működés:** Figyelmeztet, ha legalább egy számlasoron termékdíjadatok szerepelnek, de a
termékdíj-összesítő nincs kitöltve.

```
Csak akkor fut le, ha legalább egy számlasoron termékdíjadatok kerültek
rögzítésre.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent
InvoiceData/invoiceMain/invoice/productFeeSummary
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/productFeeSummary
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 471.
Figyelmeztetés csoport:** MISSING_PRODUCT_FEE_DATA
hiányzó termékdíjadat
**Figyelmeztetés kód: MISSING_LINE_PRODUCT_FEE_CONTENT
Figyelmeztetés szövege: A termékdíj-összesítő kitöltött, de a számlatétel(ek) nem tartalmaz(nak)
termékdíjadatot.
Működés:** Figyelmeztet, ha a termékdíj-összesítő kitöltött, de a számlatételek közül egy
esetben sem került termékdíjra vonatkozó adat feltüntetésre.

```
Csak akkor fut le, a termékdíj-összesítőben adatok kerültek rögzítésre.
```
InvoiceData/invoiceMain/invoice/productFeeSummary
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/productFeeSummary
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 480.
Figyelmeztetés csoport:** MISSING_PRODUCT_FEE_DATA
hiányzó termékdíjadat
**Figyelmeztetés kód: MISSING_PRODUCT_FEE_DATA_LINE_QUANTITY_SUMMARY_QUANTITY
Figyelmeztetés szövege: A számlasorokban termékkódonként összegzett termékmennyiség eltér az
összesítőben szereplő termékkódonkénti mennyiségtől.**

**Működés:** Figyelmeztet, ha a számlasorokban termékkódonként összegzett
termékmennyiség eltér az összesítőben szereplő termékkódonkénti
mennyiségtől.

```
Csak akkor fut le, ha valamennyi elem kitöltött, illetve módosító/sztornó
számla esetén csak akkor, ha lineOperation = CREATE.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeQuantity
InvoiceData/invoiceMain/invoice/productFeeSummary/productFeeData/
productFeeQuantity
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/productFeeSummary/productFeeData/
productFeeQuantity
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 490.
Figyelmeztetés csoport:** MISSING_PRODUCT_FEE_DATA
hiányzó termékdíjadat
**Figyelmeztetés kód: MISSING_PRODUCT_FEE_DATA_LINE_MEASURING_SUMMARY
Figyelmeztetés szövege: Számlasor(ok)ban és termékdíj összesítésben elétérő díjtétel szerepel.
Működés:** Figyelmeztet, ha a számlasorokban és a termékdíjas összesítőben eltérő
díjtétel kerül megadásra termékkódonként.

```
Csak akkor fut le, ha valamennyi elem kitöltött, illetve módosító/sztornó
számla esetén csak akkor, ha lineOperation = CREATE.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeMeasuringUnit
InvoiceData/invoiceMain/invoice/productFeeSummary/productFeeData/
productFeeMeasuringUnit
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/productFeeSummary/productFeeData/
productFeeMeasuringUnit
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 651.
Figyelmeztetés csoport:** INCORRECT_PRODUCT_FEE_DATA
helytelen termékdíjadat
**Figyelmeztetés kód: INCORRECT_PRODUCT_FEE_DATA_OBLIGATED_LINE
Figyelmeztetés szövege: Termékdíjas tétel esetén a jogszabályok által előírt termékdíj tartalmára
vonatkozó adatok kitöltése kötelező.
Működés:** Ha a számlatétel termékdíj tartalmára vonatkozó adat(ok) kitöltött(ek), akkor
az obligatedProductFee csak „true” értéket vehet fel.

#### Csak akkor fut, ha lineProductFeeContent kitöltött.

InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent
InvoiceData/invoiceMain/invoice/invoiceLines/line/obligatedForProductFee
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceLines/line/obligatedForProductFee
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -

**Azonosító: 670.
Figyelmeztetés csoport:** MISSING_PRODUCT_FEE_DATA
hiányzó termékdíjadat
**Figyelmeztetés kód: INCORRECT_PRODUCT_FEE_DATA_CHARGE_SUM
Figyelmeztetés szövege: A számla termékdíj-összesítést tartalmaz, de a számlatétel(ek) termékdíj
tartalmára vonatkozó adat nincs rögzítve.
Működés:** Figyelmeztet a hiányzó termékdíjadat(ok)ra, ha a termékdíj-összesítő
kitöltött.

```
Csak akkor fut, ha a termékdíj összesítő kitöltött.
```
InvoiceData/invoiceMain/invoice/productFeeSummary
InvoiceData/invoiceMain/invoice/invoiceLines/line/
lineProductFeeContent
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/productFeeSummary
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** + + + -


**Azonosító: 780.
Figyelmeztetés csoport:** INCORRECT_PRODUCT_FEE_CALCULATION
helytelen termékdíj-számítás
**Figyelmeztetés kód: INCORRECT_PRODUCT_FEE_CALCULATION_PRODUCT_FEE_AMOUNT
Figyelmeztetés szövege: A termékdíjjal érintett termék mennyiség és díjtétel szorzata nem egyenlő a
termékdíj összegével.
Működés:** Figyelmeztet, ha a termékdíjjal érintett termékek mennyiségének és a
termékdíj díjtételének szorzata eltér a termékdíj összegétől termékdíj
kódonként. (productFeeQuantity * productFeeRate <> productFeeAmount)

```
Csak akkor fut le, ha a termékdíjjal kapcsolatos összesítő adatok kitöltöttek.
```
```
A tolerált eltérés a számított forintban kifejezett érték 1%-a, de legalább 1 HUF
és a számla pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/productFeeSummary/productFeeData/
productFeeQuantity
InvoiceData/invoiceMain/invoice/productFeeSummary/productFeeData/
productFeeRate
InvoiceData/invoiceMain/invoice/productFeeSummary/productFeeData/
productFeeAmount
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/productFeeSummary/productFeeData/
productFeeAmount
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -


**Azonosító: 790.
Figyelmeztetés csoport:** INCORRECT_PRODUCT_FEE_CALCULATION
helytelen termékdíj-számítás
**Figyelmeztetés kód: INCORRECT_PRODUCT_FEE_CALCULATION_AGGREGATE_PRODUCT_CHARGE
_SUM
Figyelmeztetés szövege: Helytelen termékdíj-számítás. A termékdíjak termékkódonkénti összege eltér
a termékdíj összesen értéktől.
Működés:** Figyelmeztet, ha a termékdíjak összege forintban (productFeeAmount)
termékkódonkénti összege eltér a termékdíj összesen értékétől.

```
Csak akkor fut le, ha a termékdíjjal kapcsolatos összesítő adatok kitöltöttek,
illetve módosító/sztornó számla esetén csak a lineOperation = CREATE sorok
termékdíjai kerülnek összeadásra.
```
```
Tolerált eltérés: A productChargeSum a forintban kifejezett érték 1%-a, de
legalább 1 HUF és a számla pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeAmount
InvoiceData/invoiceMain/invoice/productFeeSummary/productChargeSum
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/productFeeSummary/productChargeSum
```
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE**^ +^ +^ +^ -^


**Azonosító: 810.
Figyelmeztetés csoport:** INCORRECT_PRODUCT_FEE_CALCULATION
helytelen termékdíj-számítás
**Figyelmeztetés kód: INCORRECT_PRODUCT_FEE_CALCULATION_PRODUCT_FEE_AMOUNT_SUMM
ARY
Figyelmeztetés szövege: A számla tételsor(ok) és az összesítő termékdíj tartalmak kódonként
összegzett értéke(i) eltér(nek).
Működés:** Figyelmeztet, ha a számla tételsor(ok) és az összesítő termékdíj tartalmak
kódonként összegzett értéke(i) eltér(nek).

```
Csak akkor fut le, ha valamennyi elem szerepel, illetve módosító/sztornó
számla esetén csak akkor, ha lineOperation = CREATE.
```
```
Tolerált eltérés: az összesítőben szereplő productFeeAmount forintban
kifejezett értékének 1%-a, de legalább 1 HUF és a számla pénznemének 0,01
egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineProductFeeContent/
productFeeAmount
InvoiceData/invoiceMain/invoice/productFeeSummary/productFeeData/
productFeeAmount
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/productFeeSummary/productFeeData/
productFeeAmount
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED + + + -

##### AGGREGATE + + + -


### I.4 AZ ÖSSZESÍTŐ ADATOKRA VONATKOZÓ FIGYELMEZTETÉSEK

```
Azonosító: 680.
Figyelmeztetés csoport: INCORRECT_SUMMARY_DATA
helytelen összesítő adatok
Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_VAT_PERCENTAGE
Figyelmeztetés szövege: Számlasoroktól eltérő áfamérték az összesítésben.
Működés: Figyelmeztet, ha az áfamérték(ek) eltér(nek) a számlasor(ok)ban és az
összesítőben.
```
```
MODIFY esetben csak akkor fut le, ha létezik a lineAmountsNormal csomópont
```
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/vatPercentage
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatPercentage
Találat esetén hibásként
megjelölt elem:
```
```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatPercentage
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 690.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adatok
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_VAT_EXEMPTION
Figyelmeztetés szövege: Az adómentesség jelölés a tételsorok és az összesítő közül csak az egyikben
fordul elő, a másikból hiányzik.
Működés:** Figyelmeztet, ha az adómentesség jelölés eltér a számlasor(ok)ban és az
összesítőben.

```
MODIFY esetben csak akkor fut le, ha létezik a lineAmountsNormal
csomópont
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/vatExemption/case
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatExemption/case
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatExemption/case
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 691.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítőadat
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_VAT_EXEMPTION_NORMAL
Figyelmeztetés szövege: Az áfaáfamérték szerinti összesítés adómentesség jelölés ellenére
áfaadat(ok) szerepel(nek).
Működés:** Figyelmeztet, ha a normál vagy gyűjtőszámla áfamérték szerinti összesítés
adómentesség jelölés szerepel, mégis 0-tól eltérő adómértékhez tartozó
áfaadat(ok) kerül(nek) megadásra.

InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatExemption
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateVatData
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatExemption
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -


**Azonosító: 700.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adatok
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_VAT_OUT_OF_SCOPE
Figyelmeztetés szövege: Az Áfa törvény hatályán kívüli jelölés a tételsorok és az összesítő közül csak
az egyikben fordul elő, a másikból hiányzik.
Működés:** Figyelmeztet, ha az Áfa törvény hatályán kívüli jelölés eltér a
számlasor(ok)ban és az összesítőben.

```
MODIFY esetben csak akkor fut le, ha létezik a lineAmountsNormal
csomópont
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/vatOutOfScope/case
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatOutOfScope/case
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatOutOfScope/case
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 701.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adat
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_VAT_OUT_OF_SCOPE_NORMAL
Figyelmeztetés szövege: Az áfaáfamérték szerinti összesítés Áfa törvény hatályán kívüli jelölés
ellenére áfaadat(ok) szerepel(nek).
Működés:** Figyelmeztet, ha a normál vagy gyűjtőszámla áfaáfamérték szerinti összesítés
Áfa törvény hatályon kívüli jelölés szerepel, mégis 0-tól eltérő adómértékhez
tartozó áfaadat(ok) kerül(nek) megadásra.

InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatOutOfScope
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateVatData
**Találat esetén hibásként
megjelölt elem:**

```
nvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/ vatOutOfScope
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + (^) + -
**SIMPLIFIED** - - (^) - -
**AGGREGATE** + + (^) + -


**Azonosító: 710.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adatok
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_VAT_DOMESTIC_REVERSE_CHARGE
Figyelmeztetés szövege: A belföldi fordított adózásra vonatkozó jelölés a tételsorok és az összesítő
közül csak az egyikben fordul elő, a másikból hiányzik.
Működés:** Figyelmeztet, ha a belföldi fordított adózás jelölés eltér a számlasor(ok)ban és
az összesítőben.

```
MODIFY esetben csak akkor fut le, ha létezik a lineAmountsNormal
csomópont
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/vatDomesticReverseCharge
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatDomesticReverseCharge
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatDomesticReverseCharge
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 711.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adat
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_VAT_DOMESTIC_REVERSE_CHARGE_NORMAL
Figyelmeztetés szövege: Az áfamérték szerinti összesítés belföldi fordított adózás jelölés ellenére
áfaadat(ok) szerepel(nek).
Működés:** Figyelmeztet, ha a normál vagy gyűjtőszámla áfamérték szerinti összesítés
belföldi fordított adózás jelölése true érték szerepel, mégis 0-tól eltérő
adómértékhez tartozó áthárított áfaadat(ok) kerül(nek) megadásra.

InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatDomesticReverseCharge
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateVatData
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatDomesticReverseCharge
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -


**Azonosító: 720.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adatok
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_MARGIN_SCHEME_INDICATOR
Figyelmeztetés szövege: A számla különbözet szerinti szabályozás jelölései a tételsorokban és az
összesítőben eltérnek.
Működés:** Figyelmeztet, ha a számla tételsoraiban és az összesítőben szereplő különbözet
szerinti szabályozás jelölések halmaza egymástól eltér.

```
MODIFY és STORNO esetben csak akkor fut le, ha létezik a lineAmountsNormal
csomópont.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/marginSchemeIndicator
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/marginSchemeIndicator
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/marginSchemeIndicator
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 731.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adat
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_MARGIN_SCHEME_INDICATOR_NORMAL
Figyelmeztetés szövege: Az áfamérték szerinti összesítés különbözet szerinti adózás jelölés ellenére
áfaadat(ok) szerepel(nek).
Működés:** Figyelmeztet, ha a normál vagy gyűjtőszámla áfamérték szerinti összesítés
különbözet szerinti adózás jelölése ellenére 0-tól eltérő adómértékhez tartozó
áfaadat(ok) kerül(nek) megadásra.

```
Csak akkor fut le, ha marginSchemeIndicator értéke <> TRAVEL_AGENCY.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/marginSchemeIndicator
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateVatData
**Találat esetén hibásként
megjelölt elem:**

```
IInvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/marginSchemeIndicator
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

**SIMPLIFIED** - - (^) - -
**AGGREGATE** + + + -


**Azonosító: 733.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adatok
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_VAT_AMOUNT_MISMATCH_NORMAL
Figyelmeztetés szövege: Az adóalap és felszámított adó eltérésének esete a tételsorok és az összesítő
közül csak az egyikben fordul elő, a másikból hiányzik.
Működés:** Figyelmeztet, ha az adóalap és felszámított adó eltérésének esete a tételsorok és
az összesítő közül csak az egyikben fordul elő.

```
MODIFY és STORNO esetben csak akkor fut le, ha létezik a lineAmountsNormal
csomópont
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/vatAmountMismatch/case
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineVatRate/vatAmountMismatch/vatRate
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatAmountMismatch/case
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatAmountMismatch/vatRate
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate/vatAmountMismatch
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -


**Azonosító: 820.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_VAT_RATE_NET_AMOUNT_LINE
Figyelmeztetés szövege: A tételsorok nettó értékének egy vagy több, adómértékenként számított
összege nem egyezik meg a számlaösszesítőben szereplő, egyező
adómértéknél közölt nettó értékkel.
Működés:** Figyelmeztet, ha a tételsorok nettó értékének összege nem egyezik meg a
számlaösszesítőben szereplő nettó értékkel az adott áfakulcs (ideértve a
mentesség, hatályon kívüliség, fordított adózás és a kétféle különbözeti adózás
esetét is) vonatkozásában.

```
Csak akkor fut le, ha az áfa alapja nem nulla (vatRateNetAmount <> 0).
Tolerált eltérés: vatRateNetAmount 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.
```
```
MODIFY esetben csak akkor fut le, ha létezik a lineAmountsNormal csomópont.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineNetAmountData/lineNetAmount
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateNetData/vatRateNetAmount
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateNetData/vatRateNetAmount
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 821.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítés számítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_VAT_RATE_NET_AMOUNT_HUF_LINE
Figyelmeztetés szövege: A tételsorok nettó értékének egy vagy több, adómértékenként számított
összege forintban nem egyezik meg a számlaösszesítőben szereplő, egyező
adómértéknél közölt forintban számított nettó értékkel.
Működés:** Figyelmeztet, ha a tételsorok nettó értékének összege forintban nem egyezik
meg a számlaösszesítőben szereplő forintban megadott nettó értékkel az adott
áfakulcs (ideértve a mentesség, hatályon kívüliség, fordított adózás és a kétféle
különbözeti adózás esetét is) vonatkozásában.

```
Csak akkor fut le, ha az áfa alapja nem nulla (vatRateNetAmountHUF <> 0).
MODIFY esetben csak akkor fut le, ha létezik a lineAmountsNormal csomópont
```
```
Tolerált eltérés: vatRateNetAmountHUF 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineNetAmountData/lineNetAmountHUF
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateNetData/vatRateNetAmountHUF
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateNetData/vatRateNetAmountHUF
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -


**Azonosító: 840.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_INVOICE_NET_AMOUNT
Figyelmeztetés szövege: Az adókulcsonkénti összesített nettó értékek összege eltér a számla nettó
értékétől.
Működés:** Figyelmeztet, ha a számlaösszesítőben szereplő adókulcsonkénti (ideértve a
mentesség, hatályon kívüliség, fordított adózás és a kétféle különbözeti adózás
jelölését) nettó értékek összege eltér a számla nettó értékétől.

```
Tolerált eltérés: invoiceNetAmount forintban kifejezett érték 1%-a, de legalább 1
HUF és a számla pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateNetData/vatRateNetAmount
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceNetAmount
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceNetAmount
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 841.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_INVOICE_NET_AMOUNT_HUF
Figyelmeztetés szövege: Az adókulcsonkénti összesített nettó értékek összege forintban eltér a számla
forintban feltüntetett nettó értékétől.
Működés:** Figyelmeztet, ha a számlaösszesítőben szereplő adókulcsonkénti (ideértve a
mentesség, hatályon kívüliség, fordított adózás és a kétféle különbözeti adózás
jelölését) nettó értékek összege forintban eltér a számla forintban megadott
nettó értékétől.

```
Tolerált eltérés: invoiceNetAmountHUF forintban kifejezett érték 1%-a, de
legalább 1 HUF és a számla pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateNetData/vatRateNetAmountHUF
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceNetAmountHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceNetAmountHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -


**Azonosító: 850.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_INVOICE_VAT_AMOUNT_SUMMARY
Figyelmeztetés szövege: Az adókulcsonkénti áfaértékek összege eltér a számla áfaösszegétől.
Működés:** Figyelmeztet, ha a számlaösszesítőben szereplő adókulcsonkénti (ideértve a
mentesség, hatályon kívüliség, fordított adózás és a kétféle különbözeti adózás
jelölését) áfaértékek összege eltér a számla áfaértékétől a számla pénznemében

```
Tolerált eltérés: invoiceVatAmount forintban kifejezett érték 1%-a, de legalább 1
HUF és a számla pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateVatData/vatRateVatAmount
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceVatAmount
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceVatAmount
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 860.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_INVOICE_VAT_AMOUNT_HUF_SUMM
ARY
Figyelmeztetés szövege: Az adókulcsonkénti áfaértékek összege eltér a számla áfaértékétől forintban.
Működés:** Figyelmeztet, ha a számlaösszesítőben szereplő adókulcsonkénti (ideértve a
mentesség, hatályon kívüliség, fordított adózás és a kétféle különbözeti adózás
jelölését) áfaértékek összege forintban eltér a számla forintban számított
áfaértékétől.

```
Csak akkor fut le, ha az adott adómértékhez tartozó értékesítés vagy
szolgáltatásnyújtás áfaértéke forintban (vatRateVatAmountHUF) elem kitöltött.
```
```
Tolerált eltérés: invoiceVatAmountHUF 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateVatData/vatRateVatAmountHUF
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceVatAmountHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceVatAmountHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 880.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_INVOICE_GROSS_AMOUNT_SUMMAR
Y
Figyelmeztetés szövege: A számlaösszesítő nettó és áfaértékek összege eltér a számla bruttó értékétől.
Működés:** Figyelmeztet, ha a számlaösszesítő nettó és áfaértékek összege eltér számla
bruttó értékétől.

```
Csak akkor fut, ha a számla bruttó összege elem kitöltött.
```
```
Tolerált eltérés: invoiceGrossAmount 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceNetAmount
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceVatAmount
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmount
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmount
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -


**Azonosító: 881.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_INVOICE_GROSS_AMOUNT_HUF_SUM
MARY
Figyelmeztetés szövege: A számlaösszesítő nettó és áfaértékek összege forintban eltér a számla
forintban feltüntetett bruttó értékétől.
Működés:** Figyelmeztet, ha a számlaösszesítő nettó és áfaértékek összege forintban eltér
számla forintban megadott bruttó értékétől.

```
Csak akkor fut, ha a számla bruttó összege elem kitöltött.
```
```
Tolerált eltérés: invoiceGrossAmountHUF 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceNetAmountHUF
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceVatAmountHUF
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmountHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmountHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 890.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_VAT_RATE_VAT_AMOUNT_SUMMARY
Figyelmeztetés szövege: Az áfamértékhez tartozó nettó összegből és az alkalmazott adómértékből
számított áfaösszeg eltér a feltüntetett áfaösszegtől**.
**Működés:** Figyelmeztet, ha az adott áfakulcshoz (ideértve a mentesség, hatályon kívüliség,
fordított adózás és a kétféle különbözeti adózás jelölését) nettó összegéből és az
alkalmazott adómértékből következő áfaösszeg eltér a feltüntetett áfaösszegtől.

```
Csak akkor fut le, ha az áfa alapja nem nulla (vatRateNetAmount <> 0).
```
```
Tolerált eltérés: vatRateVatAmount 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateNetData/vatRateNetAmount
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateVatData/vatRateVatAmount
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateVatData/vatRateVatAmount
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 891.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_VAT_RATE_VAT_AMOUNT_HUF_SUM
MARY
Figyelmeztetés szövege: Az áfamértékhez tartozó nettó összegből és az alkalmazott adómértékből
számított áfaösszeg forintban eltér a forintban feltüntetett áfaösszegtől**.
**Működés:** Figyelmeztet, ha az adott áfakulcshoz (ideértve a mentesség, hatályon kívüliség,
fordított adózás és a kétféle különbözeti adózás jelölését) nettó összegéből és az
alkalmazott adómértékből következő áfaösszeg forintban eltér a forintban
feltüntetett áfaösszegtől.

```
Csak akkor fut le, ha az áfa alapja nem nulla (vatRateNetAmountHUF <> 0).
```
```
Tolerált eltérés: vatRateVatAmountHUF 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateNetData/vatRateNetAmountHUF
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRate
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateVatData/vatRateVatAmountHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateVatData/vatRateVatAmountHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -


**Azonosító: 900.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_INVOICE_GROSS_AMOUNT_LINE
Figyelmeztetés szövege: Az egyszerűsített számla egyes tételsoraiban szereplő bruttó értékek összege
eltér a számla bruttó összegétől**.
**Működés:** Figyelmeztet, ha az egyszerűsített számla egyes tételsoraiban szereplő bruttó
értékek összege eltér a számla bruttó összegétől.

```
Tolerált eltérés: invoiceGrossAmount 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineGrossAmountSimplified
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmount
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmount
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED + + + -

##### AGGREGATE - - - -


**Azonosító: 901.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_INVOICE_GROSS_AMOUNT_HUF_LINE
Figyelmeztetés szövege: Az egyszerűsített számla egyes tételsoraiban szereplő forintban feltüntetett
bruttó értékek összege eltér a számla forintban megadott bruttó összegétől**.
**Működés:** Figyelmeztet, ha az egyszerűsített számla egyes tételsoraiban szereplő bruttó
értékek forintban szereplő összege eltér a számla forintban megadott bruttó
összegétől.

```
Tolerált eltérés: invoiceGrossAmountHUF 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineGrossAmountSimplifiedHUF
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmountHUF
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmountHUF
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -


**Azonosító: 910.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_VAT_CONTENT_SUMMARY_SIMPLIFIE
D
Figyelmeztetés szövege: Az egyszerűsített számla tételsoraiban szereplő áfatartalom jelölés eltér az
összesítőben szereplő áfatartalom jelölésektől.
Működés:** Figyelmeztet, ha az egyszerűsített számla tételsoraiban szereplő áfatartalom
jelölések nem pontosan ugyanazok, mint az összesítőben szereplő áfatartalom
jelölések

```
MODIFY és STORNO esetben csak akkor fut le, ha létezik a
lineAmountsSimplified csomópont
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineVatRate/lineVatContent
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatRate/vatContent
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatRate/vatContent
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -


**Azonosító: 911.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítés számítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_VAT_EXEMPTION_SUMMARY_SIMPLIFIED
Figyelmeztetés szövege: Az egyszerűsített számla adómentesség jelölése a tételsorok és az összesítő közül
csak az egyikben szerepel.
Működés:** Figyelmeztet, ha az egyszerűsített számla tételsoraiban és az összesítőben szereplő
adómentesség jelölések egymástól eltérnek.

InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineVatRate/vatExemption/case
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatRate/vatExemption/case
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatRate/vatExemption/case
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -
**Azonosító: 912.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítés számítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_VAT_OUT_OF_SCOPE_SUMMARY_SIM
PLIFIED
Figyelmeztetés szövege: Az egyszerűsített számla Áfa törvény hatályán kívüli jelölés a tételsorok és az
összesítő közül csak az egyikben szerepel.
Működés:** Figyelmeztet, ha az egyszerűsített számla tételsoraiban és az összesítőben
szereplő Áfa törvény hatályán kívüli jelölések egymástól eltérnek.
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineVatRate/vatOutOfScope/case
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatRate/vatOutOfScope/case
**Találat esetén hibásként
megjelölt elem:**
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatRate/vatOutOfScope/case
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED + + + -

##### AGGREGATE - - - -


**Azonosító: 913.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítés számítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_VAT_DOMESTIC_REVERSE_CHARGE_S
UMMARY_SIMPLIFIED
Figyelmeztetés szövege: Az egyszerűsített számla belföldi fordított adózás jelölése a tételsorok és az
összesítő közül csak az egyikben szerepel.
Működés:** Figyelmeztet, ha az egyszerűsített számla tételsoraiban és az összesítőben
szereplő belföldi fordított adózás jelölések egymástól eltérnek.

InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineVatRate/vatDomesticReverseCharge
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatRate/ vatDomesticReverseCharge
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatRate/ vatDomesticReverseCharge
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -


**Azonosító: 914.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítés számítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_MARGIN_SCHEME_INDICATOR_SUMMARY_SI
MPLIFIED
Figyelmeztetés szövege: Az egyszerűsített számla különbözet szerinti szabályozás jelölés értéke a
tételsorok és az összesítő között eltér.
Működés:** Figyelmeztet, ha az egyszerűsített számla tételsoraiban és az összesítőben
szereplő különbözet szerinti szabályozás jelölések értékei egymástól eltérnek.

InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineVatRate/marginSchemeIndicator
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatRate/ marginSchemeIndicator
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatRate/marginSchemeIndicator
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -


**Azonosító: 916.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítés számítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_VAT_AMOUNT_MISMATCH_SUMMAR
Y_SIMPLIFIED
Figyelmeztetés szövege: Az egyszerűsített számla adóalap és felszámított adó eltérésének esetei
jelölése a tételsorok és az összesítő közül csak az egyikben szerepel.
Működés:** Figyelmeztet, ha az egyszerűsített számla tételsoraiban és az összesítőben
szereplő adóalap és felszámított adó eltérésének esetei jelölések egymástól
eltérnek.

InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineVatRate/vatAmountMismatch/vatRate
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineVatRate/vatAmountMismatch/case
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatRate/ vatAmountMismatch/vatRate
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatRate/ vatAmountMismatch/case
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatRate/vatAmountMismatch
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -


**Azonosító: 920.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_VAT_CONTENT_GROSS_AMOUNT_SU
MMARY_SIMPLIFIED
Figyelmeztetés szövege: Az egyszerűsített számla egy vagy több adótartalomhoz tartozó tételsoraiban
szereplő bruttó értékek összege eltér az összesítésében a hozzá tartozó
adótartalomnál szereplő bruttó összegtől.
Működés:** Figyelmeztet, ha az egyszerűsített számla adott adótartalomhoz tartozó
tételsoraiban szereplő bruttó összegek összege eltér az összesítésében, az adott
adótartalomnál szereplő bruttó összegtől.

```
Tolerált eltérés: számla bruttó értékének 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineGrossAmountSimplified
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatContentGrossAmount
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatContentGrossAmount
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -


**Azonosító: 921.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_VAT_CONTENT_GROSS_AMOUNT_HUF
_SUMMARY_SIMPLIFIED
Figyelmeztetés szövege: Az egyszerűsített számla egy vagy több adótartalomhoz tartozó tételsoraiban
szereplő forintban megadott bruttó értékek összege, eltér az összesítésében a
hozzá tartozó adótartalomnál szereplő forintban feltüntetett bruttó összegtől.
Működés:** Figyelmeztet, ha az egyszerűsített számla adott adótartalomhoz tartozó
tételsoraiban szereplő forintban megadott bruttó összegek összege eltér az
összesítésében, az adott adótartalomnál szereplő bruttó összeg forintban
szereplő értékétől.

```
Tolerált eltérés: vatContentGrossAmountHUF értékének 1%-a, de legalább 1 HUF
és a számla pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsSimplified/
lineGrossAmountSimplifiedHUF
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatContentGrossAmountHUF
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatContentGrossAmountHUF
**Hatókör:
operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED + + + -

##### AGGREGATE - - - -


**Azonosító: 930.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_INVOICE_VAT_AMOUNT
Figyelmeztetés szövege: A számlaösszesítő áfatartalmanként összegzett bruttó értéke eltér a számla
bruttó értékétől.
Működés:** Figyelmeztet, ha az egyszerűsített számlában a számlaösszesítő áfatartalmanként
t összegzett bruttó értéke eltér a számla bruttó értékétől.

```
Tolerált eltérés: invoiceGrossAmount 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatContentGrossAmount
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmount
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmount
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED + + + -

##### AGGREGATE - - - -


**Azonosító: 931.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_INVOICE_VAT_AMOUNT_HUF
Figyelmeztetés szövege: A számlaösszesítő áfatartalmanként összegzett bruttó értéke forintban eltér a
számla forintban feltüntetett bruttó értékétől.
Működés:** Figyelmeztet, ha az egyszerűsített számlában a számlaösszesítő áfatartalmanként
összegzett bruttó értéke forintban eltér a számla forintban megadott bruttó
értékétől.

```
Tolerált eltérés: invoiceGrossAmountHUF 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatContentGrossAmountHUF
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmountHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmountHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED + + + -

##### AGGREGATE - - - -


**Azonosító: 941.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_CALCULATION
helytelen összesítésszámítás
**Figyelmeztetés kód: INCORRECT_SUMMARY_CALCULATION_INVOICE_NET_AMOUNT_LINE_HUF
Figyelmeztetés szövege: A számlasor(ok) forintban megadott nettó értéke(inek) összege eltér a
számla forintban feltüntetett nettó értékétől.
Működés:** Figyelmeztet, ha a számlasor(ok) forintban szereplő nettó értéke(inek) összege
eltér a számla forintban megadott nettó értékétől.

```
Tolerált eltérés: invoiceNetAmountHUF 1%-a, de legalább 1 HUF és a számla
pénznemének 0,01 egysége közül a nagyobb.
```
```
MODIFY esetben csak akkor fut le, ha létezik a lineAmountsNormal csomópont
```
InvoiceData/invoiceMain/invoice/invoiceLines/line/lineAmountsNormal/
lineNetAmountData/lineNetAmountHUF
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceNetAmountHUF
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceNetAmountHUF
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** + + + -


**Azonosító: 970.
Figyelmeztetés csoport:** LINE_SUMMARY_TYPE_MISMATCH
sor-összesítés típuseltérés
**Figyelmeztetés kód: LINE_SUMMARY_TYPE_MISMATCH_SUMMARY_SIMPLIFIED
Figyelmeztetés szövege: Hibás számlaösszesítő. Normál vagy gyűjtőszámla egyszerűsített
számlaösszesítőt tartalmaz.
Működés:** Figyelmeztet, ha normál-, vagy gyűjtőszámlában egyszerűsített számla
összesítő adatok kerülnek kitöltésre.

InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/invoiceCategory
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE + + + -

**Megjegyzés:** ERROR szintre emelve.

**Azonosító: 990.
Figyelmeztetés csoport:** LINE_SUMMARY_TYPE_MISMATCH
sor-összesítés típuseltérés
**Figyelmeztetés kód: LINE_SUMMARY_TYPE_MISMATCH_SUMMARY_NORMAL
Figyelmeztetés szövege: Hibás számlaösszesítő. Az egyszerűsített számla normál számlaösszesítőt
tartalmaz.
Működés:** Figyelmeztet, ha egyszerűsített számlában normál számla összesítő adatok
kerülnek kitöltésre.

InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/invoiceCategory
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED + + + -

##### AGGREGATE - - - -

**Megjegyzés:** (^) ERROR szintre emelve.


**Azonosító: 1070.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adatok
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_INVOICE_VAT_AMOUNT_HUF
Figyelmeztetés szövege: Eltérés az áfaösszeg eredeti pénznemben és forintban megadott értékei
között.
Működés:** Figyelmeztet, ha a számla áfaösszege a számla pénznemében és a számla
áfaösszege forintban eltér egymástól, figyelembe véve az alkalmazott
árfolyamot.
invoiceVatAmount * exchangeRate <> invoiceVatAmountHUF

```
A tolerált eltérés a forintban kifejezett érték 1%-a, de legalább 1 HUF és a
számla pénznemének 0,01 egysége közül a nagyobb.
```
```
Csak akkor fut le, ha mindhárom elem kitöltött.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/
exchangeRate
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceVatAmount
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceVatAmountHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceVatAmountHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - - -


**Azonosító: 1071.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adatok
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_INVOICE_NET_AMOUNT_HUF
Figyelmeztetés szövege: Eltérés a számla eredeti pénznemben és forintban megadott nettó értékei
között.
Működés:** Figyelmeztet, ha a számla nettó összege és a számla nettó összege forintban
eltér egymástól, figyelembe véve az alkalmazott árfolyamot.
invoiceNetAmount * exchangeRate <> invoiceNetAmountHUF

```
A tolerált eltérés a forintban kifejezett érték 1%-a, de legalább 1 HUF és a
számla pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceNetAmount
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceNetAmountHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceNetAmountHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - - -


**Azonosító: 1072.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adatok
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_INVOICE_VAT_CONTENT_GROSS_AMOUNT_
HUF
Figyelmeztetés szövege: Eltérés az egyszerűsített számla eredeti pénznemben és forintban megadott
bruttó értékei között.
Működés:** Figyelmeztet, ha az egyszerűsített számla adótartalomhoz tartozó értékesítés
vagy szolgáltatás nyújtás bruttó összege és annak forintban meghatározott
összege eltér egymástól, figyelembe véve az alkalmazott árfolyamot.
vatContentGrossAmount * exchangeRate <> vatContentGrossAmountHUF

```
A tolerált eltérés a forintban kifejezett érték 1%-a, de legalább 1 HUF és a
számla pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatContentGrossAmount
InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatContentGrossAmountHUF
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceSummary/summarySimplified/
vatContentGrossAmountHUF
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -


**Azonosító: 1073.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adatok
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_INVOICE_GROSS_AMOUNT_HUF
Figyelmeztetés szövege: Eltérés a számla eredeti pénznemben és forintban megadott bruttó összegei
között.
Működés:** Figyelmeztet, ha a számla bruttó összege és a számla bruttó összege forintban
eltér egymástól, figyelembe véve az alkalmazott árfolyamot.
invoiceGrossAmount * exchangeRate <> invoiceGrossAmountHUF

```
A tolerált eltérés a forintban kifejezett érték 1%-a, de legalább 1 HUF és a
számla pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmount
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmountHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmountHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** + + + -
**AGGREGATE** - - - -


**Azonosító: 1074.
Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adatok
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_INVOICE_VAT_RATE_NET_AMOUNT_HUF
Figyelmeztetés szövege: Eltérés a számla eredeti pénznemben és forintban megadott adómértékhez
tartozó értékesítés vagy szolgáltatásnyújtás nettó összegei között.
Működés:** Figyelmeztet, ha a számla adott adómértékhez tartozó értékesítés vagy
szolgáltatásnyújtás nettó összege és nettó összege forintban eltér egymástól,
figyelembe véve az alkalmazott árfolyamot.
vatRateNetAmount * exchangeRate <> vatRateNetAmountHUF

```
A tolerált eltérés a forintban kifejezett érték 1%-a, de legalább 1 HUF és a
számla pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateNetData/vatRateNetAmount
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateNetData/vatRateNetAmountHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateNetData/vatRateNetAmountHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + + + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - - -


**Azonosító: 1075.**

**Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adatok
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_INVOICE_VAT_RATE_VAT_AMOUNT_HUF
Figyelmeztetés szövege: Eltérés a számla eredeti pénznemben és forintban megadott adómértékhez
tartozó értékesítés vagy szolgáltatásnyújtás áfaösszegei között.
Működés:** Figyelmeztet, ha a számla adott adómértékhez tartozó értékesítés vagy
szolgáltatásnyújtás áfaösszege és áfaösszege forintban eltér egymástól,
figyelembe véve az alkalmazott árfolyamot.
vatRateVatAmount * exchangeRate <> vatRateVatAmountHUF

```
A tolerált eltérés a forintban kifejezett érték 1%-a, de legalább 1 HUF és a
számla pénznemének 0,01 egysége közül a nagyobb.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/exchangeRate
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateVatData/vatRateVatAmount
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateVatData/vatRateVatAmountHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
summaryByVatRate/vatRateVatData/vatRateVatAmountHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + + + -

##### SIMPLIFIED - - - -

##### AGGREGATE - - - -


**Azonosító: 1090.**^

**Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adatok
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_INVOICE_NET_AMOUNT**

**Figyelmeztetés szövege: Eredeti (CREATE) számla nettó összege nem lehet negatív.
Működés:** Figyelmeztet, ha eredeti számla (CREATE) esetén a normál vagy gyűjtőszámla
nettó összege negatív érték.

InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceNetAmount
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceSummary/summaryNormal/
invoiceNetAmount
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** + - - -
**SIMPLIFIED** - - - -
**AGGREGATE** + - - -

**Azonosító: 1100.**

**Figyelmeztetés csoport:** INCORRECT_SUMMARY_DATA
helytelen összesítő adatok
**Figyelmeztetés kód: INCORRECT_SUMMARY_DATA_INVOICE_GROSS_AMOUNT**

**Figyelmeztetés szövege: Eredeti (CREATE) egyszerűsített számla bruttó összege nem lehet negatív.
Működés:** Figyelmeztet, ha eredeti számla (CREATE) esetén az egyszerűsített számla bruttó
összege negatív érték.
Csak akkor fut, ha invoiceGrossAmount kitöltött.

InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmount
**Találat esetén hibásként
megjelölt elem:**

InvoiceData/invoiceMain/invoice/invoiceSummary/summaryGrossData/
invoiceGrossAmount
**Hatókör:
operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - - -
**SIMPLIFIED** + - - -
**AGGREGATE** - - - -


### I.5 INKONZISZTENS SZÁMLAMÓDOSÍTÁSI ADATOK CSOPORT

```
Azonosító: 1140.
```
```
Figyelmeztetés csoport: INCONSISTENT_MODIFICATION_DATA
Inkonzisztens számlamódosítás adatok
Figyelmeztetés kód: INCONSISTENT_MODIFICATION_DATA_STORNO_ALREADY_EXISTS
Figyelmeztetés szövege: A hivatkozott alapszámlára korábban már érkezett sztornó okirat
Működés: Módosító vagy érvénytelenítő számlaként beküldött számla (API
invoiceOperation=MODIFY vagy invoiceOperation=STORNO) esetén
figyelmeztet, ha a hivatkozott alapszámlára (CREATE) korábban már érkezett
érvénytelenítő számláról szóló adatszolgáltatás (API
invoiceOperation=STORNO).
```
```
Csak akkor fut le, ha az adatszolgáltatás beküldésekor az API
invoiceOperation=MODIFY vagy invoiceOperation=STORNO.
Jogelőd számlájára való hivatkozásnál a jogelőd és a jogutód számlalánc
elemeit is figyelembe veszi.
```
```
Találat esetén hibásként
megjelölt elem:
```
```
InvoiceData/invoiceMain/invoice/invoiceReference/originalInvoiceNumber
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - + + -

##### SIMPLIFIED - + + -

##### AGGREGATE - + + -


**Azonosító: 1200.**

**Figyelmeztetés csoport:** INCONSISTENT_MODIFICATION_DATA
Inkonzisztens számlamódosítás adatok
**Figyelmeztetés kód: INCONSISTENT_MODIFICATION_DATA_NETAMOUNT_NOT_ZERO_NORMAL
Figyelmeztetés szövege: Érvénytelenítő számla nettó összege nem ad nullát az alapszámla
módosításaival összesített nettó összegével összeadva
Működés:** Érvénytelenítő számlaként (API invoiceOperation=STORNO) beküldött normál
vagy gyűjtőszámla esetén figyelmeztet, ha a hivatkozott alapszámlának és
korábbi módosításainak összesített nettó összegéhez (invoiceNetAmount) a
STORNO operációval beküldött számla összegét hozzáadva nem nulla adódik.

```
Tolerált eltérés: 1 egység a számla pénznemében.
```
```
Csak akkor fut le, ha az adatszolgáltatás beküldésekor az API
invoiceOperation=STORNO és modifyWithoutMaster = false és a korábbi
módosítások lánca (modificationIndex) hiánytalan.
Jogelőd számlájára való hivatkozásnál a jogelőd és a jogutód számlalánc
elemeit is figyelembe veszi.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/SummaryNormal/
invoiceNetAmount
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/SummaryNormal/
invoiceNetAmount
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - + -


**Azonosító: 1210.
Figyelmeztetés csoport:** INCONSISTENT_MODIFICATION_DATA
Inkonzisztens számlamódosítás adatok
**Figyelmeztetés kód: INCONSISTENT_MODIFICATION_DATA_AMOUNT_NOT_ZERO_SIMPLIFIED
Figyelmeztetés szövege: Érvénytelenítő egyszerűsített számla bruttó összege nem ad nullát az
alapszámla módosításaival összesített bruttó összegével összeadva
Működés:** Érvénytelenítő számlaként (API invoiceOperation=STORNO) beküldött
egyszerűsített számla esetén figyelmeztet, ha a hivatkozott alapszámlának és
korábbi módosításainak összesített bruttó összegéhez (invoiceGrossAmount) a
STORNO operációval beküldött számla összegét hozzáadva nem nulla adódik.

```
Tolerált eltérés: 1 egység a számla pénznemében.
```
```
Csak akkor fut le, ha az adatszolgáltatás beküldésekor az API
invoiceOperation=STORNO és a korábbi módosítások lánca (modificationIndex)
hiánytalan.
Jogelőd számlájára való hivatkozásnál a jogelőd és a jogutód számlalánc
elemeit is figyelembe veszi.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/SummarySimplified/
invoiceGrossAmount
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/SummarySimplified/
invoiceGrossAmount
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - - - -

##### SIMPLIFIED - - + -

##### AGGREGATE - - - -


**Azonosító: 1220.**

**Figyelmeztetés csoport:** INCONSISTENT_MODIFICATION_DATA
Inkonzisztens számlamódosítás adatok
**Figyelmeztetés kód: INCONSISTENT_MODIFICATION_DATA_VATAMOUNT_NOT_ZERO
Figyelmeztetés szövege: Érvénytelenítő számla ÁFA összege nem ad nullát az alapszámla
módosításaival összesített ÁFA összegével összeadva
Működés:** Érvénytelenítő számlaként beküldött számla (API invoiceOperation=STORNO)
esetén figyelmeztet, ha a hivatkozott alapszámlának és módosításainak
összesített áfa összegéhez (invoiceVatAmount) a STORNO számla áfa összegét
adva nem nulla adódik.

```
Tolerált eltérés: 1 egység a számla pénznemében.
```
```
Csak akkor fut le, ha az adatszolgáltatás beküldésekor az API
invoiceOperation=STORNO és modifyWithoutMaster = false és a korábbi
módosítások lánca (modificationIndex) hiánytalan.
Jogelőd számlájára való hivatkozásnál a jogelőd és a jogutód számlalánc
elemeit is figyelembe veszi.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/SummaryNormal/
invoiceVatAmount
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/SummaryNormal/
invoiceVatAmount
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - + -


**Azonosító: 1230.**

**Figyelmeztetés csoport:** INCONSISTENT_MODIFICATION_DATA
Inkonzisztens számlamódosítás adatok
**Figyelmeztetés kód: INCONSISTENT_MODIFICATION_DATA_VATAMOUNT_NOT_ZERO_HUF
Figyelmeztetés szövege: Érvénytelenítő számla ÁFA összege forintban nem ad nullát az alapszámla
módosításaival összesített ÁFA forint összegével összeadva
Működés:** Érvénytelenítő számlaként (API invoiceOperation=STORNO) beküldött számla
esetén figyelmeztet, ha a hivatkozott alapszámlának és korábbi módosításainak
összesített forintban meghatározott áfa összegéhez (invoiceVatAmountHUF) a
STORNO számla forintban meghatározott áfa összegét adva nem nulla adódik.

```
Tolerált eltérés: 1 forint, illetve a számla pénznemének 0,01 egysége közül a
nagyobb.
```
```
Csak akkor fut le, ha az adatszolgáltatás beküldésekor az API
invoiceOperation=STORNO és a korábbi módosítások lánca (modificationIndex)
hiánytalan.
```
InvoiceData/invoiceMain/invoice/invoiceSummary/SummaryNormal/
invoiceVatAmountHUF
**Találat esetén hibásként
megjelölt elem:**

```
InvoiceData/invoiceMain/invoice/invoiceSummary/SummaryNormal/
invoiceVatAmountHUF
```
**Hatókör:** (^)
**operation/
invoiceCategory CREATE**^ **MODIFY**^ **STORNO**^ **ANNUL**^
**NORMAL** - - + -
**SIMPLIFIED** - - - -
**AGGREGATE** - - + -


## II. AZ ONLINE SZÁMLA RENDSZER ÁLTAL KÜLDÖTT INFORMÁCIÓS ÜZENETEK

```
Azonosító: 10 311.
INFO csoport: INFO
INFO kód: INCORRECT_DATE_INVOICE_ISSUE_DATE_EARLY
INFO szövege: Számla kelte több, mint 1 0 nappal korábbi, mint az adatszolgáltatás dátuma.
Működés: Jelez, ha a számla kelte lényegesen korábbi, mint az adatszolgáltatás dátuma.
```
```
Tolerált eltérés: 1 0 nap.
```
```
InvoiceData/invoiceIssueDate
Találat esetén megjelölt
elem:
```
```
InvoiceData/invoiceIssueDate
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + - - -

##### SIMPLIFIED + - - -

##### AGGREGATE + - - -

```
Azonosító: 10082.
INFO csoport: INCORRECT_HEAD_DATA
helytelen számlafej adat
INFO kód: INCORRECT_HEAD_DATA_CUSTOMER_TAXPAYERID_DIFFERS
INFO szövege: A vevő adószáma nem egyezik az alapszámlán feltüntetett vevői adószámmal.
Működés: Jelez, ha a MODIFY/STORNO számlán feltüntetett vevő belföldi adószáma eltér az
alapszámlán feltüntetett vevő belföldi adószámától.
```
```
Csak akkor fut, ha customerVatData kitöltött.
```
```
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerVatData/
customerTaxNumber
Találat esetén megjelölt
elem:
```
```
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo/customerVatData/
customerTaxNumber
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - + + -

##### SIMPLIFIED - + + -

##### AGGREGATE - + + -


**Azonosító: 10021.
INFO csoport:** INCORRECT_HEAD_DATA
helytelen számlafej adat
**INFO kód: INCORRECT_HEAD_DATA_SUPPLIER_BANKACCOUNT_MISSING
INFO szövege: Eladó bankszámlaszáma hiányzik.
Működés:** Jelez, ha a Fizetés módja ki van töltve és értéke banki átutalás
(paymentMethod=TRANSFER), de supplierBankAccountNumber nincs kitöltve.

InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/paymentMethod
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierBankAccountNumber
**Találat esetén megjelölt
elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/supplierInfo/
supplierBankAccountNumber
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL + - - -

##### SIMPLIFIED + - - -

##### AGGREGATE + - - -

**Megjegyzés:** (^) Inaktív.


**Azonosító: 11250.
INFO csoport:** INCONSISTENT_MODIFICATION_DATA
Inkonzisztens számlamódosítás adatok
**INFO kód: MODIFICATIONINDEX_SEQUENCE_INCOMPLETE
INFO szövege: Számla módosítás sorszámozása hiányos
Működés:** Jelez, ha a beküldött módosítás az adott alapszámlához korábban beérkezett
módosításokkal együtt nem ad hiánytalan modificationIndex sorozatot.

```
Csak akkor fut le, ha az adatszolgáltatás beküldésekor az API
invoiceOperation=MODIFY vagy invoiceOperation=STORNO.
Csak akkor fut le, ha modifyWithoutMaster=false
```
```
Jogelőd számlájára való hivatkozásnál a jogelőd és a jogutód számlalánc
elemeit is figyelembe veszi.
```
```
InvoiceData/invoiceMain/invoice/invoiceReference/modificationIndex
```
**Találat esetén megjelölt
elem:**

```
InvoiceData/invoiceMain/invoice/invoiceReference/modificationIndex
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - + + -

##### SIMPLIFIED - + + -

##### AGGREGATE - + + -


**Azonosító: 11400.
INFO csoport:** INFO
**INFO kód: UNINTENDED_MODIFICATION_DELIVERY_DATE
INFO szövege: A módosítás az eredeti számla teljesítési dátumát a módosító számla keltére
módosítja
Működés:** Jelez, ha a beküldött módosítás vagy érvénytelenítés az alapszámla teljesítési
dátumát a módosító számla keltére módosítja. Ez egy többször előforduló hiba
a számlázó programokban.

```
Csak akkor fut le, ha a módosító vagy érvénytelenítő számla tartalmaz tételsort
vagy a vevő adataiban van változás az alapszámlához képest.
```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/
invoiceDeliveryDate
InvoiceData/invoiceIssueDate
InvoiceData/invoiceMain/invoice/invoiceHead/customerInfo
**Találat esetén megjelölt
elem:**

```
InvoiceData/invoiceMain/invoice/invoiceHead/invoiceDetail/
invoiceDeliveryDate
```
**Hatókör:** (^)
**operation/
invoiceCategory**

##### CREATE MODIFY STORNO ANNUL

##### NORMAL - + + -

##### SIMPLIFIED - + + -

##### AGGREGATE - + + -

**Megjegyzés:** (^) Inaktív.


## III. AZ ONLINE SZÁMLA RENDSZER ADATSZÓTÁRA................................................................................

### III.1 MEGFELELTETÉS

```
Adat megnevezése Elemnév a sémaleíróban
Felső szintű adatok InvoiceData
```
#### Számla vagy módosító okirat sorszáma - Áfa tv. 169. § b) vagy 170. § (1) b) invoiceNumber

#### Számla vagy módosító okirat kelte - Áfa tv. 169. § a), Áfa tv. 170. § (1) a) invoiceIssueDate

#### Jelöli, ha az adatszolgáltatás maga a számla (a számlán nem szerepel több adat) completenessIndicator

```
Módosítás, vagy érvénytelenítés adatai invoiceReference
```
#### Az eredeti számla száma - Áfa tv. 170. § (1) c) originalInvoiceNumber

#### Annak jelzése, hogy a módosítás olyan alapszámlára hivatkozik, melyről a módosítás pillanatáig nem

#### történt adatszolgáltatás

#### modifyWithoutMaster

#### A számlára vonatkozó módosító okirat egyedi sorszáma modificationIndex

```
Számlafej (bizonylat egészére vonatkozó adatok) invoiceHead
Eladó adatai supplierInfo
```
#### Belföldi adószám, amely alatt a számlán szereplő termékértékesítés vagy szolgáltatásnyújtás történt.

#### Lehet csoportazonosító szám is

#### supplierTaxNumber

#### Csoporttag adószáma, ha a termékbeszerzés vagy szolgáltatás nyújtása csoportazonosító szám alatt

#### történt

#### groupMemberTaxNumber

#### Az eladó (szállító) neve supplierName

#### Az eladó (szállító) címe supplierAddress

#### Az eladó (szállító) bankszámlaszáma supplierBankAccountNumber

```
Vevő adatai customerInfo
```

#### Vevő áfa szerinti státusza customerVatStatus

#### A vevő áfaalanyisági adatai customerVatData

#### Adószám, amely alatt a számlán szereplő termékbeszerzés vagy szolgáltatás igénybevétele történt. Lehet

#### csoportazonosító szám is

#### customerTaxNumber

#### Csoporttag adószáma, ha a termékbeszerzés vagy szolgáltatás nyújtása csoportazonosító szám alatt

#### történt

#### groupMemberTaxNumber

#### Közösségi adószám communityVatNumber

#### Harmadik országbeli adóazonosító thirdStateTaxId

#### A vevő neve customerName

#### A vevő címe customerAddress

#### Vevő bankszámlaszáma customerBankAccountNumber

**Pénzügyi képviselő adatai fiscalRepresentativeInfo**

#### Pénzügyi képviselő adószáma fiscalRepresentativeTaxNumber

#### Pénzügyi képviselő neve fiscalRepresentativeName

#### Pénzügyi képviselő címe fiscalRepresentativeAddress

#### Pénzügyi képviselő által a számlakibocsátó (eladó) számára megnyitott bankszámla bankszámlaszáma fiscalRepresentativeBankAccountNumber

**Számla részletező adatok invoiceDetail**

#### A számla típusa, módosító okirat esetén az eredeti számla típusa invoiceCategory

#### Teljesítés dátuma (ha nem szerepel a számlán, akkor azonos a számla keltével) - Áfa tv. 169. § g) invoiceDeliveryDate

#### Ha a számla egy időszakra vonatkozik, akkor az időszak első napja invoiceDeliveryPeriodStart

#### Ha a számla egy időszakra vonatkozik, akkor az időszak utolsó napja invoiceDeliveryPeriodEnd

#### Számviteli teljesítés dátuma. Időszak esetén az időszak utolsó napja invoiceAccountingDeliveryDate


#### Annak jelzése, ha a felek a termékértékesítés, szolgáltatásnyújtás során időszakonkénti elszámolásban

#### vagy fizetésben állapodnak meg, vagy a termékértékesítés, szolgáltatásnyújtás ellenértékét

#### meghatározott időpontra állapítják meg.

#### periodicalSettelment

#### Kisadózó jelzése smallBusinessIndicator

#### A számla pénzneme az ISO 4217 szabvány szerint currencyCode

#### HUF-tól különböző pénznem esetén az alkalmazott árfolyam: egy egység értéke HUF-ban exchangeRate

#### Közmű elszámoló-számla jelölése (2013.évi CLXXXVIII törvény szerinti elszámoló-számla) utilitySettlementIndicator

#### Önszámlázás jelölése (önszámlázás esetén true) - Áfa tv. 169. § l). selfBillingIndicator

#### Fizetés módja paymentMethod

#### Fizetési határidő paymentDate

#### Pénzforgalmi elszámolás jelölése, ha az szerepel a számlán - Áfa tv. 169. § h). Értéke true pénzforgalmi

#### elszámolás esetén

#### cashAccountingIndicator

#### A számla vagy módosító okirat megjelenési formája invoiceAppearance

**Számlasor(ok)ra vonatkozó adatok invoiceLines**

#### Jelöli, ha az adatszolgáltatás méretcsökkentés miatt összevont soradatokat tartalmaz mergedItemIndicator

#### Számlatétel sorszáma lineNumber

#### Tételsor módosítás jellegének jelölése lineModificationReference

#### Hivatkozás kapcsolódó tételekre, ha ez az Áfa törvény alapján szükséges referenceToOtherLines

#### Előleghez kapcsolódó adatok advanceData

#### Termékkódok productCodes

#### A tétel mennyiségi egysége természetes mértékegységben kifejezhető lineExpressionIndicator

#### Termékértékesítés vagy szolgáltatás nyújtás jellegének jelzése lineNatureIndicator

#### Termék vagy szolgáltatás megnevezése lineDescription

#### Termék vagy szolgáltatás mennyisége quantity

#### Termék vagy szolgáltatás mennyiségi egysége unitOfMeasure

#### A számlán szereplő mennyiségi egység literális kifejezése unitOfMeasureOwn


#### Egységár a számla pénznemében unitPrice

#### Egységár forintban unitPriceHUF

#### Tételhez tartozó árengedmény lineDiscountData

#### Normál és gyűjtőszámla esetén kitöltendő adatok lineAmountsNormal

#### Egyszerűsített számla esetén kitöltendő tétel érték adatok lineAmountsSimplefied

#### Közvetített szolgáltatás intermediatedService

#### Gyűjtőszámla adatok aggregateInvoiceLineData

#### Új közlekedési eszköz értékesítés - Áfa tv. 89. § ill. 169. § o) newTransportMean *

#### Betétdíj depositIndicator

#### Különbözet szerinti szabályozás jelölése - Áfa tv. 169. § p), q) marginSchemeIndicator

#### Termékdíjfizetési kötelezettség obligatedForProductFee

#### Földgáz, villamos energia, szén jövedéki adója forintban - Jöt. 118. § (2) GPCExcise

#### Gázolaj adózottan történő beszerzésének adatai – 45/2016. (XI. 29.) NGM rendelet 75. § (1) a) dieselOilPurchase

#### Neta tv-ben meghatározott adókötelezettség az adó alanyát terheli. 2011. évi CIII. tv. 3.§ (2) netaDeclaration

#### A környezetvédelmi termékdíjról szóló 2011. évi LXXXV. tv. szerinti, tételre vonatkozó záradékok productFeeClause

#### A tétel termékdíj tartalmára vonatkozó adatok lineProductFeeContent

#### A számlafeldolgozást segítő, egyezményesen nevesített, egyéb adatok conventionalLineInfo

#### A termék/szolgáltatás tételhez kapcsolódó, további adat additionalLineData

**Termékdíjjal kapcsolatos összesítő adatok productFeeSummary**

**Összesítő adatok (Áfa törvény szerint) invoiceSummary**

#### Számla összesítés (nem egyszerűsített számla esetén) summaryNormal

#### Összesítés áfamérték vagy adómentesség szerint summaryByVatRate

#### A számla nettó összege a számla pénznemében invoiceNetAmount

#### A számla nettó összege forintban invoiceNetAmountHUF

#### A számla áfaösszege a számla pénznemében invoiceVatAmount


#### A számla áfaösszege forintban invoiceVatAmountHUF

#### Egyszerűsített számla összesítés summarySimplified

#### Egyszerűsített számla esetén az adótartalom aránya vagy adómentesség jelzése vatRate

#### Az adott adótartalomhoz tartozó értékesítés vagy szolgáltatásnyújtás bruttó összege a számla

#### pénznemében

#### vatContentGrossAmount

#### Az adott adótartalomhoz tartozó értékesítés vagy szolgáltatásnyújtás bruttó összege forintban vatContentGrossAmountHUF

#### A számla bruttó összege a számla pénznemében invoiceGrossAmount

#### A számla bruttó összege forintban invoiceGrossAmountHUF

* - Az adatszolgáltatással érintett számlákban az elem tartalma nem releváns.

### III.2 KÖTELEZŐSÉGEK

#### Elemnév a sémaleíróban Technikailag szükséges Áfa törvény szerint kötelező Adatszolgáltatásban kötelező

#### invoiceNumber Igen Igen Igen

#### invoiceIssueDate Igen Igen (explicit vagy implicit módon) Igen

#### completenessIndicator Igen Nem Igen

**invoiceReference Nem Módosítás vagy érvénytelenítés esetén igen** (^) Ha releváns

#### originalInvoiceNumber Nem Módosítás vagy érvénytelenítés esetén igen Ha releváns

#### modifyWithoutMaster Igen Nem Igen

#### modificationIndex Igen Nem Igen (ha a szülőelem szerepel)

#### invoiceHead Igen Nem Igen

#### supplierInfo Igen Igen Igen

#### supplierTaxNumber Igen Igen Igen

#### groupMemberTaxNumber Nem Ha releváns Ha releváns

#### supplierName Nem Igen Igen


#### supplierAddress Nem Igen Igen

#### supplierBankAccountNumber Nem Nem Nem

**customerInfo Igen Igen** (^) Igen

#### customerVatStatus Igen Nem Igen

#### customerTaxNumber Ha releváns Feltételekkel igen Ha releváns

#### groupMemberTaxNumber Nem Ha releváns Ha releváns

#### communityVatNumber Nem Ha releváns Ha releváns

#### thirdStateTaxId Nem Ha releváns Ha releváns

#### customerName Nem Ha releváns

#### Ha releváns (kivéve

#### magánszemély)

#### customerAddress Nem Ha releváns

#### Ha releváns (kivéve

#### magánszemély)

#### customerBankAccountNumber Nem Nem Nem

#### fiscalRepresentativeInfo Nem Ha releváns Ha releváns

#### fiscalRepresentativeTaxNumber Nem Ha releváns Ha releváns

#### fiscalRepresentativeName Nem Ha releváns Ha releváns

#### fiscalRepresentativeAddress Nem Ha releváns Ha releváns

#### fiscalRepresentativeBankAccountNumber Nem Nem Nem

**invoiceDetail Igen Igen** (^) Igen

#### invoiceCategory Igen Igen Igen

#### invoiceDeliveryDate Igen Normál számla esetén igen Igen

#### invoiceDeliveryPeriodStart Nem Nem Nem

#### invoiceDeliveryPeriodEnd Nem Nem Nem

#### invoiceAccountingDeliveryDate Nem Nem Nem


#### periodicalSettelment Nem Nem Ha releváns

#### smallBusinessIndicator Nem Nem Nem

#### currencyCode Igen Ha releváns Igen

#### exchangeRate Nem Nem Igen

#### utilitySettlementIndicator Nem Ha releváns Ha releváns

#### selfBillingIndicator Nem Ha releváns Ha releváns

#### paymentMethod Nem Nem Nem

#### paymentDate Nem Nem Nem

#### cashAccountingIndicator Nem Ha releváns Ha releváns

**invoiceLines Számla esetén igen**

```
Számla esetén igen, módosítás esetén, ha
releváns
```
#### Ha releváns

#### mergedItemIndicator Számla esetén igen^

```
Számla esetén igen, módosítás esetén, ha
```
#### releváns Ha releváns^

#### lineNumber Igen Nem Igen

#### lineModificationReference

#### Módosítás/érvénytelenítés

#### esetén igen

#### Nem

#### Módosítás/érvénytelenítés

#### esetén igen

#### referenceToOtherLines Nem Ha releváns Ha releváns

#### advanceIndicator Ha releváns Nem Ha releváns

#### advancePaymentData Nem Nem Nem

#### productCodes Nem Nem Nem

#### lineExpressionIndicator Igen Igen Igen

#### lineNatureIndicator Nem Nem Nem

#### lineDescription Nem Igen Igen

#### quantity Nem Ha releváns Ha releváns

#### unitOfMeasure Nem Ha releváns Ha releváns

#### unitOfMeasureOwn Nem Ha releváns Ha releváns


#### unitPrice Nem Ha releváns Ha releváns

#### lineDiscountData Nem Ha releváns Ha releváns

#### lineAmountsNormal Nem Normál/gyűjtőszámla esetén igen

#### Normál/gyűjtőszámla esetén

#### igen

#### lineAmountsSimplefied Nem Egyszerűsített számla esetén igen

#### Egyszerűsített számla esetén

#### igen

#### intermediatedService Nem Ha releváns Ha releváns

#### aggregateInvoiceLineData Nem Gyűjtőszámla esetén igen Gyűjtőszámla esetén igen

#### newTransportMean Nem Ha releváns Ha releváns

#### depositIndicator Nem Ha releváns Ha releváns

#### marginSchemeIndicator Nem Ha releváns Ha releváns

#### ekaerIds Nem Nem Nem

#### obligatedForProductFee Nem Nem Nem

#### GPCExcise Nem Nem Nem

#### dieselOilPurchase Nem Nem Nem

#### netaDeclaration Nem Nem Nem

#### productFeeClause Nem Nem Nem

#### lineProductFeeContent Nem Nem Nem

#### additionalLineData Nem Nem Nem

**productFeeSummary Nem Nem** (^) Nem
**invoiceSummary Igen Egyes esetekben nem** (^) Igen

#### summaryNormal Nem Normál/gyűjtőszámla esetén igen

#### Normál/gyűjtőszámla esetén

#### igen

#### summaryByVatRate Nem Normál/gyűjtőszámla esetén igen

#### Normál/gyűjtőszámla esetén

#### igen


#### invoiceNetAmount Nem Normál/gyűjtőszámla esetén igen

#### Normál/gyűjtőszámla esetén

#### igen

#### invoiceNetAmountHUF Nem Normál/gyűjtőszámla esetén igen

#### Normál/gyűjtőszámla esetén

#### igen

#### invoiceVatAmount Nem Normál/gyűjtőszámla esetén igen

#### Normál/gyűjtőszámla esetén

#### igen

#### invoiceVatAmountHUF Igen Normál/gyűjtőszámla esetén igen

#### Normál/gyűjtőszámla esetén

#### igen

#### summarySimplified Nem Egyszerűsített számla esetén igen

#### Normál/gyűjtőszámla esetén

#### igen

#### vatRate Nem Egyszerűsített számla esetén igen

#### Egyszerűsített számla esetén

#### igen

#### vatContentGrossAmount Nem Egyszerűsített számla esetén igen

#### Egyszerűsített számla esetén

#### igen

#### vatContentGrossAmountHUF Nem Egyszerűsített számla esetén igen

#### Egyszerűsített számla esetén

#### igen

#### invoiceGrossAmount Igen Egyszerűsített számla esetén igen

#### Egyszerűsített számla esetén

#### igen

#### invoiceGrossAmountHUF Igen Egyszerűsített számla esetén igen

#### Egyszerűsített számla esetén

#### igen


## IV. AZ ONLINE SZÁMLA ÉS AZ ONLINE PÉNZTÁRGÉP RENDSZER KAPCSOLATA

Az Online Száma rendszerben (OSA) 2021. október 2-től elérhetővé válnak az online pénztárgépeken
(OPG) 2021. szeptember 30. után kiállított egyes adóügyi bizonylatok adatai az alábbiakban ismertetett
átadási folyamat eredményeként.

Az adatátadás során az OPG rendszerben tárolt adatokból az OSA felé átadásra kerül a pénztárgépes
adóügyi bizonylatok itt meghatározott köre. Az átadott bizonylatok adatai az OSA-ban megszokott

módon érhetőek el gép-gép kapcsolaton és a webportálon egyaránt.

A pénztárgépekre vonatkozó műszaki-technikai szabályozás a 48/2013 (XI. 15.) NGM rendeletben
található.

A leírás célja kizárólag a tájékoztatás, a mellékletben szereplő információk közzététele nem
eredményez az Online Számla rendszerben a számlázóprogramokra nézve követelmény változást.

### IV. I. BIZONYLAT TÍPUSOK

A pénztárgépek által kiállítható bizonylatok típusainak adatait a pénztárgépek Adóügyi Ellenőrző
Egysége (AEE) szabványos XML sémában rögzíti.

Az AEE XML aktuális specifikációja itt található:

https://www.nav.gov.hu/nav/ado/onlinepenztargepek_1417761437385/gyartok_forgalmazok/Kozle
meny_az_onlinepe20210126.html

#### IV. 1. 1. Pénztárgépi bizonylat típusok

Az OPG – OSA átadásban érintett bizonylatok az alábbiak, melyek szerkezetét a fenti XML specifikáció
tartalmazza:

- P17 típusú bizonylatok (sztornó)
- P18 típusú bizonylatok (visszáru)
- P20 típusú bizonylatok (egyszerűsített számlák)

### IV.2. ÁTADÁSI FOLYAMAT

A pénztárgépek a NAV szerverrel történő kommunikációs folyamat részeként szolgáltathatnak adatot.

A szerver oldalán működő terheléselosztási logika határozza meg, hogy a NAV a pénztárgép aktuális
bejelentkezését követően kér-e adatot a pénztárgéptől. Alap esetben 24 óra alatt a bejelentkező
pénztárgéptől átlagosan a NAV szervere kétszer kér állományt, mely során az addig be nem küldött
valamennyi lezárt naplóállományt bekéri. Ettől azonban eltérhet bizonyos esetekben terheléstől vagy
más külső ok miatt (Pl: karbantartás).

Az Online Számla felé a NAV napi egyszeri frissítéssel a hajnali órákban adja át az adokat. Ennek
megfelelően az új pénztárgépes számlák megjelenésére az előző napi forgalomból általános esetben
másnap reggel vagy egy nappal később lehet számítani. Az OPG-s számlák 3.0-s alakra konvertálva
kerülnek betöltésre, így azok kliens oldali feldolgozása külön fejlesztés nélkül, automatikusan
lehetséges.

Az átadás a 2021.09.30-át követően kiállított bizonylatokra indul el, a korábban keletkezett bizonylatok
később sem lesznek elérhetőek. Az OPG rendszer rendszer kialakítása lényegesen korábbi, mint az OSA,


ezért működése teljesen eltérő, más koncepción alapul. Az OPG rendszerben a pénztárgépekről

megvalósított adatküldés más validációs pontokat tartalmaz. Az OSA rendszer inputként kizárólag
olyan OPG bizonylatok adatai jelennek meg, amelyek:

- Sikeresen kiállításra és naplózásra kerültek a pénztárgépen.
- A pénztárgép AEE a vonatkozó naplóállományt sikeresen beküldte a NAV infrastruktúrájába.
- A beküldött naplóállomány feldolgozása sikeresen megtörtént.
- Jelen mellékletben részletezett átadási folyamat sikeresen lezajlik az adott bizonylat adatainak
    vonatkozásában.

A fenti tényekből adódóan tehát lesznek olyan OPG-s bizonylatok, amelyek nem, vagy csak később
fognak bekerülni az Online Számla rendszerbe az OPG rendszeréből.

Ennek alapvetően több oka lehet:

- A pénztárgép nem feldolgozható vagy hibás állományt küld be a NAV részére.
- A pénztárgépen történő kézi bevitel nem megfelelő.
- A pénztárgépről később érkeznek meg az adatok időben.
- A pénztárgépről hiba miatt nem érkeznek be az állományok.

#### IV. 2.1. Bizonylatok szétválasztása

Annak érdekében, hogy az OPG-s számla adatok megfeleljenek az Online Számla által végzett
validációknak, az alábbiakban leírt műveletek elvégzése szükséges.

Az OPG rendszerből minden esetben átadásra kerülnek az egyszerűsített számlák (ESN, P20 típusú
bizonylatok). Ezek az OSA-ban egyszerűsített számlaként (invoiceCategory=”SIMPLIFIED”) jelennek
meg.

Viszont az AEE által leírt adatmodellből csak a P20 típusú bizonylatokról lehet egyértelműen, minden
további vizsgálat nélkül kijelenteni, hogy azok fogalmilag számlát tartalmaznak. Ez a feltételezés a
sztornó (P17) és a visszáru (P18) bizonylatoknál már nem áll fenn, mert azok kapcsolódhatnak
nyugtához és számlához is egyaránt.

Annak érdekében, hogy a P20 típusú bizonylatok módosításai is megjelenhessenek az Online Számla
rendszerben, egy szétválasztási logikát alkalmazunk a P17 és P18 típusú bizonylatokra. Ez alapján a
bizonylatot akkor lehet számlának tekinteni, ha:

- a bizonylat nem megszakított (CNC = 0) **ÉS**
- a bizonylat nem 0 összegű (SUM <> 0) **ÉS**
    o a hivatkozott bizonylat száma (P17/SBN vagy P18/VDB) mező értéke nagybetűre
       konvertálva tartalmazza az ’SZ/’ értéket, **VAGY**
    o a vevő adószáma (VED/ASZ) mezőben balról jobbra található első 8 számjegyből álló
       összefüggő karaktersorozat olyan kód, ami a NAV adózói törzsnyilvántartás szerint
       érvényes adószám és az előzmény bizonylat nem explicit nyugtaként van jelölve
       (P17/SBN vagy P18/VDB mező értéke nem tartalmazza a „NY/” karaktersorozatot.)

A fenti feltételeknek nem megfelelő sztornó és visszáru bizonylatok nem kerülnek átadásra az OSA-ba.

Ezen felül, az OPG rendszerből nem kerülnek átadásra a pénztárgépeken a gyakorló módban kiadott
bizonylatok (EST, VBT, SZT) sem.


#### IV.2.2 Deduplikáció..............................................................................................................................

Az átadási folyamat előtt ellenőrzésre kerül, hogy az egyes OPG-s bizonylatokból képzendő számlaszám
(invoiceNumber) egyedi lesz-e. Egyes speciális esetekben bizonyos műszaki hibás pénztárgépek
ugyanis megsérthetik a bizonylatszám egyediségére vonatkozó szabályokat. A duplikált sorszámú
bizonylatok nem kerülnek átadásra az OSA-ba. A számlasorszámokat egyéves intervallumra
visszamenőleg vizsgálva deduplikálja a rendszer az alábbiak szerint:

- P20 esetén bizonylatszám és a kiállító adószáma alapján,
- P17, P18 esetén bizonylatszám és AP szám alapján.

A deduplikáció során kiszűrt bizonylatok nem kerülnek átadásra.

A deduplikációs fázisban kiszűrésre kerülnek azok a bizonylatok is, amelyek valamilyen műszaki hiba
miatt nem rendelkeznek bizonylatszámmal vagy nincsenek tétel adataik. Ezen bizonylati adatok sem
kerülnek átadásra az OSA felé.

#### IV.2.3 Adószám forgatás ÁFA csoport tagok esetén

Ha a pénztárgépes bizonylaton az eladó ÁFA csoport tagja, akkor az eladó adatai között az átadásban
az ÁFA csoport adószáma jelenik meg.

Az ÁFA csoport tag saját adószámát az átadási logika megőrzi, azokat mint csoport tag adószám
(groupMemberTaxNumber) szerepelteti.

### IV.3 SZÁRMAZTATOTT ADATOK

Annak érdekében, hogy a kliensek minden blokkoló validáción sikeresen átjutó, 3.0 séma valid OPG-s
egyszerűsített számlákat lássanak az OSA-ban, a két adatmodell közti eltérés okán szükség van további,
származtatott adatok megadására is. Megjegyzendő, hogy a származtatott adatok összefüggéseire az
XML transzformációs logika is épít, így a két fejezetben leírt működési logikát össze kell olvasni a teljes
megértéshez.

Ezen származtatott szintén az adattárházi rétegből származnak, az alábbiak szerint.

#### IV.3.1 Vevői adószámra illesztés

Az OPG-s adatmodellben a vevő adószámaként megadható magyar és külföldi adószám is, illetve a
felhasználói adatbevitel eredményeként előálló egyéb karaktersorozat is.

A 9/2016. (III. 25.) NGM rendelet által meghatározott követelményeknek nem megfelelő pénztárgépek
esetén (V1-es gépek) a vevői adószám illesztése nem történik meg. Az érintett pénztárgépek
forgalmazási engedélye 2017 során visszavonásra került, de a jogszabály alapján 2022. júliusáig még
üzemeltethetők a forgalmazási engedély visszavonása előtt üzembe helyezett gépek.

A 9/2016. (III. 25.) NGM rendelet által meghatározott követelményeknek megfelelő pénztárgépek (V2-
es gépek) esetén a következő:

Az átadási folyamat előtt a VED/ASZ mezőben szereplő karaktersorozatban balról jobbra haladva a
rendszer megkeresi az első egybefüggő nyolc számjegyből álló karaktersorozatot. Ha ez a bizonylat
kiállításának napján létező magyar adószám törzsszámaként értelmezhető, akkor ez az adószám lesz a
vevő törzsszáma.


#### IV.3.2 Előzményre illesztés

Az előzményre illesztés célja eldönteni, hogy adott OPG-s módosító vagy sztornó számla előzményes
vagy előzmény nélküli, illetve, hogy mi a módosítások egymáshoz képesti sorrendje, mivel az OSA-ban
ezen adatok a módosító és érvénytelenítő bizonylatok esetén kötelezőek.

Az előzményre illesztés 1 évre visszamenőleg történik, sztornó bizonylat esetén az SBN, visszáru
bizonylat esetén pedig a VDB mező értéke alapján. Az azonos alapbizonylatra hivatkozó módosító
bizonylatokat a logika a kiállításuk szerint időben sorrendezi. A sorrendezés a pénztárgép óráját veszi
alapul, nem pedig a beérkezés időpontját.

Az illesztési művelet kimenete az illesztés logikai sikeressége, az előzmény bizonylat száma, valamint a
módosítás sorrendje. Ha az előzmény számla nem található, akkor a rá hivatkozó módosító bizonylatok
előzmény nélküliként, 1-től induló futó sorszámot kapnak. (az 1 éves vizsgálati időtartamon belül)

#### IV.3.3 Számlasor pozíció illesztése

A számlasor pozíció illesztésének feladata a számlaláncon belül keletkezett tételsorok egyértelmű
azonosítása. Az illesztés előzménye szervesen függ az előző fejezetben leírt előzményre illesztés
kimenetétől.

Sikeresen előzményre illesztett számlalánc esetén a számlasor pozíció az alapszámla max(ITL) + 1
értékétől indul, és duplikáció nélkül, hézagmentesen tart a végtelenbe, figyelembe véve az előzmények
egymáshoz képesti sorrendjét.

A sikertelenül előzményre illesztett számlalánc esetén a számlasor pozíció értéke a lánc minden
tagjánál a számlasor saját, bizonylaton belüli sorszáma.

#### IV.3.4 Karakter konverziós műveletek

A karakter konverzió feladata feloldalni az OPG és az OSA sémák string típusú megszorításai közötti

eltéréseket, az alábbiak szerint.

Whitespace normalizáció

A művelet az egyes unicode karakterekre az alábbi normalizációs műveletet hajtja végre:

```
Unicode karakter Elvégzendő művelet Művelet pozíciója
CR (carriage return) eltávolítás minden előforduláson
LF (line feed)
CRLF (carriage return &
line feed)
SP és minden deriváltja
(space, non-breakable
space, zero-width space
stb)
```
```
levágás csak sor eleji (leading) és
sorvégi (trailing)
előforduláson
```
```
HT (horizontal tabulation) eltávolítás minden előforduláson
```
Defaultolás


Az alapértelmezett (default) érték megadásának szükségessége mindig a normalizáció elvégzése után

kerül megvizsgálásra. Ha a normalizáció után megmaradó karakterlánc nem teljesíti a szükséges hossz

vagy összetételi szabályt, akkor az értéket defaultolni kell a számára meghatározott értékre.

Számla fej adatok konverziója

```
Logikai adat Whitespace normalizáció
mikor szükséges
```
```
Default érték megadás
mikor szükséges
```
```
Default érték
```
```
Eladó irányítászám mindig Ha normalizáció után a
string nem pontosan 4
számból áll
```
##### ’0000’

```
Eladó település Ha normalizáció után a
string null
```
##### ’N/A’

```
Eladó közterület
Eladó közterület jelleg
Eladó házszám
Vevő név ha a vevő nem
magánszemély
```
```
Ha normalizáció után a
string null
```
##### ‘N/A’

```
Vevő irányítászám Ha normalizáció után a
string nem pontosan 4
számból áll
```
##### ‘0000’

```
Vevő település Ha normalizáció után a
string null
```
##### ‘N/A’

```
Vevő közterület
Vevő közterület jelleg
Vevő házszám
```
Számla sor adatok konverziója

```
Logikai adat Whitespace normalizáció
mikor szükséges
```
```
Default érték megadás
mikor szükséges
```
```
Default érték
```
```
Tétel megnevezés mindig Ha normalizáció után a
string null
```
##### ’-’

#### IV.3.5 Összesítő adatok kiszámítása

Az összesítő adatok kiszámításának feladata az OPG-s számla összesítőjét a regiszter adatok (A-E)
összegéből meghatározni.

A művelet kimenete a regiszter adatok ÁFA kulcsokkénti összesítése.

### IV.4 XML TRANSZFORMÁCIÓ

Az XML transzformáció során keletkezik az OPG-s számla adatokból az invoiceData.xsd szerinti számla
XML.

#### IV.4.1 invoiceOperation értékadás

Az OPG-s XML element értéke explicit meghatározza az invoiceOperation értékét, az alábbiak szerint.

ESN –> invoiceOperation = CREATE
VBN –> invoiceOperation = MODIFY
SZN –> invoiceOperation = STORNO


#### IV.4.2 XML root értékadás

Minden számla esetén kötelező a töltése.

```
XML tag OPG forrás Származtatott adat Default kitöltés
invoiceNumber * - -
invoiceIssueDate DTS - -
completenessIndicator - - false
```
* P20 esetén IID, P17 esetén SBS, P18 esetén VBS. Sztornó bizonylat (P1 7 ) esetén „S” prefixet kapnak.

Visszáru bizonylat (P1 8 ) esetén „V” prefixet kapnak. Valamint a kétvállalkozós pénztárgépek esetén a

prefix után egy üzemeltetőt jelölő „/A” vagy „/B” jelölés szerepelhet.

#### IV.4.3 invoiceMain csomópont választás....................................................................................................

Minden számla esetén kötelező a töltése.


A konverziónak mindig az egyes számlákhoz használt **../invoiceMain/invoice** útvonalat kell

kiválasztani, kötegelt módosítás (batch) az OPG-ben fogalmilag nincs.

#### IV.4.4 invoice/invoiceReference értékadás

Csak P17 és P18 esetén kitöltött, P20 esetén nem.


```
XML tag OPG forrás Származtatott adat Default kitöltés
originalInvoiceNumber P17 esetén SBN, P18 esetén VDB - -
modifyWithoutMaster - - *
modificationIndex ld: előzményre
illesztés
```
##### -

* - Ha ORIGINAL_INVOICE_NUMBER != null akkor false, egyébként true.

#### IV.4.5 invoice/invoiceHead csomópont értékadás

Minden számla esetén kötelezően kitöltött.


IV.4.5.1 supplierInfo csomópont értékadás
Minden számla esetén kötelezően kitöltött.

```
XML tag OPG forrás Származtatott adat Default kitöltés
```

```
supplierTaxNumber/taxpayerId TSZ ld: adószám forgatás
ÁFA csoport tagoknál
```
##### -

```
supplierName INF_tip/NAM - -
groupMemberTaxNumber/ taxpayerId * - ld: adószám forgatás
ÁFA csoport tagoknál
```
##### -

supplierAddress/detailedAddress/countryCode - - HU
supplierAddress/detailedAddress/postalCode INF_tip/IRS - -
supplierAddress/detailedAddress/city INF_tip/TEL - -
supplierAddress/detailedAddress/streetName INF_tip/KZT - -
supplierAddress/detailedAddress/publicPlaceCategory INF_tip/KZJ - -
supplierAddress/detailedAddress/number INF_tip/HSZ - -
* - Csak akkor szabad megadni, ha adószám forgatás történt

```
IV.4.5.2 customerInfo csomópont értékadás
Minden számla esetén kötelezően kitöltött.
```

```
XML tag OPG
forrás
```
```
Származtatott
adat
```
```
Default
kitöltés
customerVatStatus * - ld: vevői
adószámra
illesztés
```
##### -

```
customerVatData/customerTaxNumber/taxpayerId** VED/ASZ -
customerName ** VED/NAM -
customerAddress/detailedAddress/countryCode ** - HU
customerAddress/detailedAddress/postalCode ** VED/IRS -
customerAddress/detailedAddress/city ** VED/TEL -
customerAddress/detailedAddress/streetName ** VED/KZT -
customerAddress/detailedAddress/publicPlaceCategory** VED/KZJ -
customerAddress/detailedAddress/number ** VED/HSZ -
```
* - Ha a vevői adószámra illesztés sikertelen akkor PRIVATE_PERSON, egyébként DOMESTIC.

** - Ha customerVatStatus = PRIVATE_PERSON, a számlán sem a vevő neve, sem a címe nem

szerepelhet, még akkor sem, ha megvan rá az adat.

IV.4.5.3 fiscalRepresentativeInfo csomópont értékadás
A csomópont nincs képezve egyik esetben sem.

IV.4.5.4 invoiceDetail csomópont értékadás
Minden számla esetén kötelező a töltése.


**XML tag OPG forrás Származtatott adat Default kitöltés**
invoiceCategory - - SIMPLIFIED
invoiceDeliveryDate * DTS - -
currencyCode - - HUF
exchangeRate - - 1
invoiceAppearance - - PAPER


* - alapszámla (CREATE) és előzmény nélküli módosító vagy sztornó számla esetén a pénztárgépi óra

időpontja. (DTS) Előzményes módosító vagy sztornó számla esetében az alapszámlához tartozó DTS.

#### IV.4.6 invoice/invoiceLines csomópont értékadás

P20 esetén kötelezően kitöltött, P18-ban és P17-ben csak akkor, ha rendelkezésre áll.

```
XML tag OPG forrás Származtatott adat Default kitöltés
mergedItemIndicator - - false
```
IV.4.6.1 line csomópont értékadás
A csomópont kötelezősége azonos a szülőével.



```
XML tag OPG
forrás
```
```
Származtatott
adat
```
```
Default
kitöltés
lineNumber - - -
lineModificationReference/lineNumberReference - ld: számlasor
pozíció
illesztése
```
##### *

```
lineModificationReference/lineOperation - CREATE*
```
```
lineExpressionIndicator - - true
lineDescription ITL/NA - -
quantity ITL/QY - -
unitOfMeasure ITL/IU - PIECE
unitPrice ITL/UN - -
unitPriceHUF ITL/UN - -
```
* - A lineModificationReference reference csomópontot P20 esetén tilos, P17, P18 esetén kötelező

képezni.

IV.4.6.2 lineAmountsSimplified csomópont értékadás
A csomópont kötelezősége azonos a szülőével.


```
XML tag OPG forrás Származtatott
adat
```
**Default
kitöltés**
lineVatRate/vatContent ITL/VC * -
lineVatRate/vatOutOfScope ITL/VC** ** -
lineVatRate/vatOutOfScope/case - ATK
lineVatRate/vatOutOfScope/reason - OPG „D”
gyűjtő
lineVatRate/vatExemption ITL/VC*** *** -
lineVatRate/vatExemption/case - TAM
lineVatRate/vatExemption/reason - OPG „E”
gyűjtő
lineGrossAmountSimplified ITL/SU - -
lineGrossAmountSimplifiedHUF ITL/SU - -


* - ha a használt pénztárgépi gyűjtő (REGISTER_TYPE) A, B vagy C akkor A esetén 0.0476, B esetén

0.1525, illetve C esetén 0.2126

** - ha a használt pénztárgépi gyűjtő (REGISTER_TYPE ) = D

*** - ha a használt pénztárgépi gyűjtő (REGISTER_TYPE) = E

#### IV.4.7 invoice/ProductFeeSummary csomópont értékadás

A csomópont nincs képezve egyik esetben sem.

#### IV.4.8 invoice/invoiceSummary csomópont értékadás

Minden számla esetén kötelező a töltése.

```
XML tag OPG
forrás
```
```
Származtatott
adat
```
```
Default
kitöltés
summarySimplified/vatRate * ld: összesítő
adatok
kiszámítása
```
##### -

```
summarySimplified/vatContentGrossAmount -
summarySimplified/vatContentGrossAmountHUF -
summaryGrossData/invoiceGrossAmount SUM -
summaryGrossData/invoiceGrossAmountHUF SUM -
```

* - a summarySimplified szerkezetet annyiszor kell képezni, amennyiszer adott pénztárgépi regiszter

nem 0 értékkel szerepel az XML-ben.

### IV.5 TRANZAKCIÓS MŰVELETEK

Jelen fejezet az OPG-s bizonylatok adatainak tranzakciós műveleteit, az arra ráépülő OSA funkciók
működését mutatja be.

#### IV.5.1 Adatszolgáltatások

Az előző fejezetek szerint bemutatott, 3.0-ás adatszolgáltatásra kész XML fájlokat külön alrendszer
küldi be az OSA-nak egy dedikált interfészen keresztül. Ezt az adatszolgáltatást a NAV végzi, az
adózónak ezzel kapcsolatban semmilyen felelőssége, feladata nincs.

A beküldés során 1 tranzakció – 1 számla elve érvényesül, kötegelt beküldés nincs. Az adatszolgáltatás
során a tranzakció saját tranzakció azonosítót kap, mely a felületen és a gépi API-n listázva is látható.
A fentiekből következik, hogy az adózó – versengve az adatszolgáltatási alrendszerrel – saját maga is
lekérdezheti ezeknek az adatszolgáltatások eredményét a /queryTransactionStatus operációval, de
fontos megjegyezni, hogy ezeknek a tranzakcióknak a lekérdezését a NAV alrendszere ütemezetten
elvégzi, az nem az adózó feladata. Adózót hátrányos jogkövetkezmény nem terheli azért, mert OPG-s

adatszolgáltatás feldolgozási eredménye nincs vagy nem azonnal került lekérdezésre. A
/queryTransactionStatus operációban az adatszolgáltatás adószám szerinti tulajdonosa az OPG-s
adatszolgáltatás eredeti adatát (returnOriginalRequest) is lekérheti.

#### IV.5.2 Feldolgozási műveletek

Az OPG-s adatszolgáltatások ugyan olyan feldolgozási folyamaton mennek keresztül, mint a többi
forrásból érkező adatszolgáltatások. Ennek megfelelően elképzelhető, hogy blokkoló validáció miatt
ABORTED státuszba kerülnek, vagy a feldolgozásuk sikeres lesz ugyan, de WARN vagy INFO üzenetek
keletkeznek a kiértékelés során. Az adózót hátrányos jogkövetkezmény nem terheli azért, mert OPG-s

adatszolgáltatása ABORTED státuszba került.

ABORTED státuszba - NAV oldali beküldés során - jelenleg egy esetben kerülhet OPG-s bizonylat:

Ha 1 éven belül ugyanarra az alapszámlára úgy érkezik több módosítás, hogy azt az előzményre illesztés
nem találja meg, és így azok az előzmény nélküli ágra kerülnek. Ekkor az első módosító vagy sztornó
számla még feldolgozódik sikeresen, de az utána érkezők feldolgozása INVOICE_LINE_ALREADY_EXISTS
hibával le fog állni.

A fentiektől eltérő blokkoló hibákat a NAV folyamatosan vizsgálni fogja az adatszolgáltatási
alrendszerben, és ha azok kód vagy konverziós hibára vezethetők vissza, akkor intézkedik a javításról
és az újbóli beküldésről.

Az adatszolgáltatások WARN és INFO kiértékelésének megtekintése API-n és a felületen is megtehető.
Ezek a hibák mindig a bizonylat felütésénél, ember által keletkeznek, azok az OSA rendszerben nem
javíthatók. Ebben az esetben javasoljuk a fokozottabb körültekintést a bizonylatok rögzítésénél.

#### IV.5.3 Módosítás, annulálás

Az OPG-s alapszámlák az OSA rendszerben forrásfüggetlenül – értsd: nem csak pénztárgépen keresztül,
hanem gépi számlázóból is – módosíthatók vagy sztornózhatók, két megkötéssel. Az egyik, hogy a
módosító vagy sztornó számla kizárólag egyszerűsített (SIMPLIFIED) típusú lehet, a másik pedig, hogy

az első ilyen nem OPG-s forrásból érkező módosítás vagy sztornó feldolgozása után a szóban forgó P20
bizonylatot pénztárgépen már nem lehet úgy helyesbíteni, hogy az megjelenjen az OSA rendszerben.


Az ilyen OPG-ből érkező P17 vagy P18 bizonylatokat az OSA rendszer az áttöltéskor

MODIFICATION_SOURCE_MISMATCH hibával el fogja buktatni. Ez a másik valid eset, amikor az
adatszolgáltatás ABORTED státuszba kerül. Kérjük, ha egy OPG-s számla módosítása
számlázóprogamon keresztül történt, akkor annak a további módosításai is így történjenek!

OPG-s számlák annulálása sem a gépi interfészen, sem a felületen nem lehetséges az adózók által. OPG-
s számlát annulálni kizárólag a NAV képes, hibajavítás miatt. Ebben az esetben a NAV az annulálást
követően intézkedik az adatok újbóli, helyes adatszolgáltatásának pótlása felől.

#### IV.5.4 Statisztika, notifikáció

Az OPG-s forrásból érkező tranzakciók összegzései ugyan úgy megjelennek az adózói statisztikában,
mint a többi forrásé. Az ABORTED státuszba kerülő adatszolgáltatásokról a rendszer akkor sem küld
emailes értesítést, ha azt az adózó az OSA felületén beállította.


