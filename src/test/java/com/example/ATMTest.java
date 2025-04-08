import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class ATMTest {

    @Test
    public void testIntroduction() {
        // Redirige la sortie standard vers un flux de sortie temporaire
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));
        
        // Exécute la méthode à tester
        ATM.introduction();
        
        // Récupère le contenu du flux de sortie
        String output = outputStream.toString();
        
        // Vérifie que la sortie contient le message d'introduction attendu
        assertEquals("Welcome to the ATM Project!\n", output);
        
        // Restaure la sortie standard
        System.setOut(System.out);
    }
}
