# Battle of Agents Pro — अपना APK कैसे बनाएँ

यह फ़ोल्डर **Battle of Agents Pro** का पूरा सोर्स कोड है (Expo / React Native ऐप,
package id `com.battleofagents.pro`)।

> **ज़रूरी बात:** यहाँ APK फ़ाइल नहीं बनी है। Android/iOS ऐप को किसी बिल्ड सर्विस से
> बनाना और साइन करना पड़ता है — और वह बिल्ड **आपके अपने मुफ़्त Expo अकाउंट** से होगा।
> नीचे दिए स्टेप्स बस फ़ॉलो करें, लगभग 15 मिनट लगेंगे (प्लस Expo की बिल्ड कतार)।

आपको एक कंप्यूटर चाहिए (Windows, macOS या Linux) जिसमें **Node.js 20 या नया**
(https://nodejs.org) हो। Android Studio, Java या Mac की ज़रूरत नहीं।

---

## 1. Android APK बनाना (मुफ़्त)

1. मुफ़्त अकाउंट बनाएँ: https://expo.dev/signup
2. इस फ़ोल्डर को unzip करें, उसके अंदर टर्मिनल खोलें, और चलाएँ:

   ```bash
   npm install
   npm install -g eas-cli
   eas login
   eas init
   eas build --platform android --profile preview
   ```

   - `eas init` पहली बार प्रोजेक्ट को आपके अकाउंट से जोड़ता है — **Yes** कहें।
   - जब नया Android keystore बनाने को पूछे — **Yes** कहें। Expo उसे संभाल कर रखता है,
     इसलिए आगे के हर बिल्ड पर वही key रहेगी और अपडेट की तरह इंस्टॉल होगा।
3. बिल्ड Expo के क्लाउड में चलता है। मुफ़्त अकाउंट कम प्राथमिकता वाली कतार में होता है,
   व्यस्त समय में एक घंटे से ज़्यादा लग सकता है।
   बिल्ड पूरा होने पर टर्मिनल और expo.dev का पेज एक लिंक और QR कोड दिखाते हैं।
   उसे अपने Android फ़ोन पर खोलें, `.apk` डाउनलोड करें और इंस्टॉल करें
   (Android पूछे तो ब्राउज़र के लिए "unknown apps इंस्टॉल करने दें" चालू करें)।

मुफ़्त प्लान में महीने में सीमित बिल्ड मिलते हैं (लगभग 15 Android बिल्ड,
देखें https://expo.dev/pricing)।

---

## 2. iPhone और Play Store (वैकल्पिक)

- **iPhone** के लिए Apple Developer Program मेंबरशिप (99 USD/साल) चाहिए। फिर:
  `eas build --platform ios --profile production` और `eas submit --platform ios`,
  और TestFlight से इंस्टॉल करें। विवरण: https://docs.expo.dev/submit/ios/
- **Google Play** पर डालने के लिए `eas build --platform android --profile production`
  (यह `.aab` बनाता है) और फिर `eas submit --platform android`।
  विवरण: https://docs.expo.dev/submit/android/

---

## 3. बिना APK, फ़ोन पर सीधे चलाकर देखना (Expo Go)

APK बनाने से पहले गेम देखना है? यह सबसे तेज़ तरीका है:

1. फ़ोन पर **Expo Go** ऐप इंस्टॉल करें (Play Store / App Store)।
2. कंप्यूटर पर इस फ़ोल्डर में:

   ```bash
   npm install
   npx expo start
   ```

3. टर्मिनल में दिखा QR कोड Expo Go से स्कैन करें। गेम फ़ोन पर खुल जाएगा।

> **ध्यान:** Expo Go में **Hotspot Wi-Fi मल्टीप्लेयर काम नहीं करेगा**, क्योंकि
> `react-native-tcp-socket` एक native मॉड्यूल है जो सिर्फ़ असली बिल्ड (APK) में चलता है।
> Expo Go में सोलो मोड (बॉट्स के साथ) पूरा चलेगा। Hotspot मोड के लिए APK बनाएँ।

---

## 4. गेम में क्या-क्या है

| चीज़ | विवरण |
|---|---|
| **मोड** | सिर्फ़ एक TDM (टीम डेथमैच), 5v5, पहले 30 किल या 7 मिनट |
| **एरिना** | 3 PUBG-स्टाइल मैप — Warehouse 17 (Erangel), Mylta Compound (Miramar), Dockyard Night (Vikendi) |
| **एजेंट** | 5 PUBG-स्टाइल ऑपरेटर — Specter, Vandal, Nyx, Ranger, Blitz (अलग-अलग कपड़े/गियर) |
| **गन** | 8 हथियार — M416, AKM, SCAR-L, UMP45, Kar98k, AWM, S686, M249 |
| **स्किन** | हर गन पर Glacier (सफ़ेद बर्फ़ + नीली नसें) सहित 2–4 स्किन, M416 पर 4 |
| **डैमेज** | PUBG वाला मॉडल — हेडशॉट 2.5×, हेलमेट/वेस्ट Lv.1–3, दूरी से डैमेज कम, TTK असली जैसा |
| **हिलिंग** | First Aid, Med Kit, Energy Drink, Painkiller + Boost रीजन (PUBG जैसा) |
| **मूवमेंट** | PUBG जैसा चलना/भागना/क्राउच/प्रोन, वज़न के हिसाब से स्पीड, जंप, गिरने पर डैमेज |
| **मल्टीप्लेयर** | **सिर्फ़ Hotspot Wi-Fi** — कोई इंटरनेट, कोई अकाउंट नहीं |

---

## 5. Hotspot Wi-Fi मैच कैसे खेलें

1. **होस्ट फ़ोन:** Settings → Hotspot चालू करें।
2. होस्ट ऐप में **HOTSPOT** टैब → **HOST A ROOM** दबाएँ। स्क्रीन पर एक address दिखेगा
   (आमतौर पर `192.168.43.1`)।
3. **बाकी फ़ोन:** उसी hotspot की Wi-Fi से जुड़ें → ऐप में **HOTSPOT** टैब →
   वही address टाइप करें → **CONNECT**।
4. होस्ट **START MATCH** दबाएगा — सब एक ही एरिना में उतर जाएँगे।

> सब फ़ोन पर एक ही वर्ज़न (यही APK) होना चाहिए। पोर्ट `41234` खुला रहना चाहिए —
> कुछ फ़ोन के firewall इसे रोक सकते हैं, तो होस्ट फ़ोन पर ऐप को network permission दें।

---

## 6. सोर्स कोड में क्या कहाँ है

```
battle-of-agents/
├── app.json                     ऐप कॉन्फ़िग (नाम, package id, permissions, landscape)
├── eas.json                     APK बिल्ड प्रोफ़ाइल
├── BUILD_GUIDE.md               यह फ़ाइल
├── assets/
│   ├── arena.html               ★ पूरा 3D गेम इंजन (three.js + गेम कोड, एक फ़ाइल में)
│   └── images/icon.png          ऐप आइकन
├── tools/
│   ├── arena.src.html           गेम का HTML शेल (HUD, CSS)
│   ├── game/                    गेम इंजन के मॉड्यूल
│   │   ├── 00_core.js           स्टेट, मैथ, कॉन्फ़िग
│   │   ├── 10_arena.js          3 एरिना की ज्यामिति + कोलिज़न
│   │   ├── 20_soldier.js        एजेंट मॉडल + एनिमेशन
│   │   ├── 30_combat.js         PUBG डैमेज मॉडल, हेल्थ/बूस्ट, गोलियाँ
│   │   ├── 40_movement.js       PUBG मूवमेंट + बॉट AI
│   │   ├── 50_fx.js             ट्रेसर, इम्पैक्ट, आवाज़ (WebAudio)
│   │   ├── 60_hud.js            HUD, टच कंट्रोल, कैमरा, मिनीमैप
│   │   └── 70_main.js           मैच सेटअप + गेम लूप
│   ├── build_arena.py           ★ arena.html दोबारा बनाने की स्क्रिप्ट
│   └── smoke_test.js            ★ हेडलेस टेस्ट (गेम लॉजिक जाँचता है)
└── src/
    ├── app/                     स्क्रीन (expo-router)
    │   ├── (tabs)/index.tsx     लॉबी
    │   ├── (tabs)/loadout.tsx   एजेंट + गन स्किन चुनना
    │   ├── (tabs)/hotspot.tsx   Hotspot Wi-Fi रूम
    │   ├── (tabs)/settings.tsx  प्रोफ़ाइल + सेटिंग
    │   ├── match.tsx            मैच स्क्रीन (3D व्यू)
    │   └── results.tsx          नतीजे
    ├── components/arena-view.tsx  WebView जो गेम चलाता है
    ├── constants/catalog.ts     ★ सारे हथियार, स्किन, एजेंट, एरिना का डेटा
    ├── constants/theme.ts       रंग
    └── lib/
        ├── hotspot.ts           Hotspot Wi-Fi LAN (TCP)
        ├── game-store.ts        सेव किया हुआ लोडआउट + करियर
        └── match-bus.ts         स्क्रीन के बीच डेटा
```

### गेम में बदलाव करना है?

- **गन का डैमेज/स्पीड बदलें** → `src/constants/catalog.ts` में `WEAPONS` एडिट करें।
- **नई स्किन जोड़ें** → उसी फ़ाइल में हथियार के `skins` ऐरे में एक और entry डालें।
- **एरिना का लेआउट बदलें** → `tools/game/10_arena.js`।
- **बदलाव के बाद गेम फ़ाइल दोबारा बनाएँ:**

  ```bash
  python3 tools/build_arena.py     # assets/arena.html फिर से बनाता है
  node tools/smoke_test.js         # गेम लॉजिक की जाँच (RESULT: PASS आना चाहिए)
  ```

  फिर `npx expo start` या नया APK बिल्ड।

---

## 7. कुछ गड़बड़ हो तो

| दिक्कत | हल |
|---|---|
| `eas: command not found` | `npm install -g eas-cli` फिर से चलाएँ |
| बिल्ड फेल: "keystore" | `eas build --platform android --profile preview --clear-cache` |
| Hotspot में कनेक्ट नहीं हो रहा | दोनों फ़ोन एक ही hotspot पर हैं? address सही है? होस्ट का firewall? |
| गेम खुलते ही काली स्क्रीन | फ़ोन का WebView पुराना है — Play Store से "Android System WebView" अपडेट करें |
| ऐप इंस्टॉल नहीं हो रहा | पुराना वर्ज़न पहले uninstall करें (अलग key से साइन हो सकता है) |

---

## 8. ज़रूरी नोट

- यह ऐप **किसी और के APK को decompile/repackage करके** नहीं बना है। यह एक नया,
  साफ़-सुथरा सोर्स प्रोजेक्ट है जो आपकी बताई सारी चीज़ें (PUBG-स्टाइल TDM, गन स्किन,
  एजेंट, Hotspot Wi-Fi, PUBG डैमेज) खुद से बनाता है।
- गेम का 3D हिस्सा फ़ोन के WebView में three.js से चलता है और पूरी तरह **ऑफ़लाइन**
  है — कोई इंटरनेट कॉल नहीं, कोई ट्रैकिंग नहीं।
- यहाँ सिर्फ़ यह जाँचा गया है कि कोड type-check पास करता है, Android का JavaScript
  bundle बनता है, और गेम का लॉजिक हेडलेस टेस्ट में सही चलता है। असली फ़ोन पर
  इंस्टॉल/रन यहाँ नहीं जाँचा जा सका (यहाँ फ़ोन नहीं है)।
