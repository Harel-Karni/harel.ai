
# ניתוח תרחישים 
---

ניתוח תרחישים (Scenario Analysis)הוא כלי להערכת סיכונים שבוחן את ביצועי ההשקעה או התיק בתנאים משתנים של מספר גורמים סיכון בו-זמנית. בניגוד לניתוח רגישות המתמקד במשתנה יחיד, ניתוח תרחישים יוצר **"סיפורים" או "מצבי שוק" סבירים וקיצוניים** (תרחישים), ובודק כיצד ההשקעה תתנהג תחת כל אחד מהם.

**מטרתו:** להבין את החשיפה הכוללת של ההשקעה לאירועים מורכבים או למצבי שוק לא רצויים, ולבחון את עמידות התיק בתנאי לחץ.

**דוגמאות לתרחישים:**

- **תרחיש מיתון כלכלי חמור:** כולל ירידה בתמ"ג, עלייה באבטלה, ירידה ברווחי חברות, עלייה בריביות. כיצד ישפיע על תיק מניות, אגרות חוב ותיק נדל"ן?
    
- **תרחיש משבר גיאופוליטי:** כולל עלייה חדה במחירי הנפט, פיחות במטבע המקומי, ירידות בשווקי מניות גלובליים.
    
- **תרחיש "בום טכנולוגי":** צמיחה מהירה במגזר הטכנולוגיה, עליות חדות במניות טכנולוגיה, ירידה בתשואות באגרות חוב ממשלתיות.
    

**כיצד זה מתבצע?**

1. **הגדרת התרחישים:** קביעת מספר מוגבל של תרחישים סבירים (לרוב 3-5): תרחיש בסיס (Baseline), תרחיש אופטימי ותרחיש פסימי/קיצוני. כל תרחיש כולל קבוצה של הנחות עקביות לגבי משתני מפתח (לדוגמה, שיעורי ריבית, שיעורי צמיחה, מחירי סחורות, שערי חליפין).
    
2. **השפעה על תיק ההשקעות:** עבור כל תרחיש, מודלים פיננסיים מחשבים את התוצאה הצפויה עבור תיק ההשקעות (לדוגמה, שווי התיק, תשואה, הפסד).
    
3. **ניתוח התוצאות:** השוואת ביצועי התיק בין התרחישים השונים מסייעת לזהות את הפגיעות הפוטנציאלית ואת עמידות התיק.
    

**יתרונות:** ניתוח תרחישים מספק תמונה מציאותית יותר של הסיכון, כיוון שהוא מביא בחשבון את הקשרים בין משתנים שונים. הוא מאפשר לבחון אירועים קיצוניים ("זנבות שמנים") שסטיית תקן רגילה אינה לוכדת היטב, ומסייע בקבלת החלטות אסטרטגיות בתנאי אי-ודאות.

**מגבלות:** תלוי במידת הדיוק של התרחישים שנבחרו. קשה לכמת את ההסתברות להתרחשות כל תרחיש, ולרוב מדובר בתרחישים סובייקטיביים. יש סכנה להתעלם מ"ברבורים שחורים" (אירועים בלתי צפויים לחלוטין) שלא נכללו בתרחישים.

## מבחני לחץ 

**מבחני לחץ (Stress Testing)** הם סוג ספציפי של ניתוח תרחישים, המתמקדים בתרחישים קיצוניים מאוד ופחות סבירים, אך בעלי פוטנציאל להשפעה הרסנית על תיק ההשקעות או על המוסד הפיננסי. מטרתם היא לבדוק את עמידות התיק בתנאי שוק קשים במיוחד, שמעולם לא התרחשו או שהתרחשו לעיתים רחוקות מאוד בעבר.

**ההבדל העיקרי מניתוח תרחישים:** בעוד שניתוח תרחישים יכול לכלול גם תרחישים מתונים או סבירים, מבחני לחץ מתמקדים ב"מה אם הגרוע מכל יקרה?" – למשל, ירידה של 30% בשוק המניות תוך שבוע, או משבר אשראי עולמי בסדר גודל של 2008.

**יישומים:** מבחני לחץ נפוצים מאוד במוסדות פיננסיים (בנקים, חברות ביטוח) ככלי רגולטורי לניהול סיכונים. הם בודקים את יכולת המוסד לעמוד בזעזועים גדולים בשוק, וקובעים את דרישות ההון שהוא צריך להחזיק.

**יתרונות:** מספקים תובנה לגבי חשיפה לסיכוני זנב (Tail Risks) – אירועים בעלי סבירות נמוכה אך השפעה הרסנית. מסייעים למנהלי סיכונים לתכנן תגובות לאירועים קיצוניים ולבנות "כרית ביטחון".

**מגבלות:** תלויים מאוד בבחירת התרחישים הקיצוניים. לעיתים קרובות מבוססים על אירועי עבר (אך אינם בהכרח משקפים את המשבר הבא). יכולים להוביל לדרישות הון גבוהות מדי שפוגעות ביעילות.

## סימולציות מונטה קרלו 

**סימולציות מונטה קרלו (Monte Carlo Simulations)** הן שיטה חישובית המשתמשת בדגימה אקראית חוזרת ונשנית כדי למדל את ההתנהגות האפשרית של מערכת או השקעה מורכבת. בהקשר של השקעות, הן מאפשרות לחזות טווח רחב של תוצאות אפשריות עבור תיק השקעות, בהתחשב באי-ודאות של המשתנים השונים.

**כיצד זה מתבצע?**

1. **הגדרת מודל:** הגדרת מודל פיננסי המקשר בין משתני הקלט (לדוגמה, תשואות נכסים, מתאמים, אינפלציה) לבין התוצאה הסופית (לדוגמה, שווי תיק עתידי).
    
2. **הגדרת התפלגויות הסתברות:** לכל משתנה קלט, מגדירים התפלגות הסתברות ריאלית (לדוגמה, תשואות מניות יכולות להתפלג נורמלית סביב ממוצע מסוים עם סטיית תקן נתונה).
    
3. **ביצוע סימולציות:** המחשב מריץ אלפי ואף עשרות אלפי איטרציות (סימולציות). בכל איטרציה:
    
    - נדגמים ערכים אקראיים מתוך התפלגויות ההסתברות של כל משתני הקלט.
        
    - המודל מחושב עם הערכים שנדגמו, ומתקבלת תוצאה אחת אפשרית.
        
4. **ניתוח התוצאות:** לאחר השלמת כל האיטרציות, מתקבלת התפלגות של אלפי תוצאות אפשריות (לדוגמה, התפלגות של שווי התיק הסופי). מתוך התפלגות זו, ניתן לחשב הסתברויות לתרחישים שונים (לדוגמה, מה הסיכוי שהתיק יגיע לשווי מסוים, או מה הסיכוי להפסיד יותר מ-X%?).
    

**יתרונות:** סימולציות מונטה קרלו מספקות תמונה מקיפה של טווח התוצאות האפשריות ושל ההסתברות לכל תוצאה. הן מאפשרות להתחשב בקשרים מורכבים בין משתנים (מתאמים) ובאי-לינאריות, ואינן מוגבלות להנחת התפלגות נורמלית. הן שימושיות מאוד לתכנון פרישה, הערכת יעדי חיסכון, וקבלת החלטות השקעה לטווח ארוך בתנאי אי-ודאות.

**מגבלות:** דורשות כוח חישוב משמעותי. איכות התוצאות תלויה באיכות ההנחות לגבי התפלגויות ההסתברות ומתאמים בין המשתנים. הן אינן יכולות לחזות אירועים שלא נכללו במודל (כמו "ברבורים שחורים" אמיתיים).



לסיכום, ניתוח רגישות, תרחישים, מבחני לחץ וסימולציות מונטה קרלו הם כלים חיוניים המשלמים את מדדי הסיכון המסורתיים. הם מעניקים למשקיעים יכולת לבחון את עמידות השקעותיהם בתנאים עתידיים משתנים, להבין את מקורות הסיכון העיקריים, ולתכנן אסטרטגיות הגנה ובניית תיק שיעמוד במבחן הזמן גם בתקופות אי-ודאות.

