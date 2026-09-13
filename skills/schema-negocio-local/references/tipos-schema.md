# Sector español → tipo de schema.org

Una fila por tipo. "Google muestra" indica si ese tipo puede generar un
resultado enriquecido específico en Google (ficha con horarios, estrellas,
etc.) o si Google solo lo lee para entender la entidad. Para la IA todos
cuentan igual: lo que importa es el tipo correcto y el NAP.

Todos son subtipos de `LocalBusiness` salvo que se indique, y heredan sus
propiedades (`name`, `address`, `telephone`, `openingHoursSpecification`,
`priceRange`, `image`, `geo`, `sameAs`, `areaServed`, `aggregateRating`).

| Sector | `@type` | Propiedades específicas útiles | Google muestra |
|---|---|---|---|
| Restaurante | `Restaurant` | `servesCuisine` (p. ej. "Castellana", "Mediterránea"), `menu` (URL de la carta), `acceptsReservations` (`true`/URL), `hasMenu` | Sí: ficha con carta, reservas y valoraciones |
| Bar, taberna, cervecería | `BarOrPub` | `servesCuisine`, `menu` | Sí |
| Cafetería, pastelería | `CafeOrCoffeeShop`, `Bakery` | `servesCuisine`, `menu` | Sí |
| Clínica dental | `Dentist` | `medicalSpecialty` ("Dentistry"), `availableService`, `isAcceptingNewPatients` | Sí (ficha básica); las valoraciones de salud tienen restricciones |
| Clínica médica, centro de salud privado | `MedicalClinic` | `medicalSpecialty`, `availableService`, `healthPlanNetworkId` (mutuas) | Sí (ficha básica) |
| Médico o consulta individual | `Physician` | `medicalSpecialty`, `hospitalAffiliation` | Sí (ficha básica) |
| Fisioterapia, osteopatía | `MedicalBusiness` (no hay tipo específico) | `medicalSpecialty` ("Physiotherapy") | Solo lee |
| Farmacia | `Pharmacy` | — | Sí |
| Asesoría, gestoría | `AccountingService` | `areaServed`, `serviceType` | Solo lee |
| Abogados, despacho | `LegalService` o `Attorney` | `areaServed`, `serviceType` (p. ej. "Derecho laboral") | Solo lee |
| Notaría | `Notary` | — | Solo lee |
| Taller mecánico | `AutoRepair` | `areaServed`, `makesOffer` | Sí (ficha básica) |
| Concesionario | `AutoDealer` | `brand` | Sí (ficha básica) |
| Peluquería | `HairSalon` | `priceRange` | Sí (ficha básica) |
| Centro de estética, spa | `BeautySalon`, `DaySpa` | `priceRange` | Sí (ficha básica) |
| Tienda genérica | `Store` | `paymentAccepted`, `currenciesAccepted` | Sí |
| Tienda de ropa | `ClothingStore` | — | Sí |
| Ferretería | `HardwareStore` | — | Sí |
| Tienda de muebles | `FurnitureStore` | — | Sí |
| Joyería | `JewelryStore` | — | Sí |
| Librería | `BookStore` | — | Sí |
| Supermercado, ultramarinos | `GroceryStore` | — | Sí |
| Floristería | `Florist` | — | Sí |
| Hotel | `Hotel` | `starRating` (`{"@type":"Rating","ratingValue":"3"}`), `checkinTime`, `checkoutTime`, `amenityFeature`, `petsAllowed`, `numberOfRooms` | Sí, pero Google usa su propio módulo de hoteles; el schema ayuda a la entidad |
| Casa rural, apartamento turístico | `LodgingBusiness` o `VacationRental` | `checkinTime`, `checkoutTime`, `amenityFeature`, `numberOfRooms` | Igual que hotel |
| Inmobiliaria | `RealEstateAgent` | `areaServed` | Solo lee |
| Gimnasio | `ExerciseGym` | `amenityFeature`, `membershipProgram` | Sí (ficha básica) |
| Centro deportivo, club | `HealthClub`, `SportsActivityLocation` | `amenityFeature` | Sí (ficha básica) |
| Fontanero | `Plumber` | `areaServed` (varias localidades o `GeoCircle`) | Solo lee |
| Electricista | `Electrician` | `areaServed` | Solo lee |
| Reformas, albañilería | `GeneralContractor` | `areaServed` | Solo lee |
| Instalador solar / energía | `HomeAndConstructionBusiness` o `Electrician` | `areaServed`, `makesOffer` | Solo lee |
| Cerrajero | `Locksmith` | `areaServed`, `openingHours` 24 h si aplica | Solo lee |
| Limpieza de hogares y oficinas | `LocalBusiness` (no hay tipo específico) | `areaServed`, `serviceType` ("Limpieza de oficinas") | Solo lee |
| Tintorería, lavandería | `DryCleaningOrLaundry` | — | Sí (ficha básica) |
| Pintor | `HousePainter` | `areaServed` | Solo lee |
| Academia, autoescuela | `EducationalOrganization` (no es LocalBusiness: añadir `address` y `telephone` igualmente) o `School` | `hasCourse` | Solo lee |
| Guardería | `Preschool` | — | Solo lee |
| Veterinario | `VeterinaryCare` | `medicalSpecialty` | Sí (ficha básica) |
| Tienda de animales | `PetStore` | — | Sí |
| Agencia de viajes | `TravelAgency` | — | Sí (ficha básica) |
| Agencia de marketing, estudio | `ProfessionalService` | `serviceType`, `areaServed` | Solo lee |
| Fotógrafo | `ProfessionalService` (`Photographer` no existe como LocalBusiness) | `serviceType` | Solo lee |
| Funeraria | `FuneralHome` | — | Solo lee |
| Óptica | `Optician` | — | Sí (ficha básica) |
| Gasolinera | `GasStation` | — | Sí |
| Parking | `ParkingFacility` (no es LocalBusiness) | — | Sí |
| Negocio que no encaja en nada | `LocalBusiness` | `description` que diga qué es | Sí (ficha básica) |

## Notas

- Cuando dudes entre dos tipos, elige el más específico que sea cierto. Un
  bar que sirve comidas es `Restaurant`; una cafetería que no sirve alcohol
  es `CafeOrCoffeeShop`.
- Se pueden combinar tipos con array: `"@type": ["Dentist", "MedicalClinic"]`.
  Úsalo solo cuando los dos sean ciertos.
- Los tipos médicos (`Dentist`, `MedicalClinic`, `Physician`) tienen
  restricciones en Google para mostrar `aggregateRating`. Incluirla no
  perjudica, pero no esperar estrellas.
- `areaServed` acepta texto (`"Valladolid y provincia"`), una lista de
  `City`, o un `GeoCircle` con `geoMidpoint` y `geoRadius` en metros. Para
  negocios que se desplazan y no reciben público, se puede omitir `address`
  visible en Google Business Profile, pero en schema conviene mantener la
  dirección fiscal como `address`.
- `EducationalOrganization` y `ParkingFacility` no heredan de
  `LocalBusiness`; siguen aceptando `address`, `telephone` y
  `openingHoursSpecification`.
- Consulta siempre la lista oficial en schema.org/LocalBusiness para tipos
  nuevos; esta tabla se revisó el 13 de septiembre de 2026.
