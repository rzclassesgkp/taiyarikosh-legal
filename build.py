#!/usr/bin/env python3
"""Generate the public legal pages of TaiyariKosh (by KS Infotech Labs) as plain static HTML, English + Hindi.

Run: python legal-site/build.py   (writes the .html files next to this file; no dependencies).
Publish by pushing the .html files to the PUBLIC GitHub repo that has Pages enabled (see README.md here).
Every factual statement here describes what the app really does; if the app changes (new SDK, new data, new
processor), update the text FIRST, then rebuild, then update the Play Data-safety form.
"""
import html
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
OUT = Path(__file__).resolve().parent

APP = "TaiyariKosh"
CO = "KS Infotech Labs"
EMAIL = "rzclassesgkp@gmail.com"
UPDATED = "15 October 2026"
VERSION = "2.0"
YEAR = "2026"
TRIAL = 7
# False = the free launch (no prices, trial, autopay or Razorpay anywhere). True = the paid-plans wording kept below.
# Keep in step with VITE_PAYMENTS_ENABLED in the app (see src/lib/features.ts).
PAYMENTS = False
PLANS = "Monthly ₹49, 6 Months ₹199 and Yearly ₹299"
PLANS_HI = "मासिक ₹49, 6 महीने ₹199 और वार्षिक ₹299"
MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

# ---------------------------------------------------------------------------------------------------------------
# Content. Block kinds: ("h2"|"h3"|"p"|"note"|"warn", en, hi), ("ul"|"ol", [en...], [hi...]),
#                       ("table", (head, rows), (head_hi, rows_hi)), ("glance", [en...], [hi...])
# ---------------------------------------------------------------------------------------------------------------

PRIVACY = [
    ("glance", [
        f"<b>Who we are:</b> {APP} is designed, developed and operated by <b>{CO}</b> (India).",
        "<b>What we collect:</b> only what is needed to run your account, your study progress and your subscription (listed in section 3).",
        "<b>No ads, no tracking:</b> the app has no advertising, no advertising ID, no analytics or crash-reporting SDK and no data selling.",
        "<b>Payments:</b> card / UPI details go straight to Razorpay. We never see or store them.",
        "<b>Your control:</b> edit your details, turn on 2-step verification, and delete your account and all data inside the app, at any time.",
        f"<b>Questions:</b> write to {MAIL}.",
    ], [
        f"<b>हम कौन हैं:</b> {APP} को <b>{CO}</b> (भारत) ने डिज़ाइन, विकसित और संचालित किया है।",
        "<b>हम क्या लेते हैं:</b> सिर्फ़ उतना, जितना आपका अकाउंट, पढ़ाई की प्रगति और सब्सक्रिप्शन चलाने के लिए ज़रूरी है (खंड 3 में सूची)।",
        "<b>कोई विज्ञापन या ट्रैकिंग नहीं:</b> ऐप में कोई विज्ञापन, एडवर्टाइज़िंग आईडी, एनालिटिक्स या क्रैश-रिपोर्टिंग SDK नहीं है, और हम डेटा बेचते नहीं।",
        "<b>भुगतान:</b> कार्ड / UPI का विवरण सीधे Razorpay को जाता है। हम उसे न देखते हैं, न रखते हैं।",
        "<b>आपका नियंत्रण:</b> अपनी जानकारी बदलें, 2-स्टेप वेरिफिकेशन चालू करें, और जब चाहें ऐप के अंदर से अकाउंट व सारा डेटा डिलीट करें।",
        f"<b>सवाल:</b> {MAIL} पर लिखें।",
    ]),

    ("h2", "1. About this policy", "1. इस पॉलिसी के बारे में"),
    ("p",
     f'This Privacy Policy explains how <b>{CO}</b> ("<b>{CO}</b>", "we", "us", "our") collects, uses, stores, shares and protects personal information when you use the <b>{APP}</b> Android app and the {APP} website (together, the "<b>Service</b>"). By creating an account or using the Service you confirm that you have read this policy. Where the law requires your consent, we ask for it separately (for example, when you save your profile).',
     f'यह प्राइवेसी पॉलिसी बताती है कि जब आप <b>{APP}</b> एंड्रॉइड ऐप और {APP} वेबसाइट (मिलाकर "<b>सेवा</b>") का उपयोग करते हैं, तब <b>{CO}</b> ("हम") आपकी व्यक्तिगत जानकारी कैसे लेता, उपयोग करता, रखता, साझा करता और सुरक्षित रखता है। अकाउंट बनाकर या सेवा का उपयोग करके आप पुष्टि करते हैं कि आपने यह पॉलिसी पढ़ ली है। जहाँ कानून आपकी सहमति माँगता है, वहाँ हम अलग से सहमति लेते हैं (जैसे प्रोफ़ाइल सेव करते समय)।'),
    ("p",
     f"This policy is written to follow the Information Technology Act, 2000 and the rules made under it, the Digital Personal Data Protection Act, 2023 (to the extent it applies and as it comes into force) and Google Play's User Data policy.",
     "यह पॉलिसी सूचना प्रौद्योगिकी अधिनियम, 2000 और उसके तहत बने नियमों, डिजिटल व्यक्तिगत डेटा संरक्षण अधिनियम, 2023 (जहाँ तक लागू हो और जैसे-जैसे लागू हो) तथा Google Play की User Data पॉलिसी के अनुरूप लिखी गई है।"),

    ("h2", "2. Who is responsible for your data", "2. आपके डेटा की ज़िम्मेदारी किसकी है"),
    ("p",
     f"{CO} (India) decides why and how your personal information is processed, so it is the data fiduciary / controller for the Service. Contact: {MAIL}. For data requests and complaints see section 12 and our <a href=\"contact.html\">Contact &amp; Grievance page</a>.",
     f"{CO} (भारत) तय करता है कि आपकी व्यक्तिगत जानकारी क्यों और कैसे प्रोसेस हो, इसलिए सेवा के लिए वही डेटा फिड्यूशियरी / कंट्रोलर है। संपर्क: {MAIL}। डेटा अनुरोध और शिकायत के लिए खंड 12 और हमारा <a href=\"contact.html\">संपर्क व शिकायत पेज</a> देखें।"),

    ("h2", "3. Information we collect and why", "3. हम कौन-सी जानकारी लेते हैं और क्यों"),
    ("table",
     (["Information", "What exactly", "Why we use it", "Required?"], [
         ["Account", "Email address; an internal account ID. No password is stored (you sign in with a one-time code sent to your email).", "Create and secure your account, sign you in, send service emails.", "Required"],
         ["Two-step verification (optional)", "A secret for your authenticator app, stored encrypted by our sign-in provider.", "Extra protection for your account.", "Only if you turn it on"],
         ["Profile details", "Name, father's name, date of birth, mobile number, qualification, exam(s) you are preparing for, target year, state, district and study hours per day. Optional: gender, category (General/OBC/SC/ST/EWS) and preferred medium.", "Run your account, personalise preparation, verify identity for support and billing queries, prevent misuse.", "Required, except the optional fields"],
         ["Mobile number verification", "Your phone number and technical anti-abuse signals (such as IP address and a device / app-instance identifier) are processed by Google Firebase Authentication to send and check the SMS code.", "Confirm that the number is yours; prevent fraud and SMS abuse.", "Required"],
         ["Study activity", "Questions you attempted, your answers, mock-test results and times, bookmarks, language choice and daily streak.", "Show progress and weak areas, resume where you stopped, build revision lists.", "Created as you use the app"],
         ["Subscription and payment status", "Trial and plan dates, plan type, status, and Razorpay's payment / subscription reference IDs and amount. Never your card, UPI or bank details.", "Give or stop paid access, handle renewals, cancellations and refunds, keep records required by law.", "When you subscribe"],
         ["Consent record", "The date and time at which you accepted this policy when saving your profile.", "Keep proof of your consent.", "Required"],
         ["Support messages", "What you write to us by email, including your email address.", "Reply to you and resolve your request.", "Only if you contact us"],
     ]),
     (["जानकारी", "क्या-क्या", "उपयोग क्यों", "ज़रूरी है?"], [
         ["अकाउंट", "ईमेल पता; एक आंतरिक अकाउंट ID। कोई पासवर्ड स्टोर नहीं होता (आप ईमेल पर आए वन-टाइम कोड से साइन-इन करते हैं)।", "आपका अकाउंट बनाना व सुरक्षित रखना, साइन-इन कराना, सेवा-संबंधी ईमेल भेजना।", "ज़रूरी"],
         ["2-स्टेप वेरिफिकेशन (वैकल्पिक)", "आपके ऑथेंटिकेटर ऐप की गुप्त कुंजी, जिसे हमारा साइन-इन प्रदाता एन्क्रिप्टेड रूप में रखता है।", "अकाउंट की अतिरिक्त सुरक्षा।", "सिर्फ़ चालू करने पर"],
         ["प्रोफ़ाइल की जानकारी", "नाम, पिता का नाम, जन्म तिथि, मोबाइल नंबर, योग्यता, जिस परीक्षा की तैयारी कर रहे हैं, लक्षित वर्ष, राज्य, ज़िला और रोज़ पढ़ाई के घंटे। वैकल्पिक: लिंग, वर्ग (सामान्य/ओबीसी/एससी/एसटी/ईडब्ल्यूएस) और पसंदीदा माध्यम।", "अकाउंट चलाना, तैयारी को आपके अनुसार बनाना, सहायता व बिलिंग सवालों में पहचान की पुष्टि, दुरुपयोग रोकना।", "ज़रूरी, वैकल्पिक फ़ील्ड को छोड़कर"],
         ["मोबाइल नंबर की पुष्टि", "आपका फ़ोन नंबर और दुरुपयोग रोकने वाले तकनीकी संकेत (जैसे IP पता और डिवाइस / ऐप-इंस्टेंस पहचानकर्ता) Google Firebase Authentication द्वारा SMS कोड भेजने और जाँचने के लिए प्रोसेस होते हैं।", "यह पक्का करना कि नंबर आपका है; धोखाधड़ी और SMS के दुरुपयोग को रोकना।", "ज़रूरी"],
         ["पढ़ाई की गतिविधि", "आपने कौन-से प्रश्न हल किए, आपके उत्तर, मॉक-टेस्ट के नतीजे व समय, बुकमार्क, भाषा का चुनाव और रोज़ाना की स्ट्रीक।", "प्रगति और कमज़ोर क्षेत्र दिखाना, जहाँ छोड़ा वहीं से शुरू कराना, रिवीज़न सूची बनाना।", "ऐप चलाने पर बनती है"],
         ["सब्सक्रिप्शन और भुगतान की स्थिति", "ट्रायल व प्लान की तारीखें, प्लान का प्रकार, स्थिति, तथा Razorpay का भुगतान / सब्सक्रिप्शन रेफ़रेंस ID और राशि। आपके कार्ड, UPI या बैंक का विवरण कभी नहीं।", "पेड एक्सेस देना या रोकना, रिन्यूअल, कैंसिलेशन व रिफंड संभालना, कानून द्वारा ज़रूरी रिकॉर्ड रखना।", "सब्सक्राइब करने पर"],
         ["सहमति का रिकॉर्ड", "प्रोफ़ाइल सेव करते समय आपने इस पॉलिसी को किस तारीख़ व समय पर स्वीकार किया।", "आपकी सहमति का प्रमाण रखना।", "ज़रूरी"],
         ["सहायता संदेश", "आप हमें ईमेल में जो लिखते हैं, आपके ईमेल पते सहित।", "आपको जवाब देना और आपका अनुरोध हल करना।", "सिर्फ़ हमसे संपर्क करने पर"],
     ])),
    ("p",
     "<b>What we do not collect:</b> location, contacts, photos or files, camera or microphone data, SMS inbox, call logs, health data, advertising ID, or your card / UPI / bank details. The app does not read your SMS (code auto-fill uses Google's system SMS Retriever, which needs no SMS permission).",
     "<b>हम क्या नहीं लेते:</b> लोकेशन, कॉन्टैक्ट, फ़ोटो या फ़ाइलें, कैमरा या माइक्रोफ़ोन डेटा, SMS इनबॉक्स, कॉल लॉग, स्वास्थ्य डेटा, एडवर्टाइज़िंग आईडी, या आपके कार्ड / UPI / बैंक का विवरण। ऐप आपके SMS नहीं पढ़ता (कोड ऑटो-फ़िल Google के सिस्टम SMS Retriever से होता है, जिसे SMS अनुमति नहीं चाहिए)।"),

    ("h2", "4. How we use your information", "4. जानकारी का उपयोग"),
    ("ul", [
        "To provide the Service: sign you in, sync progress across your devices, run practice sets, mock tests and analytics.",
        "To manage your subscription: start, renew, cancel and refund, and keep legally required accounting records.",
        "To keep the Service secure: verify your phone number, enforce 2-step verification, detect abuse such as account sharing or scraping, and fix errors.",
        "To communicate with you: one-time sign-in codes, billing and subscription notices, important changes to the Service or these policies, and replies to your requests. We do not send marketing emails without asking you first.",
        "To meet legal obligations and to establish, exercise or defend legal claims.",
    ], [
        "सेवा देने के लिए: साइन-इन कराना, आपके डिवाइसों में प्रगति सिंक करना, प्रैक्टिस सेट, मॉक टेस्ट और एनालिटिक्स चलाना।",
        "सब्सक्रिप्शन संभालने के लिए: शुरू, रिन्यू, कैंसिल और रिफंड करना, तथा कानूनन ज़रूरी लेखा रिकॉर्ड रखना।",
        "सेवा को सुरक्षित रखने के लिए: आपका फ़ोन नंबर सत्यापित करना, 2-स्टेप वेरिफिकेशन लागू करना, अकाउंट साझा करने या स्क्रैपिंग जैसे दुरुपयोग का पता लगाना और गलतियाँ सुधारना।",
        "आपसे संवाद के लिए: वन-टाइम साइन-इन कोड, बिलिंग व सब्सक्रिप्शन सूचनाएँ, सेवा या इन पॉलिसियों में अहम बदलाव, और आपके अनुरोधों के जवाब। आपसे पूछे बिना हम मार्केटिंग ईमेल नहीं भेजते।",
        "कानूनी ज़िम्मेदारियाँ निभाने और कानूनी दावों को स्थापित करने, उनका प्रयोग या बचाव करने के लिए।",
    ]),
    ("p",
     f"<b>Legal basis:</b> your consent (profile and account), performance of the service you asked for (account, progress, subscription), our legitimate interest in security and fraud prevention, and compliance with law.",
     "<b>कानूनी आधार:</b> आपकी सहमति (प्रोफ़ाइल व अकाउंट), आपकी माँगी हुई सेवा का निष्पादन (अकाउंट, प्रगति, सब्सक्रिप्शन), सुरक्षा व धोखाधड़ी रोकने में हमारा वैध हित, और कानून का पालन।"),
    ("note",
     "<b>We do not sell your personal information</b>, we do not rent it, we do not use it for advertising, and we do not build advertising profiles. The Service contains no ads and no third-party analytics or tracking SDKs.",
     "<b>हम आपकी व्यक्तिगत जानकारी बेचते नहीं</b>, किराये पर नहीं देते, विज्ञापन के लिए उपयोग नहीं करते और विज्ञापन-प्रोफ़ाइल नहीं बनाते। सेवा में कोई विज्ञापन और कोई थर्ड-पार्टी एनालिटिक्स या ट्रैकिंग SDK नहीं है।"),

    ("h2", "5. Who receives your information (service providers)", "5. आपकी जानकारी किसे मिलती है (सेवा प्रदाता)"),
    ("p",
     "We share personal information only with service providers who process it on our behalf and only to run the Service. They may not use it for their own advertising. We do not share it with any other third party except as described in section 6.",
     "हम व्यक्तिगत जानकारी सिर्फ़ उन सेवा प्रदाताओं के साथ साझा करते हैं जो हमारी ओर से और सिर्फ़ सेवा चलाने के लिए इसे प्रोसेस करते हैं। वे इसे अपने विज्ञापन के लिए उपयोग नहीं कर सकते। खंड 6 में बताए गए मामलों के सिवा हम इसे किसी और तीसरे पक्ष को नहीं देते।"),
    ("table",
     (["Provider", "What it does for us", "Data it handles", "Where"], [
         ["Supabase", "Secure database, sign-in and server functions.", "Account, profile, study activity, subscription status.", "Hosted in the AWS Asia Pacific (Mumbai) region, India."],
         ["Brevo", "Delivers sign-in code and service emails.", "Your email address and the email content.", "Provider's infrastructure (EU)."],
         ["Google Firebase Authentication", "Sends and checks the SMS code that verifies your mobile number.", "Phone number, IP address and device / app-instance identifier.", "Google's global infrastructure."],
         ["Razorpay", "Payments and autopay mandates (RBI-authorised payment aggregator).", "Payment details you enter on Razorpay; we receive only status, IDs and amount.", "India."],
     ]),
     (["प्रदाता", "हमारे लिए क्या करता है", "कौन-सा डेटा संभालता है", "कहाँ"], [
         ["Supabase", "सुरक्षित डेटाबेस, साइन-इन और सर्वर फ़ंक्शन।", "अकाउंट, प्रोफ़ाइल, पढ़ाई की गतिविधि, सब्सक्रिप्शन की स्थिति।", "AWS एशिया पैसिफ़िक (मुंबई) रीजन, भारत में होस्ट।"],
         ["Brevo", "साइन-इन कोड और सेवा के ईमेल पहुँचाता है।", "आपका ईमेल पता और ईमेल की सामग्री।", "प्रदाता का इंफ्रास्ट्रक्चर (EU)।"],
         ["Google Firebase Authentication", "आपके मोबाइल नंबर की पुष्टि के लिए SMS कोड भेजता और जाँचता है।", "फ़ोन नंबर, IP पता और डिवाइस / ऐप-इंस्टेंस पहचानकर्ता।", "Google का वैश्विक इंफ्रास्ट्रक्चर।"],
         ["Razorpay", "भुगतान और ऑटोपे मैंडेट (RBI से अधिकृत पेमेंट एग्रीगेटर)।", "भुगतान का जो विवरण आप Razorpay पर भरते हैं; हमें सिर्फ़ स्थिति, ID और राशि मिलती है।", "भारत।"],
     ])),
    ("p",
     "Some providers (for example Google and Brevo) may process data on servers outside India. We choose providers that protect data with industry-standard safeguards, and we send them only what is needed for their function.",
     "कुछ प्रदाता (जैसे Google और Brevo) डेटा को भारत के बाहर के सर्वरों पर प्रोसेस कर सकते हैं। हम ऐसे प्रदाता चुनते हैं जो उद्योग-मानक सुरक्षा उपायों से डेटा की रक्षा करते हैं, और उन्हें सिर्फ़ उतना ही भेजते हैं जितना उनके काम के लिए ज़रूरी है।"),

    ("h2", "6. Other disclosures", "6. अन्य खुलासे"),
    ("ul", [
        "<b>Legal and safety:</b> when required by law, court order or a lawful request from a government authority, or to protect the rights, safety and property of users, the public or us.",
        "<b>Business change:</b> if {co} is merged with or acquired by another business, your information may move with the Service. We will tell you first and the same protection will continue.".format(co=CO),
        "<b>With your consent:</b> in any other case we will ask you first.",
    ], [
        "<b>कानूनी और सुरक्षा:</b> जब कानून, अदालती आदेश या किसी सरकारी प्राधिकारी के वैध अनुरोध के तहत ज़रूरी हो, या उपयोगकर्ताओं, जनता या हमारे अधिकारों, सुरक्षा और संपत्ति की रक्षा के लिए।",
        f"<b>व्यवसाय में बदलाव:</b> अगर {CO} का किसी दूसरे व्यवसाय में विलय या उसके द्वारा अधिग्रहण हो, तो आपकी जानकारी सेवा के साथ जा सकती है। हम पहले आपको बताएँगे और वही सुरक्षा जारी रहेगी।",
        "<b>आपकी सहमति से:</b> बाकी हर स्थिति में हम पहले आपसे पूछेंगे।",
    ]),

    ("h2", "7. How we protect your information", "7. हम आपकी जानकारी की सुरक्षा कैसे करते हैं"),
    ("ul", [
        "<b>Encryption in transit:</b> all traffic between the app / website and our servers uses HTTPS (TLS).",
        "<b>Passwordless sign-in:</b> short-lived one-time codes mean there is no password for an attacker to steal or reuse.",
        "<b>Two-step verification:</b> optional authenticator-app protection, enforced on the server, not only in the app.",
        "<b>Strict access rules:</b> the database uses row-level security so every account can read and change only its own data; administrative keys are kept on the server and are never placed in the app.",
        "<b>No payment data:</b> card / UPI / bank details never reach our systems; they go directly to Razorpay.",
        "<b>App lock (optional):</b> on Android you can lock the app with your fingerprint, face or screen lock and hide its preview in the recent-apps screen. The fingerprint / face check is done by Android; the app never receives or stores biometric data.",
        "<b>Limited internal access:</b> only the people who need it to run and support the Service can access personal data, and secrets are kept out of source code.",
        "<b>Device storage:</b> the app keeps a small cache (such as your language, theme and a copy of your profile and recent results) on your device so it opens quickly. It is cleared when you sign out or delete your account.",
    ], [
        "<b>ट्रांज़िट में एन्क्रिप्शन:</b> ऐप / वेबसाइट और हमारे सर्वर के बीच सारा ट्रैफ़िक HTTPS (TLS) से होता है।",
        "<b>बिना पासवर्ड साइन-इन:</b> कम अवधि वाले वन-टाइम कोड का मतलब है कि कोई पासवर्ड नहीं जिसे हमलावर चुरा या दोबारा इस्तेमाल कर सके।",
        "<b>2-स्टेप वेरिफिकेशन:</b> वैकल्पिक ऑथेंटिकेटर-ऐप सुरक्षा, जो सिर्फ़ ऐप में नहीं बल्कि सर्वर पर लागू होती है।",
        "<b>सख़्त एक्सेस नियम:</b> डेटाबेस रो-लेवल सिक्योरिटी इस्तेमाल करता है, इसलिए हर अकाउंट सिर्फ़ अपना डेटा पढ़ या बदल सकता है; एडमिन कुंजियाँ सर्वर पर रहती हैं और ऐप में कभी नहीं रखी जातीं।",
        "<b>कोई भुगतान डेटा नहीं:</b> कार्ड / UPI / बैंक का विवरण हमारे सिस्टम तक नहीं पहुँचता; वह सीधे Razorpay को जाता है।",
        "<b>ऐप लॉक (वैकल्पिक):</b> एंड्रॉइड पर आप ऐप को फ़िंगरप्रिंट, चेहरा या स्क्रीन लॉक से लॉक कर सकते हैं और हाल के ऐप्स में उसका प्रीव्यू छिपा सकते हैं। फ़िंगरप्रिंट / चेहरे की जाँच एंड्रॉइड करता है; ऐप को बायोमेट्रिक डेटा न मिलता है, न वह उसे रखता है।",
        "<b>सीमित आंतरिक एक्सेस:</b> व्यक्तिगत डेटा तक सिर्फ़ वही लोग पहुँच सकते हैं जिन्हें सेवा चलाने और सहायता देने के लिए ज़रूरी हो, और गोपनीय कुंजियाँ सोर्स कोड से बाहर रखी जाती हैं।",
        "<b>डिवाइस स्टोरेज:</b> ऐप जल्दी खुले, इसके लिए आपके डिवाइस पर एक छोटी कैश (जैसे भाषा, थीम और आपकी प्रोफ़ाइल व हाल के नतीजों की कॉपी) रखता है। साइन-आउट या अकाउंट डिलीट करने पर यह साफ़ हो जाती है।",
    ]),
    ("p",
     "No system is completely secure. If a breach affects your personal information we will act promptly to contain it and will inform affected users and the authorities as the law requires.",
     "कोई भी सिस्टम पूरी तरह सुरक्षित नहीं होता। अगर किसी उल्लंघन से आपकी व्यक्तिगत जानकारी प्रभावित होती है, तो हम तुरंत उसे रोकने की कार्रवाई करेंगे और कानून के अनुसार प्रभावित उपयोगकर्ताओं व अधिकारियों को सूचित करेंगे।"),

    ("h2", "8. App permissions (Android)", "8. ऐप की अनुमतियाँ (एंड्रॉइड)"),
    ("table",
     (["Permission", "Why the app needs it"], [
         ["INTERNET", "To load questions, save progress and sign you in."],
         ["ACCESS_NETWORK_STATE", "To show an offline screen and retry when your connection returns."],
         ["USE_BIOMETRIC / USE_FINGERPRINT", "Only for the optional App lock. Android performs the check; we never see biometric data."],
         ["READ_GSERVICES", "Used by Google Play services / Firebase to verify your phone number."],
     ]),
     (["अनुमति", "ऐप को इसकी ज़रूरत क्यों है"], [
         ["INTERNET", "प्रश्न लोड करने, प्रगति सेव करने और साइन-इन कराने के लिए।"],
         ["ACCESS_NETWORK_STATE", "ऑफ़लाइन स्क्रीन दिखाने और कनेक्शन लौटने पर दोबारा कोशिश करने के लिए।"],
         ["USE_BIOMETRIC / USE_FINGERPRINT", "सिर्फ़ वैकल्पिक ऐप लॉक के लिए। जाँच एंड्रॉइड करता है; हम बायोमेट्रिक डेटा कभी नहीं देखते।"],
         ["READ_GSERVICES", "आपका फ़ोन नंबर सत्यापित करने के लिए Google Play services / Firebase द्वारा उपयोग।"],
     ])),
    ("p",
     "The app requests no location, contacts, camera, microphone, storage or SMS permission.",
     "ऐप कोई लोकेशन, कॉन्टैक्ट, कैमरा, माइक्रोफ़ोन, स्टोरेज या SMS अनुमति नहीं माँगता।"),

    ("h2", "9. Cookies and browser storage (website)", "9. कुकीज़ और ब्राउज़र स्टोरेज (वेबसाइट)"),
    ("p",
     "The website uses your browser's local storage, not advertising or tracking cookies. It holds your sign-in session, language and theme choice, and a small cache so pages open quickly. You can clear it any time from your browser settings (you will be signed out). This legal website (the pages you are reading) stores only your language choice.",
     "वेबसाइट आपके ब्राउज़र की लोकल स्टोरेज इस्तेमाल करती है, विज्ञापन या ट्रैकिंग कुकीज़ नहीं। इसमें आपका साइन-इन सेशन, भाषा व थीम का चुनाव और पेज जल्दी खोलने वाली एक छोटी कैश रहती है। आप इसे ब्राउज़र सेटिंग से कभी भी साफ़ कर सकते हैं (आप साइन-आउट हो जाएँगे)। यह लीगल वेबसाइट (जो पेज आप पढ़ रहे हैं) सिर्फ़ आपकी भाषा का चुनाव रखती है।"),

    ("h2", "10. How long we keep your information", "10. हम जानकारी कितने समय रखते हैं"),
    ("table",
     (["Information", "How long"], [
         ["Account, profile, study activity, bookmarks, mock results", "While your account is active. Deleted immediately when you delete your account."],
         ["Subscription status", "While your account is active. Deleted with the account."],
         ["Payment records (amount, dates, Razorpay IDs)", "Kept after account deletion only in anonymised form (not linked to you) for the period tax and accounting laws require."],
         ["Support emails", "For as long as needed to resolve your request and to keep a record of it, then deleted."],
         ["Backups at our hosting provider", "Deleted data may remain in encrypted backups for a short, limited period set by the provider and then ages out; it is not used."],
     ]),
     (["जानकारी", "कितने समय"], [
         ["अकाउंट, प्रोफ़ाइल, पढ़ाई की गतिविधि, बुकमार्क, मॉक नतीजे", "जब तक आपका अकाउंट चालू है। अकाउंट डिलीट करते ही तुरंत हटा दिए जाते हैं।"],
         ["सब्सक्रिप्शन की स्थिति", "जब तक अकाउंट चालू है। अकाउंट के साथ हट जाती है।"],
         ["भुगतान रिकॉर्ड (राशि, तारीखें, Razorpay ID)", "अकाउंट डिलीट होने के बाद सिर्फ़ अज्ञात (आपसे जुड़े बिना) रूप में, उतनी अवधि तक जितनी कर और लेखा कानूनों में ज़रूरी हो।"],
         ["सहायता ईमेल", "जब तक आपका अनुरोध हल करने और उसका रिकॉर्ड रखने के लिए ज़रूरी हो, फिर हटा दिए जाते हैं।"],
         ["होस्टिंग प्रदाता के बैकअप", "डिलीट किया डेटा प्रदाता द्वारा तय एक छोटी, सीमित अवधि तक एन्क्रिप्टेड बैकअप में रह सकता है, फिर अपने-आप हट जाता है; उसका उपयोग नहीं होता।"],
     ])),

    ("h2", "11. Your rights and choices", "11. आपके अधिकार और विकल्प"),
    ("ul", [
        "<b>Access and correction:</b> see and edit your profile details any time in the app (Account).",
        "<b>Deletion:</b> delete your account and all linked data in the app (Account → Delete account) or follow the steps on the <a href=\"delete-account.html\">Delete account page</a>. You can also ask us by email to delete specific data.",
        "<b>Withdraw consent:</b> you may withdraw consent at any time by deleting your account; withdrawing does not affect what we did before, and some features cannot run without the data.",
        "<b>Optional data:</b> gender, category and preferred medium are optional; you can leave them empty.",
        "<b>Grievance redressal:</b> if you are not satisfied, contact us (section 12). You may also approach the Data Protection Board of India or another competent authority as the law provides.",
        "<b>Nomination:</b> where the law gives this right, you may nominate a person to exercise your rights in case of your death or incapacity.",
    ], [
        "<b>देखना और सुधारना:</b> ऐप में (अकाउंट) कभी भी अपनी प्रोफ़ाइल की जानकारी देखें और बदलें।",
        "<b>डिलीट करना:</b> ऐप में (अकाउंट → अकाउंट डिलीट करें) अपना अकाउंट और जुड़ा सारा डेटा डिलीट करें, या <a href=\"delete-account.html\">अकाउंट डिलीट पेज</a> के चरण अपनाएँ। आप ईमेल से किसी खास डेटा को हटाने का अनुरोध भी कर सकते हैं।",
        "<b>सहमति वापस लेना:</b> आप अकाउंट डिलीट करके कभी भी सहमति वापस ले सकते हैं; इससे पहले किए गए काम पर असर नहीं पड़ता और कुछ फ़ीचर डेटा के बिना नहीं चल सकते।",
        "<b>वैकल्पिक डेटा:</b> लिंग, वर्ग और पसंदीदा माध्यम वैकल्पिक हैं; आप इन्हें खाली छोड़ सकते हैं।",
        "<b>शिकायत निवारण:</b> संतुष्ट न हों तो हमसे संपर्क करें (खंड 12)। कानून के अनुसार आप भारतीय डेटा संरक्षण बोर्ड या अन्य सक्षम प्राधिकारी के पास भी जा सकते हैं।",
        "<b>नामांकन:</b> जहाँ कानून यह अधिकार देता है, वहाँ आप अपनी मृत्यु या अक्षमता की स्थिति में अपने अधिकारों के प्रयोग के लिए किसी व्यक्ति को नामित कर सकते हैं।",
    ]),

    ("h2", "12. Contact and grievance officer", "12. संपर्क और शिकायत अधिकारी"),
    ("p",
     f"For any privacy question, data request or complaint write to the Grievance Officer, {CO}, at {MAIL} from your registered email address. We aim to acknowledge your message within 3 working days and to resolve it within 30 days, or sooner if the law requires. Details are on the <a href=\"contact.html\">Contact &amp; Grievance page</a>.",
     f"किसी भी प्राइवेसी सवाल, डेटा अनुरोध या शिकायत के लिए अपने रजिस्टर्ड ईमेल से शिकायत अधिकारी, {CO}, को {MAIL} पर लिखें। हमारा लक्ष्य आपके संदेश की पावती 3 कार्य-दिवसों में देना और 30 दिनों में, या कानून माँगे तो उससे पहले, समाधान करना है। विवरण <a href=\"contact.html\">संपर्क व शिकायत पेज</a> पर है।"),

    ("h2", "13. Children", "13. बच्चे"),
    ("p",
     f"{APP} is meant for job-exam candidates aged <b>18 or above</b> and is not directed at children. We do not knowingly collect personal information from anyone under 18. If you believe a child has given us information, write to {MAIL} and we will delete it.",
     f"{APP} 18 वर्ष या उससे अधिक उम्र के परीक्षा-अभ्यर्थियों के लिए है और बच्चों के लिए नहीं बनाया गया। हम जानबूझकर 18 वर्ष से कम उम्र के किसी व्यक्ति से व्यक्तिगत जानकारी नहीं लेते। अगर आपको लगता है कि किसी बच्चे ने हमें जानकारी दी है, तो {MAIL} पर लिखें; हम उसे हटा देंगे।"),

    ("h2", "14. Changes to this policy", "14. इस पॉलिसी में बदलाव"),
    ("p",
     "We may update this policy when the Service or the law changes. The date and version at the top show the latest update. For important changes we will tell you in the app or by email before they take effect. Continuing to use the Service after that means you accept the updated policy; if you do not, you can delete your account.",
     "सेवा या कानून बदलने पर हम इस पॉलिसी को अपडेट कर सकते हैं। ऊपर की तारीख़ और संस्करण ताज़ा अपडेट बताते हैं। अहम बदलावों के लागू होने से पहले हम ऐप में या ईमेल से बताएँगे। उसके बाद सेवा का उपयोग जारी रखने का मतलब है कि आप अपडेट की गई पॉलिसी मानते हैं; न मानें तो आप अपना अकाउंट डिलीट कर सकते हैं।"),
]

TERMS = [
    ("glance", [
        f"{APP} is an independent exam-preparation app by <b>{CO}</b>. It is <b>not</b> a government or exam-board product.",
        f"New accounts get a <b>{TRIAL}-day free trial</b>. Paid plans: {PLANS} (taxes included), billed by Razorpay autopay, cancel any time.",
        "We work hard on accuracy but cannot guarantee selection or marks. Always check the official notification.",
        "Be 18 or older, keep your account to yourself, and do not copy or resell the content.",
    ], [
        f"{APP}, <b>{CO}</b> का एक स्वतंत्र परीक्षा-तैयारी ऐप है। यह किसी सरकार या परीक्षा-बोर्ड का उत्पाद <b>नहीं</b> है।",
        f"नए अकाउंट को <b>{TRIAL} दिन का फ्री ट्रायल</b> मिलता है। पेड प्लान: {PLANS_HI} (करों सहित), Razorpay ऑटोपे से बिल, कभी भी कैंसिल करें।",
        "हम सटीकता पर पूरी मेहनत करते हैं, पर चयन या अंकों की गारंटी नहीं दे सकते। हमेशा आधिकारिक अधिसूचना जाँचें।",
        "18 वर्ष या उससे अधिक के हों, अपना अकाउंट अपने तक रखें, और सामग्री को कॉपी या दोबारा न बेचें।",
    ]),
    ("h2", "1. Agreement", "1. समझौता"),
    ("p",
     f'These Terms of Use ("Terms") are a legal agreement between you and <b>{CO}</b> ("we", "us") for the {APP} Android app and website (the "Service"). By creating an account or using the Service you accept these Terms, our <a href="privacy.html">Privacy Policy</a> and our <a href="refund.html">Refund &amp; Cancellation Policy</a>. If you do not accept them, do not use the Service.',
     f'ये उपयोग की शर्तें ("शर्तें") आपके और <b>{CO}</b> ("हम") के बीच {APP} एंड्रॉइड ऐप और वेबसाइट ("सेवा") के लिए एक कानूनी समझौता हैं। अकाउंट बनाकर या सेवा का उपयोग करके आप इन शर्तों, हमारी <a href="privacy.html">प्राइवेसी पॉलिसी</a> और <a href="refund.html">रिफंड व कैंसिलेशन पॉलिसी</a> को स्वीकार करते हैं। स्वीकार न हो तो सेवा का उपयोग न करें।'),
    ("h2", "2. Who can use the Service", "2. सेवा कौन उपयोग कर सकता है"),
    ("ul", [
        "You must be <b>18 years or older</b> and able to enter a binding contract under Indian law.",
        "You must give correct information (including your mobile number and email) and keep it up to date.",
        "One account is for one person. You are responsible for everything done through your account.",
    ], [
        "आपकी उम्र <b>18 वर्ष या अधिक</b> हो और आप भारतीय कानून के तहत बाध्यकारी अनुबंध करने में सक्षम हों।",
        "आपको सही जानकारी (मोबाइल नंबर और ईमेल सहित) देनी होगी और उसे अद्यतन रखना होगा।",
        "एक अकाउंट एक व्यक्ति के लिए है। अपने अकाउंट से होने वाली हर गतिविधि के लिए आप ज़िम्मेदार हैं।",
    ]),
    ("h2", "3. What the Service is", "3. सेवा क्या है"),
    ("p",
     f"{APP} offers practice questions, topic-wise tests, full-length and subject mock tests, answer explanations, bookmarks, progress analytics and revision tools in English and Hindi, to help candidates prepare for the UP Super TET and similar teacher eligibility exams. The content is prepared for this app by {CO}, may be drafted with the help of software tools, and is reviewed for accuracy. Questions follow common exam patterns but are <b>not official exam papers</b>.",
     f"{APP} अभ्यर्थियों को UP Super TET और ऐसी ही शिक्षक पात्रता परीक्षाओं की तैयारी में मदद के लिए अंग्रेज़ी और हिन्दी में प्रैक्टिस प्रश्न, टॉपिक-वार टेस्ट, फ़ुल-लेंथ व सब्जेक्ट मॉक टेस्ट, उत्तरों की व्याख्या, बुकमार्क, प्रगति एनालिटिक्स और रिवीज़न टूल देता है। सामग्री {CO} द्वारा इस ऐप के लिए तैयार की जाती है, उसका प्रारूप सॉफ़्टवेयर टूल की मदद से बन सकता है, और सटीकता के लिए उसकी समीक्षा होती है। प्रश्न प्रचलित परीक्षा-पैटर्न के अनुसार हैं पर <b>आधिकारिक परीक्षा पत्र नहीं</b> हैं।"),
    ("note",
     f"<b>No affiliation.</b> {APP} is an independent study aid. It is not affiliated with, endorsed by, sponsored by or approved by any government body, ministry or exam board, including the Uttar Pradesh Education Service Selection Commission (UPESSC), NCERT, NCTE or CBSE. Names such as \"UP Super TET\", \"UPESSC\", \"CTET\" and \"NCERT\" are used only to describe the exams and study material the app helps you prepare for; they belong to their respective owners.",
     f"<b>कोई संबद्धता नहीं।</b> {APP} एक स्वतंत्र अध्ययन-सहायक है। यह किसी सरकारी संस्था, मंत्रालय या परीक्षा बोर्ड, जिसमें उत्तर प्रदेश शिक्षा सेवा चयन आयोग (UPESSC), NCERT, NCTE या CBSE शामिल हैं, से जुड़ा, उनके द्वारा मान्य, प्रायोजित या अनुमोदित नहीं है। \"UP Super TET\", \"UPESSC\", \"CTET\" और \"NCERT\" जैसे नाम सिर्फ़ उन परीक्षाओं और अध्ययन-सामग्री का वर्णन करने के लिए हैं जिनकी तैयारी में ऐप मदद करता है; वे अपने-अपने स्वामियों के हैं।"),
    ("h2", "4. Accuracy and no guarantee", "4. सटीकता और कोई गारंटी नहीं"),
    ("p",
     "Exam patterns, syllabi, laws and facts change. We make every reasonable effort to keep the content correct and up to date, and we correct errors when we find or are told about them, but we do not promise that it is complete or error-free. We do not guarantee selection, rank, marks or any result. Always confirm the official notification, syllabus and dates on the exam board's own website. If you find a mistake, please write to us.",
     "परीक्षा-पैटर्न, पाठ्यक्रम, कानून और तथ्य बदलते रहते हैं। हम सामग्री को सही और अद्यतन रखने की हर उचित कोशिश करते हैं, और गलती मिलने या बताए जाने पर सुधारते हैं, पर यह वादा नहीं करते कि वह पूर्ण या त्रुटि-रहित है। हम चयन, रैंक, अंक या किसी भी नतीजे की गारंटी नहीं देते। आधिकारिक अधिसूचना, पाठ्यक्रम और तारीखें हमेशा परीक्षा बोर्ड की अपनी वेबसाइट से पक्की करें। कोई गलती दिखे तो हमें लिखें।"),
    ("h2", "5. Free trial, plans and payment", "5. फ्री ट्रायल, प्लान और भुगतान"),
    ("ul", [
        f"A new account receives a <b>{TRIAL}-day free trial</b> with access to the Service. No payment details are needed for the trial, and it is given once per account.",
        f"After the trial, paid access needs a plan: {PLANS}. Prices are in Indian rupees and include applicable taxes. We may change prices for future periods; the price you agreed to does not change during a period you have already paid for.",
        "Paid plans are subscriptions processed by <b>Razorpay</b> using UPI AutoPay or a card mandate. The amount is charged automatically every month, 6 months or year (according to the plan) until you cancel. You will receive pre-debit and payment notifications as RBI rules require.",
        "You can cancel autopay any time in the app (Account). After cancelling there is no next charge and you keep access until the end of the period you have paid for.",
        "When a paid period ends without renewal, paid access stops. Your data stays until you delete your account.",
        "Refunds are governed by our <a href=\"refund.html\">Refund &amp; Cancellation Policy</a>.",
    ], [
        f"नए अकाउंट को सेवा के एक्सेस के साथ <b>{TRIAL} दिन का फ्री ट्रायल</b> मिलता है। ट्रायल के लिए भुगतान का विवरण नहीं चाहिए, और यह प्रति अकाउंट एक बार मिलता है।",
        f"ट्रायल के बाद पेड एक्सेस के लिए प्लान चाहिए: {PLANS_HI}। कीमतें भारतीय रुपयों में और लागू करों सहित हैं। हम आगामी अवधियों के लिए कीमतें बदल सकते हैं; जिस अवधि का आप भुगतान कर चुके हैं उसमें आपकी तय कीमत नहीं बदलती।",
        "पेड प्लान <b>Razorpay</b> द्वारा संसाधित सब्सक्रिप्शन हैं, जो UPI AutoPay या कार्ड मैंडेट से चलते हैं। प्लान के अनुसार हर महीने, 6 महीने या साल में राशि अपने-आप कटती है, जब तक आप कैंसिल न करें। RBI के नियमों के अनुसार आपको प्री-डेबिट और भुगतान की सूचनाएँ मिलेंगी।",
        "आप ऐप में (अकाउंट) कभी भी ऑटोपे कैंसिल कर सकते हैं। कैंसिल के बाद अगला चार्ज नहीं लगता और भुगतान की अवधि के अंत तक एक्सेस बना रहता है।",
        "बिना रिन्यूअल पेड अवधि खत्म होने पर पेड एक्सेस बंद हो जाता है। आपका डेटा तब तक रहता है जब तक आप अकाउंट डिलीट न करें।",
        "रिफंड हमारी <a href=\"refund.html\">रिफंड व कैंसिलेशन पॉलिसी</a> से तय होते हैं।",
    ]),
    ("h2", "6. Your responsibilities and acceptable use", "6. आपकी ज़िम्मेदारी और स्वीकार्य उपयोग"),
    ("p", "You agree that you will not:", "आप सहमत हैं कि आप ये नहीं करेंगे:"),
    ("ul", [
        "share, sell, rent or lend your account, or let several people use one account;",
        "copy, scrape, download in bulk, republish, translate for resale, or otherwise redistribute questions, explanations or other content, or use it to train a competing product;",
        "bypass, probe or disable security, payment or access controls, or use bots, scripts or tools to automate access;",
        "reverse-engineer, decompile or tamper with the app, except as the law expressly allows;",
        "use the Service for anything unlawful, or in a way that harms the Service, other users or us;",
        "give false information, or use another person's identity, phone number or email.",
    ], [
        "अपना अकाउंट साझा, बेचना, किराये पर या उधार देना, या एक अकाउंट कई लोगों से इस्तेमाल करवाना;",
        "प्रश्नों, व्याख्याओं या अन्य सामग्री को कॉपी करना, स्क्रैप करना, बड़ी मात्रा में डाउनलोड करना, दोबारा प्रकाशित करना, बिक्री के लिए अनुवाद करना या किसी और तरह बाँटना, या उससे प्रतिस्पर्धी उत्पाद को प्रशिक्षित करना;",
        "सुरक्षा, भुगतान या एक्सेस-कंट्रोल को बायपास करना, जाँचना या बंद करना, या एक्सेस को स्वचालित करने के लिए बॉट, स्क्रिप्ट या टूल इस्तेमाल करना;",
        "ऐप को रिवर्स-इंजीनियर, डीकंपाइल या उसके साथ छेड़छाड़ करना, सिवाय उसके जो कानून स्पष्ट रूप से अनुमति दे;",
        "सेवा का किसी गैरकानूनी काम में, या सेवा, अन्य उपयोगकर्ताओं या हमें नुकसान पहुँचाने के तरीके से उपयोग करना;",
        "झूठी जानकारी देना, या किसी और की पहचान, फ़ोन नंबर या ईमेल इस्तेमाल करना।",
    ]),
    ("h2", "7. Intellectual property", "7. बौद्धिक संपदा"),
    ("p",
     f"The Service, including the app, its design, software, questions, explanations, translations, logos and the name {APP}, belongs to {CO} or its licensors and is protected by Indian and international intellectual-property law. We give you a personal, non-exclusive, non-transferable, revocable licence to use the Service for your own exam preparation while you comply with these Terms. No other right is granted. Third-party names and marks belong to their owners.",
     f"सेवा, जिसमें ऐप, उसका डिज़ाइन, सॉफ़्टवेयर, प्रश्न, व्याख्याएँ, अनुवाद, लोगो और {APP} नाम शामिल हैं, {CO} या उसके लाइसेंसदाताओं की है और भारतीय तथा अंतरराष्ट्रीय बौद्धिक-संपदा कानून से संरक्षित है। इन शर्तों का पालन करने तक हम आपको अपनी परीक्षा की तैयारी के लिए सेवा के उपयोग का एक निजी, गैर-विशिष्ट, अहस्तांतरणीय, वापस लेने योग्य लाइसेंस देते हैं। कोई और अधिकार नहीं दिया जाता। तीसरे पक्षों के नाम और चिह्न उनके स्वामियों के हैं।"),
    ("h2", "8. Availability and changes", "8. उपलब्धता और बदलाव"),
    ("p",
     "We try to keep the Service available, but it may be interrupted for maintenance, updates or reasons beyond our control (such as network, hosting or payment-provider outages). We may add, change or remove features and content. If we stop the Service entirely, we will give reasonable notice and, for any paid period that cannot be served, a pro-rata refund.",
     "हम सेवा को उपलब्ध रखने की कोशिश करते हैं, पर रखरखाव, अपडेट या हमारे नियंत्रण से बाहर कारणों (जैसे नेटवर्क, होस्टिंग या पेमेंट-प्रदाता की खराबी) से वह बाधित हो सकती है। हम फ़ीचर और सामग्री जोड़, बदल या हटा सकते हैं। अगर हम सेवा पूरी तरह बंद करेंगे, तो उचित सूचना देंगे और जिस पेड अवधि की सेवा नहीं दी जा सकेगी उसका आनुपातिक रिफंड देंगे।"),
    ("h2", "9. Suspension and ending your account", "9. निलंबन और अकाउंट समाप्त करना"),
    ("p",
     "You can stop using the Service and delete your account at any time (see <a href=\"delete-account.html\">Delete account</a>). We may suspend or end an account, with notice where practical, if you break these Terms, misuse the Service or the law requires it. Rights and duties that by nature continue (for example intellectual property, limits of liability and dispute resolution) survive the end of the account.",
     "आप कभी भी सेवा का उपयोग बंद कर अपना अकाउंट डिलीट कर सकते हैं (<a href=\"delete-account.html\">अकाउंट डिलीट</a> देखें)। अगर आप इन शर्तों को तोड़ें, सेवा का दुरुपयोग करें या कानून ऐसा माँगे, तो हम जहाँ व्यावहारिक हो सूचना देकर अकाउंट निलंबित या समाप्त कर सकते हैं। जो अधिकार और कर्तव्य स्वभाव से जारी रहते हैं (जैसे बौद्धिक संपदा, ज़िम्मेदारी की सीमा और विवाद-समाधान) वे अकाउंट समाप्त होने के बाद भी लागू रहते हैं।"),
    ("h2", "10. Disclaimer and limits of liability", "10. अस्वीकरण और ज़िम्मेदारी की सीमा"),
    ("p",
     "To the fullest extent the law allows, the Service is provided \"as is\" and \"as available\", without warranties of any kind about fitness for a particular purpose or uninterrupted, error-free operation. To the extent the law allows, we are not liable for indirect, incidental or consequential loss, or for loss of opportunity, marks, selection or income, and our total liability for any claim relating to the Service is limited to the amount you paid us for the Service in the 12 months before the claim. Nothing in these Terms limits any right you have under the Consumer Protection Act, 2019 or any liability that cannot be limited by law.",
     "कानून जितनी अनुमति दे उस सीमा तक, सेवा \"जैसी है\" और \"जैसी उपलब्ध है\" के आधार पर दी जाती है, किसी खास उद्देश्य की उपयुक्तता या निर्बाध, त्रुटि-रहित संचालन की किसी भी तरह की वारंटी के बिना। कानून की अनुमति की सीमा तक हम अप्रत्यक्ष, आनुषंगिक या परिणामी नुकसान, या अवसर, अंक, चयन या आय के नुकसान के लिए ज़िम्मेदार नहीं हैं, और सेवा से जुड़े किसी भी दावे के लिए हमारी कुल ज़िम्मेदारी दावे से पहले के 12 महीनों में आपके द्वारा सेवा के लिए हमें दी गई राशि तक सीमित है। इन शर्तों का कोई भी हिस्सा उपभोक्ता संरक्षण अधिनियम, 2019 के तहत आपके किसी अधिकार, या कानून से सीमित न की जा सकने वाली किसी ज़िम्मेदारी को सीमित नहीं करता।"),
    ("h2", "11. Governing law and disputes", "11. लागू कानून और विवाद"),
    ("p",
     f"These Terms are governed by the laws of India. Please first write to us at {MAIL} so we can try to resolve any complaint informally. If that does not work, the courts of competent jurisdiction in India will decide the dispute, without limiting any right you have as a consumer to approach a consumer forum.",
     f"ये शर्तें भारत के कानूनों से संचालित हैं। कृपया पहले {MAIL} पर हमें लिखें ताकि हम किसी भी शिकायत को आपसी तौर पर सुलझाने की कोशिश कर सकें। इससे हल न हो तो भारत की सक्षम अधिकारिता वाली अदालतें विवाद तय करेंगी, और इससे उपभोक्ता के रूप में उपभोक्ता मंच जाने के आपके किसी अधिकार पर असर नहीं पड़ता।"),
    ("h2", "12. Changes to these Terms and contact", "12. शर्तों में बदलाव और संपर्क"),
    ("p",
     f"We may update these Terms; the date and version at the top show the latest update, and for important changes we will inform you in the app or by email. Continuing to use the Service after a change means you accept it. Questions: {MAIL}.",
     f"हम इन शर्तों को अपडेट कर सकते हैं; ऊपर की तारीख़ और संस्करण ताज़ा अपडेट बताते हैं, और अहम बदलावों की सूचना ऐप में या ईमेल से देंगे। बदलाव के बाद सेवा का उपयोग जारी रखने का मतलब है कि आप उसे मानते हैं। सवाल: {MAIL}।"),
]

REFUND = [
    ("glance", [
        f"You get a <b>{TRIAL}-day free trial</b> to try everything before paying.",
        "<b>Cancel autopay any time</b> in the app. No next charge; access continues until the paid period ends.",
        "Because digital access starts immediately, refunds are generally not given for a period already paid. <b>Exceptions</b> (double charge, payment taken but access not activated, a charge after cancellation) get a <b>full refund</b>.",
        "Approved refunds go back to the original payment method in 5–7 working days.",
    ], [
        f"भुगतान से पहले सब कुछ आज़माने के लिए आपको <b>{TRIAL} दिन का फ्री ट्रायल</b> मिलता है।",
        "ऐप में <b>कभी भी ऑटोपे कैंसिल करें</b>। अगला चार्ज नहीं लगता; भुगतान की अवधि खत्म होने तक एक्सेस रहता है।",
        "डिजिटल एक्सेस तुरंत शुरू हो जाने से, जिस अवधि का भुगतान हो चुका है उसका रिफंड आम तौर पर नहीं मिलता। <b>अपवादों</b> (दो बार चार्ज, भुगतान कटा पर एक्सेस चालू नहीं हुआ, कैंसिल के बाद चार्ज) में <b>पूरा रिफंड</b> मिलता है।",
        "मंज़ूर रिफंड 5–7 कार्य-दिवसों में मूल भुगतान माध्यम में लौटता है।",
    ]),
    ("h2", "1. Free trial", "1. फ्री ट्रायल"),
    ("p",
     f"Every new account gets a {TRIAL}-day free trial, with no payment details needed, so that you can test the full Service before you decide to pay. When the trial ends, paid access needs a plan; nothing is charged automatically at the end of the trial.",
     f"हर नए अकाउंट को {TRIAL} दिन का फ्री ट्रायल मिलता है, बिना भुगतान विवरण के, ताकि आप पैसे देने का फ़ैसला करने से पहले पूरी सेवा आज़मा सकें। ट्रायल खत्म होने पर पेड एक्सेस के लिए प्लान चाहिए; ट्रायल के अंत में अपने-आप कुछ चार्ज नहीं होता।"),
    ("h2", "2. Plans and billing", "2. प्लान और बिलिंग"),
    ("p",
     f"Plans: {PLANS}, in Indian rupees, taxes included. Payment is taken by Razorpay through UPI AutoPay or a card mandate on the plan's cycle (monthly, 6-monthly or yearly) until you cancel.",
     f"प्लान: {PLANS_HI}, भारतीय रुपयों में, करों सहित। भुगतान Razorpay द्वारा UPI AutoPay या कार्ड मैंडेट से प्लान के चक्र (मासिक, 6-मासिक या वार्षिक) पर तब तक लिया जाता है जब तक आप कैंसिल न करें।"),
    ("h2", "3. How to cancel", "3. कैंसिल कैसे करें"),
    ("ol", [
        f"Open the app and go to <b>Account</b>.",
        "In the subscription section choose <b>Cancel autopay</b> and confirm.",
        "You will see that auto-renewal is off. If you cannot sign in, email us from your registered address and we will cancel it for you.",
    ], [
        "ऐप खोलें और <b>अकाउंट</b> पर जाएँ।",
        "सब्सक्रिप्शन सेक्शन में <b>ऑटोपे कैंसिल करें</b> चुनें और पुष्टि करें।",
        "आपको दिखेगा कि ऑटो-रिन्यूअल बंद है। साइन-इन न हो पा रहा हो तो अपने रजिस्टर्ड पते से हमें ईमेल करें; हम आपके लिए कैंसिल कर देंगे।",
    ]),
    ("p",
     "After cancelling, no further amount is charged and you keep paid access until the end of the period you have already paid for. Deleting your account also cancels autopay first.",
     "कैंसिल करने के बाद आगे कोई राशि नहीं कटती और जिस अवधि का आप भुगतान कर चुके हैं उसके अंत तक पेड एक्सेस रहता है। अकाउंट डिलीट करने पर भी पहले ऑटोपे कैंसिल होता है।"),
    ("h2", "4. Refunds", "4. रिफंड"),
    ("p",
     "Because digital access starts as soon as you pay, we generally do not refund a subscription period that has already been paid for and started. We will give a <b>full refund</b> in these cases:",
     "डिजिटल एक्सेस भुगतान होते ही शुरू हो जाता है, इसलिए हम आम तौर पर उस सब्सक्रिप्शन अवधि का रिफंड नहीं देते जिसका भुगतान हो चुका और जो शुरू हो चुकी हो। इन स्थितियों में हम <b>पूरा रिफंड</b> देंगे:"),
    ("ul", [
        "You were charged <b>twice</b> (duplicate payment) for the same period.",
        "The payment was deducted but <b>paid access was not activated</b> and we could not fix it.",
        "You were charged <b>after you cancelled</b> autopay.",
        "We stop the Service before the end of a paid period (pro-rata refund for the unused part).",
    ], [
        "एक ही अवधि के लिए आपसे <b>दो बार</b> चार्ज हुआ (दोहरा भुगतान)।",
        "भुगतान कटा पर <b>पेड एक्सेस चालू नहीं हुआ</b> और हम उसे ठीक नहीं कर सके।",
        "ऑटोपे <b>कैंसिल करने के बाद</b> आपसे चार्ज हुआ।",
        "हम किसी पेड अवधि के खत्म होने से पहले सेवा बंद कर दें (अनुपयोगी हिस्से का आनुपातिक रिफंड)।",
    ]),
    ("p",
     "This policy does not affect any right you have under the Consumer Protection Act, 2019 or other law.",
     "यह पॉलिसी उपभोक्ता संरक्षण अधिनियम, 2019 या किसी अन्य कानून के तहत आपके किसी अधिकार को प्रभावित नहीं करती।"),
    ("h2", "5. How to ask for a refund", "5. रिफंड कैसे माँगें"),
    ("p",
     f"Email {MAIL} from your registered email address with the subject \"Refund request\", the date and amount of the payment, and the Razorpay payment ID (or a screenshot of the payment message). Please write within 7 days of the charge where you can; we still look at later requests. We will investigate and reply within 3 working days.",
     f"अपने रजिस्टर्ड ईमेल पते से {MAIL} पर \"Refund request\" विषय के साथ भुगतान की तारीख़ और राशि, और Razorpay पेमेंट ID (या भुगतान संदेश का स्क्रीनशॉट) भेजें। हो सके तो चार्ज के 7 दिनों के भीतर लिखें; बाद के अनुरोध भी हम देखते हैं। हम जाँच करके 3 कार्य-दिवसों में जवाब देंगे।"),
    ("h2", "6. How refunds are paid", "6. रिफंड का भुगतान कैसे होता है"),
    ("p",
     "An approved refund is sent through Razorpay to the original payment method (UPI account or card) within 5–7 working days. Your bank may take extra time to show it. Where a failed payment was debited, the bank or Razorpay may reverse it automatically.",
     "मंज़ूर रिफंड Razorpay के ज़रिये मूल भुगतान माध्यम (UPI खाता या कार्ड) में 5–7 कार्य-दिवसों में भेजा जाता है। आपके बैंक को दिखाने में अतिरिक्त समय लग सकता है। जहाँ विफल भुगतान कट गया हो, वहाँ बैंक या Razorpay उसे अपने-आप वापस कर सकते हैं।"),
]

DELETE = [
    ("glance", [
        "You can delete your account and <b>all data linked to it</b> yourself, any time, inside the app.",
        "Deletion happens <b>immediately</b> and cannot be undone. If autopay is on, it is cancelled first.",
        f"Cannot sign in? Email {MAIL} from your registered address and we will delete it for you.",
    ], [
        "आप जब चाहें ऐप के अंदर खुद अपना अकाउंट और <b>उससे जुड़ा सारा डेटा</b> डिलीट कर सकते हैं।",
        "डिलीशन <b>तुरंत</b> होता है और वापस नहीं लिया जा सकता। ऑटोपे चालू हो तो पहले वह कैंसिल होता है।",
        f"साइन-इन नहीं हो रहा? अपने रजिस्टर्ड पते से {MAIL} पर ईमेल करें; हम आपके लिए डिलीट कर देंगे।",
    ]),
    ("p",
     f"This page explains how to delete your <b>{APP}</b> account (a service of {CO}) and the data linked to it. It is the account-deletion page for Google Play.",
     f"यह पेज बताता है कि अपना <b>{APP}</b> अकाउंट ({CO} की सेवा) और उससे जुड़ा डेटा कैसे डिलीट करें। यह Google Play के लिए अकाउंट-डिलीशन पेज है।"),
    ("h2", "1. Delete inside the app (recommended)", "1. ऐप के अंदर डिलीट करें (अनुशंसित)"),
    ("ol", [
        f"Open <b>{APP}</b> and sign in (or open the website and sign in).",
        "Go to <b>Account</b> and scroll down to <b>Delete account</b>.",
        "Read the warning and confirm. The account is deleted at once and you are signed out.",
    ], [
        f"<b>{APP}</b> खोलें और साइन-इन करें (या वेबसाइट खोलकर साइन-इन करें)।",
        "<b>अकाउंट</b> पर जाएँ और नीचे <b>अकाउंट डिलीट करें</b> तक स्क्रॉल करें।",
        "चेतावनी पढ़कर पुष्टि करें। अकाउंट तुरंत डिलीट हो जाता है और आप साइन-आउट हो जाते हैं।",
    ]),
    ("h2", "2. Cannot sign in? Ask us", "2. साइन-इन नहीं हो रहा? हमसे कहें"),
    ("p",
     f"Email <b>{MAIL}</b> from the email address registered on the account with the subject \"Delete my account\". We may ask you to confirm a detail of the profile to make sure it is you. We will delete the account and confirm by email, normally within 7 days.",
     f"खाते पर रजिस्टर्ड ईमेल पते से <b>{MAIL}</b> पर \"Delete my account\" विषय के साथ ईमेल करें। यह पक्का करने के लिए कि वह आप ही हैं, हम प्रोफ़ाइल की कोई जानकारी पूछ सकते हैं। हम अकाउंट डिलीट करके ईमेल से पुष्टि करेंगे, आम तौर पर 7 दिनों में।"),
    ("h2", "3. What is deleted", "3. क्या डिलीट होता है"),
    ("ul", [
        "Your account and sign-in details, including your email address and any 2-step verification secret.",
        "Your profile: name, father's name, date of birth, mobile number, qualification, exam details, state, district and the optional fields.",
        "Your study data: attempted questions and answers, mock-test history, bookmarks, streak and preferences.",
        "Your subscription record. If autopay is active it is cancelled first, so you are not charged after deleting.",
        "The copy of your data cached on your device is cleared when you sign out or uninstall the app.",
    ], [
        "आपका अकाउंट और साइन-इन विवरण, जिसमें आपका ईमेल पता और कोई भी 2-स्टेप वेरिफिकेशन कुंजी शामिल है।",
        "आपकी प्रोफ़ाइल: नाम, पिता का नाम, जन्म तिथि, मोबाइल नंबर, योग्यता, परीक्षा का विवरण, राज्य, ज़िला और वैकल्पिक फ़ील्ड।",
        "आपका पढ़ाई का डेटा: हल किए प्रश्न व उत्तर, मॉक-टेस्ट का इतिहास, बुकमार्क, स्ट्रीक और पसंद।",
        "आपका सब्सक्रिप्शन रिकॉर्ड। ऑटोपे चालू हो तो पहले वह कैंसिल होता है, ताकि डिलीट के बाद आपसे चार्ज न हो।",
        "आपके डिवाइस पर कैश की गई आपके डेटा की कॉपी साइन-आउट करने या ऐप अनइंस्टॉल करने पर साफ़ हो जाती है।",
    ]),
    ("h2", "4. What may be kept, and for how long", "4. क्या रखा जा सकता है और कितने समय"),
    ("ul", [
        "<b>Payment records</b> (amount, dates, Razorpay reference IDs) that tax and accounting laws require us to keep. They are kept <b>without your identity</b> (no longer linked to you) for the legally required period.",
        "<b>Backups</b> at our hosting provider may hold deleted data in encrypted form for a short, limited period before they age out; it is not used or restored.",
        "<b>Our own correspondence</b> (the emails you send us) is kept only as long as needed to handle your request and keep a record of it.",
    ], [
        "<b>भुगतान रिकॉर्ड</b> (राशि, तारीखें, Razorpay रेफ़रेंस ID) जिन्हें कर और लेखा कानूनों के कारण रखना ज़रूरी है। वे कानूनन आवश्यक अवधि तक <b>आपकी पहचान के बिना</b> (आपसे जुड़े नहीं) रखे जाते हैं।",
        "हमारे होस्टिंग प्रदाता के <b>बैकअप</b> में डिलीट किया डेटा एक छोटी, सीमित अवधि तक एन्क्रिप्टेड रूप में रह सकता है, फिर हट जाता है; उसका उपयोग या बहाली नहीं होती।",
        "<b>हमारा पत्राचार</b> (आपके भेजे ईमेल) सिर्फ़ उतने समय रखा जाता है जितना आपका अनुरोध संभालने और उसका रिकॉर्ड रखने के लिए ज़रूरी हो।",
    ]),
    ("h2", "5. Delete only some data", "5. सिर्फ़ कुछ डेटा डिलीट करना"),
    ("p",
     f"You can edit or clear the optional profile fields (gender, category, preferred medium) yourself in <b>Account</b>. To remove other specific data without deleting the whole account, email {MAIL} and tell us what to remove. Some data (such as your email and mobile number) is needed for the account to work.",
     f"आप <b>अकाउंट</b> में वैकल्पिक प्रोफ़ाइल फ़ील्ड (लिंग, वर्ग, पसंदीदा माध्यम) खुद बदल या खाली कर सकते हैं। पूरा अकाउंट डिलीट किए बिना कोई और खास डेटा हटाने के लिए {MAIL} पर ईमेल करके बताएँ कि क्या हटाना है। कुछ डेटा (जैसे आपका ईमेल और मोबाइल नंबर) अकाउंट चलने के लिए ज़रूरी है।"),
    ("warn",
     "Deleting your account is permanent. Your progress and any remaining paid time cannot be restored. If you only want to stop paying, cancel autopay instead (see the <a href=\"refund.html\">Refund &amp; Cancellation page</a>).",
     "अकाउंट डिलीट करना स्थायी है। आपकी प्रगति और बची हुई पेड अवधि वापस नहीं लाई जा सकती। अगर आप सिर्फ़ भुगतान रोकना चाहते हैं, तो इसके बजाय ऑटोपे कैंसिल करें (<a href=\"refund.html\">रिफंड व कैंसिलेशन पेज</a> देखें)।"),
]

CONTACT = [
    ("p",
     f"{APP} is designed, developed and operated by <b>{CO}</b>, India. We read every message. Please write from the email address registered on your account so we can find and protect your data.",
     f"{APP} को <b>{CO}</b>, भारत ने डिज़ाइन, विकसित और संचालित किया है। हम हर संदेश पढ़ते हैं। कृपया अपने अकाउंट पर रजिस्टर्ड ईमेल पते से लिखें ताकि हम आपका डेटा ढूँढ और सुरक्षित रख सकें।"),
    ("h2", "Support and grievance contact", "सहायता और शिकायत संपर्क"),
    ("table",
     (["For", "Write to", "What to include", "Our target reply"], [
         ["Help with the app, sign-in, subscription", MAIL, "Your registered email, what happened, device model and Android version, a screenshot if possible.", "3 working days"],
         ["Refund request or billing problem", MAIL, "Subject \"Refund request\", payment date, amount, Razorpay payment ID.", "3 working days"],
         ["Privacy question, access / correction / deletion request", MAIL, "Subject \"Privacy request\" or \"Delete my account\", from your registered email.", "Acknowledged in 3 working days; resolved within 30 days"],
         ["Complaint / Grievance Officer", MAIL, f"Subject \"Grievance\", addressed to the Grievance Officer, {CO}; describe the issue and the outcome you want.", "Acknowledged in 3 working days; resolved within 30 days"],
         ["Wrong or outdated question / content error", MAIL, "The subject, topic and question text, and what you think is correct (with a source if you have one).", "We review and correct errors quickly"],
     ]),
     (["किस लिए", "कहाँ लिखें", "क्या बताएँ", "हमारा जवाब लक्ष्य"], [
         ["ऐप, साइन-इन, सब्सक्रिप्शन में मदद", MAIL, "आपका रजिस्टर्ड ईमेल, क्या हुआ, डिवाइस मॉडल व एंड्रॉइड संस्करण, हो सके तो स्क्रीनशॉट।", "3 कार्य-दिवस"],
         ["रिफंड अनुरोध या बिलिंग की समस्या", MAIL, "विषय \"Refund request\", भुगतान की तारीख़, राशि, Razorpay पेमेंट ID।", "3 कार्य-दिवस"],
         ["प्राइवेसी सवाल, एक्सेस / सुधार / डिलीशन अनुरोध", MAIL, "विषय \"Privacy request\" या \"Delete my account\", आपके रजिस्टर्ड ईमेल से।", "3 कार्य-दिवस में पावती; 30 दिनों में समाधान"],
         ["शिकायत / शिकायत अधिकारी", MAIL, f"विषय \"Grievance\", शिकायत अधिकारी, {CO} को संबोधित; समस्या और चाहा गया समाधान बताएँ।", "3 कार्य-दिवस में पावती; 30 दिनों में समाधान"],
         ["गलत या पुराना प्रश्न / सामग्री की त्रुटि", MAIL, "विषय, टॉपिक और प्रश्न का पाठ, और आपके अनुसार सही क्या है (स्रोत हो तो साथ में)।", "हम जल्दी समीक्षा कर सुधारते हैं"],
     ])),
    ("note",
     "<b>Please never email your password, card number, UPI PIN or OTP.</b> We never ask for them. The Service has no password, and a one-time code is only for you to type into the app.",
     "<b>कृपया अपना पासवर्ड, कार्ड नंबर, UPI PIN या OTP कभी ईमेल न करें।</b> हम इन्हें कभी नहीं माँगते। सेवा में कोई पासवर्ड नहीं है, और वन-टाइम कोड सिर्फ़ आपके ऐप में डालने के लिए है।"),
    ("h2", "About us", "हमारे बारे में"),
    ("p",
     f"{CO} builds focused learning tools. {APP} brings exam-style practice, mock tests and clear explanations in English and Hindi to candidates preparing for the UP Super TET and similar teacher-eligibility exams. It is an independent product and is not affiliated with any government body or exam board.",
     f"{CO} केंद्रित लर्निंग टूल बनाता है। {APP} UP Super TET और ऐसी शिक्षक-पात्रता परीक्षाओं की तैयारी कर रहे अभ्यर्थियों तक अंग्रेज़ी और हिन्दी में परीक्षा-शैली का अभ्यास, मॉक टेस्ट और स्पष्ट व्याख्याएँ पहुँचाता है। यह एक स्वतंत्र उत्पाद है और किसी सरकारी संस्था या परीक्षा बोर्ड से संबद्ध नहीं है।"),
]

# ---------------------------------------------------------------------------------------------------------------
# Free launch: rewrite the payment wording above without touching it (flip PAYMENTS = True to get it all back).
# ---------------------------------------------------------------------------------------------------------------
def _map(obj, fn):
    if isinstance(obj, str):
        return fn(obj)
    if isinstance(obj, list):
        return [_map(o, fn) for o in obj]
    if isinstance(obj, tuple):
        return tuple(_map(o, fn) for o in obj)
    return obj


_REPL = [
    # privacy
    ("your study progress and your subscription (listed in section 3)", "and your study progress (listed in section 3)"),
    ("<b>Payments:</b> card / UPI details go straight to Razorpay. We never see or store them.",
     "<b>No payments:</b> the app is free to use. We collect no card, UPI or bank details."),
    ("सब्सक्रिप्शन चलाने के लिए ज़रूरी है (खंड 3 में सूची)", "ज़रूरी है (खंड 3 में सूची)"),
    ("<b>भुगतान:</b> कार्ड / UPI का विवरण सीधे Razorpay को जाता है। हम उसे न देखते हैं, न रखते हैं।",
     "<b>कोई भुगतान नहीं:</b> ऐप इस्तेमाल के लिए मुफ़्त है। हम कार्ड, UPI या बैंक का कोई विवरण नहीं लेते।"),
    ("verify identity for support and billing queries", "verify identity for support queries"),
    ("सहायता व बिलिंग सवालों में पहचान की पुष्टि", "सहायता सवालों में पहचान की पुष्टि"),
    ("Account, profile, study activity, subscription status.", "Account, profile and study activity."),
    ("अकाउंट, प्रोफ़ाइल, पढ़ाई की गतिविधि, सब्सक्रिप्शन की स्थिति।", "अकाउंट, प्रोफ़ाइल और पढ़ाई की गतिविधि।"),
    ("one-time sign-in codes, billing and subscription notices, important changes", "one-time sign-in codes, important changes"),
    ("वन-टाइम साइन-इन कोड, बिलिंग व सब्सक्रिप्शन सूचनाएँ, सेवा या इन पॉलिसियों", "वन-टाइम साइन-इन कोड, सेवा या इन पॉलिसियों"),
    ("(account, progress, subscription)", "(account, progress)"),
    ("(अकाउंट, प्रगति, सब्सक्रिप्शन)", "(अकाउंट, प्रगति)"),
    ("<b>No payment data:</b> card / UPI / bank details never reach our systems; they go directly to Razorpay.",
     "<b>No payment data:</b> the app takes no payments, so no card / UPI / bank details are ever collected."),
    ("<b>कोई भुगतान डेटा नहीं:</b> कार्ड / UPI / बैंक का विवरण हमारे सिस्टम तक नहीं पहुँचता; वह सीधे Razorpay को जाता है।",
     "<b>कोई भुगतान डेटा नहीं:</b> ऐप कोई भुगतान नहीं लेता, इसलिए कार्ड / UPI / बैंक का कोई विवरण नहीं लिया जाता।"),
    # terms
    ("these Terms, our <a href=\"privacy.html\">Privacy Policy</a> and our <a href=\"refund.html\">Refund &amp; Cancellation Policy</a>",
     "these Terms and our <a href=\"privacy.html\">Privacy Policy</a>"),
    ("इन शर्तों, हमारी <a href=\"privacy.html\">प्राइवेसी पॉलिसी</a> और <a href=\"refund.html\">रिफंड व कैंसिलेशन पॉलिसी</a> को स्वीकार करते हैं",
     "इन शर्तों और हमारी <a href=\"privacy.html\">प्राइवेसी पॉलिसी</a> को स्वीकार करते हैं"),
    (" and, for any paid period that cannot be served, a pro-rata refund", ""),
    ("उचित सूचना देंगे और जिस पेड अवधि की सेवा नहीं दी जा सकेगी उसका आनुपातिक रिफंड देंगे", "उचित सूचना देंगे"),
    ("network, hosting or payment-provider outages", "network or hosting-provider outages"),
    ("नेटवर्क, होस्टिंग या पेमेंट-प्रदाता की खराबी", "नेटवर्क या होस्टिंग-प्रदाता की खराबी"),
    # delete
    (" If autopay is on, it is cancelled first.", ""),
    (" ऑटोपे चालू हो तो पहले वह कैंसिल होता है।", ""),
    ("Deleting your account is permanent. Your progress and any remaining paid time cannot be restored. If you only want to stop paying, cancel autopay instead (see the <a href=\"refund.html\">Refund &amp; Cancellation page</a>).",
     "Deleting your account is permanent. Your progress and bookmarks cannot be restored."),
    ("अकाउंट डिलीट करना स्थायी है। आपकी प्रगति और बची हुई पेड अवधि वापस नहीं लाई जा सकती। अगर आप सिर्फ़ भुगतान रोकना चाहते हैं, तो इसके बजाय ऑटोपे कैंसिल करें (<a href=\"refund.html\">रिफंड व कैंसिलेशन पेज</a> देखें)।",
     "अकाउंट डिलीट करना स्थायी है। आपकी प्रगति और बुकमार्क वापस नहीं लाए जा सकते।"),
    ("the amount you paid us for the Service in the 12 months before the claim", "the amount (if any) you paid us for the Service in the 12 months before the claim"),
    ("आपके द्वारा सेवा के लिए हमें दी गई राशि", "आपके द्वारा सेवा के लिए हमें दी गई राशि (यदि कोई हो)"),
    # contact
    ("Help with the app, sign-in, subscription", "Help with the app and sign-in"),
    ("ऐप, साइन-इन, सब्सक्रिप्शन में मदद", "ऐप और साइन-इन में मदद"),
]

_DROP_ROWS = (
    "Subscription and payment status", "सब्सक्रिप्शन और भुगतान की स्थिति", "Razorpay", "Subscription status",
    "सब्सक्रिप्शन की स्थिति", "Payment records", "भुगतान रिकॉर्ड", "Refund request or billing problem", "रिफंड अनुरोध या बिलिंग की समस्या",
)
_DROP_ITEMS = (
    "To manage your subscription", "सब्सक्रिप्शन संभालने के लिए", "Your subscription record.", "आपका सब्सक्रिप्शन रिकॉर्ड।",
    "<b>Payment records</b>", "<b>भुगतान रिकॉर्ड</b>",
)


def _free_text(s: str) -> str:
    for a, b in _REPL:
        s = s.replace(a, b)
    return s


def _free_blocks(blocks):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "table":
            tabs = []
            for head, rows in (b[1], b[2]):
                tabs.append((head, [r for r in rows if not any(r[0].startswith(d) for d in _DROP_ROWS)]))
            out.append(("table", tabs[0], tabs[1]))
        elif kind in ("ul", "ol"):
            out.append((kind, [i for i in b[1] if not any(i.startswith(d) for d in _DROP_ITEMS)],
                        [i for i in b[2] if not any(i.startswith(d) for d in _DROP_ITEMS)]))
        else:
            out.append(b)
    return _map(out, _free_text)


if not PAYMENTS:
    PRIVACY = _free_blocks(PRIVACY)
    DELETE = _free_blocks(DELETE)
    CONTACT = _free_blocks(CONTACT)
    # terms: new glance bullet + a short "free to use" section instead of trial / plans / autopay
    _terms = []
    _skip = 0
    for b in TERMS:
        if _skip:
            _skip -= 1
            continue
        if b[0] == "glance":
            en = [i for i in b[1] if "free trial" not in i]
            hi = [i for i in b[2] if "फ्री ट्रायल" not in i]
            en.insert(1, f"The app is <b>free to use</b>. If we ever add paid plans, we will tell you in advance and update these Terms first.")
            hi.insert(1, "ऐप इस्तेमाल के लिए <b>मुफ़्त</b> है। अगर हम कभी पेड प्लान जोड़ेंगे, तो पहले से बताएँगे और पहले ये शर्तें अपडेट करेंगे।")
            _terms.append(("glance", en, hi))
        elif b[0] == "h2" and b[1].startswith("5. Free trial"):
            _terms.append(("h2", "5. Free to use", "5. इस्तेमाल मुफ़्त"))
            _terms.append((
                "p",
                f"{APP} is free to use and takes no payment. If we introduce paid plans in the future, we will tell you in advance, update these Terms and the Privacy Policy first, and never charge you without your clear consent.",
                f"{APP} इस्तेमाल के लिए मुफ़्त है और कोई भुगतान नहीं लेता। अगर हम भविष्य में पेड प्लान लाएँगे, तो पहले से बताएँगे, पहले ये शर्तें और प्राइवेसी पॉलिसी अपडेट करेंगे, और आपकी साफ़ सहमति के बिना कभी चार्ज नहीं करेंगे।",
            ))
            _skip = 3  # the ul, the autopay h2 and its paragraph
        else:
            _terms.append(b)
    TERMS = _map(_terms, _free_text)
    REFUND = [
        ("glance", [
            f"{APP} is <b>free to use</b> and takes no payments, so there is nothing to cancel or refund right now.",
            "If we introduce paid plans in the future, we will tell you in advance and publish the cancellation and refund rules here <b>before</b> any payment is taken.",
        ], [
            f"{APP} इस्तेमाल के लिए <b>मुफ़्त</b> है और कोई भुगतान नहीं लेता, इसलिए अभी रद्द करने या रिफंड करने के लिए कुछ नहीं है।",
            "अगर भविष्य में हम पेड प्लान लाएँगे, तो पहले से बताएँगे और कोई भी भुगतान लेने से <b>पहले</b> रद्द करने और रिफंड के नियम यहीं प्रकाशित करेंगे।",
        ]),
        ("h2", "1. Currently free", "1. अभी मुफ़्त"),
        ("p",
         f"Every feature of {APP} (practice questions, mock tests, explanations, progress analytics and bookmarks) is free. We do not ask for a card, UPI or any other payment detail.",
         f"{APP} की हर सुविधा (प्रैक्टिस प्रश्न, मॉक टेस्ट, व्याख्या, प्रगति एनालिटिक्स और बुकमार्क) मुफ़्त है। हम कार्ड, UPI या कोई और भुगतान-विवरण नहीं माँगते।"),
        ("h2", "2. If paid plans are introduced later", "2. अगर आगे पेड प्लान आए"),
        ("ul", [
            "We will tell you in the app and by email well before any plan starts.",
            "Nothing will be charged without your clear, separate consent.",
            "This page and the Privacy Policy will be updated first, with the cancellation and refund rules and how to ask for a refund.",
        ], [
            "किसी भी प्लान के शुरू होने से काफ़ी पहले हम ऐप में और ईमेल से बताएँगे।",
            "आपकी साफ़, अलग सहमति के बिना कुछ भी चार्ज नहीं होगा।",
            "यह पेज और प्राइवेसी पॉलिसी पहले अपडेट होंगे, जिनमें रद्द करने और रिफंड के नियम और रिफंड माँगने का तरीका होगा।",
        ]),
    ]


PAGES = [
    ("privacy.html", "Privacy Policy", "प्राइवेसी पॉलिसी", PRIVACY, True, True),
    ("terms.html", "Terms of Use", "उपयोग की शर्तें", TERMS, True, True),
    ("refund.html", "Refund & Cancellation Policy" if PAYMENTS else "Payments & Refunds", "रिफंड और कैंसिलेशन पॉलिसी" if PAYMENTS else "भुगतान और रिफंड", REFUND, True, True),
    ("delete-account.html", "Delete your account", "अपना अकाउंट डिलीट करें", DELETE, True, True),
    ("contact.html", "Contact & Grievance", "संपर्क और शिकायत", CONTACT, False, False),
]
NAV = [
    ("privacy.html", "Privacy Policy", "प्राइवेसी पॉलिसी"),
    ("terms.html", "Terms of Use", "उपयोग की शर्तें"),
    ("refund.html", "Refund &amp; Cancellation" if PAYMENTS else "Payments &amp; Refunds", "रिफंड और कैंसिलेशन" if PAYMENTS else "भुगतान और रिफंड"),
    ("delete-account.html", "Delete Account", "अकाउंट डिलीट करें"),
    ("contact.html", "Contact &amp; Grievance", "संपर्क और शिकायत"),
]

CSS = """
:root{--bg:#fff;--card:#f8fafc;--fg:#334155;--head:#0f172a;--mute:#64748b;--line:#e2e8f0;--brand:#047857;--brand-bg:#ecfdf5;--warn:#b45309;--warn-bg:#fffbeb}
@media (prefers-color-scheme:dark){:root{--bg:#020617;--card:#0b1220;--fg:#cbd5e1;--head:#fff;--mute:#94a3b8;--line:#1e293b;--brand:#34d399;--brand-bg:#06281f;--warn:#fbbf24;--warn-bg:#2a1d05}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.7 system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans Devanagari",sans-serif;-webkit-text-size-adjust:100%}
a{color:var(--brand)}
header.top{border-bottom:1px solid var(--line);position:sticky;top:0;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(8px);z-index:5}
.bar{max-width:62rem;margin:0 auto;padding:.7rem 1rem;display:flex;justify-content:space-between;align-items:center;gap:1rem}
.brand{display:flex;align-items:center;gap:.6rem;text-decoration:none;color:var(--head);font-weight:800;line-height:1.15}
.brand small{display:block;font-weight:500;color:var(--mute);font-size:.74rem}
.mark{width:2.2rem;height:2.2rem;border-radius:.6rem;background:linear-gradient(135deg,#04c8ae,#047857);color:#fff;display:grid;place-items:center;font-weight:800;font-size:.95rem;flex:none}
button.lang{border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:.6rem;padding:.4rem .85rem;font:inherit;font-size:.9rem;cursor:pointer}
.wrap{max-width:62rem;margin:0 auto;padding:1.5rem 1rem 3rem;display:grid;gap:2rem;grid-template-columns:minmax(0,1fr)}
@media(min-width:60rem){.wrap.has-toc{grid-template-columns:15rem minmax(0,1fr)}}
aside.toc{font-size:.9rem}
@media(min-width:60rem){aside.toc{position:sticky;top:5rem;align-self:start;max-height:calc(100vh - 6rem);overflow:auto}}
aside.toc b{display:block;color:var(--head);margin-bottom:.4rem}
aside.toc ol{list-style:none;margin:0;padding:0;border-left:2px solid var(--line)}
aside.toc li{margin:0}aside.toc a{display:block;padding:.22rem .7rem;text-decoration:none;color:var(--fg)}
aside.toc a:hover{color:var(--brand);background:var(--card)}
details.tocm{border:1px solid var(--line);border-radius:.75rem;padding:.6rem .9rem;background:var(--card)}
@media(min-width:60rem){details.tocm{display:none}}
@media(max-width:59.99rem){aside.toc>div.deskonly{display:none}}
h1{color:var(--head);font-size:clamp(1.7rem,4vw,2.3rem);line-height:1.2;margin:.2rem 0 .4rem;letter-spacing:-.01em}
h2{color:var(--head);font-size:1.25rem;margin:2.2rem 0 .6rem;scroll-margin-top:5rem;padding-top:.4rem;border-top:1px solid var(--line)}
p{margin:.6rem 0}ul,ol{padding-left:1.3rem}li{margin:.4rem 0}
.meta{display:flex;flex-wrap:wrap;gap:.4rem .6rem;margin:.3rem 0 1rem}
.chip{border:1px solid var(--line);background:var(--card);border-radius:999px;padding:.15rem .7rem;font-size:.8rem;color:var(--mute)}
.glance{background:var(--brand-bg);border:1px solid color-mix(in srgb,var(--brand) 35%,transparent);border-radius:1rem;padding:1rem 1.25rem;margin:1rem 0}
.glance h3{margin:0 0 .3rem;color:var(--head);font-size:1rem}.glance ul{margin:.3rem 0 0}
.note,.warn{border-radius:.8rem;padding:.8rem 1rem;margin:1rem 0;border:1px solid var(--line);background:var(--card)}
.warn{background:var(--warn-bg);border-color:color-mix(in srgb,var(--warn) 40%,transparent);color:var(--fg)}
.tw{overflow-x:auto;margin:1rem 0;border:1px solid var(--line);border-radius:.8rem}
table{border-collapse:collapse;width:100%;min-width:32rem;font-size:.92rem}
th,td{text-align:left;vertical-align:top;padding:.6rem .8rem;border-bottom:1px solid var(--line)}
th{background:var(--card);color:var(--head);font-weight:700}tr:last-child td{border-bottom:0}
.cards{display:grid;gap:.8rem;grid-template-columns:repeat(auto-fit,minmax(14rem,1fr));margin:1.2rem 0}
.card{border:1px solid var(--line);border-radius:1rem;padding:1rem 1.1rem;background:var(--card);text-decoration:none;display:block;color:var(--fg)}
.card b{display:block;color:var(--head);margin-bottom:.2rem}.card:hover{border-color:var(--brand)}
footer{border-top:1px solid var(--line);margin-top:2.5rem;padding-top:1.2rem;font-size:.88rem;color:var(--mute)}
footer nav{display:flex;flex-wrap:wrap;gap:.4rem 1.2rem;margin-bottom:.8rem}
html:not(.hi) [data-l=hi]{display:none!important}html.hi [data-l=en]{display:none!important}
@media print{header.top,aside.toc,details.tocm,button.lang{display:none}.wrap{display:block}a{color:inherit}}
"""
JS = """<script>(function(){var b=document.body,k='lang',h=document.documentElement;
function set(hi){h.classList.toggle('hi',hi);h.lang=hi?'hi':'en';try{localStorage.setItem(k,hi?'hi':'en')}catch(e){}}
try{if(localStorage.getItem(k)==='hi')set(true)}catch(e){}
document.getElementById('lang').addEventListener('click',function(){set(!h.classList.contains('hi'))})})();</script>"""


def both(en: str, hi: str, tag: str = "span") -> str:
    return f'<{tag} data-l="en">{en}</{tag}><{tag} data-l="hi">{hi}</{tag}>'


def cell(s: str) -> str:
    return s


def render_table(spec) -> str:
    head, rows = spec
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{cell(c)}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="tw"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def render(blocks, with_toc):
    out, toc = [], []
    n = 0
    for b in blocks:
        kind = b[0]
        if kind == "glance":
            for lang, items in (("en", b[1]), ("hi", b[2])):
                title = "In short" if lang == "en" else "संक्षेप में"
                out.append(f'<div class="glance" data-l="{lang}"><h3>{title}</h3><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>")
        elif kind == "h2":
            n += 1
            sid = f"s{n}"
            toc.append((sid, b[1], b[2]))
            out.append(f'<h2 id="{sid}" data-l="en">{b[1]}</h2><h2 data-l="hi" id="{sid}-hi">{b[2]}</h2>')
        elif kind == "p":
            out.append(f'<p data-l="en">{b[1]}</p><p data-l="hi">{b[2]}</p>')
        elif kind in ("note", "warn"):
            out.append(f'<div class="{kind}" data-l="en">{b[1]}</div><div class="{kind}" data-l="hi">{b[2]}</div>')
        elif kind in ("ul", "ol"):
            for lang, items in (("en", b[1]), ("hi", b[2])):
                out.append(f'<{kind} data-l="{lang}">' + "".join(f"<li>{i}</li>" for i in items) + f"</{kind}>")
        elif kind == "table":
            out.append(f'<div data-l="en">{render_table(b[1])}</div><div data-l="hi">{render_table(b[2])}</div>')
        else:
            raise ValueError(kind)
    return "\n".join(out), toc


def page(fname, title_en, title_hi, blocks, with_toc, with_meta):
    body, toc = render(blocks, with_toc)
    meta = (
        f'<div class="meta"><span class="chip">{both("Effective " + UPDATED, "लागू: " + UPDATED)}</span>'
        f'<span class="chip">{both("Version " + VERSION, "संस्करण " + VERSION)}</span>'
        f'<span class="chip">{both("Applies to: " + APP + " app and website", "लागू: " + APP + " ऐप और वेबसाइट")}</span></div>'
        if with_meta else ""
    )
    toc_html = ""
    if with_toc and toc:
        items_en = "".join(f'<li><a href="#{i}">{e}</a></li>' for i, e, _ in toc)
        items_hi = "".join(f'<li><a href="#{i}-hi">{h}</a></li>' for i, _, h in toc)
        toc_html = (
            f'<aside class="toc"><div class="deskonly"><b data-l="en">On this page</b><b data-l="hi">इस पेज पर</b>'
            f'<ol data-l="en">{items_en}</ol><ol data-l="hi">{items_hi}</ol></div>'
            f'<details class="tocm"><summary><b data-l="en">On this page</b><b data-l="hi">इस पेज पर</b></summary>'
            f'<ol data-l="en">{items_en}</ol><ol data-l="hi">{items_hi}</ol></details></aside>'
        )
    return shell(title_en, title_hi, f"{meta}{body}", toc_html, f"{title_en} of {APP} by {CO}.")


def shell(title_en, title_hi, body, toc_html="", desc=""):
    nav = "".join(f'<a href="{h}">{both(e, hh)}</a>' for h, e, hh in NAV)
    has = " has-toc" if toc_html else ""
    t_en = html.unescape(title_en)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(t_en)} | {APP} by {CO}</title>
<meta name="description" content="{html.escape(desc)}"><meta name="robots" content="index,follow"><meta name="theme-color" content="#047857">
<style>{CSS}</style></head><body>
<header class="top"><div class="bar"><a class="brand" href="index.html"><span class="mark">KS</span><span>{APP}<small>by {CO}</small></span></a>
<button class="lang" id="lang" type="button" aria-label="Switch language / भाषा बदलें">EN / हिन्दी</button></div></header>
<div class="wrap{has}">{toc_html}<main>
<h1>{both(title_en, title_hi)}</h1>
{body}
<footer><nav aria-label="Policies">{nav}</nav>
<div>© {YEAR} {CO}. All rights reserved. {APP} is a product of {CO}, India. Contact: {MAIL}</div></footer>
</main></div>{JS}</body></html>
"""


def index() -> str:
    cards = "".join(
        f'<a class="card" href="{h}"><b>{both(e, hh)}</b>'
        f'<span>{both(d_en, d_hi)}</span></a>'
        for (h, e, hh), (d_en, d_hi) in zip(NAV, [
            ("What we collect, why, who receives it, how we protect and delete it.", "हम क्या लेते हैं, क्यों, किसे मिलता है, कैसे सुरक्षित रखते और डिलीट करते हैं।"),
            ("The rules for using the app, plans, acceptable use and disclaimers.", "ऐप के उपयोग के नियम, प्लान, स्वीकार्य उपयोग और अस्वीकरण।")
            if PAYMENTS else ("The rules for using the app, acceptable use and disclaimers.", "ऐप के उपयोग के नियम, स्वीकार्य उपयोग और अस्वीकरण।"),
            (f"{TRIAL}-day free trial, cancelling autopay and when you get a refund.", f"{TRIAL} दिन का फ्री ट्रायल, ऑटोपे कैंसिल करना और रिफंड कब मिलता है।")
            if PAYMENTS else ("The app is free; what happens if paid plans are ever introduced.", "ऐप मुफ़्त है; आगे पेड प्लान आए तो क्या होगा।"),
            ("Delete your account and all your data, in the app or by email.", "ऐप में या ईमेल से अपना अकाउंट और सारा डेटा डिलीट करें।"),
            ("Support, refund requests, privacy requests and the Grievance Officer.", "सहायता, रिफंड अनुरोध, प्राइवेसी अनुरोध और शिकायत अधिकारी।")
            if PAYMENTS else ("Support, privacy requests and the Grievance Officer.", "सहायता, प्राइवेसी अनुरोध और शिकायत अधिकारी।"),
        ])
    )
    body = (
        f'<p data-l="en"><b>{APP}</b> is an independent exam-preparation app for the UP Super TET and similar teacher eligibility exams, '
        f'designed, developed and operated by <b>{CO}</b>, India. These pages are its public policies.</p>'
        f'<p data-l="hi"><b>{APP}</b> UP Super TET और ऐसी शिक्षक पात्रता परीक्षाओं की तैयारी के लिए एक स्वतंत्र ऐप है, जिसे <b>{CO}</b>, भारत ने '
        f'डिज़ाइन, विकसित और संचालित किया है। ये पेज इसकी सार्वजनिक पॉलिसियाँ हैं।</p>'
        f'<div class="cards">{cards}</div>'
        f'<div class="note" data-l="en"><b>Not a government app.</b> {APP} is not affiliated with, endorsed by or sponsored by any government body or exam board, including UPESSC.</div>'
        f'<div class="note" data-l="hi"><b>सरकारी ऐप नहीं।</b> {APP} किसी सरकारी संस्था या परीक्षा बोर्ड, जिसमें UPESSC भी शामिल है, से संबद्ध, उनके द्वारा समर्थित या प्रायोजित नहीं है।</div>'
    )
    return shell(APP, APP, body, "", f"Public policies of {APP} by {CO}: privacy, terms, payments and refunds, account deletion, contact.")


def main() -> None:
    for fname, en, hi, blocks, toc, meta in PAGES:
        (OUT / fname).write_text(page(fname, en, hi, blocks, toc, meta), encoding="utf-8", newline="\n")
        print("wrote", fname)
    (OUT / "index.html").write_text(index(), encoding="utf-8", newline="\n")
    print("wrote index.html")


if __name__ == "__main__":
    main()
