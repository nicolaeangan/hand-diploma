# -*- coding: utf-8 -*-
"""Content model for the Upper Limb Atlas template.

Edit this file (or replace it) and run `python3 build.py` to regenerate the site.
Every article lists `tags` (the "cards"). Two articles that share a card are linked
on both article pages and joined by an edge in the network graph.
"""

SITE = {
    "name": "Upper Limb Atlas",
    "tagline": "Shoulder · Elbow · Wrist · Hand · Nerve",
    "description": "A cross-linked reference on upper limb surgery. Sample template content.",
}

# category id -> (label, css var suffix)
CATEGORIES = {
    "shoulder": "Shoulder",
    "elbow": "Elbow",
    "wrist": "Wrist",
    "hand": "Hand",
    "reconstruction": "Reconstruction",
}

# card (tag) id -> (label, kind)
TAGS = {
    "shoulder": ("Shoulder", "Region"),
    "elbow": ("Elbow", "Region"),
    "wrist": ("Wrist", "Region"),
    "hand": ("Hand", "Region"),
    "rotator-cuff": ("Rotator cuff", "Structure"),
    "glenohumeral": ("Glenohumeral joint", "Structure"),
    "biceps": ("Biceps", "Structure"),
    "radius": ("Radius", "Structure"),
    "carpus": ("Carpus", "Structure"),
    "tendons": ("Tendons", "Structure"),
    "median-nerve": ("Median nerve", "Structure"),
    "ulnar-nerve": ("Ulnar nerve", "Structure"),
    "radial-nerve": ("Radial nerve", "Structure"),
    "brachial-plexus": ("Brachial plexus", "Structure"),
    "fracture": ("Fracture", "Pathology"),
    "instability": ("Instability", "Pathology"),
    "arthritis": ("Arthritis", "Pathology"),
    "degenerative": ("Degenerative", "Pathology"),
    "tendinopathy": ("Tendinopathy", "Pathology"),
    "nerve-compression": ("Nerve compression", "Pathology"),
    "trauma": ("Trauma", "Pathology"),
    "arthroscopy": ("Arthroscopy", "Approach"),
    "arthroplasty": ("Arthroplasty", "Approach"),
    "fixation": ("Fixation", "Approach"),
    "nerve-surgery": ("Nerve surgery", "Approach"),
    "tendon-transfer": ("Tendon transfer", "Approach"),
    "microsurgery": ("Microsurgery", "Approach"),
    "nonoperative": ("Non-operative", "Approach"),
    "rehab": ("Rehabilitation", "Approach"),
}


def S(h, p=None, ul=None):
    return {"h": h, "p": p or [], "ul": ul or []}


ARTICLES = [
    # ------------------------------------------------------------------ SHOULDER
    {
        "slug": "rotator-cuff-repair", "title": "Rotator Cuff Tears and Repair", "cat": "shoulder",
        "type": "Condition", "date": "2026-01-12",
        "summary": "Degenerative and traumatic cuff tears: when to treat non-operatively, how arthroscopic repair works, and what to do with irreparable tears.",
        "tags": ["shoulder", "rotator-cuff", "arthroscopy", "degenerative", "nonoperative", "rehab"],
        "sections": [
            S("Overview", ["Rotator cuff tears are a leading cause of shoulder pain and weakness in adults. Most involve the supraspinatus and are degenerative, although acute traumatic tears occur in younger patients after a fall or dislocation. Many tears, including some full-thickness tears, stay quiet or settle without surgery."]),
            S("Presentation and indications", None, [
                "Lateral shoulder pain, night pain and weakness of elevation or external rotation.",
                "Examination: painful arc, drop-arm or external rotation lag signs, supraspinatus and infraspinatus strength testing.",
                "Ultrasound or MRI defines tear size, retraction and fatty infiltration of the muscle.",
                "Surgery is favoured for acute traumatic tears, active patients with full-thickness tears, and failure of structured non-operative care."]),
            S("Management", None, [
                "Non-operative: activity modification, targeted physiotherapy, analgesia and selective injection.",
                "Arthroscopic repair with suture anchors, single-row or double-row, aiming for a tension-free footprint repair.",
                "Partial repair, superior capsular reconstruction or tendon transfer for large tears that cannot be repaired.",
                "Reverse shoulder arthroplasty when the cuff is irreparable and the joint is arthritic or pseudoparalytic."]),
            S("Outcomes and pitfalls", ["Pain relief is reliable after repair. Healing is less certain: re-tear risk rises with tear size, age, smoking and fatty infiltration. Stiffness is the commonest early complication, so the rehabilitation plan has to match the quality of the repair."]),
        ],
        "key_points": ["Tear size and tissue quality drive healing, not just surgical technique.", "Many degenerative tears do well without surgery.", "Irreparable tears need a different strategy, not a stronger repair."],
    },
    {
        "slug": "reverse-shoulder-arthroplasty", "title": "Reverse Total Shoulder Arthroplasty", "cat": "shoulder",
        "type": "Procedure", "date": "2026-01-26",
        "summary": "How the reverse design restores elevation without a working cuff, who it suits, and the complications to plan for.",
        "tags": ["shoulder", "glenohumeral", "rotator-cuff", "arthroplasty", "arthritis", "fracture"],
        "sections": [
            S("Overview", ["In a reverse prosthesis the ball is fixed to the glenoid and the socket to the humerus. This medialises and lowers the centre of rotation and lengthens the deltoid lever arm, so the deltoid can elevate the arm when the rotator cuff cannot."]),
            S("Indications", None, [
                "Cuff tear arthropathy and irreparable cuff tears with pseudoparalysis.",
                "Complex proximal humerus fractures in older patients.",
                "Osteoarthritis with glenoid bone loss or an insufficient cuff.",
                "Revision of failed anatomic arthroplasty or hemiarthroplasty."]),
            S("Technique", None, [
                "Deltopectoral approach, subscapularis managed according to surgeon preference and implant.",
                "Glenoid baseplate placed with secure fixation and attention to inferior tilt and overhang.",
                "Humeral stem cemented or press-fit, with version and soft-tissue tension set to balance stability and motion.",
                "A functioning deltoid and axillary nerve are prerequisites."]),
            S("Outcomes and pitfalls", ["Pain relief and elevation are generally good. Dislocation, scapular notching, acromial or scapular spine stress fracture, infection and loosening are the main concerns. Rotation, particularly internal rotation, is often limited."]),
        ],
        "key_points": ["Success depends on the deltoid, not the cuff.", "Component positioning governs stability and notching.", "Counsel on limited internal rotation and activity limits."],
    },
    {
        "slug": "anterior-shoulder-instability-bankart", "title": "Anterior Shoulder Instability and Bankart Repair", "cat": "shoulder",
        "type": "Procedure", "date": "2026-02-09",
        "summary": "Capsulolabral injury after dislocation, the role of bone loss in decision making, and arthroscopic Bankart repair.",
        "tags": ["shoulder", "glenohumeral", "instability", "arthroscopy", "rehab"],
        "sections": [
            S("Overview", ["After a first anterior dislocation, the anteroinferior labrum and capsule often detach from the glenoid (the Bankart lesion). Young, active patients have a high risk of recurrence with non-operative treatment alone."]),
            S("Assessment", None, [
                "History of dislocation mechanism, number of episodes and sports demands.",
                "Apprehension and relocation tests, assessment of generalised laxity.",
                "MR arthrography or CT for labral injury, glenoid bone loss and Hill-Sachs lesion.",
                "The 'glenoid track' concept helps decide whether soft-tissue repair alone is enough."]),
            S("Treatment", None, [
                "Arthroscopic Bankart repair with suture anchors, with or without capsular plication.",
                "Remplissage can be added for an engaging Hill-Sachs lesion.",
                "Significant glenoid bone loss or failed repair points towards a bony procedure such as Latarjet.",
                "Sling for a few weeks, then staged range of motion and strengthening before return to sport."]),
            S("Outcomes and pitfalls", ["Results are good in well-selected patients. Recurrence is more likely with bone loss, contact sport, young age and too few anchors. Missed bone loss is the classic cause of failure."]),
        ],
        "key_points": ["Measure bone loss before choosing a procedure.", "Recurrence risk is highest in young contact athletes.", "Rehabilitation is a phased programme, not a rest period."],
    },
    {
        "slug": "latarjet-procedure", "title": "The Latarjet Procedure", "cat": "shoulder",
        "type": "Procedure", "date": "2026-02-23",
        "summary": "Coracoid transfer for recurrent anterior instability: the triple-blocking effect, indications and neurological risks.",
        "tags": ["shoulder", "glenohumeral", "instability", "fixation", "trauma"],
        "sections": [
            S("Overview", ["The Latarjet procedure transfers the coracoid process with the conjoint tendon to the anterior glenoid, usually fixed with two screws. It stabilises the shoulder by three mechanisms: bone block, a sling effect from the conjoint tendon, and capsular repair."]),
            S("Indications", None, [
                "Recurrent anterior instability with significant glenoid bone loss.",
                "Off-track Hill-Sachs lesion.",
                "Failed prior soft-tissue stabilisation.",
                "Contact and collision athletes at high risk of recurrence."]),
            S("Technique", None, [
                "Deltopectoral approach with a subscapularis split or tenotomy.",
                "Coracoid osteotomy, preparation of the graft and glenoid neck.",
                "Screw fixation flush to the glenoid articular surface, avoiding overhang.",
                "Capsule repaired to the coracoacromial ligament stump."]),
            S("Risks", ["The musculocutaneous and axillary nerves lie close to the field and can be injured by traction or screw placement. Other problems are graft non-union or resorption, screw prominence and, in the long term, glenohumeral arthritis."]),
        ],
        "key_points": ["A robust option when bone loss makes soft-tissue repair unreliable.", "Graft position and screw length are technique-critical.", "Know the nerve anatomy around the coracoid."],
    },
    {
        "slug": "proximal-humerus-fractures", "title": "Proximal Humerus Fractures", "cat": "shoulder",
        "type": "Condition", "date": "2026-03-06",
        "summary": "Classification, the evidence for non-operative care, and the choice between plate, nail and arthroplasty.",
        "tags": ["shoulder", "fracture", "fixation", "arthroplasty", "trauma", "nonoperative"],
        "sections": [
            S("Overview", ["These are common fragility fractures in older adults, and a significant injury in younger patients after high-energy trauma. The Neer classification describes the four parts: head, greater tuberosity, lesser tuberosity and shaft."]),
            S("Assessment", None, [
                "Check axillary nerve function and distal pulses.",
                "True AP, scapular Y and axillary radiographs; CT for complex patterns.",
                "Consider bone quality, hand dominance, comorbidity and functional demands.",
                "Head-split and anatomical neck fractures carry the highest risk of avascular necrosis."]),
            S("Management", None, [
                "Most fractures are minimally displaced and do well with a sling and early guided motion.",
                "Displaced fractures: locking plate, intramedullary nail or arthroplasty, tailored to age and bone quality.",
                "Reverse arthroplasty is increasingly used in older patients with complex fractures.",
                "Randomised trials have not shown a consistent advantage of surgery for many displaced fractures in older adults."]),
            S("Outcomes and pitfalls", ["Complications include stiffness, malunion, screw cut-out, avascular necrosis and tuberosity failure. Early physiotherapy matters whatever the treatment chosen."]),
        ],
        "key_points": ["Treat the patient, not just the radiograph.", "Non-operative care is a valid first choice for many.", "Tuberosity healing determines the result of arthroplasty."],
    },
    {
        "slug": "clavicle-fractures", "title": "Clavicle Fractures", "cat": "shoulder",
        "type": "Condition", "date": "2026-03-20",
        "summary": "Midshaft and lateral-third fractures: which ones need fixation and how to avoid hardware problems.",
        "tags": ["shoulder", "fracture", "fixation", "trauma", "nonoperative"],
        "sections": [
            S("Overview", ["The clavicle is one of the most frequently broken bones, mainly in the middle third. Most heal with non-operative care, but displaced and shortened fractures in active adults have a higher non-union risk than once believed."]),
            S("When to operate", None, [
                "Open fractures, skin tenting, or neurovascular compromise.",
                "Displaced, comminuted or markedly shortened midshaft fractures in active adults.",
                "'Floating shoulder' with scapular neck fracture.",
                "Symptomatic non-union or malunion; unstable lateral-third fractures."]),
            S("Techniques", None, [
                "Plate fixation, superior or anteroinferior, is the commonest approach.",
                "Intramedullary devices offer smaller incisions but different failure modes.",
                "Lateral fractures may need hook plates or coracoclavicular reconstruction.",
                "Sling for comfort, with early pendulum and progressive motion."]),
            S("Pitfalls", ["Supraclavicular nerve branches lie across the incision and numbness below the scar is common. Plate prominence leads to implant removal in a minority of patients."]),
        ],
        "key_points": ["Most fractures heal without surgery.", "Shortening and displacement raise the case for fixation.", "Warn patients about scar numbness."],
    },
    {
        "slug": "acromioclavicular-joint-injuries", "title": "Acromioclavicular Joint Injuries", "cat": "shoulder",
        "type": "Condition", "date": "2026-04-03",
        "summary": "Rockwood grading, the grey zone of type III injuries, and reconstruction of the coracoclavicular ligaments.",
        "tags": ["shoulder", "instability", "trauma", "nonoperative", "arthroscopy"],
        "sections": [
            S("Overview", ["AC joint injuries typically follow a fall onto the point of the shoulder. The Rockwood classification (I to VI) grades damage to the AC and coracoclavicular ligaments and the position of the clavicle relative to the acromion."]),
            S("Decision making", None, [
                "Types I and II: sling, analgesia and early rehabilitation.",
                "Type III: individualised; many do well without surgery, especially non-overhead athletes.",
                "Types IV to VI: surgery is usually recommended.",
                "Horizontal instability matters as much as vertical displacement."]),
            S("Surgical options", None, [
                "Coracoclavicular ligament reconstruction with tendon graft.",
                "Suture-button devices, open or arthroscopic assisted.",
                "Hook plate, with planned removal.",
                "Acute fixation within a few weeks generally gives better results than delayed reconstruction."]),
            S("Pitfalls", ["Loss of reduction, coracoid or clavicle tunnel fracture, hardware irritation and persisting pain are recognised problems."]),
        ],
        "key_points": ["Grade type III injuries by function and demands.", "Biologic reconstruction holds better than suture alone.", "Assess horizontal stability."],
    },
    {
        "slug": "frozen-shoulder", "title": "Frozen Shoulder (Adhesive Capsulitis)", "cat": "shoulder",
        "type": "Condition", "date": "2026-04-17",
        "summary": "A self-limiting but long stiff-shoulder condition, with a stage-based approach to injection, hydrodilatation and release.",
        "tags": ["shoulder", "glenohumeral", "nonoperative", "rehab", "arthroscopy"],
        "sections": [
            S("Overview", ["Primary frozen shoulder is a painful contracture of the glenohumeral capsule, most often in people aged 40 to 60, and associated with diabetes and thyroid disease. It runs through freezing, frozen and thawing phases over months to a few years."]),
            S("Diagnosis", None, [
                "Global loss of active and passive motion, especially external rotation.",
                "Radiographs exclude glenohumeral arthritis and locked dislocation.",
                "Diagnosis is clinical; MRI is rarely needed.",
                "Rule out secondary causes, such as post-traumatic or post-surgical stiffness."]),
            S("Treatment", None, [
                "Education, analgesia and gentle stretching within pain limits.",
                "Intra-articular corticosteroid injection, particularly in the painful early phase.",
                "Hydrodilatation as an option for persistent symptoms.",
                "For refractory cases: arthroscopic capsular release or manipulation under anaesthesia."]),
            S("Pitfalls", ["Aggressive stretching in the freezing phase can inflame the capsule. Manipulation carries a small risk of humeral fracture or labral injury, so many surgeons prefer arthroscopic release."]),
        ],
        "key_points": ["Match treatment to the stage.", "Most patients improve, but slowly.", "Surgery is for the refractory minority."],
    },
    # ------------------------------------------------------------------ ELBOW
    {
        "slug": "distal-biceps-tendon-rupture", "title": "Distal Biceps Tendon Rupture", "cat": "elbow",
        "type": "Condition", "date": "2026-04-30",
        "summary": "Diagnosis with the hook test and fixation options that restore supination strength and flexion endurance.",
        "tags": ["elbow", "biceps", "tendons", "trauma", "fixation"],
        "sections": [
            S("Overview", ["Distal biceps rupture typically affects men in their thirties to fifties during an eccentric load on a flexed elbow, with a pop and pain in the antecubital fossa. The tendon avulses from the radial tuberosity."]),
            S("Diagnosis", None, [
                "Bruising, a proximally retracted muscle belly and a positive hook test.",
                "Weakness mainly in supination, less in flexion.",
                "Ultrasound or MRI if the diagnosis is uncertain or the tear is partial.",
                "Early diagnosis keeps repair simpler."]),
            S("Treatment", None, [
                "Non-operative care is reasonable for low-demand patients.",
                "Anatomic repair to the tuberosity within a few weeks, using cortical button, suture anchors or interference screw.",
                "Single-incision and two-incision approaches both have a place.",
                "Protected motion, then strengthening from around three months."]),
            S("Pitfalls", ["Lateral antebrachial cutaneous neuropraxia is common, posterior interosseous nerve injury is rare but serious, and heterotopic ossification is linked to the two-incision approach. Chronic ruptures may require graft reconstruction."]),
        ],
        "key_points": ["Supination strength is the main functional loss.", "Early repair beats late reconstruction.", "Protect the posterior interosseous nerve."],
    },
    {
        "slug": "lateral-epicondylitis", "title": "Lateral Epicondylitis (Tennis Elbow)", "cat": "elbow",
        "type": "Condition", "date": "2026-05-11",
        "summary": "A tendinopathy of the extensor carpi radialis brevis origin: what works, what does not, and the differentials that get missed.",
        "tags": ["elbow", "tendons", "tendinopathy", "nonoperative", "rehab", "radial-nerve"],
        "sections": [
            S("Overview", ["Lateral epicondylitis is a degenerative tendinopathy of the common extensor origin, particularly extensor carpi radialis brevis. Despite the name it is not primarily inflammatory, and it affects manual workers and desk workers alike."]),
            S("Clinical features", None, [
                "Pain over the lateral epicondyle on gripping or resisted wrist extension.",
                "Pain on resisted middle-finger extension and on passive wrist flexion with elbow extended.",
                "Most cases settle within a year.",
                "Always consider radial tunnel syndrome, cervical radiculopathy and posterolateral rotatory instability."]),
            S("Treatment", None, [
                "Load management, strengthening and physiotherapy are first-line.",
                "Counterforce bracing may help symptoms.",
                "Corticosteroid injection gives short-term relief but poorer outcomes at one year in several trials.",
                "Surgery after 6 to 12 months of failed care: debridement of the degenerate ECRB origin, open, arthroscopic or percutaneous."]),
            S("Pitfalls", ["Repeated steroid injections can weaken the tendon and cause skin atrophy. Failure of surgery usually means the diagnosis was wrong."]),
        ],
        "key_points": ["A tendinopathy, not an inflammatory condition.", "Rehabilitation outperforms repeated injections over the long term.", "Revisit the diagnosis if surgery fails."],
    },
    {
        "slug": "terrible-triad-elbow-injury", "title": "Terrible Triad Injury of the Elbow", "cat": "elbow",
        "type": "Procedure", "date": "2026-05-25",
        "summary": "Elbow dislocation with radial head and coronoid fractures: a stepwise fixation sequence and the aim of early motion.",
        "tags": ["elbow", "radius", "fracture", "instability", "fixation", "arthroplasty", "trauma"],
        "sections": [
            S("Overview", ["The terrible triad combines elbow dislocation, a radial head fracture and a coronoid fracture, with disruption of the lateral collateral ligament complex. It is notoriously unstable and prone to stiffness."]),
            S("Principles", None, [
                "Concentric reduction first, then CT to define the coronoid and radial head fractures.",
                "Restore the bony restraints before the soft tissues.",
                "Avoid isolated radial head excision in this setting.",
                "Aim for a stable arc allowing early active motion."]),
            S("Fixation sequence", None, [
                "Coronoid fixation or repair of the anterior capsule.",
                "Radial head fixation if reconstructable, otherwise radial head arthroplasty.",
                "Lateral collateral ligament repair.",
                "Medial collateral repair or a hinged external fixator if the elbow remains unstable."]),
            S("Pitfalls", ["Stiffness, heterotopic ossification, ulnar neuropathy, post-traumatic arthritis and persistent instability. Early motion within a safe arc is the single most useful way to limit stiffness."]),
        ],
        "key_points": ["Bony stability comes first.", "Radial head replacement is preferable to excision.", "Early motion is part of the surgery."],
    },
    {
        "slug": "cubital-tunnel-syndrome", "title": "Cubital Tunnel Syndrome", "cat": "elbow",
        "type": "Condition", "date": "2026-06-08",
        "summary": "Ulnar nerve compression at the elbow: when to splint, and decompression versus transposition.",
        "tags": ["elbow", "ulnar-nerve", "nerve-compression", "nerve-surgery", "nonoperative"],
        "sections": [
            S("Overview", ["Cubital tunnel syndrome is the second most common compression neuropathy of the upper limb after carpal tunnel syndrome. The ulnar nerve is compressed or stretched behind the medial epicondyle, particularly with sustained elbow flexion."]),
            S("Presentation", None, [
                "Tingling in the small finger and ulnar half of the ring finger, worse with elbow flexion.",
                "Weak pinch and clumsiness; later, intrinsic wasting, clawing and Froment sign.",
                "Tinel sign at the elbow and positive elbow flexion test.",
                "Nerve conduction studies help grade severity, though they can be normal early."]),
            S("Treatment", None, [
                "Mild or intermittent symptoms: avoid prolonged flexion and leaning on the elbow, night extension splint.",
                "Surgery for persistent or progressive symptoms, or motor loss.",
                "In situ decompression, open or endoscopic, is as effective as transposition for straightforward cases.",
                "Anterior transposition or medial epicondylectomy for subluxing nerve or revision."]),
            S("Pitfalls", ["Medial antebrachial cutaneous branches cross the incision and a neuroma can be a source of persistent pain. Long-standing compression with muscle wasting recovers incompletely."]),
        ],
        "key_points": ["Do not wait for wasting before offering surgery.", "In situ decompression is often enough.", "Protect cutaneous branches."],
    },
    # ------------------------------------------------------------------ WRIST
    {
        "slug": "distal-radius-fractures", "title": "Distal Radius Fractures", "cat": "wrist",
        "type": "Condition", "date": "2026-06-22",
        "summary": "The most common upper limb fracture: radiographic parameters, cast versus plate, and the older-adult evidence.",
        "tags": ["wrist", "radius", "fracture", "fixation", "trauma", "nonoperative", "median-nerve"],
        "sections": [
            S("Overview", ["Distal radius fractures are among the commonest fractures seen in adults, with peaks in older women after a low-energy fall and in younger patients after high-energy trauma."]),
            S("Assessment", None, [
                "Check median nerve function and skin integrity; acute carpal tunnel symptoms need prompt attention.",
                "Radiographic parameters: radial height, radial inclination, volar tilt and articular step-off.",
                "CT for intra-articular fractures.",
                "Associated injuries include DRUJ disruption, ulnar styloid fracture and scapholunate injury."]),
            S("Management", None, [
                "Stable, minimally displaced fractures: cast immobilisation.",
                "Randomised trials in older adults show that cast treatment gives similar function to surgery for many displaced fractures.",
                "Younger or active patients with unstable or articular fractures: volar locking plate.",
                "K-wires, external fixation and dorsal plating for specific patterns."]),
            S("Pitfalls", ["Extensor pollicis longus rupture, flexor tendon irritation from prominent plates, malunion, stiffness and complex regional pain syndrome. Finger and forearm motion should start early."]),
        ],
        "key_points": ["Age and demand outweigh radiographs in older adults.", "Always screen the median nerve.", "Early finger motion prevents stiffness."],
    },
    {
        "slug": "scaphoid-fractures-and-nonunion", "title": "Scaphoid Fractures and Non-union", "cat": "wrist",
        "type": "Condition", "date": "2026-07-06",
        "summary": "A fracture with a precarious blood supply: occult injuries, screw fixation and vascularised bone grafting for non-union.",
        "tags": ["wrist", "carpus", "fracture", "fixation", "trauma", "nonoperative", "arthritis"],
        "sections": [
            S("Overview", ["The scaphoid is the most commonly fractured carpal bone. Its blood supply enters distally and flows retrogradely, so proximal pole fractures are at high risk of avascular necrosis and non-union."]),
            S("Diagnosis", None, [
                "Snuffbox tenderness, pain on axial thumb loading and scaphoid tubercle tenderness.",
                "Initial radiographs may be normal, so suspected fractures need MRI, CT or repeat imaging.",
                "CT defines displacement, humpback deformity and union.",
                "Missed fractures lead to non-union and, over time, SNAC wrist arthritis."]),
            S("Treatment", None, [
                "Undisplaced waist fractures: cast immobilisation or percutaneous headless screw fixation.",
                "Displaced fractures and proximal pole fractures: screw fixation.",
                "Non-union: bone graft with fixation; vascularised grafts for avascular fragments.",
                "Salvage for established arthritis includes proximal row carpectomy or four-corner fusion."]),
            S("Pitfalls", ["Screw too long or prominent into the joint, persistent stiffness and non-union. Smoking impairs healing."]),
        ],
        "key_points": ["Treat suspected scaphoid injuries as fractures until proven otherwise.", "Proximal pole fractures heal poorly.", "Untreated non-union leads to predictable arthritis."],
    },
    {
        "slug": "tfcc-injuries", "title": "TFCC Injuries and Ulnar-sided Wrist Pain", "cat": "wrist",
        "type": "Condition", "date": "2026-07-20",
        "summary": "Palmer classification, DRUJ stability and the arthroscopic repair techniques for the triangular fibrocartilage complex.",
        "tags": ["wrist", "carpus", "radius", "arthroscopy", "instability", "trauma"],
        "sections": [
            S("Overview", ["The triangular fibrocartilage complex (TFCC) stabilises the distal radioulnar joint (DRUJ) and cushions the ulnar carpus. Injury may be traumatic (Palmer class 1) or degenerative (class 2)."]),
            S("Assessment", None, [
                "Ulnar-sided pain with forearm rotation, clicking and grip weakness.",
                "Ulnar fovea sign and DRUJ ballottement test.",
                "MRI or MR arthrography; arthroscopy remains the reference standard.",
                "Check ulnar variance for ulnar impaction syndrome."]),
            S("Treatment", None, [
                "Immobilisation and therapy for many stable tears.",
                "Arthroscopic debridement of central tears.",
                "Repair of peripheral tears; foveal reattachment when the DRUJ is unstable.",
                "Ulnar shortening osteotomy for ulnar impaction."]),
            S("Pitfalls", ["Dorsal sensory branch of the ulnar nerve injury during repair, persistent DRUJ instability and failure to address ulnar variance."]),
        ],
        "key_points": ["Distinguish stable from unstable DRUJ.", "Peripheral tears heal, central tears generally do not.", "Check ulnar variance."],
    },
    {
        "slug": "wrist-arthroscopy", "title": "Wrist Arthroscopy: Indications and Technique", "cat": "wrist",
        "type": "Technique", "date": "2026-09-14",
        "summary": "Portals, set-up and the expanding indications from diagnostic assessment to fracture-assisted fixation.",
        "tags": ["wrist", "carpus", "radius", "arthroscopy", "instability", "fracture", "arthritis"],
        "sections": [
            S("Overview", ["Wrist arthroscopy gives direct visualisation of the radiocarpal and midcarpal joints with limited soft-tissue disruption. It is both a diagnostic tool and a platform for treatment."]),
            S("Indications", None, [
                "TFCC tears and ulnar impaction.",
                "Scapholunate and lunotriquetral ligament injuries (Geissler grading).",
                "Arthroscopic assistance in intra-articular distal radius and scaphoid fractures.",
                "Synovitis, loose bodies, dorsal ganglion excision and selected arthritic wrists."]),
            S("Technique", None, [
                "Traction tower with 10 to 15 lb of finger traction under regional or general anaesthesia.",
                "Standard portals: 3-4, 4-5, 6R and 6U radiocarpal; radial and ulnar midcarpal.",
                "Outflow and low-pressure irrigation reduce extravasation risk.",
                "Systematic inspection of articular surfaces, ligaments and the TFCC."]),
            S("Pitfalls", ["Dorsal sensory nerve branches of the radial and ulnar nerves are at risk during portal creation; extensor tendon injury and fluid extravasation can also occur."]),
        ],
        "key_points": ["Careful portal creation avoids nerve injury.", "Arthroscopy refines, rather than replaces, the clinical assessment.", "Skill with small joint arthroscopy takes practice."],
    },
    # ------------------------------------------------------------------ HAND
    {
        "slug": "carpal-tunnel-syndrome", "title": "Carpal Tunnel Syndrome and Release", "cat": "hand",
        "type": "Condition", "date": "2026-07-27",
        "summary": "Median nerve compression: diagnosis, splinting and injection, and open versus endoscopic release.",
        "tags": ["hand", "wrist", "median-nerve", "nerve-compression", "nerve-surgery", "nonoperative", "tendon-transfer"],
        "sections": [
            S("Overview", ["Carpal tunnel syndrome (CTS) is the commonest entrapment neuropathy. The median nerve is compressed beneath the transverse carpal ligament, causing numbness and tingling in the thumb, index, middle and radial half of the ring finger."]),
            S("Diagnosis", None, [
                "Night-time paraesthesia, shaking the hand for relief, clumsiness.",
                "Phalen, Tinel and carpal compression tests; thenar wasting in advanced disease.",
                "Nerve conduction studies for atypical or severe cases and before surgery in some pathways.",
                "Consider cervical radiculopathy, pronator syndrome and polyneuropathy."]),
            S("Treatment", None, [
                "Neutral wrist night splints and corticosteroid injection for mild to moderate disease.",
                "Carpal tunnel release for persistent symptoms or motor involvement.",
                "Open or endoscopic release under local anaesthesia, usually as a day case.",
                "Opponensplasty in rare cases of fixed loss of thumb opposition."]),
            S("Pitfalls", ["Pillar pain and scar tenderness, incomplete release, recurrence and, rarely, injury to the palmar cutaneous or recurrent motor branch. Complex regional pain syndrome is uncommon but serious."]),
        ],
        "key_points": ["Symptom relief is excellent after release.", "Wasting means recovery will be partial.", "Question the diagnosis when symptoms persist."],
    },
    {
        "slug": "dupuytren-contracture", "title": "Dupuytren Contracture", "cat": "hand",
        "type": "Condition", "date": "2026-08-03",
        "summary": "Palmar fascia fibromatosis: timing of treatment and the spectrum from needle fasciotomy to dermofasciectomy.",
        "tags": ["hand", "tendons", "degenerative", "nonoperative", "rehab"],
        "sections": [
            S("Overview", ["Dupuytren disease is a benign fibroproliferative condition of the palmar fascia that forms nodules and cords and gradually flexes the fingers, most often the ring and small fingers. It is more common in men and people of Northern European ancestry."]),
            S("Assessment", None, [
                "Nodules and cords in the palm; extent of metacarpophalangeal (MCP) and proximal interphalangeal (PIP) contracture.",
                "Hueston table-top test.",
                "Associated Ledderhose disease, Garrod pads and a family history may indicate a stronger diathesis.",
                "Observation is appropriate until contracture interferes with function."]),
            S("Treatment", None, [
                "Needle (percutaneous) fasciotomy for MCP contractures and well-defined cords.",
                "Collagenase injection where available.",
                "Limited fasciectomy for more extensive disease.",
                "Dermofasciectomy with skin graft for recurrent or aggressive disease."]),
            S("Pitfalls", ["Recurrence is common and the disease cannot be cured. Digital nerve or artery injury, skin necrosis, stiffness and complex regional pain syndrome are the main operative risks. PIP contractures correct less reliably than MCP."]),
        ],
        "key_points": ["A chronic condition: manage expectations.", "MCP joints correct better than PIP.", "Therapy and splinting support the result."],
    },
    {
        "slug": "trigger-finger", "title": "Trigger Finger", "cat": "hand",
        "type": "Condition", "date": "2026-08-10",
        "summary": "Stenosing tenosynovitis of the A1 pulley: injection first, release when it persists.",
        "tags": ["hand", "tendons", "tendinopathy", "degenerative", "nonoperative"],
        "sections": [
            S("Overview", ["Trigger finger results from a size mismatch between the flexor tendon and the A1 pulley, causing painful catching or locking of the digit. It is more common in women in their fifties and in people with diabetes."]),
            S("Presentation", None, [
                "Painful clicking and locking in flexion, often worse in the morning.",
                "Tender nodule at the A1 pulley in the distal palm.",
                "Multiple digits and bilateral disease are common in diabetes.",
                "Fixed flexion with a locked finger needs prompt treatment."]),
            S("Treatment", None, [
                "Splinting and activity modification for mild cases.",
                "Corticosteroid injection into the flexor sheath is effective in many patients.",
                "Percutaneous or open release of the A1 pulley for failed injection or recurrent triggering.",
                "Early finger motion after release."]),
            S("Pitfalls", ["Injury to the digital nerves, particularly the radial digital nerve in the thumb, bowstringing if the A2 pulley is divided, and transient hyperglycaemia after steroid injection in people with diabetes."]),
        ],
        "key_points": ["Injection is a sensible first step.", "Release the A1 pulley only.", "Diabetes predicts recurrence."],
    },
    {
        "slug": "thumb-cmc-arthritis", "title": "Thumb Carpometacarpal Arthritis", "cat": "hand",
        "type": "Condition", "date": "2026-08-17",
        "summary": "Basal thumb osteoarthritis: staging, conservative options and trapeziectomy versus arthroplasty.",
        "tags": ["hand", "arthritis", "arthroplasty", "degenerative", "nonoperative", "arthroscopy", "tendons"],
        "sections": [
            S("Overview", ["Osteoarthritis of the thumb carpometacarpal (CMC) joint is very common in post-menopausal women and causes pain with pinch and grip, loss of key-pinch strength and, later, adduction deformity with MCP hyperextension."]),
            S("Assessment", None, [
                "Pain at the base of the thumb, positive grind test, crepitus and tenderness.",
                "Radiographs: Eaton-Littler staging.",
                "Examine the MCP joint and the scaphotrapezial joint.",
                "Rule out de Quervain tenosynovitis and flexor carpi radialis tendinopathy."]),
            S("Treatment", None, [
                "Splints, hand therapy, analgesia and corticosteroid injection.",
                "Arthroscopic debridement or ligament reconstruction in early disease.",
                "Trapeziectomy, with or without ligament reconstruction and tendon interposition.",
                "Prosthetic replacement is an option in selected patients."]),
            S("Pitfalls", ["Randomised trials suggest additional procedures do not clearly improve outcomes compared with trapeziectomy alone. Complications of surgery include scar pain, nerve irritation and, for implants, loosening and dislocation."]),
        ],
        "key_points": ["Most patients improve without surgery.", "Simple trapeziectomy remains a reliable operation.", "Treat MCP hyperextension when present."],
    },
    {
        "slug": "flexor-tendon-repair", "title": "Flexor Tendon Repair", "cat": "hand",
        "type": "Procedure", "date": "2026-08-24",
        "summary": "Zones of injury, core suture principles and early mobilisation protocols that balance gliding against rupture.",
        "tags": ["hand", "tendons", "trauma", "rehab", "median-nerve"],
        "sections": [
            S("Overview", ["Flexor tendon lacerations are classified into five zones. Zone II, within the digital sheath, is the most demanding because tendons glide in a tight fibro-osseous tunnel and are prone to adhesion."]),
            S("Principles", None, [
                "Repair within days, under wide-awake local anaesthesia or regional block.",
                "Multi-strand core suture, usually four or more strands, with epitendinous suture.",
                "Preserve the A2 and A4 pulleys to prevent bowstringing.",
                "Check for associated digital nerve and artery injury, and median nerve in zone V."]),
            S("Rehabilitation", None, [
                "Dorsal blocking splint with early protected active or passive motion.",
                "Therapist-led protocols tailored to repair strength and patient compliance.",
                "Light use from about six weeks; heavy loading later.",
                "Staged reconstruction with a silicone rod and tendon graft for failed or neglected injuries."]),
            S("Pitfalls", ["Rupture, adhesions, interphalangeal joint contracture and infection. Rehabilitation is half the repair."]),
        ],
        "key_points": ["Zone II is the hardest zone.", "Strong repair allows early motion.", "Plan therapy before the operation."],
    },
    # ------------------------------------------------------------------ RECONSTRUCTION
    {
        "slug": "brachial-plexus-injuries", "title": "Brachial Plexus Injuries", "cat": "reconstruction",
        "type": "Condition", "date": "2026-09-01",
        "summary": "Mechanisms, root avulsion, timing of exploration and a reconstructive ladder from nerve transfer to functional muscle transfer.",
        "tags": ["brachial-plexus", "nerve-surgery", "trauma", "microsurgery", "tendon-transfer", "rehab"],
        "sections": [
            S("Overview", ["Brachial plexus injuries range from stretch neuropraxia to complete root avulsion. Closed traction injuries after motorcycle or high-energy trauma are the most common in adults; obstetric injuries occur at birth."]),
            S("Assessment", None, [
                "Map the level of injury by muscle group and sensory loss.",
                "Horner syndrome suggests a proximal lower trunk or root avulsion.",
                "MRI or CT myelography, plus electrodiagnostics from about three to four weeks.",
                "Look for associated vascular and bony injury."]),
            S("Reconstruction", None, [
                "Priorities: elbow flexion, shoulder stability and abduction, hand sensation, then prehension.",
                "Exploration and nerve grafting or transfer when there is no recovery after three to six months.",
                "Tendon transfers and free functional muscle transfer for late cases.",
                "Shoulder arthrodesis or palliative procedures when reconstruction is not possible."]),
            S("Pitfalls", ["The time window for motor reinnervation is limited. Pain from root avulsion can be severe and needs a dedicated pain strategy. Realistic goal setting is essential."]),
        ],
        "key_points": ["Timing governs motor recovery.", "Avulsed roots need transfers, not grafts.", "Rehabilitation continues for years."],
    },
    {
        "slug": "nerve-transfers-upper-limb", "title": "Nerve Transfers in the Upper Limb", "cat": "reconstruction",
        "type": "Technique", "date": "2026-09-08",
        "summary": "Re-routing expendable donors close to the target muscle: Oberlin, spinal accessory to suprascapular, and distal transfers.",
        "tags": ["brachial-plexus", "nerve-surgery", "microsurgery", "ulnar-nerve", "median-nerve", "elbow"],
        "sections": [
            S("Overview", ["A nerve transfer connects a functioning, expendable donor nerve or fascicle to a denervated recipient nerve close to its target muscle. The short regeneration distance and the absence of a long graft improve the chance of reinnervation before the motor endplate degenerates."]),
            S("Common transfers", None, [
                "Oberlin: ulnar nerve fascicle to the biceps branch for elbow flexion.",
                "Median nerve fascicle to the brachialis branch (double fascicular transfer).",
                "Spinal accessory nerve to the suprascapular nerve for shoulder abduction and external rotation.",
                "Triceps branch of the radial nerve to the axillary nerve for deltoid function."]),
            S("Principles", None, [
                "Donor must be expendable and of sufficient axon count.",
                "Perform within about six to twelve months of injury.",
                "Coaptation without tension under magnification, with nerve stimulation to confirm fascicle function.",
                "Postoperative cortical re-education improves outcome."]),
            S("Pitfalls", ["Late presentation, an inadequate donor, and weak target muscles. Cross-talk between donor and recipient functions needs retraining."]),
        ],
        "key_points": ["Transfers shorten the distance to the target muscle.", "Choose donors carefully.", "Time is the limiting factor."],
    },
    {
        "slug": "tendon-transfers-radial-nerve-palsy", "title": "Tendon Transfers for Radial Nerve Palsy", "cat": "reconstruction",
        "type": "Procedure", "date": "2026-09-22",
        "summary": "Restoring wrist, finger and thumb extension with pronator teres, flexor carpi and palmaris longus transfers.",
        "tags": ["radial-nerve", "tendon-transfer", "tendons", "wrist", "hand", "rehab", "trauma"],
        "sections": [
            S("Overview", ["High radial nerve palsy, for instance after a humeral shaft fracture, causes wrist drop and loss of finger and thumb extension. When recovery fails or is not expected, tendon transfers restore a functional hand."]),
            S("Principles", None, [
                "Supple joints and healed soft tissues before transfer.",
                "Donor tendons of adequate strength, expendable, with a straight line of pull.",
                "One tendon, one function; synergistic muscles where possible.",
                "Anticipate recovery of the nerve before choosing transfers."]),
            S("Classic transfers", None, [
                "Pronator teres to extensor carpi radialis brevis for wrist extension.",
                "Flexor carpi radialis or ulnaris to extensor digitorum communis for finger extension.",
                "Palmaris longus to extensor pollicis longus for thumb extension.",
                "Pulvertaft weave to secure the transfers at appropriate tension."]),
            S("Rehabilitation", ["Immobilisation for about three to four weeks, then supervised re-education. Patients must learn to extend the fingers by contracting the transferred muscles."]),
        ],
        "key_points": ["Wait for nerve recovery, but not forever.", "Tension setting determines the result.", "Re-education is part of treatment."],
    },
    {
        "slug": "replantation-and-microsurgery", "title": "Replantation and Hand Microsurgery", "cat": "reconstruction",
        "type": "Procedure", "date": "2026-10-06",
        "summary": "Indications for digit and hand replantation, the order of repair and post-operative monitoring.",
        "tags": ["hand", "microsurgery", "trauma", "fixation", "nerve-surgery", "tendons", "rehab"],
        "sections": [
            S("Overview", ["Replantation re-attaches a completely amputated part. It requires a coordinated team, rapid transfer and an operation lasting many hours. Outcomes are best after clean-cut injuries and in children."]),
            S("Indications", None, [
                "Thumb, multiple digits, hand or distal forearm amputations.",
                "Single-digit amputations distal to the flexor digitorum superficialis insertion.",
                "Children, whenever feasible.",
                "Relative contraindications: severe crush or avulsion, multi-level injury, major comorbidity."]),
            S("Sequence", None, [
                "Debridement, bone shortening and rigid fixation.",
                "Extensor and flexor tendon repair.",
                "Arterial repair, then vein repair or grafting, then nerve repair.",
                "Skin cover without tension, with early planning for secondary procedures."]),
            S("Monitoring and pitfalls", ["Warm ischaemia tolerance is shorter for amputations containing muscle than for digits, and cooling extends the window. Post-operative vascular compromise is managed early; leech therapy and anticoagulation have roles. Cold intolerance and sensory problems are common."]),
        ],
        "key_points": ["Prompt cooling of the amputated part preserves options.", "Bone first, then tendons, vessels and nerves.", "Plan for secondary surgery."],
    },
    {
        "slug": "postoperative-hand-therapy", "title": "Post-operative Rehabilitation and Hand Therapy", "cat": "reconstruction",
        "type": "Technique", "date": "2026-10-20",
        "summary": "Phased rehabilitation principles that link surgery, splinting, scar management and return to work or sport.",
        "tags": ["rehab", "tendons", "shoulder", "hand", "nonoperative", "nerve-surgery", "tendon-transfer"],
        "sections": [
            S("Overview", ["Surgery creates the opportunity for recovery, and rehabilitation realises it. In upper limb surgery, the hand therapist works with the surgeon to protect repairs, restore motion and rebuild strength."]),
            S("Phases", None, [
                "Protection: splinting, oedema control, wound care, and early motion where the repair allows.",
                "Mobilisation: restoring range of motion and tendon gliding.",
                "Strengthening: progressive loading once the tissue has healed.",
                "Return to function: work simulation, sport-specific training, and activity advice."]),
            S("Procedure-specific points", None, [
                "Flexor tendon and rotator cuff repairs need protocols matched to repair strength.",
                "Nerve repairs and transfers need sensory re-education and desensitisation.",
                "Tendon transfers require training to use the transferred muscle.",
                "Stiffness prevention is easier than stiffness treatment."]),
            S("Pitfalls", ["Over-immobilisation, over-aggressive loading, poor adherence and untreated pain. Early recognition of complex regional pain syndrome improves the outcome."]),
        ],
        "key_points": ["A shared protocol between surgeon and therapist works best.", "Education drives adherence.", "Set function-based goals."],
    },
]
