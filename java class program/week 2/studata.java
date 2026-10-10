import java.awt.*;

public class studata extends Frame {
    public Label nameLabel, ageLabel;
    public TextField nameField, ageField;

    public studata() {
        setTitle("Student Data Form");
        setSize(300, 150);
        setLayout(new GridLayout(2, 2));

        nameLabel = new Label("Name:");
        ageLabel = new Label("Age:");

        nameField = new TextField(20);
        ageField = new TextField(20);

        add(nameLabel);
        add(nameField);
        add(ageLabel);
        add(ageField);
    }

    public static void main(String[] args) {
        studata form = new studata();
        form.setVisible(true);
    }
}
