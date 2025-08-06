mapping = [
    {
        'column_name': 'Számla sorszáma',
        'field_name': 'invoiceNumber',
        'xml_paths': ['invoiceNumber'],
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Számla kelte',
        'field_name': 'invoiceIssueDate',
        'xml_paths': ['invoiceIssueDate'],
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Teljesítés dátuma',
        'field_name': 'invoiceDeliveryDate',
        'xml_paths': ['invoiceMain.invoice.invoiceHead.invoiceDetail.invoiceDeliveryDate'],
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Számla pénzneme',
        'field_name': 'currencyCode',
        'xml_path': 'invoiceMain.invoice.invoiceHead.invoiceDetail.currencyCode',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Alkalmazott árfolyam',
        'field_name': 'exchangeRate',
        'xml_path': 'invoiceMain.invoice.invoiceHead.invoiceDetail.exchangeRate',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Eladó adószáma (törzsszám)',
        'field_name': 'taxpayerId',
        'xml_path': 'invoiceMain.invoice.invoiceHead.supplierInfo.supplierTaxNumber.taxpayerId',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Eladó adószáma (ÁFA-kód)',
        'field_name': 'vatCode',
        'xml_path': 'invoiceMain.invoice.invoiceHead.supplierInfo.supplierTaxNumber.vatCode',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Eladó adószáma (megyekód)',
        'field_name': 'countyCode',
        'xml_path': 'invoiceMain.invoice.invoiceHead.supplierInfo.supplierTaxNumber.countyCode',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Eladó neve',
        'field_name': 'supplierName',
        'xml_path': 'invoiceMain.invoice.invoiceHead.supplierInfo.supplierName',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Eladó országkódja',
        'field_name': 'supplierCountryCode',
        'xml_paths': [
            'invoiceMain.invoice.invoiceHead.supplierInfo.supplierAddress.simpleAddress.countryCode',
            'invoiceMain.invoice.invoiceHead.supplierInfo.supplierAddress.detailedAddress.countryCode'
        ],
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Eladó irányítószáma',
        'field_name': 'supplierPostalCode',
        'xml_paths': [
            'invoiceMain.invoice.invoiceHead.supplierInfo.supplierAddress.simpleAddress.postalCode',
            'invoiceMain.invoice.invoiceHead.supplierInfo.supplierAddress.detailedAddress.postalCode'
        ],
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Eladó települése',
        'field_name': 'supplierCity',
        'xml_paths': [
            'invoiceMain.invoice.invoiceHead.supplierInfo.supplierAddress.simpleAddress.city',
            'invoiceMain.invoice.invoiceHead.supplierInfo.supplierAddress.detailedAddress.city'
        ],
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Eladó többi címadata',
        'field_name': 'supplierAdditionalAddressDetail',
        'xml_paths': [
            'invoiceMain.invoice.invoiceHead.supplierInfo.supplierAddress.simpleAddress.additionalAddressDetail'
        ],
        'xml_path_combiner': [
            'invoiceMain.invoice.invoiceHead.supplierInfo.supplierAddress.detailedAddress.streetName',
            'invoiceMain.invoice.invoiceHead.supplierInfo.supplierAddress.detailedAddress.publicPlaceCategory',
            'invoiceMain.invoice.invoiceHead.supplierInfo.supplierAddress.detailedAddress.number'
        ],
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Vevő adószáma (törzsszám)',
        'field_name': 'customerTaxpayerId',
        'xml_path': 'invoiceMain.invoice.invoiceHead.customerInfo.customerTaxNumber.taxpayerId',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Vevő adószáma (ÁFA-kód)',
        'field_name': 'customerVatCode',
        'xml_path': 'invoiceMain.invoice.invoiceHead.customerInfo.customerTaxNumber.vatCode',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Vevő adószáma (megyekód)',
        'field_name': 'customerCountyCode',
        'xml_path': 'invoiceMain.invoice.invoiceHead.customerInfo.customerTaxNumber.countyCode',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Vevő neve',
        'field_name': 'customerName',
        'xml_path': 'invoiceMain.invoice.invoiceHead.customerInfo.customerName',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Vevő státusza',
        'field_name': 'customerVatStatus',
        'xml_path': 'invoiceMain.invoice.invoiceHead.customerInfo.customerVatStatus',
        'type': 'text',
        'default': 'n/a',
        'replace_values': {
            'DOMESTIC': 'Belföldi ÁFA alany',
            'PRIVATE_PERSON': 'Nem ÁFA alany (belföldi vagy külföldi) természetes személy',
            'OTHER': 'Egyéb (belföldi nem ÁFA alany, nem természetes személy, külföldi Áfa alany és külföldi nem ÁFA alany, nem természetes személy)'
        }
    },
    {
        'column_name': 'Vevő közösségi adószáma',
        'field_name': 'customerCommunityTaxNumber',
        'xml_path': 'invoiceMain.invoice.invoiceHead.customerInfo.customerVatData.communityVatNumber',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Vevő harmadik országbeli adószáma',
        'field_name': 'customerThirdCountryTaxNumber',
        'xml_path': 'invoiceMain.invoice.invoiceHead.customerInfo.customerVatData.thirdStateTaxId',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Vevő országkódja',
        'field_name': 'customerCountryCode',
        'xml_paths': [
            'invoiceMain.invoice.invoiceHead.customerInfo.customerAddress.simpleAddress.countryCode',
            'invoiceMain.invoice.invoiceHead.customerInfo.customerAddress.detailedAddress.countryCode'
        ],
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Vevő irányítószáma',
        'field_name': 'customerPostalCode',
        'xml_paths': [
            'invoiceMain.invoice.invoiceHead.customerInfo.customerAddress.simpleAddress.postalCode',
            'invoiceMain.invoice.invoiceHead.customerInfo.customerAddress.detailedAddress.postalCode'
        ],
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Vevő települése',
        'field_name': 'customerCity',
        'xml_paths': [
            'invoiceMain.invoice.invoiceHead.customerInfo.customerAddress.simpleAddress.city',
            'invoiceMain.invoice.invoiceHead.customerInfo.customerAddress.detailedAddress.city'
        ],
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Vevő többi címadata',
        'field_name': 'customerAdditionalAddressDetail',
        'xml_paths': [
            'invoiceMain.invoice.invoiceHead.customerInfo.customerAddress.simpleAddress.additionalAddressDetail'
        ],
        'xml_path_combiner': [
            'invoiceMain.invoice.invoiceHead.customerInfo.customerAddress.detailedAddress.streetName',
            'invoiceMain.invoice.invoiceHead.customerInfo.customerAddress.detailedAddress.publicPlaceCategory',
            'invoiceMain.invoice.invoiceHead.customerInfo.customerAddress.detailedAddress.number'
        ],
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Eredeti számla száma',
        'field_name': 'originalInvoiceNumber',
        'xml_path': 'invoiceMain.invoice.invoiceReference.originalInvoiceNumber',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Módosító okirat kelte',
        'field_name': 'modificationDate',
        'xml_paths': ['invoiceIssueDate'],
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Módosítás sorszáma',
        'field_name': 'modificationIndex',
        'xml_path': 'invoiceMain.invoice.invoiceReference.modificationIndex',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Számla nettó összege (a számla pénznemében)',
        'field_name': 'invoiceNetAmount',
        'xml_path': 'invoiceMain.invoice.invoiceSummary.summaryNormal.invoiceNetAmount',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Számla nettó összege (forintban)',
        'field_name': 'invoiceNetAmountHUF',
        'xml_path': 'invoiceMain.invoice.invoiceSummary.summaryNormal.invoiceNetAmountHUF',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Számla ÁFA összege (a számla pénznemében)',
        'field_name': 'invoiceVatAmount',
        'xml_path': 'invoiceMain.invoice.invoiceSummary.summaryNormal.invoiceVatAmount',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Számla ÁFA összege (forintban)',
        'field_name': 'invoiceVatAmountHUF',
        'xml_path': 'invoiceMain.invoice.invoiceSummary.summaryNormal.invoiceVatAmountHUF',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Számla bruttó összege (a számla pénznemében)',
        'field_name': 'invoiceGrossAmount',
        'xml_path': 'invoiceMain.invoice.invoiceSummary.summaryGrossData.invoiceGrossAmount',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Számla bruttó összege (forintban)',
        'field_name': 'invoiceGrossAmountHUF',
        'xml_path': 'invoiceMain.invoice.invoiceSummary.summaryGrossData.invoiceGrossAmountHUF',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Fizetési határidő',
        'field_name': 'paymentDate',
        'xml_path': 'invoiceMain.invoice.invoiceHead.invoiceDetail.paymentDate',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Fizetési mód',
        'field_name': 'paymentMethod',
        'xml_path': 'invoiceMain.invoice.invoiceHead.invoiceDetail.paymentMethod',
        'type': 'text',
        'default': 'n/a',
        'replace_values': {
            'TRANSFER': 'Banki átutalás',
            'CASH': 'Készpénz',
            'CARD': 'Bankkártya, hitelkártya, egyéb készpénz helyettesítő eszköz',
        }
    },
    {
        'column_name': 'Kisadózó jelölése',
        'field_name': 'smallBusinessIndicator',
        'xml_path': 'invoiceMain.invoice.invoiceHead.invoiceDetail.smallBusinessIndicator',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Pénzforgalmi elszámolás jelölése',
        'field_name': 'cashAccountingIndicator',
        'xml_path': 'invoiceMain.invoice.invoiceHead.invoiceDetail.cashAccountingIndicator',
        'type': 'text',
        'default': 'Nem',
        'replace_values': {
            True: 'Igen',
            False: 'Nem',
            'FALSE': 'Nem',
            'TRUE': 'Igen',
            'false': 'Nem',
            'true': 'Igen'
        }
    },
    {
        'column_name': 'Számla típusa',
        'field_name': 'invoiceCategory',
        'xml_path': 'invoiceMain.invoice.invoiceHead.invoiceDetail.invoiceCategory',
        'type': 'text',
        'default': 'n/a',
        'replace_values': {
            'NORMAL': 'Normál',
            'SIMPLIFIED': 'Egyszerűsített',
            'AGGREGATE': 'Gyűjtőszámla'
        }
    },
    {
        'column_name': 'Az adatszolgáltatás maga a számla',
        'field_name': 'completenessIndicator',
        'xml_path': 'completenessIndicator',
        'type': 'text',
        'default': 'Nem',
        'replace_values': {
            True: 'Igen',
            False: 'Nem',
            'FALSE': 'Nem',
            'TRUE': 'Igen',
            'false': 'Nem',
            'true': 'Igen'
        }
    }
]

# Additional mappings for line-level data (invoice lines)
line_mapping = [
    {
        'column_name': 'Számla sorszáma',
        'field_name': 'invoiceNumber',
        'xml_path': 'invoiceNumber',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Vevő adószáma (törzsszám)',
        'field_name': 'customerTaxpayerId',
        'xml_path': 'invoiceMain.invoice.invoiceHead.customerInfo.customerTaxNumber.taxpayerId',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Vevő neve',
        'field_name': 'customerName',
        'xml_path': 'invoiceMain.invoice.invoiceHead.customerInfo.customerName',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Eladó adószáma (törzsszám)',
        'field_name': 'supplierTaxpayerId',
        'xml_path': 'invoiceMain.invoice.invoiceHead.supplierInfo.supplierTaxNumber.taxpayerId',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Eladó neve',
        'field_name': 'supplierName',
        'xml_path': 'invoiceMain.invoice.invoiceHead.supplierInfo.supplierName',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Tétel sorszáma',
        'field_name': 'lineNumber',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineNumber',
        'type': 'int',
        'default': 'n/a',
    },
    {
        'column_name': 'Módosítással érintett tétel sorszáma',
        'field_name': 'lineNumberReference',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineModificationReference.lineNumberReference',
        'type': 'int',
        'default': 'n/a',
    },
    {
        'column_name': 'Módosítás jellege',
        'field_name': 'lineOperation',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineModificationReference.lineOperation',
        'type': 'text',
        'default': 'n/a',
        'replace_values': {
            'CREATE': 'Új sor felvétele',
        }
    },
    {
        'column_name': 'Megnevezés',
        'field_name': 'lineDescription',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineDescription',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Mennyiség',
        'field_name': 'quantity',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.quantity',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Mennyiségi egység',
        'field_name': 'unitOfMeasure',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.unitOfMeasure',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Egységár',
        'field_name': 'unitPrice',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.unitPrice',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Nettó összeg (a számla pénznemében)',
        'field_name': 'lineNetAmount',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineNetAmountData.lineNetAmount',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Nettó összeg (forintban)',
        'field_name': 'lineNetAmountHUF',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineNetAmountData.lineNetAmountHUF',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Adó mértéke',
        'field_name': 'vatPercentage',
        'xml_paths': [
            'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatRate.vatPercentage',
            # 'invoiceMain.invoice.invoiceLines.line.lineAmountsSimplified.lineVatRate.vatContent'
        ],
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Áfamentesség jelölés',
        'field_name': 'vatExemptionIndicator',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsVatExempt.lineVatData.vatExemption.indicator',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Áfamentesség esete',
        'field_name': 'vatExemptionCase',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatRate.vatExemption.case',
        'type': 'text',
        'default': 'n/a',
        'replace_values': {
            'AAM': 'Alanyi adómentes',
            'TAM': 'Tárgyi adómentes ill. a tevékenység közérdekű vagy speciális jellegére tekintettel adómentes',
            'KBAET': 'Adómentes Közösségen belüli termékértékesítés, új közlekedési eszköz nélkül',
            'KBAUK': 'Adómentes Közösségen belüli új közlekedési eszköz értékesítés',
            'EAM': 'Adómentes termékértékesítés a Közösség területén kívülre (termékexport harmadik országba)',
            'NAM': 'Egyéb nemzetközi ügyletekhez kapcsolódó jogcímen megállapított adómentesség',
            'UNKNOWN': '3.0 előtti számlára hivatkozó, illetve előzmény nélküli módosító és sztornó számlák esetén használható'
        }
    },
    {
        'column_name': 'Áfamentesség leírása',
        'field_name': 'vatExemptionReason',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatRate.vatExemption.reason',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'ÁFA törvény hatályán kívüli jelölés',
        'field_name': 'vatOutOfScopeIndicator',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsVatOutOfScope.lineVatData.vatOutOfScope.indicator',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'ÁFA törvény hatályon kívüliségének esete',
        'field_name': 'vatOutOfScopeCase',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatRate.vatOutOfScope.case',
        'type': 'text',
        'default': 'n/a',
        # 'replace_values': {
        #     'ATK': 'Áfa tárgyi hatályán kívül',
        #     'EUFAD37': 'Áfa tv. 37. §-a alapján másik tagállamban teljesített, fordítottan adózó ügylet',
        #     'EUFADE': 'Másik tagállamban teljesített, nem az Áfa tv. 37. §-a alá tartozó, fordítottan adózó ügylet',
        #     'EUE': 'Másik tagállamban teljesített, nem fordítottan adózó ügylet',
        #     'HO': 'Harmadik országban teljesített ügylet',
        #     'UNKNOWN': '3.0 előtti számlára hivatkozó, illetve előzmény nélküli módosító és sztornó számlák esetén használható'
        # }
    },
    {
        'column_name': 'ÁFA törvény hatályon kívüliségének leírása',
        'field_name': 'vatOutOfScopeReason',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatRate.vatOutOfScope.reason',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Adóalap és felszámított adó eltérésének esete',
        'field_name': 'taxBaseAndVatDifferenceCase',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatRate.vatAmountMismatch.case',
        'type': 'text',
        'default': 'n/a',
        'replace_values': {
            'REFUNDABLE_VAT': 'Az áfa felszámítása a 11. vagy 14. § alapján történt és az áfát a számla címzettjének meg kell térítenie',
            'NONREFUNDABLE_VAT': 'Az áfa felszámítása a 11. vagy 14. § alapján történt és az áfát a számla címzettjének nem kell megtérítenie',
            'UNKNOWN': '3.0 előtti számlára hivatkozó, illetve előzmény nélküli módosító és sztornó számlák esetén használható'
        }
    },
    {
        'column_name': 'Eltérő adóalap és felszámított adó adómérték, adótartalom',
        'field_name': 'differentTaxRate',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatRate.vatAmountMismatch.vatRate',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Belföldi fordított adózás jelölés',
        'field_name': 'domesticReverseChargeIndicator',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatRate.vatDomesticReverseCharge',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Áthárított adót tartalmazó különbözet szerinti adózás',
        'field_name': 'marginSchemeWithVatIndicator',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatRate.marginSchemeIndicator',
        'type': 'text',
        'default': 'n/a',
        'replace_values': {
            'TRAVEL_AGENCY': 'Utazási irodák',
            'SECOND_HAND': 'Használt cikkek',
            'ARTWORK': 'Műalkotások',
            'ANTIQUES': 'Gyűjteménydarabok és régiségek'
        }
    },
    {
        'column_name': 'Áthárított adót nem tartalmazó különbözet szerinti adózás',
        'field_name': 'marginSchemeNoVatIndicator',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatData.marginSchemeNoVat',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Különbözet szerinti adózás',
        'field_name': 'marginSchemeIndicator',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatRate.marginSchemeIndicator',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'ÁFA összeg (a számla pénznemében)',
        'field_name': 'lineVatAmount',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatData.lineVatAmount',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'ÁFA összeg (forintban)',
        'field_name': 'lineVatAmountHUF',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatData.lineVatAmountHUF',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Bruttó összeg (a számla pénznemében)',
        'field_name': 'lineGrossAmountNormal',
        'xml_paths': [
            'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineGrossAmountData.lineGrossAmountNormal',
            'invoiceMain.invoice.invoiceLines.line.lineAmountsSimplified.lineGrossAmountSimplified'
        ],
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Bruttó összeg (forintban)',
        'field_name': 'lineGrossAmountNormalHUF',
        'xml_paths': [
            'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineGrossAmountData.lineGrossAmountNormalHUF',
            'invoiceMain.invoice.invoiceLines.line.lineAmountsSimplified.lineGrossAmountSimplifiedHUF'
        ],
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'ÁFA tartalom',
        'field_name': 'vatContent',
        'xml_paths': [
            'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatRate.vatContent',
            'invoiceMain.invoice.invoiceLines.line.lineAmountsSimplified.lineVatRate.vatContent'
        ],
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Előleg jelleg jelölése',
        'field_name': 'advanceIndicator',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.advanceIndicator',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Tétel árfolyam',
        'field_name': 'lineExchangeRate',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineExchangeRate',
        'type': 'float',
        'default': 'n/a',
    },
    {
        'column_name': 'Tétel teljesítés dátuma',
        'field_name': 'lineDeliveryDate',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineDeliveryDate',
        'type': 'text',
        'default': 'n/a',
    },
    {
        'column_name': 'Nincs felszámított áfa az áfa törvény 17. § alapján',
        'field_name': 'noVatCharge',
        'xml_path': 'invoiceMain.invoice.invoiceLines.line.lineAmountsNormal.lineVatRate.noVatCharge',
        'type': 'text',
        'default': 'n/a',
        'replace_values': {
            True: 'Igen',
            False: 'Nem',
            'FALSE': 'Nem',
            'TRUE': 'Igen',
            'false': 'Nem',
            'true': 'Igen'
        }
    }
]